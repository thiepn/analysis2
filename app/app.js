const data = window.STUDY_DATA;
const examData = window.EXAM_DATA || {exams: [], tasks: [], topicLabels: {}, studyMix: {}};
const F = window.StudyFormatting;
const L = window.ExamLogic;
const views = document.querySelectorAll('.view');
const itemList = document.querySelector('#itemList');
const search = document.querySelector('#search');
const kindFilter = document.querySelector('#kindFilter');
const resultCount = document.querySelector('#resultCount');
const emptyState = document.querySelector('#emptyState');
const detailOverlay = document.querySelector('#detailOverlay');
const detailTitle = document.querySelector('#detailTitle');
const detailMeta = document.querySelector('#detailMeta');
const detailBadges = document.querySelector('#detailBadges');
const detailBody = document.querySelector('#detailBody');
const renderedToggle = document.querySelector('#renderedToggle');
const rawToggle = document.querySelector('#rawToggle');
const taskOverlay = document.querySelector('#taskOverlay');
const taskDetailTitle = document.querySelector('#taskDetailTitle');
const taskDetailMeta = document.querySelector('#taskDetailMeta');
const taskDetailBadges = document.querySelector('#taskDetailBadges');
const taskDetailBody = document.querySelector('#taskDetailBody');

const initialSearch = new URLSearchParams(window.location.search).get('suche');
if (initialSearch) search.value = initialSearch;

let currentDetail = null;
let detailMode = 'rendered';
let questionIndex = 0;
let flashcardIndex = 0;
let flashcardAnswerVisible = false;
let currentExamTask = null;
let examTimerHandle = null;

function mathJaxAvailable() {
  return Boolean(window.MathJax && typeof window.MathJax.typesetPromise === 'function');
}

async function typeset(container) {
  if (!container || !mathJaxAvailable()) return;
  try {
    if (window.MathJax.startup?.promise) await window.MathJax.startup.promise;
    if (typeof window.MathJax.typesetClear === 'function') window.MathJax.typesetClear([container]);
    await window.MathJax.typesetPromise([container]);
  } catch (error) {
    console.warn('Mathematische Darstellung konnte nicht vollständig gesetzt werden', error);
    container.querySelectorAll('mjx-merror').forEach(node => {
      const fallback = document.createElement('span');
      fallback.className = 'math-fallback';
      fallback.textContent = 'Mathematische Quelle muss geprüft werden.';
      node.replaceWith(fallback);
    });
  }
}

function reviewBadge(item) {
  return item.needsReview ? '<span class="badge review-badge">Quellprüfung</span>' : '';
}

function difficultyBadge(item) {
  const raw = item.exam || 'medium';
  const label = F.difficultyLabel(raw);
  const className = raw === 'high' || raw === 'hoch'
    ? 'difficulty-high'
    : raw === 'low' || raw === 'niedrig'
      ? 'difficulty-low'
      : 'difficulty-medium';
  return `<span class="badge ${className}">${F.escapeHtml(label)}</span>`;
}

function contentMarkup(item, {preview = false, raw = false} = {}) {
  if (raw) return `<pre class="raw-source">${F.escapeHtml(item.statement || item.strategy || '')}</pre>`;
  const allBlocks = item.contentBlocks || [];
  let blocks = preview ? allBlocks.slice(0, 7) : allBlocks;
  if (preview && blocks.at(-1)?.type === 'label' && allBlocks.length > blocks.length) {
    blocks = [...blocks, allBlocks[blocks.length]];
  }
  const markup = F.renderBlocks(blocks, item.id, false, mathJaxAvailable());
  return markup || '<p>Für diesen Lernblock liegt kein darstellbarer Inhalt vor.</p>';
}

function cardMarkup(item, options = {}) {
  const isProof = item.kind === 'Beweis';
  const buttonKind = isProof ? 'proof' : 'item';
  return `<article class="study-card" data-card-id="${F.escapeHtml(item.id)}">
    <p class="metadata-row">${F.escapeHtml(F.metadataText(item.metadata))}</p>
    <div class="card-heading">
      <h3>${F.escapeHtml(F.titleText(item))}</h3>
      <div class="badge-row">
        ${isProof ? '' : difficultyBadge(item)}
        ${reviewBadge(item)}
      </div>
    </div>
    <p class="card-summary">${F.escapeHtml(item.summary || '')}</p>
    <div class="math-box">${contentMarkup(item, {preview: true})}</div>
    <footer class="card-footer">
      <button class="primary-button" data-open-kind="${buttonKind}" data-open-id="${F.escapeHtml(item.id)}">Lernen</button>
    </footer>
  </article>`;
}

function renderItems() {
  const query = search.value.trim().toLocaleLowerCase('de');
  const kind = kindFilter.value;
  const filtered = data.items.filter(item => {
    const searchable = [item.id, item.kind, item.title, item.summary, item.metadata?.sectionTitle]
      .join(' ')
      .toLocaleLowerCase('de');
    return (!kind || item.kind === kind) && (!query || searchable.includes(query));
  });
  resultCount.textContent = `${filtered.length} ${filtered.length === 1 ? 'Lernkarte' : 'Lernkarten'}`;
  emptyState.hidden = filtered.length !== 0;
  itemList.innerHTML = filtered.slice(0, 180).map(item => cardMarkup(item)).join('');
  typeset(itemList);
}

function findDetail(kind, id) {
  if (kind === 'proof') return data.proofs.find(item => item.id === id);
  if (kind === 'question') return data.questions.find(item => item.id === id);
  return data.items.find(item => item.id === id);
}

