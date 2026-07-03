const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const F = require('./formatting.js');

test('deutsche Schwierigkeitsgrade werden zentral abgebildet', () => {
  assert.equal(F.difficultyLabel('low'), 'niedrig');
  assert.equal(F.difficultyLabel('medium'), 'mittel');
  assert.equal(F.difficultyLabel('high'), 'hoch');
});

test('LaTeX-Normalisierung repariert mathbb und sqrt', () => {
  assert.equal(F.normalizeLatex('\\mathbb R'), '\\mathbb{R}');
  assert.equal(F.normalizeLatex('\\sqrt 2'), '\\sqrt{2}');
});

test('nicht geschlossene Mathematik wird erkannt', () => {
  assert.ok(F.validateLatex('\\mathbb{R').includes('nicht geschlossene geschweifte Klammer'));
  assert.ok(F.validateLatex('\\sqrt').includes('Wurzel ohne sicheres Argument'));
  assert.ok(F.validateLatex('\\(x').includes('nicht passende Inline-Mathematik-Trennzeichen'));
});

test('ungültige Formel erzeugt lesbaren Fallback ohne Parserfehler', () => {
  const output = F.mathMarkup('\\sqrt', true, 'test');
  assert.match(output, /math-fallback/);
  assert.doesNotMatch(output, /Missing argument|mjx-merror/);
});

test('Display- und Inline-Mathematik verwenden getrennte Trennzeichen', () => {
  assert.equal(F.mathMarkup('x^2', true), '\\[x^2\\]');
  assert.equal(F.mathMarkup('x^2', false), '\\(x^2\\)');
});

test('indizierte Wurzeln bleiben im Offline-Fallback lesbar', () => {
  assert.equal(F.readableFallback('\\sqrt[k]{x}'), 'k-te Wurzel aus (x)');
});

test('Metadaten stehen in einer deutschen separaten Zeile', () => {
  const value = F.metadataText({
    document: 'PDF',
    page: 103,
    sectionNumber: '6.4',
    sectionTitle: 'Der Hauptsatz der Differential- und Integralrechnung'
  });
  assert.equal(value, 'PDF · Seite 103 · Abschnitt 6.4 · Der Hauptsatz der Differential- und Integralrechnung');
});

test('Karteninhalt nutzt semantische Blöcke und Display-Mathematik', () => {
  const html = F.renderBlocks([
    {type: 'label', text: 'Aussage'},
    {type: 'text', text: 'Sei I ein Intervall.'},
    {type: 'math', tex: 'I \\subseteq \\mathbb{R}'}
  ], 'test');
  assert.match(html, /content-label/);
  assert.match(html, /formula-block/);
  assert.match(html, /\\\[/);
});

test('responsive Kartenregeln und deutscher Lernen-Button sind vorhanden', () => {
  const css = fs.readFileSync(path.join(__dirname, 'styles.css'), 'utf8');
  const app = fs.readFileSync(path.join(__dirname, 'app.js'), 'utf8');
  assert.match(css, /@media \(max-width: 820px\)/);
  assert.match(css, /overflow-x: auto/);
  assert.match(css, /\.primary-button/);
  assert.match(app, />Lernen</);
});
