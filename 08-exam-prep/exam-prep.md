# Exam Preparation

## High-Yield Theorem List

- Satz 1.3.4: Induktionsprinzip — Used for powers, binomial identities, estimates, and recursive definitions.
- Satz 1.3.6: Bernoulli-Ungleichung — Used in estimates for sequences, exponential-type behavior, and convergence arguments.
- Satz 1.6.1: Prinzip von Archimedes — Converts qualitative smallness into explicit natural-number thresholds.
- Satz 1.6.5: Dichtheit von Q in R — Used for approximation, interval arguments, and examples/counterexamples.
- Satz 1.6.10: Intervallschachtelungsprinzip — A concrete form of completeness used in convergence and existence proofs.
- Satz 2.1.7: Monotonieprinzip — Used in Bolzano-Weierstrass, series tests, and many existence proofs.
- Satz 2.2.2: Konvergenz und algebraische Operationen — The main toolkit for computing limits.
- Satz 2.2.5: Einschließungsprinzip — Useful for limits where direct algebra is awkward.
- Satz 2.4.4: Satz von Bolzano-Weierstraß — A cornerstone for compactness and many existence arguments.
- Satz 2.4.9: Cauchy-Kriterium — Central for convergence proofs where the candidate limit is unknown.
- Satz 3.2.3: Cauchy-Kriterium für Reihen — Basis of many convergence tests.
- Lemma 3.4.2: Abelsches Konvergenzlemma — Key step for radius of convergence.
- Satz 3.4.4: Konvergenzradius — Organizes all power-series questions.
- Satz 4.2.1: Zwischenwertsatz — Existence theorem for roots and equations.
- Folgerung 4.3.2: Satz vom Maximum und Minimum — Fundamental for optimization and compactness.
- Satz 5.2.4: Kettenregel — Essential calculation rule for derivatives.
- Satz 5.3.5: Mittelwertsatz — Drives monotonicity, estimates, inverse arguments, and l'Hospital-type reasoning.
- Satz 6.4.2: Hauptsatz der Differential- und Integralrechnung — Central bridge between calculus operations.
- Satz 6.6.5: Taylorformel — Used for approximation, asymptotics, extrema, and estimates.
- Satz 7.1.14: Höldersche Ungleichung — Supports norm inequalities and functional estimates.
- Satz 7.1.15: Minkowski-Ungleichung — Shows $\|\cdot\|_p$ is a norm.
- Satz 7.5.6: Satz vom Maximum und Minimum — Generalizes the interval theorem and supports optimization.
- Satz 7.6.2: Zusammenhängende Teilmengen von R — Topological explanation of intermediate-value phenomena.
- Satz 8.1.8: Kettenregel — Essential for multivariable derivative computations.
- Satz 8.2.10: Hauptkriterium für Differenzierbarkeit — Practical differentiability test.
- Satz 8.3.7: Schrankensatz — Used for Lipschitz estimates and contraction arguments.
- Satz 8.4.3: Satz von Schwarz — Justifies symmetric Hessians and higher derivative notation.
- Satz 8.5.3: Taylorformel — Used for approximation and local extrema.
- Satz 8.6.3: Fermatsches Kriterium — Starts local-extrema analysis.
- Satz 8.6.4: Hinreichendes Kriterium für lokale Extrema — Main second-derivative test.
- Satz 9.1.2: Banachscher Fixpunktsatz — Existence/uniqueness engine behind inverse and implicit function arguments.
- Satz 9.2.5: Umkehrsatz — One of the main local structure theorems of multivariable analysis.
- Satz 9.3.1: Satz über implizite Funktionen — Explains constraint solving and manifolds as graphs.
- Satz 9.4.1: Multiplikatorregel von Lagrange — Main method for constrained optimization.

## Must-Know Definitions

- Def 1.1.1: Körperaxiome — This is the algebraic rulebook that makes the usual manipulation of numbers legitimate.
- Def 1.2.1: total angeordneter Körper — A compatible order lets algebra and inequalities work together.
- Def 1.5.1: Supremum/Infimum — The supremum is the least ceiling, even if the set never reaches it.
- Def 1.5.3: Vollständigkeitsaxiom — The real line has no gaps.
- Def 2.1.1: Konvergenz einer Folge — Eventually every tail of the sequence lies in every prescribed epsilon-neighborhood of the limit.
- Def 3.3.1: Absolute Konvergenz — The series converges even after removing all cancellation.
- Def 4.1.1: Stetigkeit — Inputs close to $x_0$ force outputs close to $f(x_0)$.
- Def 5.1.1: Differenzierbarkeit — The function has a best linear first-order approximation at the point.
- Def 6.2.4: Integral von Treppenfunktionen — Area is built by summing rectangles.
- Def 7.2.1: Metrik — A metric abstracts distance.
- Def 7.2.9: Vollständigkeit in metrischen Räumen — The space has no missing Cauchy limits.
- Def 7.3.1: Offene Menge — Every point has local room to move without leaving the set.
- Def 7.4.1: Stetige Abbildungen zwischen metrischen Räumen — Small input-distance implies small output-distance.
- Def 7.5.1: Kompaktheit — Compact sets are small enough for infinite processes to have finite/convergent structure.
- Def 8.1.1: Differenzierbarkeit in normierten Räumen — The derivative is the best linear approximation in all directions at once.
- Def 9.1.1: Kontraktion — The map strictly shrinks distances.