function renderDetail() {
  if (!currentDetail) return;
  const raw = detailMode === 'raw';
  renderedToggle.classList.toggle('active', !raw);
  rawToggle.classList.toggle('active', raw);
  detailTitle.textContent = currentDetail.question
    ? `Frage ${currentDetail.id}`
    : F.titleText(currentDetail);
  detailMeta.textContent = F.metadataText(currentDetail.metadata);
  detailBadges.innerHTML = currentDetail.question
    ? reviewBadge(currentDetail)
    : `${currentDetail.kind === 'Beweis' ? '' : difficultyBadge(currentDetail)}${reviewBadge(currentDetail)}`;

  if (currentDetail.question) {
    detailBody.innerHTML = raw
      ? `<pre class="raw-source">${F.escapeHtml([currentDetail.question, currentDetail.short, currentDetail.full].join('\n\n'))}</pre>`
      : `<p class="detail-summary">${F.escapeHtml(currentDetail.question)}</p>
         <div class="math-box"><h4 class="content-label">Kurzantwort</h4><p>${F.escapeHtml(currentDetail.short)}</p>
         <h4 class="content-label">Ausführliche Antwort</h4><p>${F.escapeHtml(currentDetail.full)}</p></div>`;
  } else {
    detailBody.innerHTML = `<p class="detail-summary">${F.escapeHtml(currentDetail.summary || '')}</p>
      <div class="math-box">${contentMarkup(currentDetail, {raw})}</div>
      ${currentDetail.kind === 'Beweis' && !raw ? `<h4 class="content-label">Beweisidee</h4><p>${F.escapeHtml(currentDetail.strategy || '')}</p>` : ''}`;
  }
  typeset(detailBody);
}

function openDetail(kind, id) {
  currentDetail = findDetail(kind, id);
  if (!currentDetail) return;
  detailMode = 'rendered';
  detailOverlay.hidden = false;
  document.body.style.overflow = 'hidden';
  renderDetail();
  document.querySelector('#closeDetail').focus();
}

function closeDetail() {
  detailOverlay.hidden = true;
  document.body.style.overflow = '';
  currentDetail = null;
}

function renderQuestion() {
  const question = data.questions[questionIndex % data.questions.length];
  const target = document.querySelector('#quizCard');
  target.innerHTML = `<p class="metadata-row">${F.escapeHtml(F.metadataText(question.metadata))}</p>
    <h3>Frage ${F.escapeHtml(question.id)}</h3>
    ${reviewBadge(question)}
    <div class="math-box"><p>${F.escapeHtml(question.question)}</p></div>
    <div class="card-footer"><button class="primary-button" data-show-quiz-answer>Antwort anzeigen</button></div>
    <div class="answer-block" data-quiz-answer hidden>
      <h4 class="content-label">Kurzantwort</h4>
      <p>${F.escapeHtml(question.short)}</p>
      <h4 class="content-label">Ausführliche Antwort</h4>
      <p>${F.escapeHtml(question.full)}</p>
      <button class="secondary-button" data-open-question="${F.escapeHtml(question.id)}">Im Detail lernen</button>
    </div>`;
  questionIndex += 1;
  typeset(target);
}

function renderFlashcard() {
  const item = data.items[flashcardIndex % data.items.length];
  const target = document.querySelector('#flashcard');
  target.innerHTML = `<p class="metadata-row">${F.escapeHtml(F.metadataText(item.metadata))}</p>
    <div class="card-heading"><h3>${F.escapeHtml(F.titleText(item))}</h3><div class="badge-row">${difficultyBadge(item)}${reviewBadge(item)}</div></div>
    <p class="card-summary">${F.escapeHtml(item.summary)}</p>
    <div class="answer-block" ${flashcardAnswerVisible ? '' : 'hidden'}>
      <div class="math-box">${contentMarkup(item)}</div>
      <footer class="card-footer"><button class="primary-button" data-open-kind="item" data-open-id="${F.escapeHtml(item.id)}">Lernen</button></footer>
    </div>`;
  document.querySelector('#showBack').textContent = flashcardAnswerVisible ? 'Antwort ausblenden' : 'Antwort anzeigen';
  typeset(target);
}

function renderProofs() {
  const proofList = document.querySelector('#proofList');
  proofList.innerHTML = data.proofs.map(proof => cardMarkup(proof)).join('');
  typeset(proofList);
}

const progressKey = 'analysis2-progress-v2';
const progressChecks = [
  'Kapitel 1: Grundlagen',
  'Kapitel 2: Folgen',
  'Kapitel 3: Reihen',
  'Kapitel 4: Stetigkeit',
  'Kapitel 5: Differenzierbarkeit',
  'Kapitel 6: Integralrechnung',
  'Kapitel 7: Metrik und Topologie',
  'Kapitel 8: Differenzierbare Abbildungen',
  'Kapitel 9: Umkehr- und implizite Funktionen',
  'Beweisrekonstruktion abgeschlossen',
  'Karteikarten wiederholt'
];

function getProgress() {
  try { return JSON.parse(localStorage.getItem(progressKey) || '{}'); }
  catch { return {}; }
}

function renderProgress() {
  const progress = getProgress();
  document.querySelector('#progressList').innerHTML = progressChecks.map(check => `<label class="progress-item">
    <input type="checkbox" ${progress[check] ? 'checked' : ''} data-check="${F.escapeHtml(check)}">
    <span>${F.escapeHtml(check)}</span>
  </label>`).join('');
}

