import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const base = path.resolve(here, '..');
const raw = fs.readFileSync(path.join(base, 'app', 'data.js'), 'utf8');
const prefix = 'window.STUDY_DATA = ';
if (!raw.startsWith(prefix)) throw new Error('data.js besitzt nicht das erwartete Format.');
const data = JSON.parse(raw.slice(prefix.length));

if (data.schemaVersion !== 2 || data.language !== 'de') {
  throw new Error('App-Datenschema oder Sprache ist nicht aktuell.');
}

const requiredItemFields = ['id', 'kind', 'title', 'summary', 'metadata', 'contentBlocks', 'needsReview', 'reviewIssues'];
for (const item of data.items) {
  for (const field of requiredItemFields) {
    if (!(field in item)) throw new Error(`Pflichtfeld ${field} fehlt bei ${item.id}.`);
  }
  if (!Array.isArray(item.contentBlocks) || item.contentBlocks.length === 0) {
    throw new Error(`Keine semantischen Inhaltsblöcke bei ${item.id}.`);
  }
}

const visibleValues = [];
for (const item of data.items) {
  visibleValues.push(item.title, item.summary, item.intuition);
  for (const block of item.contentBlocks) visibleValues.push(block.text || '', block.tex || '');
}
for (const question of data.questions) visibleValues.push(question.question, question.short, question.full);
for (const proof of data.proofs) {
  visibleValues.push(proof.title, proof.summary, proof.strategy);
  for (const block of proof.contentBlocks) visibleValues.push(block.text || '', block.tex || '');
}
const visibleText = visibleValues.join('\n');
const forbidden = [
  /ANALYSIS\s+I\s*[-–]\s*III/i,
  /2011\/2013\s+\d+/i,
  /unnamed definition|unnamed theorem|unknown/i,
  /\b(?:This|What|State|Proof|Assumptions|Explanation|Why|Source|Check|Apply|Define)\b/i,
  /Missing argument for \\sqrt/i,
  /Formula may be corrupted|OCR check needed/i
];
for (const pattern of forbidden) {
  if (pattern.test(visibleText)) throw new Error(`Verbotener sichtbarer Inhalt gefunden: ${pattern}`);
}

const byId = new Map(data.items.map(item => [item.id, item]));
for (const id of ['6.4.3', '4.1.4', '4.1.6']) {
  const item = byId.get(id);
  if (!item) throw new Error(`Regressionskarte ${id} fehlt.`);
  if (!item.contentBlocks.some(block => block.type === 'math')) {
    throw new Error(`Regressionskarte ${id} besitzt keinen Mathematikblock.`);
  }
}

const kinds = new Set(data.items.map(item => item.kind));
for (const kind of ['Definition', 'Satz', 'Beispiel', 'Bemerkung']) {
  if (!kinds.has(kind)) throw new Error(`Kartentyp ${kind} fehlt in den App-Daten.`);
}

console.log(`Datenschema gültig: ${data.items.length} Lernblöcke, ${data.questions.length} Fragen, ${data.proofs.length} Beweise.`);
