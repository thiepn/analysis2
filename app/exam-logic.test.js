const test = require('node:test');
const assert = require('node:assert/strict');

const L = require('./exam-logic.js');

const tasks = [
  {id: 'a', currentScopeStatus: 'confirmed_current', duplicateFamily: 'fa', points: 20, priorityScore: 9, topics: ['topologie'], techniques: ['definition'], gradingStatus: 'official_rubric', solution: {kind: 'offizielle Lösung'}},
  {id: 'b', currentScopeStatus: 'confirmed_current', duplicateFamily: 'fb', points: 15, priorityScore: 8, topics: ['extrema'], techniques: ['berechnung'], gradingStatus: 'estimated_scoring', solution: null},
  {id: 'c', currentScopeStatus: 'confirmed_current', duplicateFamily: 'fc', points: 15, priorityScore: 7, topics: ['topologie'], techniques: ['beweis'], gradingStatus: 'estimated_scoring', solution: null},
  {id: 'd', currentScopeStatus: 'unresolved', duplicateFamily: 'fd', points: 20, priorityScore: 6, topics: ['dgl'], techniques: ['berechnung'], gradingStatus: 'estimated_scoring', solution: null}
];

test('aktive Prüfung entfernt Lösungsdaten vollständig', () => {
  const locked = L.taskForMode(tasks[0], false);
  assert.equal(locked.solution, null);
  assert.deepEqual(L.taskForMode(tasks[0], true).solution, {kind: 'offizielle Lösung'});
});

test('Timer wird aus persistentem Startzeitpunkt rekonstruiert', () => {
  const active = {durationMinutes: 60, startedAt: '2026-01-01T12:00:00.000Z'};
  assert.equal(L.remainingSeconds(active, Date.parse('2026-01-01T12:15:10.000Z')), 2690);
  assert.equal(L.remainingSeconds(active, Date.parse('2026-01-01T13:30:00.000Z')), 0);
});

test('Punktwerte werden begrenzt in Prozent umgerechnet', () => {
  assert.equal(L.scorePercent(15, 20), 75);
  assert.equal(L.scorePercent(30, 20), 100);
  assert.equal(L.scorePercent(-2, 20), 0);
});

test('Probeklausur bevorzugt relevante Aufgaben und Themenbreite', () => {
  const result = L.createMockTasks(tasks, 3);
  assert.deepEqual(result.map(task => task.id), ['a', 'b', 'c']);
  assert.ok(result.every(task => task.currentScopeStatus === 'confirmed_current'));
});

test('Tagesliste priorisiert fällige und schwache Aufgaben ohne Duplikate', () => {
  const now = Date.parse('2026-01-10T00:00:00.000Z');
  const attempts = [
    {taskId: 'a', scorePercent: 40, confidence: 2, nextReviewAt: '2026-01-09T00:00:00.000Z'},
    {taskId: 'b', scorePercent: 50, confidence: 2, nextReviewAt: '2026-01-20T00:00:00.000Z'}
  ];
  const queue = L.dailyQueue(tasks, attempts, now, 4);
  assert.equal(new Set(queue.map(entry => entry.task.id)).size, queue.length);
  assert.equal(queue[0].task.id, 'a');
  assert.ok(queue.some(entry => entry.task.id === 'b'));
});

test('Kompetenzdimension folgt dem Aufgabentyp', () => {
  assert.equal(L.masteryCategory(tasks[0]), 'Nennen');
  assert.equal(L.masteryCategory(tasks[1]), 'Anwenden');
  assert.equal(L.masteryCategory(tasks[2]), 'Beweisen');
});

test('alle Lösungsstatus haben eindeutige deutsche Anzeigenamen', () => {
  assert.deepEqual([
    'official_solution', 'official_rubric', 'partial_official_solution',
    'reconstructed_solution', 'ai_generated_solution', 'no_solution'
  ].map(L.solutionLabel), [
    'Offizielle Lösung', 'Offizielles Bewertungsschema', 'Teilweise offizielle Lösung',
    'Rekonstruierte Lösung', 'KI-generierte Lösung', 'Keine verifizierte Lösung'
  ]);
});

test('inoffizielle Lösungen tragen die verpflichtende Warnung', () => {
  const warning = 'Diese Lösung ist nicht offiziell und muss mathematisch geprüft werden.';
  assert.equal(L.solutionWarning('reconstructed_solution'), warning);
  assert.equal(L.solutionWarning('ai_generated_solution'), warning);
  assert.equal(L.solutionWarning('official_solution'), '');
});

test('nur ein offizieller Bewertungsschlüssel aktiviert verifizierbare Punktwertung', () => {
  assert.equal(L.scoringMode(tasks[0]), 'verified_rubric');
  assert.equal(L.scoringMode(tasks[1]), 'self_estimated');
});

test('Probeklausur nimmt keine zwei Varianten derselben Aufgabenfamilie', () => {
  const variant = {...tasks[1], id: 'b2', duplicateFamily: 'fa', priorityScore: 10, topics: ['analysis']};
  const result = L.createMockTasks([...tasks, variant], 3);
  assert.equal(new Set(result.map(task => task.duplicateFamily)).size, result.length);
});
