# Proof Reconstruction Trainer

Work through each proof in levels. Try Level 4 before checking the answer if the theorem is high-yield.

## Proof Trainer 1.3.4 — Induktionsprinzip

### Level 1 — Full Outline

Statement:

```latex
If $A(1)$ is true and $\forall n\in\mathbb N: A(n)\Rightarrow A(n+1)$, then $A(n)$ is true for every $n\in\mathbb N$.
```

Outline: Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Inductive subsets and the definition of $\mathbb N$. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Inductive subsets and the definition of $\mathbb N$..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.

### Level 4 — Blank Proof Prompt

Prove Satz 1.3.4 (Induktionsprinzip) from the script's assumptions.

**Answer / solution sketch:** Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$. Then compare with `04-proofs/proof-database.md` and the PDF at p12.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A first domino plus a rule that every domino knocks over the next one proves the whole infinite chain.`, then deliver the proof skeleton `Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.`.

## Proof Trainer 1.3.6 — Bernoulli-Ungleichung

### Level 1 — Full Outline

Statement:

```latex
For $x\ge -1$ and $n\in\mathbb N$, $(1+x)^n\ge 1+nx$, with strict inequality for $n\ge2$ and $x\ne0$.
```

Outline: Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Induction and order rules. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Induction and order rules..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.

### Level 4 — Blank Proof Prompt

Prove Satz 1.3.6 (Bernoulli-Ungleichung) from the script's assumptions.

**Answer / solution sketch:** Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step. Then compare with `04-proofs/proof-database.md` and the PDF at p14.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `The first-order linear term underestimates the power for admissible $x$.`, then deliver the proof skeleton `Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.`.

## Proof Trainer 1.6.1 — Prinzip von Archimedes

### Level 1 — Full Outline

Statement:

```latex
For every $x\in\mathbb R$ there is $n\in\mathbb N$ with $n>x$.
```

Outline: Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Completeness and supremum. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Completeness and supremum..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.

### Level 4 — Blank Proof Prompt

Prove Satz 1.6.1 (Prinzip von Archimedes) from the script's assumptions.

**Answer / solution sketch:** Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound. Then compare with `04-proofs/proof-database.md` and the PDF at p20.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Natural numbers eventually exceed any fixed real number.`, then deliver the proof skeleton `Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.`.

## Proof Trainer 1.6.5 — Dichtheit von Q in R

### Level 1 — Full Outline

Statement:

```latex
If $a<b$ in $\mathbb R$, then there is $q\in\mathbb Q$ with $a<q<b$.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Archimedean principle and floor function. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Archimedean principle and floor function..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 1.6.5 (Dichtheit von Q in R) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p21.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Between any two real numbers sits a rational number.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 1.6.10 — Intervallschachtelungsprinzip

### Level 1 — Full Outline

Statement:

```latex
Every nested sequence of compact intervals whose lengths tend to $0$ has intersection consisting of exactly one point.
```

Outline: Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Completeness, compact intervals, supremum/infimum. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Completeness, compact intervals, supremum/infimum..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.

### Level 4 — Blank Proof Prompt

Prove Satz 1.6.10 (Intervallschachtelungsprinzip) from the script's assumptions.

**Answer / solution sketch:** Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness. Then compare with `04-proofs/proof-database.md` and the PDF at p24.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Nested closed intervals that shrink indefinitely trap one real number.`, then deliver the proof skeleton `Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.`.

## Proof Trainer 2.1.7 — Monotonieprinzip

### Level 1 — Full Outline

Statement:

```latex
A monotone increasing sequence that is bounded above converges to the supremum of its value set; analogously for decreasing sequences.
```

Outline: Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Completeness, supremum, sequence convergence. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Completeness, supremum, sequence convergence..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.

### Level 4 — Blank Proof Prompt

Prove Satz 2.1.7 (Monotonieprinzip) from the script's assumptions.

**Answer / solution sketch:** Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$. Then compare with `04-proofs/proof-database.md` and the PDF at p40.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A one-directional bounded sequence cannot wander forever; completeness forces a limit.`, then deliver the proof skeleton `Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.`.

## Proof Trainer 2.2.2 — Konvergenz und algebraische Operationen

### Level 1 — Full Outline

Statement:

```latex
If $a_n\to a$ and $b_n\to b$, then sums, scalar multiples, products, and quotients with nonzero denominator converge to the corresponding algebraic limits.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Epsilon definition, boundedness of convergent sequences. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Epsilon definition, boundedness of convergent sequences..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 2.2.2 (Konvergenz und algebraische Operationen) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p41.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Limits respect ordinary algebra when the expressions are well-defined.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 2.2.5 — Einschließungsprinzip

