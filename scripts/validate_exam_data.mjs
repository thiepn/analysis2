import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const require = createRequire(import.meta.url);
const logic = require(path.join(root, 'app', 'exam-logic.js'));
const source = fs.readFileSync(path.join(root, 'app', 'exam-data.js'), 'utf8');
const prefix = 'window.EXAM_DATA = ';
if (!source.startsWith(prefix)) throw new Error('exam-data.js hat kein gültiges Präfix.');
const data = JSON.parse(source.slice(prefix.length).replace(/;\s*$/, ''));
const pdfAssetDirectory = path.join(root, 'app', 'exam-pdfs');
const packagedPdfCount = fs.existsSync(pdfAssetDirectory)
  ? fs.readdirSync(pdfAssetDirectory).filter(file => file.toLowerCase().endsWith('.pdf')).length
  : 0;
const requirePdfAssets = process.env.ANALYSIS2_REQUIRE_PDFS === '1' || packagedPdfCount > 0;

const assert = (condition, message) => { if (!condition) throw new Error(message); };
const nearlyEqual = (a, b, epsilon = 0.011) => Math.abs(Number(a) - Number(b)) <= epsilon;

function parseSemicolonCsv(file) {
  const text = fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, '');
  const rows = [];
  let row = [];
  let value = '';
  let quoted = false;
  for (let index = 0; index < text.length; index += 1) {
    const character = text[index];
    if (character === '"') {
      if (quoted && text[index + 1] === '"') {
        value += '"';
        index += 1;
      } else quoted = !quoted;
    } else if (character === ';' && !quoted) {
      row.push(value);
      value = '';
    } else if ((character === '\n' || character === '\r') && !quoted) {
      if (character === '\r' && text[index + 1] === '\n') index += 1;
      row.push(value);
      if (row.some(cell => cell !== '')) rows.push(row);
      row = [];
      value = '';
    } else value += character;
  }
  if (value || row.length) {
    row.push(value);
    rows.push(row);
  }
  const [headers, ...records] = rows;
  return records.map(record => Object.fromEntries(headers.map((header, index) => [header, record[index] ?? ''])));
}

assert(data.schemaVersion === 2, 'Unerwartete Examenschema-Version.');
assert(data.language === 'de', 'Examendaten müssen deutsch markiert sein.');
assert(data.exams.length === 13, `Erwartet 13 Klausuren, gefunden ${data.exams.length}.`);
assert(data.tasks.length === 96, `Erwartet 96 Aufgaben, gefunden ${data.tasks.length}.`);
assert(data.sourceAudit.length === 16, `Erwartet 16 PDF-Quellen, gefunden ${data.sourceAudit.length}.`);
assert(data.evidenceSources.exerciseEvidence.status === 'not_provided', 'Fehlende Übungsblätter dürfen nicht als Evidenz gelten.');

const allowedSolutions = new Set([
  'official_solution', 'official_rubric', 'partial_official_solution',
  'reconstructed_solution', 'ai_generated_solution', 'no_solution'
]);
const allowedScope = new Set(['confirmed_current', 'likely_current', 'historically_examined', 'likely_outdated', 'unresolved']);
const allowedConfidence = new Set(['hoch', 'mittel', 'niedrig']);
const allowedGrading = new Set(['official_rubric', 'source_points_only', 'estimated_scoring']);
const allowedRelations = new Set(['exact_duplicate', 'changed_constants', 'theorem_variant', 'proof_template', 'computational_template', 'unique']);
assert(new Set(data.allowedSolutionStatuses).size === allowedSolutions.size, 'Statusliste für Lösungen ist unvollständig.');
assert(new Set(data.allowedCurrentScopeStatuses).size === allowedScope.size, 'Statusliste für Prüfungsumfang ist unvollständig.');

const examIds = new Set(data.exams.map(exam => exam.id));
const taskIds = new Set(data.tasks.map(task => task.id));
assert(examIds.size === data.exams.length, 'Doppelte Klausur-ID.');
assert(taskIds.size === data.tasks.length, 'Doppelte Aufgaben-ID.');

const auditByAsset = new Map();
for (const entry of data.sourceAudit) {
  if (entry.asset) auditByAsset.set(entry.asset, entry);
  for (const asset of entry.alternateAssets || []) auditByAsset.set(asset, entry);
}