const examProgressKey = 'analysis2-exam-progress-v1';
const errorLabels = {
  begriff: 'Begriffsfehler',
  rechnung: 'Rechenfehler',
  satzwahl: 'Falsche Satzwahl',
  beweis: 'Beweislücke',
  notation: 'Notation',
  zeit: 'Zeitmanagement'
};
const partialCreditLabels = {
  complete: 'vollständig korrekt',
  right_approach: 'richtiger Ansatz, Ausführung fehlerhaft',
  key_step: 'wesentlicher Zwischenschritt korrekt',
  incomplete: 'unvollständig',
  wrong: 'falsch',
  not_attempted: 'nicht bearbeitet'
};

function emptyExamProgress() {
  return {version: 1, attempts: [], examRuns: [], activeExam: null};
}

function getExamProgress() {
  try {
    return {...emptyExamProgress(), ...JSON.parse(localStorage.getItem(examProgressKey) || '{}')};
  } catch {
    return emptyExamProgress();
  }
}

function saveExamProgress(progress) {
  localStorage.setItem(examProgressKey, JSON.stringify(progress));
}

function examById(id) {
  return examData.exams.find(exam => exam.id === id);
}

function taskById(id) {
  return examData.tasks.find(task => task.id === id);
}

function latestAttemptMap(progress = getExamProgress()) {
  return L.latestAttemptMap(progress.attempts);
}

function relevanceBadge(task) {
  const labels = {
    confirmed_current: 'aktuell im Skript bestätigt', likely_current: 'wahrscheinlich aktuell',
    historically_examined: 'historisch geprüft', likely_outdated: 'wahrscheinlich veraltet', unresolved: 'Prüfungsumfang ungeklärt'
  };
  const classes = {
    confirmed_current: 'relevance-high', likely_current: 'relevance-medium', historically_examined: 'relevance-low',
    likely_outdated: 'relevance-outside', unresolved: 'relevance-partial'
  };
  return `<span class="badge ${classes[task.currentScopeStatus] || 'relevance-low'}">${F.escapeHtml(labels[task.currentScopeStatus] || task.currentScopeStatus)}</span>`;
}

function solutionBadge(task) {
  const status = task.officialSolutionStatus || 'no_solution';
  const classes = {
    official_solution: 'solution-official', official_rubric: 'solution-rubric',
    partial_official_solution: 'solution-partial', reconstructed_solution: 'solution-unofficial',
    ai_generated_solution: 'solution-unofficial', no_solution: 'solution-none'
  };
  return `<span class="badge ${classes[status] || 'solution-none'}">${F.escapeHtml(L.solutionLabel(status))}</span>`;
}

function unofficialSolutionWarning(task) {
  const warning = L.solutionWarning(task.officialSolutionStatus);
  return warning ? `<p class="solution-warning">${F.escapeHtml(warning)}</p>` : '';
}

function partialCreditOptions(selected = '') {
  return '<option value="">Bitte wählen</option>' + Object.entries(partialCreditLabels).map(([value, label]) =>
    `<option value="${value}" ${value === selected ? 'selected' : ''}>${F.escapeHtml(label)}</option>`
  ).join('');
}

function taskMeta(task) {
  const exam = examById(task.examId);
  const parts = [exam?.semester, exam?.lecturer, `Seite ${task.pageStart}`];
  if (task.points != null) parts.push(`${task.points} Punkte`);
  else parts.push('Punktwert unbekannt');
  return parts.filter(Boolean).join(' · ');
}

function sourceLink(asset, page, label) {
  if (!asset) return '';
  return `<a class="source-link" href="${F.escapeHtml(asset)}#page=${Number(page) || 1}" target="_blank" rel="noopener">${F.escapeHtml(label)}</a>`;
}

function taskCardMarkup(task) {
  const attempt = latestAttemptMap().get(task.id);
  const score = attempt ? `<span class="badge ${attempt.scorePercent >= 70 ? 'relevance-high' : 'relevance-outside'}">zuletzt ${Math.round(attempt.scorePercent)} %</span>` : '';
  return `<article class="task-card" data-task-id="${F.escapeHtml(task.id)}">
    <p class="metadata-row">${F.escapeHtml(taskMeta(task))}</p>
    <div class="card-heading"><h3>Aufgabe ${F.escapeHtml(task.id)}: ${F.escapeHtml(task.title)}</h3><div class="badge-row">${relevanceBadge(task)}${solutionBadge(task)}${score}</div></div>
    <p class="task-prompt">${F.escapeHtml(task.prompt)}</p>
    <div class="task-topic-list">${task.topicLabels.map(label => `<span class="topic-chip">${F.escapeHtml(label)}</span>`).join('')}</div>
    <footer class="card-footer"><button class="primary-button" data-open-exam-task="${F.escapeHtml(task.id)}">Bearbeiten</button></footer>
  </article>`;
}

function populateExamFilters() {
  const topicSelect = document.querySelector('#taskTopic');
  Object.entries(examData.topicLabels)
    .filter(([id]) => examData.tasks.some(task => task.topics.includes(id)))
    .sort((a, b) => a[1].localeCompare(b[1], 'de'))
    .forEach(([id, label]) => topicSelect.insertAdjacentHTML('beforeend', `<option value="${F.escapeHtml(id)}">${F.escapeHtml(label)}</option>`));
  const lecturerSelect = document.querySelector('#taskLecturer');
  [...new Set(examData.exams.map(exam => exam.lecturer))].sort((a, b) => a.localeCompare(b, 'de'))
    .forEach(lecturer => lecturerSelect.insertAdjacentHTML('beforeend', `<option>${F.escapeHtml(lecturer)}</option>`));
}

