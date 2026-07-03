(function initExamLogic(globalScope) {
  const solutionLabels = {
    official_solution: 'Offizielle Lösung',
    official_rubric: 'Offizielles Bewertungsschema',
    partial_official_solution: 'Teilweise offizielle Lösung',
    reconstructed_solution: 'Rekonstruierte Lösung',
    ai_generated_solution: 'KI-generierte Lösung',
    no_solution: 'Keine verifizierte Lösung'
  };

  function solutionLabel(status) {
    return solutionLabels[status] || solutionLabels.no_solution;
  }

  function solutionWarning(status) {
    return ['reconstructed_solution', 'ai_generated_solution'].includes(status)
      ? 'Diese Lösung ist nicht offiziell und muss mathematisch geprüft werden.'
      : '';
  }

  function scoringMode(task) {
    return task?.gradingStatus === 'official_rubric' ? 'verified_rubric' : 'self_estimated';
  }

  function latestAttemptMap(attempts = []) {
    const latest = new Map();
    attempts.forEach(attempt => latest.set(attempt.taskId, attempt));
    return latest;
  }

  function scorePercent(earned, maximum) {
    const raw = Number(earned) || 0;
    const max = Number(maximum) || 100;
    return Math.max(0, Math.min(100, raw / max * 100));
  }

  function remainingSeconds(activeExam, now = Date.now()) {
    if (!activeExam) return 0;
    const total = (Number(activeExam.durationMinutes) || 180) * 60;
    const elapsed = Math.floor((Number(now) - new Date(activeExam.startedAt).getTime()) / 1000);
    return Math.max(0, total - elapsed);
  }

  function taskForMode(task, solutionsUnlocked = false) {
    if (solutionsUnlocked) return {...task};
    const {solution, ...lockedTask} = task;
    return {...lockedTask, solution: null};
  }

  function createMockTasks(tasks = [], count = 7) {
    const candidates = tasks
      .filter(task => task.currentScopeStatus === 'confirmed_current' && task.points != null)
      .sort((a, b) => b.priorityScore - a.priorityScore || a.id.localeCompare(b.id));
    const selected = [];
    const topics = new Set();
    const families = new Set();
    for (const task of candidates) {
      if (selected.length >= count) break;
      if (!topics.has(task.topics[0]) && !families.has(task.duplicateFamily)) {
        selected.push(task);
        topics.add(task.topics[0]);
        families.add(task.duplicateFamily);
      }
    }
    for (const task of candidates) {
      if (selected.length >= count) break;
      if (!selected.includes(task) && !families.has(task.duplicateFamily)) {
        selected.push(task);
        families.add(task.duplicateFamily);
      }
    }
    return selected;
  }

  function dailyQueue(tasks = [], attempts = [], now = Date.now(), limit = 10) {
    const latest = latestAttemptMap(attempts);
    const due = tasks.filter(task => latest.has(task.id) && new Date(latest.get(task.id).nextReviewAt).getTime() <= now)
      .sort((a, b) => b.priorityScore - a.priorityScore);
    const weak = tasks.filter(task => latest.has(task.id) && (latest.get(task.id).scorePercent < 70 || latest.get(task.id).confidence <= 2))
      .sort((a, b) => b.priorityScore - a.priorityScore);
    const mixed = tasks.filter(task => !latest.has(task.id) && task.currentScopeStatus === 'confirmed_current')
      .sort((a, b) => b.priorityScore - a.priorityScore);
    const result = [];
    function add(items, count, reason) {
      for (const task of items) {
        if (count <= 0 || result.length >= limit) break;
        if (!result.some(entry => entry.task.id === task.id)) {
          result.push({task, reason});
          count -= 1;
        }
      }
    }
    add(due, Math.round(limit * 0.2), 'fällige Wiederholung');
    add(weak, Math.round(limit * 0.5), 'schwache Hochwert-Aufgabe');
    add(mixed, limit - result.length, 'gemischte Prüfungspraxis');
    add([...weak, ...due, ...mixed, ...tasks].sort((a, b) => b.priorityScore - a.priorityScore), limit - result.length, 'Prioritätsausgleich');
    return result;
  }

  function masteryCategory(task) {
    if (task.techniques.includes('definition') || task.techniques.includes('satzwiedergabe')) return 'Nennen';
    if (task.techniques.includes('beweis')) return 'Beweisen';
    if (task.techniques.includes('gegenbeispiel') || task.techniques.includes('klassifikation')) return 'Erkennen';
    return 'Anwenden';
  }

  const api = {
    latestAttemptMap, scorePercent, remainingSeconds, taskForMode, createMockTasks, dailyQueue, masteryCategory,
    solutionLabel, solutionWarning, scoringMode
  };
  globalScope.ExamLogic = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