### Level 1 — Full Outline

Statement:

```latex
If $a_n\le b_n\le c_n$ eventually and $a_n,c_n\to a$, then $b_n\to a$.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Comparison principle. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Comparison principle..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 2.2.5 (Einschließungsprinzip) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p43.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A squeezed sequence must follow the common limit of the bounds.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 2.4.4 — Satz von Bolzano-Weierstraß

### Level 1 — Full Outline

Statement:

```latex
Every bounded real sequence has an accumulation value, equivalently a convergent subsequence.
```

Outline: Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Completeness, monotone convergence, subsequences, accumulation values. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Completeness, monotone convergence, subsequences, accumulation values..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.

### Level 4 — Blank Proof Prompt

Prove Satz 2.4.4 (Satz von Bolzano-Weierstraß) from the script's assumptions.

**Answer / solution sketch:** Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence. Then compare with `04-proofs/proof-database.md` and the PDF at p47.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Bounded infinite data in the real line contains a convergent pattern.`, then deliver the proof skeleton `Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.`.

## Proof Trainer 2.4.9 — Cauchy-Kriterium

### Level 1 — Full Outline

Statement:

```latex
A real sequence converges if and only if it is a Cauchy sequence.
```

Outline: Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Completeness, boundedness, Bolzano-Weierstrass. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Completeness, boundedness, Bolzano-Weierstrass..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.

### Level 4 — Blank Proof Prompt

Prove Satz 2.4.9 (Cauchy-Kriterium) from the script's assumptions.

**Answer / solution sketch:** Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit. Then compare with `04-proofs/proof-database.md` and the PDF at p48.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `In $\mathbb R$, terms becoming mutually close is enough to guarantee an actual limit.`, then deliver the proof skeleton `Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.`.

## Proof Trainer 3.2.3 — Cauchy-Kriterium für Reihen

### Level 1 — Full Outline

Statement:

```latex
A series $\sum a_n$ converges iff its tails $\sum_{k=m+1}^n a_k$ become arbitrarily small.
```

Outline: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Cauchy criterion for sequences and partial sums. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Cauchy criterion for sequences and partial sums..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.

### Level 4 — Blank Proof Prompt

Prove Satz 3.2.3 (Cauchy-Kriterium für Reihen) from the script's assumptions.

**Answer / solution sketch:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails. Then compare with `04-proofs/proof-database.md` and the PDF at p58.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A series converges exactly when distant tail sums carry no mass.`, then deliver the proof skeleton `Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.`.

## Proof Trainer 3.4.2 — Abelsches Konvergenzlemma

### Level 1 — Full Outline

Statement:

```latex
If $|a_n|s^n\le M$ for some $s,M>0$, then $\sum a_nz^n$ converges absolutely for $|z|<s$.
```

Outline: Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Majorant criterion and geometric series. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Majorant criterion and geometric series..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.

### Level 4 — Blank Proof Prompt

Prove Lemma 3.4.2 (Abelsches Konvergenzlemma) from the script's assumptions.

**Answer / solution sketch:** Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series. Then compare with `04-proofs/proof-database.md` and the PDF at p62.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A power series that is controlled at one radius is dominated inside that radius by a geometric series.`, then deliver the proof skeleton `Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.`.

## Proof Trainer 3.4.4 — Konvergenzradius

### Level 1 — Full Outline

Statement:

```latex
Every power series has a radius $R$ such that it converges absolutely for $|z|<R$ and diverges for $|z|>R$.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Abel lemma, supremum, absolute convergence. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Abel lemma, supremum, absolute convergence..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 3.4.4 (Konvergenzradius) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p62.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Power series have circular domains of guaranteed convergence.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 4.2.1 — Zwischenwertsatz

### Level 1 — Full Outline

Statement:

```latex
If $f:[a,b]\to\mathbb R$ is continuous and $c$ lies between $f(a)$ and $f(b)$, then some $\xi\in[a,b]$ satisfies $f(\xi)=c$.
```

Outline: Use a supremum/nested interval argument on the set where the function lies below the target.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Continuity, intervals, completeness. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Continuity, intervals, completeness..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use a supremum/nested interval argument on the set where the function lies below the target.

### Level 4 — Blank Proof Prompt

Prove Satz 4.2.1 (Zwischenwertsatz) from the script's assumptions.

**Answer / solution sketch:** Use a supremum/nested interval argument on the set where the function lies below the target. Then compare with `04-proofs/proof-database.md` and the PDF at p70.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A continuous graph cannot jump over intermediate heights.`, then deliver the proof skeleton `Use a supremum/nested interval argument on the set where the function lies below the target.`.