function renderTasks() {
  const query = document.querySelector('#taskSearch').value.trim().toLocaleLowerCase('de');
  const topic = document.querySelector('#taskTopic').value;
  const lecturer = document.querySelector('#taskLecturer').value;
  const relevance = document.querySelector('#taskRelevance').value;
  const points = document.querySelector('#taskPoints').value;
  const filtered = examData.tasks.filter(task => {
    const exam = examById(task.examId);
    const searchable = [task.id, task.title, task.prompt, ...task.topicLabels, exam?.title, exam?.lecturer].join(' ').toLocaleLowerCase('de');
    const pointsMatch = !points || (points === 'known' ? task.points != null : (task.points || 0) >= Number(points));
    return (!query || searchable.includes(query)) && (!topic || task.topics.includes(topic)) &&
      (!lecturer || exam?.lecturer === lecturer) && (!relevance || task.currentScopeStatus === relevance) && pointsMatch;
  }).sort((a, b) => b.priorityScore - a.priorityScore);
  document.querySelector('#taskResultCount').textContent = `${filtered.length} ${filtered.length === 1 ? 'Aufgabe' : 'Aufgaben'}`;
  document.querySelector('#taskEmptyState').hidden = filtered.length !== 0;
  document.querySelector('#taskList').innerHTML = filtered.map(taskCardMarkup).join('');
  typeset(document.querySelector('#taskList'));
}

function renderTaskDetail() {
  const task = currentExamTask;
  if (!task) return;
  const exam = examById(task.examId);
  const latest = latestAttemptMap().get(task.id);
  const verifiedScoring = L.scoringMode(task) === 'verified_rubric';
  const scoringLabel = verifiedScoring ? 'Bewertung nach offiziellem Schema' : 'Geschätzte Bewertung';
  const solution = task.solution
    ? `${solutionBadge(task)}<p>${F.escapeHtml(task.solution.summary)}</p>${unofficialSolutionWarning(task)}${sourceLink(task.solution.asset, task.solution.pageStart, `${L.solutionLabel(task.officialSolutionStatus)} öffnen`)}`
    : `${solutionBadge(task)}<p>Für diese Aufgabe liegt im bereitgestellten Korpus keine verifizierte Lösung vor. Die Hinweise sind Lernhilfen, keine offizielle Musterlösung.</p>`;
  const theoryLinks = task.theoryIds.length
    ? task.theoryIds.map(id => `<a class="source-link" href="index.html?suche=${encodeURIComponent(id)}">Theorie ${F.escapeHtml(id)}</a>`).join('')
    : '<p>Diese Aufgabe ist im aktuellen Skript nicht vollständig abgedeckt.</p>';
  taskDetailMeta.textContent = taskMeta(task);
  taskDetailTitle.textContent = `Aufgabe ${task.id}: ${task.title}`;
  taskDetailBadges.innerHTML = `${relevanceBadge(task)}${solutionBadge(task)}<span class="badge ${task.sourceConfidence === 'niedrig' ? 'confidence-low' : 'relevance-low'}">Quelle ${F.escapeHtml(task.sourceConfidence)}</span>`;
  taskDetailBody.innerHTML = `<section class="task-detail-section">
      <h3>Aufgabenstellung</h3><p>${F.escapeHtml(task.prompt)}</p>
      ${sourceLink(task.source.asset, task.source.page, 'Originalaufgabe öffnen')}
    </section>
    <section class="task-detail-section"><h3>Verknüpfte Theorie</h3>${theoryLinks}</section>
    <section class="task-detail-section"><h3>Gestufte Hinweise</h3>
      <button class="secondary-button" data-show-hint="0">Hinweis 1 anzeigen</button>
      <div class="hint-panel" data-hint-panel="0" hidden>${F.escapeHtml(task.hints[0])}</div>
      <button class="secondary-button" data-show-hint="1">Hinweis 2 anzeigen</button>
      <div class="hint-panel" data-hint-panel="1" hidden>${F.escapeHtml(task.hints[1])}</div>
    </section>
    <section class="task-detail-section"><h3>Lösungskontrolle</h3>
      <button class="secondary-button" data-show-solution>Lösungshinweis anzeigen</button>
      <div class="solution-panel" data-solution-panel hidden>${solution}</div>
    </section>
    <section class="task-detail-section"><h3>Versuch bewerten</h3>
      <p class="scoring-label">${F.escapeHtml(scoringLabel)}</p>
      <p class="supporting-text">${verifiedScoring
        ? 'Nutze den verlinkten Bewertungsschlüssel. Die Eingabe bleibt deine Selbstbewertung, ist aber am offiziellen Schema prüfbar.'
        : 'Es liegt kein offizieller Bewertungsschlüssel vor. Trage nur eine begründete Prozentschätzung ein; sie ist kein offizieller Punktwert.'}</p>
      <div class="score-row">
        <label class="field"><span>Ergebnis in Prozent</span><input id="taskScorePercent" type="number" min="0" max="100" step="1" value="${latest ? Math.round(latest.scorePercent) : ''}"></label>
        <label class="field"><span>Teilbewertung</span><select id="taskPartialCredit">${partialCreditOptions(latest?.partialCreditCategory || '')}</select></label>
        <label class="field"><span>Sicherheit der Bewertung</span><select id="taskConfidence"><option value="1">1 - geraten</option><option value="2">2 - unsicher</option><option value="3" selected>3 - teilweise sicher</option><option value="4">4 - sicher</option><option value="5">5 - sehr sicher</option></select></label>
      </div>
      <div class="error-options">${Object.entries(errorLabels).map(([id, label]) => `<label><input type="checkbox" value="${id}" data-task-error> ${label}</label>`).join('')}</div>
      <button class="primary-button" data-save-task-attempt>Versuch speichern</button>
    </section>`;
  if (latest) {
    document.querySelector('#taskConfidence').value = String(latest.confidence);
    latest.errors.forEach(error => {
      const checkbox = taskDetailBody.querySelector(`[data-task-error][value="${error}"]`);
      if (checkbox) checkbox.checked = true;
    });
  }
  typeset(taskDetailBody);
}