for (const exam of data.exams) {
  assert(exam.taskIds.length === exam.taskCount && exam.taskCount > 0, `Aufgabenzahl fehlt in ${exam.id}.`);
  assert(exam.taskIds.every(id => taskIds.has(id)), `Klausur ${exam.id} verweist auf unbekannte Aufgabe.`);
  assert(allowedScope.has(exam.currentScopeStatus), `Ungültiger Klausur-Umfang in ${exam.id}.`);
  if (requirePdfAssets) assert(fs.existsSync(path.join(root, 'app', exam.asset)), `Klausur-PDF fehlt: ${exam.asset}`);
  const tasks = data.tasks.filter(task => task.examId === exam.id);
  assert(tasks.length === exam.taskIds.length, `Aufgabenzahl stimmt für ${exam.id} nicht.`);
  if (exam.totalPoints != null && tasks.every(task => task.points != null)) {
    const total = tasks.reduce((sum, task) => sum + task.points, 0);
    assert(total === exam.totalPoints, `Punktsumme ${exam.id}: ${total} statt ${exam.totalPoints}.`);
  }
}

let solutionCount = 0;
let rubricCount = 0;
for (const task of data.tasks) {
  assert(examIds.has(task.examId), `Unbekannte Klausur in ${task.id}.`);
  assert(task.title && task.prompt, `Leerer Aufgabentext in ${task.id}.`);
  assert(task.topics.length && task.topicLabels.length === task.topics.length, `Themenfehler in ${task.id}.`);
  assert(task.topicPrimary === task.topics[0], `Primärthema stimmt in ${task.id} nicht.`);
  assert(allowedSolutions.has(task.officialSolutionStatus), `Ungültiger Lösungsstatus in ${task.id}.`);
  assert(allowedScope.has(task.currentScopeStatus), `Ungültiger Umfangsstatus in ${task.id}.`);
  assert(allowedGrading.has(task.gradingStatus), `Ungültiger Bewertungsstatus in ${task.id}.`);
  assert(allowedRelations.has(task.familyRelation), `Ungültige Familienrelation in ${task.id}.`);
  assert(task.duplicateFamily, `Aufgabenfamilie fehlt in ${task.id}.`);
  assert(allowedConfidence.has(task.sourceConfidence), `Ungültige Quellenqualität in ${task.id}.`);
  assert(Number.isFinite(task.priorityScore), `Priorität fehlt in ${task.id}.`);
  assert(task.hints.length === 2 && task.hints.every(Boolean), `Hinweise fehlen in ${task.id}.`);
  if (requirePdfAssets) assert(fs.existsSync(path.join(root, 'app', task.source.asset)), `Aufgaben-PDF fehlt in ${task.id}.`);
  const sourceAudit = auditByAsset.get(task.source.asset);
  assert(sourceAudit && task.source.page <= (sourceAudit.packagedPages || sourceAudit.pages), `Ungültige Quellseite in ${task.id}.`);
  if (task.officialSolutionStatus !== 'no_solution') solutionCount += 1;
  if (task.officialSolutionStatus === 'official_rubric') rubricCount += 1;
  if (task.solution) {
    assert(task.solution.status === task.officialSolutionStatus, `Lösungsstatus driftet in ${task.id}.`);
    assert(task.solution.kind === logic.solutionLabel(task.officialSolutionStatus), `Deutsches Lösungslabel fehlt in ${task.id}.`);
    if (requirePdfAssets) assert(fs.existsSync(path.join(root, 'app', task.solution.asset)), `Lösungs-PDF fehlt in ${task.id}.`);
    const solutionAudit = auditByAsset.get(task.solution.asset);
    assert(solutionAudit && task.solution.pageEnd <= solutionAudit.pages, `Ungültige Lösungsseite in ${task.id}.`);
  } else assert(task.officialSolutionStatus === 'no_solution', `Lösungsdatei fehlt trotz Status in ${task.id}.`);
}

assert(solutionCount === 21, `Erwartet 21 Aufgaben mit offizieller Quelle, gefunden ${solutionCount}.`);
assert(rubricCount === 7, `Erwartet 7 Aufgaben mit offiziellem Schema, gefunden ${rubricCount}.`);
const familyIds = new Set(data.tasks.map(task => task.duplicateFamily));
assert(familyIds.size === 48, `Erwartet 48 Aufgabenfamilien, gefunden ${familyIds.size}.`);
assert(new Set(data.tasks.filter(task => task.familyRelation === 'exact_duplicate').map(task => task.duplicateFamily)).size === 5, 'Exact-Duplicate-Familien stimmen nicht.');

