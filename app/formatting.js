(function initStudyFormatting(globalScope) {
  const DIFFICULTY = {
    low: 'niedrig',
    medium: 'mittel',
    high: 'hoch',
    niedrig: 'niedrig',
    mittel: 'mittel',
    hoch: 'hoch'
  };

  const KIND = {
    Definition: 'Definition',
    Satz: 'Satz',
    Lemma: 'Lemma',
    Folgerung: 'Folgerung',
    Korollar: 'Korollar',
    Beispiel: 'Beispiel',
    Bemerkung: 'Bemerkung',
    Beweis: 'Beweis',
    proof: 'Beweis'
  };

  function escapeHtml(value = '') {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function normalizeLatex(value = '') {
    let text = String(value).replace(/\\\\([A-Za-z])/g, '\\$1');
    text = text.replace(/\\mathbb\s+([RNCQZ])/g, '\\mathbb{$1}');
    text = text.replace(/\\sqrt\s+([A-Za-z0-9]+)/g, '\\sqrt{$1}');
    text = text.replace(/\\(mapsto|in|exists|forall)(?=[A-Za-z])/g, '\\$1 ');
    text = text.replace(/\\le\b/g, '\\leq').replace(/\\ge\b/g, '\\geq');
    return text.trim();
  }

  function validateLatex(value = '') {
    const text = String(value);
    const issues = [];
    let depth = 0;
    let escaped = false;
    for (const char of text) {
      if (escaped) {
        escaped = false;
        continue;
      }
      if (char === '\\') {
        escaped = true;
        continue;
      }
      if (char === '{') depth += 1;
      if (char === '}') {
        depth -= 1;
        if (depth < 0) {
          issues.push('schließende Klammer ohne öffnende Klammer');
          depth = 0;
        }
      }
    }
    if (depth !== 0) issues.push('nicht geschlossene geschweifte Klammer');
    if (/\\sqrt(?!\s*(?:\[|\{))/.test(text)) issues.push('Wurzel ohne sicheres Argument');
    if (/(?<!\\)\b(?:mathbb|Rightarrow|varepsilon)\b/.test(text)) issues.push('LaTeX-Befehl ohne Backslash');
    if ((text.match(/\$/g) || []).length % 2 !== 0) issues.push('ungerade Anzahl von Dollar-Trennzeichen');
    if ((text.match(/\\\(/g) || []).length !== (text.match(/\\\)/g) || []).length) {
      issues.push('nicht passende Inline-Mathematik-Trennzeichen');
    }
    if ((text.match(/\\\[/g) || []).length !== (text.match(/\\\]/g) || []).length) {
      issues.push('nicht passende Display-Mathematik-Trennzeichen');
    }
    return [...new Set(issues)];
  }

  function readableFallback(value = '') {
    let text = normalizeLatex(value);
    const replacements = {
      '\\mathbb{R}': 'ℝ',
      '\\mathbb{C}': 'ℂ',
      '\\mathbb{N}_0': 'ℕ₀',
      '\\mathbb{N}': 'ℕ',
      '\\mathbb{Q}': 'ℚ',
      '\\mathbb{Z}': 'ℤ',
      '\\subseteq': '⊆',
      '\\subset': '⊂',
      '\\supset': '⊃',
      '\\notin': '∉',
      '\\in': '∈',
      '\\mapsto': '↦',
      '\\to': '→',
      '\\Rightarrow': '⇒',
      '\\Longleftrightarrow': '⇔',
      '\\leq': '≤',
      '\\geq': '≥',
      '\\emptyset': '∅',
      '\\infty': '∞',
      '\\varepsilon': 'ε',
      '\\lambda': 'λ',
      '\\xi': 'ξ',
      '\\varphi': 'φ',
      '\\cap': '∩',
      '\\cup': '∪',
      '\\setminus': '∖'
    };
    for (const [from, to] of Object.entries(replacements)) text = text.split(from).join(to);
    text = text.replace(/\\sqrt\[([^\]]+)\]\{([^{}]+)\}/g, '$1-te Wurzel aus ($2)');
    text = text.replace(/\\sqrt\{([^{}]+)\}/g, '√($1)');
    text = text.replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '($1)/($2)');
    text = text.replace(/\\([A-Za-z]+)/g, '$1');
    return text.replace(/\s+/g, ' ').trim();
  }

  function mathMarkup(value, display = true, itemId = '') {
    const tex = normalizeLatex(value);
    const issues = validateLatex(tex);
    if (issues.length) {
      console.warn('Mathematische Quelle muss geprüft werden', { itemId, issues, tex });
      return `<span class="math-fallback">${escapeHtml(readableFallback(tex))}</span>`;
    }
    return display ? `\\[${escapeHtml(tex)}\\]` : `\\(${escapeHtml(tex)}\\)`;
  }

  function metadataText(metadata = {}) {
    const parts = [metadata.document || 'PDF'];
    if (metadata.page) parts.push(`Seite ${metadata.page}`);
    if (metadata.sectionNumber) parts.push(`Abschnitt ${metadata.sectionNumber}`);
    if (metadata.sectionTitle) parts.push(metadata.sectionTitle);
    return parts.join(' · ');
  }

  function titleText(item = {}) {
    const type = KIND[item.kind] || '';
    const number = item.id ? ` ${item.id}` : '';
    const subtitle = String(item.title || '').trim();
    return `${type}${number}${subtitle ? `: ${subtitle}` : ''}`.trim();
  }

  function difficultyLabel(value = '') {
    return DIFFICULTY[value] || 'mittel';
  }

  function renderBlocks(blocks = [], itemId = '', raw = false, mathEnabled = true) {
    if (raw) {
      const rawText = blocks.map(block => block.tex || block.text || '').join('\n\n');
      return `<pre class="raw-source">${escapeHtml(rawText)}</pre>`;
    }
    return blocks.map(block => {
      if (block.type === 'label') return `<h4 class="content-label">${escapeHtml(block.text)}</h4>`;
      if (block.type === 'math') {
        const content = mathEnabled
          ? mathMarkup(block.tex, true, itemId)
          : `<span class="math-fallback">${escapeHtml(readableFallback(block.tex))}</span>`;
        return `<div class="formula-block">${content}</div>`;
      }
      return `<p>${escapeHtml(block.text || '')}</p>`;
    }).join('');
  }

  const api = {
    DIFFICULTY,
    KIND,
    escapeHtml,
    normalizeLatex,
    validateLatex,
    readableFallback,
    mathMarkup,
    metadataText,
    titleText,
    difficultyLabel,
    renderBlocks
  };

  globalScope.StudyFormatting = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);