function openTaskDetail(taskId) {
  currentExamTask = taskById(taskId);
  if (!currentExamTask) return;
  taskOverlay.hidden = false;
  document.body.style.overflow = 'hidden';
  renderTaskDetail();
  document.querySelector('#closeTaskDetail').focus();
}

function closeTaskDetail() {
  taskOverlay.hidden = true;
  document.body.style.overflow = '';
  currentExamTask = null;
}

function saveTaskAttempt(task, scorePercent, confidence, errors, origin = 'trainer', assessment = {}) {
  const progress = getExamProgress();
  const now = Date.now();
  const days = scorePercent < 50 ? 1 : scorePercent < 75 ? 3 : 7;
  progress.attempts.push({
    id: `${task.id}-${now}`, taskId: task.id, scorePercent, confidence, errors, origin,
    scoringMode: assessment.scoringMode || L.scoringMode(task),
    partialCreditCategory: assessment.partialCreditCategory || 'incomplete',
    earnedVerifiedPoints: assessment.earnedVerifiedPoints ?? null,
    createdAt: new Date(now).toISOString(), nextReviewAt: new Date(now + days * 86400000).toISOString()
  });
  saveExamProgress(progress);
}

function createMockTasks() {
  return L.createMockTasks(examData.tasks, 7);
}

function populateExamSelect() {
  const select = document.querySelector('#examSelect');
  select.innerHTML = '<option value="mock">Gemischte Probeklausur - hohe Skriptrelevanz</option>' + examData.exams
    .slice().sort((a, b) => (b.semester || '').localeCompare(a.semester || '', 'de'))
    .map(exam => `<option value="${F.escapeHtml(exam.id)}">${F.escapeHtml(exam.title)}</option>`).join('');
  renderExamSetupMeta();
}

function renderExamSetupMeta() {
  const id = document.querySelector('#examSelect').value;
  if (id === 'mock') {
    const tasks = createMockTasks();
    const points = tasks.reduce((sum, task) => sum + (task.points || 0), 0);
    document.querySelector('#examSetupMeta').textContent = `${tasks.length} Aufgaben · ${points} bekannte Punkte · Planzeit 180 Minuten · Lösungen bis zur Abgabe gesperrt.`;
    return;
  }
  const exam = examById(id);
  const duration = exam.durationMinutes || 180;
  const durationText = exam.durationMinutes ? `${duration} Minuten` : `${duration} Minuten Planzeit (Originaldauer unbekannt)`;
  document.querySelector('#examSetupMeta').textContent = `${exam.taskIds.length} Aufgaben · ${exam.totalPoints ?? 'Punktzahl unbekannt'} Punkte · ${durationText} · Hilfsmittel: ${exam.allowedAids}.`;
}

function startExam() {
  const selected = document.querySelector('#examSelect').value;
  const taskIds = selected === 'mock' ? createMockTasks().map(task => task.id) : examById(selected).taskIds;
  const exam = selected === 'mock' ? null : examById(selected);
  const progress = getExamProgress();
  progress.activeExam = {
    id: `run-${Date.now()}`, examId: selected, title: selected === 'mock' ? 'Gemischte Probeklausur' : exam.title,
    taskIds, index: 0, flagged: [], startedAt: new Date().toISOString(), durationMinutes: exam?.durationMinutes || 180, status: 'running'
  };
  saveExamProgress(progress);
  renderExamState();
}

function updateTimer() {
  const active = getExamProgress().activeExam;
  if (!active || active.status !== 'running') return;
  const remaining = L.remainingSeconds(active);
  const hours = String(Math.floor(remaining / 3600)).padStart(2, '0');
  const minutes = String(Math.floor((remaining % 3600) / 60)).padStart(2, '0');
  const seconds = String(remaining % 60).padStart(2, '0');
  const timer = document.querySelector('#examTimer');
  timer.textContent = `${hours}:${minutes}:${seconds}`;
  timer.classList.toggle('expired', remaining === 0);
}

function renderActiveExam(active) {
  document.querySelector('#examSetup').hidden = true;
  document.querySelector('#examReview').hidden = true;
  document.querySelector('#examWorkspace').hidden = false;
  const task = L.taskForMode(taskById(active.taskIds[active.index]), false);
  document.querySelector('#activeExamMeta').textContent = `${active.taskIds.length} Aufgaben · Lösungen gesperrt`;
  document.querySelector('#activeExamTitle').textContent = active.title;
  document.querySelector('#examTaskPosition').textContent = `Aufgabe ${active.index + 1} von ${active.taskIds.length}`;
  document.querySelector('#flagExamTask').textContent = active.flagged.includes(task.id) ? 'Markierung entfernen' : 'Aufgabe markieren';
  document.querySelector('#examTaskBody').innerHTML = `<p class="metadata-row">${F.escapeHtml(taskMeta(task))}</p><div class="badge-row">${relevanceBadge(task)}${solutionBadge(task)}</div><h4>${F.escapeHtml(task.title)}</h4><p>${F.escapeHtml(task.prompt)}</p>${sourceLink(task.source.asset, task.source.page, 'Originalaufgabe öffnen')}`;
  document.querySelector('#previousExamTask').disabled = active.index === 0;
  document.querySelector('#nextExamTask').disabled = active.index === active.taskIds.length - 1;
  typeset(document.querySelector('#examTaskBody'));
  clearInterval(examTimerHandle);
  updateTimer();
  examTimerHandle = setInterval(updateTimer, 1000);
}