## Must-Be-Able-To-Prove List

- 1.3.4: Induktionsprinzip — Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.
- 1.3.6: Bernoulli-Ungleichung — Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.
- 1.6.1: Prinzip von Archimedes — Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.
- 1.6.5: Dichtheit von Q in R — Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- 1.6.10: Intervallschachtelungsprinzip — Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.
- 2.1.7: Monotonieprinzip — Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.
- 2.2.2: Konvergenz und algebraische Operationen — Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- 2.2.5: Einschließungsprinzip — Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- 2.4.4: Satz von Bolzano-Weierstraß — Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.
- 2.4.9: Cauchy-Kriterium — Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.
- 3.2.3: Cauchy-Kriterium für Reihen — Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- 3.4.2: Abelsches Konvergenzlemma — Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.
- 3.4.4: Konvergenzradius — Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- 4.2.1: Zwischenwertsatz — Use a supremum/nested interval argument on the set where the function lies below the target.
- 5.2.4: Kettenregel — Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- 5.3.5: Mittelwertsatz — Subtract the secant line and apply Rolle's theorem.
- 7.5.6: Satz vom Maximum und Minimum — Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- 7.6.2: Zusammenhängende Teilmengen von R — Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- 8.1.8: Kettenregel — Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.
- 8.4.3: Satz von Schwarz — Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- 9.1.2: Banachscher Fixpunktsatz — Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.
- 9.4.1: Multiplikatorregel von Lagrange — Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.

## Typical Exercise Types

- Prove convergence using epsilon definitions, comparison, squeeze, monotonicity, or Cauchy.
- Determine convergence of series using comparison, absolute convergence, and power-series radius.
- Verify continuity/differentiability and compute derivatives/Jacobians.
- Use IVT/max-min/compactness to prove existence.
- Use Taylor formulas for approximation and local extrema.
- Check whether a set is open/closed/compact/connected in a metric/topological space.
- Apply Banach fixed point, inverse function theorem, implicit function theorem, or Lagrange multipliers.

## Common Proof Templates

- **Supremum proof:** define a candidate by sup/inf, show it satisfies the desired bound, then prove uniqueness or convergence.
- **Epsilon proof:** choose thresholds from earlier convergence estimates and combine them with triangle inequality.
- **Compactness proof:** extract a convergent subsequence or pass compactness through a continuous map.
- **Differential estimate proof:** write a first-order/Taylor/integral representation and bound the remainder.
- **Fixed point proof:** show iterates are Cauchy, use completeness, pass to the limit, prove uniqueness by contraction.

## Common Counterexample Patterns

- Bounded does not imply convergent: $(-1)^n$.
- Dense does not mean complete: $\mathbb Q$ is dense in $\mathbb R$ but incomplete.
- Pointwise convergence does not imply uniform convergence.
- Derivative zero on a disconnected domain need not imply global constancy across components.
- Nonzero Jacobian everywhere does not imply global injectivity without extra hypotheses.

## Checklist Before Exam

- Can you state every high-yield definition and theorem without notes?
- Can you name the assumption most often forgotten for each theorem?
- Can you reconstruct the proofs in `07-proof-training/` at Level 4?
- Can you solve at least one example/exercise type from every chapter?
- Can you explain the dependency chain from completeness to inverse/implicit functions?

## Oral Exam Questions

- Explain why completeness is needed for the Cauchy criterion.
- State Bolzano-Weierstrass and give the proof idea.
- Explain compactness and why continuous images of compact sets matter.
- Explain differentiability as linear approximation.
- State the inverse and implicit function theorems and compare them.
- Explain the Lagrange multiplier condition geometrically.

## Written Exam Questions

- Prove a sequence converges or is Cauchy from estimates.
- Determine a radius of convergence and discuss boundary cases.
- Prove existence of a root or extremum using continuity/compactness.
- Compute a Jacobian and use an inverse/implicit theorem locally.
- Find constrained extrema with Lagrange multipliers.

## If You Only Have 7 Days Left

1. Day 1: Chapters 1-2 definitions, completeness, monotone convergence, Bolzano-Weierstrass, Cauchy.
2. Day 2: Series and power series; drill convergence criteria and flashcards.
3. Day 3: Continuity and differentiability; IVT, max/min, MVT, Taylor.
4. Day 4: Integration and improper integrals; focus on theorem statements and examples.
5. Day 5: Metric/topological spaces; compactness and connectedness.
6. Day 6: Multivariable differentiability; Jacobian, gradient, Taylor, extrema.
7. Day 7: Banach, inverse/implicit functions, Lagrange; oral proof rehearsal.