assert(data.topicWeighting.length === Object.keys(data.topicLabels).length, 'Themengewichtung ist unvollständig.');
for (const topic of data.topicWeighting) {
  const related = data.tasks.filter(task => task.topics.includes(topic.topic));
  assert(topic.rawTaskCount === related.length, `Rohhäufigkeit stimmt für ${topic.topic} nicht.`);
  assert(topic.examCount === new Set(related.map(task => task.examId)).size, `Klausurhäufigkeit stimmt für ${topic.topic} nicht.`);
  assert(topic.uniqueTaskFamilyCount === new Set(related.map(task => task.duplicateFamily)).size, `Familienhäufigkeit stimmt für ${topic.topic} nicht.`);
  assert(topic.officialSolutionCount === related.filter(task => task.officialSolutionStatus !== 'no_solution').length, `Lösungszahl stimmt für ${topic.topic} nicht.`);
  assert(topic.officialRubricCount === related.filter(task => task.officialSolutionStatus === 'official_rubric').length, `Schemazahl stimmt für ${topic.topic} nicht.`);
  const exposure = related.filter(task => task.points != null).reduce((sum, task) => sum + task.points, 0);
  const allocated = related.filter(task => task.points != null).reduce((sum, task) => sum + task.points / task.topics.length, 0);
  assert(topic.knownPointTaskExposure === exposure, `Punktkontakt stimmt für ${topic.topic} nicht.`);
  assert(nearlyEqual(topic.totalAllocatedPoints, allocated), `Punktzuordnung stimmt für ${topic.topic} nicht.`);
  const componentSum = Object.values(topic.scoreComponents).filter(value => value != null).reduce((sum, value) => sum + value, 0);
  assert(nearlyEqual(topic.weightScore, componentSum, 0.06), `Gewichtssumme stimmt für ${topic.topic} nicht.`);
  assert(topic.currentExerciseCoverage === 'not_provided', `Übungsabdeckung wurde für ${topic.topic} erfunden.`);
}

const corpusDir = path.join(root, '11-exam-corpus');
const examInventory = parseSemicolonCsv(path.join(corpusDir, 'exam-inventory.csv'));
const taskInventory = parseSemicolonCsv(path.join(corpusDir, 'task-inventory.csv'));
const topicInventory = parseSemicolonCsv(path.join(corpusDir, 'topic-weighting.csv'));
assert(examInventory.length === data.exams.length, 'exam-inventory.csv stimmt nicht mit den App-Daten überein.');
assert(taskInventory.length === data.tasks.length, 'task-inventory.csv stimmt nicht mit den App-Daten überein.');
assert(topicInventory.length === data.topicWeighting.length, 'topic-weighting.csv stimmt nicht mit den App-Daten überein.');
assert(new Set(taskInventory.map(row => row.task_id)).size === data.tasks.length, 'task-inventory.csv enthält doppelte IDs.');
assert(taskInventory.every(row => allowedSolutions.has(row.official_solution_status)), 'task-inventory.csv enthält ungültige Lösungsstatus.');
assert(taskInventory.every(row => allowedScope.has(row.current_scope_status)), 'task-inventory.csv enthält ungültige Umfangsstatus.');

const blueprint = fs.readFileSync(path.join(corpusDir, 'exam-blueprint.md'), 'utf8');
const priorities = fs.readFileSync(path.join(corpusDir, 'final-study-priorities.md'), 'utf8');
const appSource = fs.readFileSync(path.join(root, 'app', 'app.js'), 'utf8');
assert(blueprint.includes(`Eigenständige Klausuren: ${data.exams.length}.`), 'Bericht nennt falsche Klausurzahl.');
assert(blueprint.includes(`Gebündelte Hauptaufgaben: ${data.tasks.length}.`), 'Bericht nennt falsche Aufgabenzahl.');
assert(blueprint.includes(`Einzigartige Aufgabenfamilien: ${familyIds.size}.`), 'Bericht nennt falsche Familienzahl.');
assert(data.topicWeighting.every(topic => priorities.includes(`### ${topic.label} (`)), 'Prioritätsbericht lässt Themen aus.');
assert(appSource.includes('Geschätzte Bewertung'), 'App kennzeichnet geschätzte Bewertungen nicht auf Deutsch.');
assert(appSource.includes('Bewertung nach offiziellem Schema'), 'App kennzeichnet offizielle Bewertungsschemata nicht.');
assert(logic.solutionWarning('ai_generated_solution') === 'Diese Lösung ist nicht offiziell und muss mathematisch geprüft werden.', 'Pflichtwarnung für KI-Lösungen fehlt.');

console.log(`Examendaten gültig: ${data.exams.length} Klausuren, ${data.tasks.length} Aufgaben, ${familyIds.size} Familien, ${solutionCount} offizielle Lösungsquellen, ${rubricCount} Bewertungsschemata.`);