function renderExamReview(active) {
  clearInterval(examTimerHandle);
  document.querySelector('#examSetup').hidden = true;
  document.querySelector('#examWorkspace').hidden = true;
  const review = document.querySelector('#examReview');
  review.hidden = false;
  review.innerHTML = `<h3>Auswertung: ${F.escapeHtml(active.title)}</h3>
    <p class="supporting-text">Die Lösungsquellen sind jetzt freigeschaltet. Exakte Punkte sind nur bei einem offiziellen Bewertungsschema verifizierbar; alle anderen Werte bleiben geschätzte Selbstbewertungen.</p>
    ${active.taskIds.map(taskId => {
      const task = taskById(taskId);
      const scoringMode = L.scoringMode(task);
      const verified = scoringMode === 'verified_rubric';
      const max = verified ? task.points : 100;
      const unit = verified ? `erreichte Punkte von ${task.points}` : 'geschätztes Ergebnis in Prozent';
      const scoringLabel = verified ? 'Bewertung nach offiziellem Schema' : 'Geschätzte Bewertung';
      const solution = task.solution
        ? `${solutionBadge(task)} ${sourceLink(task.solution.asset, task.solution.pageStart, `${L.solutionLabel(task.officialSolutionStatus)} öffnen`)}${unofficialSolutionWarning(task)}`
        : `${solutionBadge(task)} <span class="supporting-text">Keine verifizierte Lösung vorhanden.</span>`;
      return `<section class="review-task" data-review-task="${F.escapeHtml(task.id)}" data-scoring-mode="${scoringMode}"><h4>${F.escapeHtml(task.title)}</h4><p>${F.escapeHtml(taskMeta(task))}</p>${solution}
        <p class="scoring-label">${scoringLabel}</p>
        <div class="score-row"><label class="field"><span>${unit}</span><input type="number" min="0" max="${max}" step="1" data-review-score></label>
        <label class="field"><span>Teilbewertung</span><select data-review-partial>${partialCreditOptions()}</select></label>
        <label class="field"><span>Bewertungssicherheit</span><select data-review-confidence><option value="1">1 - geraten</option><option value="2">2 - unsicher</option><option value="3" selected>3 - teilweise sicher</option><option value="4">4 - sicher</option><option value="5">5 - sehr sicher</option></select></label>
        <label class="field"><span>Hauptfehler</span><select data-review-error><option value="">kein Fehler</option>${Object.entries(errorLabels).map(([id, label]) => `<option value="${id}">${label}</option>`).join('')}</select></label></div></section>`;
    }).join('')}
    <button class="primary-button" data-save-exam-review>Auswertung speichern</button>`;
}

function renderExamState() {
  const active = getExamProgress().activeExam;
  if (!active) {
    clearInterval(examTimerHandle);
    document.querySelector('#examSetup').hidden = false;
    document.querySelector('#examWorkspace').hidden = true;
    document.querySelector('#examReview').hidden = true;
  } else if (active.status === 'review') renderExamReview(active);
  else renderActiveExam(active);
}

function moveExamTask(delta) {
  const progress = getExamProgress();
  const active = progress.activeExam;
  active.index = Math.max(0, Math.min(active.taskIds.length - 1, active.index + delta));
  saveExamProgress(progress);
  renderActiveExam(active);
}

function toggleExamFlag() {
  const progress = getExamProgress();
  const active = progress.activeExam;
  const taskId = active.taskIds[active.index];
  active.flagged = active.flagged.includes(taskId) ? active.flagged.filter(id => id !== taskId) : [...active.flagged, taskId];
  saveExamProgress(progress);
  renderActiveExam(active);
}

function finishExam() {
  if (!window.confirm('Prüfung wirklich abgeben? Danach werden die Lösungshinweise freigeschaltet.')) return;
  const progress = getExamProgress();
  progress.activeExam.status = 'review';
  progress.activeExam.finishedAt = new Date().toISOString();
  progress.activeExam.elapsedSeconds = Math.floor((Date.now() - new Date(progress.activeExam.startedAt).getTime()) / 1000);
  saveExamProgress(progress);
  renderExamReview(progress.activeExam);
}