## Proof Trainer 4.3.2 — Satz vom Maximum und Minimum

### Level 1 — Full Outline

Statement:

```latex
A continuous real-valued function on a compact interval is bounded and attains its maximum and minimum.
```

Outline: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Continuity, Bolzano-Weierstrass/compact interval behavior. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Continuity, Bolzano-Weierstrass/compact interval behavior..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

### Level 4 — Blank Proof Prompt

Prove Folgerung 4.3.2 (Satz vom Maximum und Minimum) from the script's assumptions.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods. Then compare with `04-proofs/proof-database.md` and the PDF at p72.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A continuous function on a closed bounded interval cannot escape and must reach its extremes.`, then deliver the proof skeleton `Use epsilon-delta or sequential continuity and track the relevant neighborhoods.`.

## Proof Trainer 5.2.4 — Kettenregel

### Level 1 — Full Outline

Statement:

```latex
If $f$ is differentiable at $x_0$ and $g$ at $f(x_0)$, then $(g\circ f)'(x_0)=g'(f(x_0))f'(x_0)$.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Derivative definition and linear approximation. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Derivative definition and linear approximation..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 5.2.4 (Kettenregel) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p82.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Rates multiply through composition.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 5.3.5 — Mittelwertsatz

### Level 1 — Full Outline

Statement:

```latex
If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then $f(b)-f(a)=f'(\xi)(b-a)$ for some $\xi\in(a,b)$.
```

Outline: Subtract the secant line and apply Rolle's theorem.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Rolle's theorem, extrema theorem, differentiability. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Rolle's theorem, extrema theorem, differentiability..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Subtract the secant line and apply Rolle's theorem.

### Level 4 — Blank Proof Prompt

Prove Satz 5.3.5 (Mittelwertsatz) from the script's assumptions.

**Answer / solution sketch:** Subtract the secant line and apply Rolle's theorem. Then compare with `04-proofs/proof-database.md` and the PDF at p86.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Some instantaneous slope equals the average slope.`, then deliver the proof skeleton `Subtract the secant line and apply Rolle's theorem.`.

## Proof Trainer 6.4.2 — Hauptsatz der Differential- und Integralrechnung

### Level 1 — Full Outline

Statement:

```latex
Integration and differentiation are inverse in the precise forms stated in the script for regulated/continuous functions.
```

Outline: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Integral definition, continuity/regulated functions, derivative rules. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Integral definition, continuity/regulated functions, derivative rules..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

### Level 4 — Blank Proof Prompt

Prove Satz 6.4.2 (Hauptsatz der Differential- und Integralrechnung) from the script's assumptions.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods. Then compare with `04-proofs/proof-database.md` and the PDF at p103.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Accumulated change differentiates back to the original rate, and antiderivatives compute integrals.`, then deliver the proof skeleton `Use epsilon-delta or sequential continuity and track the relevant neighborhoods.`.

## Proof Trainer 6.6.5 — Taylorformel

### Level 1 — Full Outline

Statement:

```latex
A sufficiently differentiable function equals its Taylor polynomial plus a controlled remainder term.
```

Outline: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Higher derivatives, mean value ideas, integration/differentiation. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Higher derivatives, mean value ideas, integration/differentiation..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.

### Level 4 — Blank Proof Prompt

Prove Satz 6.6.5 (Taylorformel) from the script's assumptions.

**Answer / solution sketch:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails. Then compare with `04-proofs/proof-database.md` and the PDF at p108.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Near a point, derivatives determine a polynomial approximation with a measurable error.`, then deliver the proof skeleton `Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.`.

## Proof Trainer 7.1.14 — Höldersche Ungleichung

### Level 1 — Full Outline

Statement:

```latex
If $p,q>1$ and $1/p+1/q=1$, then $\sum |z_kw_k|\le \|z\|_p\|w\|_q$.
```

Outline: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Young inequality and $p$-norms. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Young inequality and $p$-norms..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.

### Level 4 — Blank Proof Prompt

Prove Satz 7.1.14 (Höldersche Ungleichung) from the script's assumptions.

**Answer / solution sketch:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails. Then compare with `04-proofs/proof-database.md` and the PDF at p118.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Dual exponents control products by separate norms.`, then deliver the proof skeleton `Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.`.

## Proof Trainer 7.1.15 — Minkowski-Ungleichung

### Level 1 — Full Outline

Statement:

```latex
For $p\ge1$, $\|z+w\|_p\le \|z\|_p+\|w\|_p$.
```

Outline: Start from the defining inequality or a known inequality, then estimate term by term.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Holder inequality. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Holder inequality..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Start from the defining inequality or a known inequality, then estimate term by term.