function saveExamReview() {
  const progress = getExamProgress();
  const active = progress.activeExam;
  const results = [];
  const sections = [...document.querySelectorAll('[data-review-task]')];
  const incomplete = sections.find(section => section.querySelector('[data-review-score]').value === '' || !section.querySelector('[data-review-partial]').value);
  if (incomplete) {
    window.alert('Bitte trage für jede Aufgabe ein Ergebnis und eine Teilbewertung ein. Für unbearbeitete Aufgaben wähle 0 und „nicht bearbeitet“.');
    incomplete.querySelector('[data-review-score]').focus();
    return;
  }
  sections.forEach(section => {
    const task = taskById(section.dataset.reviewTask);
    const raw = Number(section.querySelector('[data-review-score]').value);
    const scoringMode = section.dataset.scoringMode;
    const scorePercent = scoringMode === 'verified_rubric' ? L.scorePercent(raw, task.points) : L.scorePercent(raw, 100);
    const error = section.querySelector('[data-review-error]').value;
    const confidence = Number(section.querySelector('[data-review-confidence]').value);
    const partialCreditCategory = section.querySelector('[data-review-partial]').value;
    const earnedVerifiedPoints = scoringMode === 'verified_rubric' ? raw : null;
    saveTaskAttempt(task, scorePercent, confidence, error ? [error] : [], 'prüfung', {scoringMode, partialCreditCategory, earnedVerifiedPoints});
    results.push({
      taskId: task.id, scorePercent, scoringMode, partialCreditCategory,
      earnedVerifiedPoints, estimatedPercent: scoringMode === 'self_estimated' ? raw : null,
      max: scoringMode === 'verified_rubric' ? task.points : null
    });
  });
  const refreshed = getExamProgress();
  refreshed.examRuns.push({...active, results});
  refreshed.activeExam = null;
  saveExamProgress(refreshed);
  renderExamState();
  renderTasks();
  renderErrorAnalysis();
}

function dailyQueueTasks(progress) {
  return L.dailyQueue(examData.tasks, progress.attempts, Date.now(), 10);
}

function masteryCategory(task) {
  return L.masteryCategory(task);
}

function renderErrorAnalysis() {
  const progress = getExamProgress();
  const latest = latestAttemptMap(progress);
  const attempts = [...latest.values()];
  const average = attempts.length ? attempts.reduce((sum, attempt) => sum + attempt.scorePercent, 0) / attempts.length : 0;
  const due = attempts.filter(attempt => new Date(attempt.nextReviewAt).getTime() <= Date.now()).length;
  const rubricBased = attempts.filter(attempt => attempt.scoringMode === 'verified_rubric').length;
  document.querySelector('#examMetrics').innerHTML = [
    [latest.size, 'bearbeitete Aufgaben'], [attempts.length ? `${Math.round(average)} %` : '–', 'mittlere Selbsteinschätzung'],
    [rubricBased, 'mit offiziellem Schema'], [due, 'heute fällig'], [progress.examRuns.length, 'abgeschlossene Prüfungen']
  ].map(([value, label]) => `<div class="metric-card"><strong>${F.escapeHtml(value)}</strong><span>${F.escapeHtml(label)}</span></div>`).join('');

  const queue = dailyQueueTasks(progress);
  document.querySelector('#dailyQueue').innerHTML = queue.map(({task, reason}) => `<div class="queue-item"><div><strong>${F.escapeHtml(task.title)}</strong><p>${F.escapeHtml(reason)} · ${F.escapeHtml(taskMeta(task))}</p></div><button class="secondary-button" data-open-exam-task="${F.escapeHtml(task.id)}">Bearbeiten</button></div>`).join('');

  const categories = ['Nennen', 'Anwenden', 'Beweisen', 'Erkennen'];
  document.querySelector('#masteryList').innerHTML = categories.map(category => {
    const values = examData.tasks.filter(task => masteryCategory(task) === category && latest.has(task.id)).map(task => latest.get(task.id).scorePercent);
    const score = values.length ? Math.round(values.reduce((a, b) => a + b, 0) / values.length) : 0;
    return `<div class="mastery-row"><span>${category}</span><div class="mastery-track"><div class="mastery-fill" style="width:${score}%"></div></div><strong>${values.length ? `${score}%` : '–'}</strong></div>`;
  }).join('');

  const errors = progress.attempts.filter(attempt => attempt.errors.length).slice(-20).reverse();
  document.querySelector('#errorLog').innerHTML = errors.length ? errors.map(attempt => {
    const task = taskById(attempt.taskId);
    const scoring = attempt.scoringMode === 'verified_rubric' ? 'am offiziellen Schema geprüft' : 'geschätzte Bewertung';
    return `<div class="error-entry"><div><strong>${F.escapeHtml(task?.title || attempt.taskId)}</strong><p>${attempt.errors.map(error => errorLabels[error] || error).join(', ')} · ${Math.round(attempt.scorePercent)} % · ${scoring} · ${new Date(attempt.createdAt).toLocaleDateString('de-DE')}</p></div><button class="secondary-button" data-open-exam-task="${F.escapeHtml(attempt.taskId)}">Nacharbeiten</button></div>`;
  }).join('') : '<p class="supporting-text">Noch keine Fehler protokolliert. Speichere nach einer Aufgabe Ergebnis und Fehlerart.</p>';
}

document.querySelectorAll('[data-view]').forEach(button => {
  button.addEventListener('click', () => {
    document.querySelectorAll('[data-view]').forEach(candidate => candidate.classList.remove('active'));
    button.classList.add('active');
    views.forEach(view => view.classList.toggle('active', view.id === button.dataset.view));
    typeset(document.querySelector(`#${button.dataset.view}`));
  });
});