### Level 4 — Blank Proof Prompt

Prove Satz 7.1.15 (Minkowski-Ungleichung) from the script's assumptions.

**Answer / solution sketch:** Start from the defining inequality or a known inequality, then estimate term by term. Then compare with `04-proofs/proof-database.md` and the PDF at p118.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `The $p$-norm satisfies the triangle inequality.`, then deliver the proof skeleton `Start from the defining inequality or a known inequality, then estimate term by term.`.

## Proof Trainer 7.5.6 — Satz vom Maximum und Minimum

### Level 1 — Full Outline

Statement:

```latex
A continuous real-valued function on a compact topological space is bounded and attains maximum and minimum.
```

Outline: Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Compactness and continuity. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Compactness and continuity..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.

### Level 4 — Blank Proof Prompt

Prove Satz 7.5.6 (Satz vom Maximum und Minimum) from the script's assumptions.

**Answer / solution sketch:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction. Then compare with `04-proofs/proof-database.md` and the PDF at p142.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Compactness is the correct general reason extrema exist.`, then deliver the proof skeleton `Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.`.

## Proof Trainer 7.6.2 — Zusammenhängende Teilmengen von R

### Level 1 — Full Outline

Statement:

```latex
A subset of $\mathbb R$ is connected if and only if it is an interval.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Connectedness, intervals, order topology. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Connectedness, intervals, order topology..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 7.6.2 (Zusammenhängende Teilmengen von R) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p144.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `On the real line, connectedness is exactly having no gaps.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 8.1.8 — Kettenregel

### Level 1 — Full Outline

Statement:

```latex
For differentiable maps, $d(g\circ f)(a)=dg(f(a))\circ df(a)$.
```

Outline: Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Differential as linear map. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Differential as linear map..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.

### Level 4 — Blank Proof Prompt

Prove Satz 8.1.8 (Kettenregel) from the script's assumptions.

**Answer / solution sketch:** Write both maps as linear part plus a small remainder and show the composed remainder is still higher order. Then compare with `04-proofs/proof-database.md` and the PDF at p153.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Linear approximations compose.`, then deliver the proof skeleton `Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.`.

## Proof Trainer 8.2.10 — Hauptkriterium für Differenzierbarkeit

### Level 1 — Full Outline

Statement:

```latex
If all partial derivatives exist in a neighborhood of $a$ and are continuous at $a$, then $f$ is differentiable at $a$.
```

Outline: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Partial derivatives, Jacobian, continuity. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Partial derivatives, Jacobian, continuity..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

### Level 4 — Blank Proof Prompt

Prove Satz 8.2.10 (Hauptkriterium für Differenzierbarkeit) from the script's assumptions.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods. Then compare with `04-proofs/proof-database.md` and the PDF at p157.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Continuous partial derivatives are enough to assemble a true linear approximation.`, then deliver the proof skeleton `Use epsilon-delta or sequential continuity and track the relevant neighborhoods.`.

## Proof Trainer 8.3.7 — Schrankensatz

### Level 1 — Full Outline

Statement:

```latex
$\|f(b)-f(a)\|\le \sup_{t\in[0,1]}\|df((1-t)a+tb)\|_{\mathrm{op}}\|b-a\|$ under the stated hypotheses.
```

Outline: Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Integral representation and operator norm. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Integral representation and operator norm..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.

### Level 4 — Blank Proof Prompt

Prove Satz 8.3.7 (Schrankensatz) from the script's assumptions.

**Answer / solution sketch:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction. Then compare with `04-proofs/proof-database.md` and the PDF at p158.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Derivative bounds control total change.`, then deliver the proof skeleton `Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.`.

## Proof Trainer 8.4.3 — Satz von Schwarz

### Level 1 — Full Outline

Statement:

```latex
Under the script's continuity hypotheses, mixed partial derivatives commute: $\partial_i\partial_j f(a)=\partial_j\partial_i f(a)$.
```

Outline: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Partial derivatives and continuity. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Partial derivatives and continuity..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.

### Level 4 — Blank Proof Prompt

Prove Satz 8.4.3 (Satz von Schwarz) from the script's assumptions.

**Answer / solution sketch:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods. Then compare with `04-proofs/proof-database.md` and the PDF at p159.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `With enough regularity, the order of differentiating in two directions does not matter.`, then deliver the proof skeleton `Use epsilon-delta or sequential continuity and track the relevant neighborhoods.`.

## Proof Trainer 8.5.3 — Taylorformel

### Level 1 — Full Outline

Statement:

```latex
A $C^{p+1}$ multivariable function equals its Taylor polynomial of degree $p$ plus the stated Lagrange/integral remainder on a segment.
```

Outline: Apply one-variable Taylor reasoning along the segment from the base point to the evaluation point.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Higher differentials and one-variable Taylor along line segments. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Higher differentials and one-variable Taylor along line segments..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Apply one-variable Taylor reasoning along the segment from the base point to the evaluation point.

### Level 4 — Blank Proof Prompt

Prove Satz 8.5.3 (Taylorformel) from the script's assumptions.

**Answer / solution sketch:** Apply one-variable Taylor reasoning along the segment from the base point to the evaluation point. Then compare with `04-proofs/proof-database.md` and the PDF at p161.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Multivariable functions have polynomial local models governed by higher differentials.`, then deliver the proof skeleton `Apply one-variable Taylor reasoning along the segment from the base point to the evaluation point.`.