search.addEventListener('input', renderItems);
kindFilter.addEventListener('change', renderItems);
['taskSearch', 'taskTopic', 'taskLecturer', 'taskRelevance', 'taskPoints'].forEach(id => {
  document.querySelector(`#${id}`).addEventListener(id === 'taskSearch' ? 'input' : 'change', renderTasks);
});
itemList.addEventListener('click', event => {
  const button = event.target.closest('[data-open-kind]');
  if (button) openDetail(button.dataset.openKind, button.dataset.openId);
});
document.querySelector('#taskList').addEventListener('click', event => {
  const button = event.target.closest('[data-open-exam-task]');
  if (button) openTaskDetail(button.dataset.openExamTask);
});
document.querySelector('#errors').addEventListener('click', event => {
  const button = event.target.closest('[data-open-exam-task]');
  if (button) openTaskDetail(button.dataset.openExamTask);
});
document.querySelector('#proofList').addEventListener('click', event => {
  const button = event.target.closest('[data-open-kind]');
  if (button) openDetail(button.dataset.openKind, button.dataset.openId);
});
document.querySelector('#flashcard').addEventListener('click', event => {
  const button = event.target.closest('[data-open-kind]');
  if (button) openDetail(button.dataset.openKind, button.dataset.openId);
});
document.querySelector('#quizCard').addEventListener('click', event => {
  if (event.target.closest('[data-show-quiz-answer]')) {
    event.currentTarget.querySelector('[data-quiz-answer]').hidden = false;
    event.target.closest('[data-show-quiz-answer]').disabled = true;
  }
  const detailButton = event.target.closest('[data-open-question]');
  if (detailButton) openDetail('question', detailButton.dataset.openQuestion);
});

document.querySelector('#nextQuestion').addEventListener('click', renderQuestion);
document.querySelector('#nextFlashcard').addEventListener('click', () => {
  flashcardIndex += 1;
  flashcardAnswerVisible = false;
  renderFlashcard();
});
document.querySelector('#showBack').addEventListener('click', () => {
  flashcardAnswerVisible = !flashcardAnswerVisible;
  renderFlashcard();
});

document.querySelector('#progressList').addEventListener('change', event => {
  const checkbox = event.target.closest('[data-check]');
  if (!checkbox) return;
  const progress = getProgress();
  progress[checkbox.dataset.check] = checkbox.checked;
  localStorage.setItem(progressKey, JSON.stringify(progress));
});
document.querySelector('#resetProgress').addEventListener('click', () => {
  localStorage.removeItem(progressKey);
  renderProgress();
});

document.querySelector('#examSelect').addEventListener('change', renderExamSetupMeta);
document.querySelector('#startExam').addEventListener('click', startExam);
document.querySelector('#previousExamTask').addEventListener('click', () => moveExamTask(-1));
document.querySelector('#nextExamTask').addEventListener('click', () => moveExamTask(1));
document.querySelector('#flagExamTask').addEventListener('click', toggleExamFlag);
document.querySelector('#finishExam').addEventListener('click', finishExam);
document.querySelector('#examReview').addEventListener('click', event => {
  if (event.target.closest('[data-save-exam-review]')) saveExamReview();
});
document.querySelector('#resetExamProgress').addEventListener('click', () => {
  if (!window.confirm('Alle gespeicherten Aufgabenversuche und Prüfungsläufe löschen?')) return;
  localStorage.removeItem(examProgressKey);
  renderExamState();
  renderTasks();
  renderErrorAnalysis();
});

document.querySelector('#closeTaskDetail').addEventListener('click', closeTaskDetail);
taskOverlay.addEventListener('click', event => { if (event.target === taskOverlay) closeTaskDetail(); });
taskDetailBody.addEventListener('click', event => {
  const hintButton = event.target.closest('[data-show-hint]');
  if (hintButton) {
    taskDetailBody.querySelector(`[data-hint-panel="${hintButton.dataset.showHint}"]`).hidden = false;
    hintButton.disabled = true;
  }
  const solutionButton = event.target.closest('[data-show-solution]');
  if (solutionButton) {
    taskDetailBody.querySelector('[data-solution-panel]').hidden = false;
    solutionButton.disabled = true;
  }
  if (event.target.closest('[data-save-task-attempt]')) {
    const scoreInput = document.querySelector('#taskScorePercent');
    if (scoreInput.value === '') {
      window.alert('Bitte trage zuerst ein Ergebnis zwischen 0 und 100 Prozent ein.');
      scoreInput.focus();
      return;
    }
    const score = Math.max(0, Math.min(100, Number(scoreInput.value)));
    const confidence = Number(document.querySelector('#taskConfidence').value);
    const partialCreditCategory = document.querySelector('#taskPartialCredit').value;
    if (!partialCreditCategory) {
      window.alert('Bitte wähle eine Teilbewertung aus.');
      document.querySelector('#taskPartialCredit').focus();
      return;
    }
    const errors = [...taskDetailBody.querySelectorAll('[data-task-error]:checked')].map(input => input.value);
    saveTaskAttempt(currentExamTask, score, confidence, errors, 'trainer', {partialCreditCategory});
    closeTaskDetail();
    renderTasks();
    renderErrorAnalysis();
  }
});

document.querySelector('#closeDetail').addEventListener('click', closeDetail);
detailOverlay.addEventListener('click', event => { if (event.target === detailOverlay) closeDetail(); });
document.addEventListener('keydown', event => {
  if (event.key !== 'Escape') return;
  if (!taskOverlay.hidden) closeTaskDetail();
  else if (!detailOverlay.hidden) closeDetail();
});
renderedToggle.addEventListener('click', () => { detailMode = 'rendered'; renderDetail(); });
rawToggle.addEventListener('click', () => { detailMode = 'raw'; renderDetail(); });

renderItems();
populateExamFilters();
renderTasks();
populateExamSelect();
renderExamState();
renderErrorAnalysis();
renderQuestion();
renderFlashcard();
renderProofs();
renderProgress();