## Proof Trainer 8.6.3 — Fermatsches Kriterium

### Level 1 — Full Outline

Statement:

```latex
If $f$ is differentiable and has a local extremum at an interior point $a$, then $df(a)=0$.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Differentiability and one-dimensional extremum idea along lines. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Differentiability and one-dimensional extremum idea along lines..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 8.6.3 (Fermatsches Kriterium) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p161.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `At an interior optimum, every first-order direction has zero slope.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 8.6.4 — Hinreichendes Kriterium für lokale Extrema

### Level 1 — Full Outline

Statement:

```latex
At a critical point, positive definite Hessian gives a strict local minimum, negative definite gives a strict local maximum, and indefinite gives no local extremum.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Taylor formula and Hessian definiteness. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Taylor formula and Hessian definiteness..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 8.6.4 (Hinreichendes Kriterium für lokale Extrema) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p161.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `The quadratic part determines local shape when it is decisive.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 9.1.2 — Banachscher Fixpunktsatz

### Level 1 — Full Outline

Statement:

```latex
A contraction on a complete metric space has a unique fixed point, and the iteration $x_n=f(x_{n-1})$ converges to it with the stated error estimate.
```

Outline: Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Complete metric spaces, Cauchy sequences, contractions. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Complete metric spaces, Cauchy sequences, contractions..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.

### Level 4 — Blank Proof Prompt

Prove Satz 9.1.2 (Banachscher Fixpunktsatz) from the script's assumptions.

**Answer / solution sketch:** Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness. Then compare with `04-proofs/proof-database.md` and the PDF at p166.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `Repeated shrinking forces all iterates into one unavoidable point.`, then deliver the proof skeleton `Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.`.

## Proof Trainer 9.2.5 — Umkehrsatz

### Level 1 — Full Outline

Statement:

```latex
If $f\in C^k$ and $df(a)$ is an isomorphism, then $f$ is locally a $C^k$-diffeomorphism near $a$.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Differentials, Banach fixed point/estimates, inverse derivative rule. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Differentials, Banach fixed point/estimates, inverse derivative rule..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 9.2.5 (Umkehrsatz) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p168.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `An invertible linearization makes the nonlinear map locally invertible.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 9.3.1 — Satz über implizite Funktionen

### Level 1 — Full Outline

Statement:

```latex
If $d_y f(x_0,y_0)$ is invertible, then near $(x_0,y_0)$ the equation $f(x,y)=z_0$ can be solved uniquely as $y=g(x)$.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Inverse function theorem and block differentials. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Inverse function theorem and block differentials..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 9.3.1 (Satz über implizite Funktionen) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p171.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `A nondegenerate equation can locally be solved for the chosen variables.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.

## Proof Trainer 9.4.1 — Multiplikatorregel von Lagrange

### Level 1 — Full Outline

Statement:

```latex
At a constrained local extremum with independent constraint gradients, $\nabla f(a)$ lies in the span of the constraint gradients.
```

Outline: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.

### Level 2 — Missing Justifications

Fill in why each implication is valid: hypotheses -> construction -> Implicit function theorem, gradients, extrema. -> conclusion.

**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: Implicit function theorem, gradients, extrema..

### Level 3 — Hints Only

Hints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

### Level 4 — Blank Proof Prompt

Prove Satz 9.4.1 (Multiplikatorregel von Lagrange) from the script's assumptions.

**Answer / solution sketch:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result. Then compare with `04-proofs/proof-database.md` and the PDF at p174.

### Level 5 — Oral Exam Version

Explain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?

**Answer / solution sketch:** Say the statement, give the intuition `At a constrained optimum, the objective gradient has no component tangent to the constraint surface.`, then deliver the proof skeleton `Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.`.
