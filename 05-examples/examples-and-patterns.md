# Examples And Worked Patterns

Each numbered script example detected by extraction is rewritten as a study pattern. If a step is not explicit in the script, it is marked as supplementary.

## Beispiel 2.1.2 — example in 2.1

- **Source:** PDF p35; section 2.1. Definition und Beispiele
- **Context:** Sequences, convergence, neighborhoods, elementary limits, boundedness, monotonicity, and monotone convergence.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) Sei a \in R und ( an) mit an = a für alle n. Diese Folge konvergiert gegen a, denn für jedes \varepsilon > 0 und alle n \in N gilt | an − a| = 0 < \varepsilon. Man kann also n0 = 1 wählen. ANALYSIS I-III, 2011/2013 34 (ii) Sei an = 1 n , also ( an) = (1, 1 2 , 1 3 . . .). Dies ist eine Nullfolge. Denn zu beliebigem \varepsilon > 0 kann man n0 so wählen, dass n0 > 1 \varepsilon (archimedisches Prinzip). Optimal ist n0(\varepsilon) = ⌊ 1 \varepsilon⌋ + 1. Für n ≥ n0 gilt dann 0 < 1 n < 1 n0 < \varepsilon, also | an| < \varepsilon. Siehe Abbildung 3. 10 20 30 40 50 0.1 0.2 0.3 0.4 0.5 n0 = 10 n an = 1 n \varepsilon-band (\varepsilon = 0.1) an = 1 n \varepsilon = 0.1 ABBILDUNG 3. Konvergenz der Nullfolge an = 1 n (iii) Sei an = (− 1)n n also ( an) = (− 1, 1 2 ,− 1 3 , 1 4 , . . .). Dies ist eine Nullfolge, da | an| = 1 n und damit für n0(\varepsilon) = ⌊ 1 \varepsilon⌋ + 1. gilt, dass | an| < \varepsilon für alle n ≥ n0(\varepsilon) wie im vorangehenden Beispiel. Siehe Abbildung 4. 5 10 15 20 25 30 35 40 45 50 − 0.6 − 0.4 − 0.2 0.2 0.4 0.6 n an = (− 1)n ·1 n \varepsilon-Band \varepsilon = 0.1 an = (− 1)n ·1 n n0 = 11 ABBILDUNG 4. Konvergenz der alternierenden Nullfolge an = (− 1)n ·1 n (iv) Die Folge ( an) mit an = (− 1)n ist divergent. Zum Beweis müssen wir zeigen, dass es kein a \in R gibt mit limn→\infty an = a. Wir zeigen, dass für alle a \in R es unendlich viele n gibt, so dass an ̸\in (a − 1 2 , a + 1 2 ). Falls a ≥ 0, so ist − 1 < a − 1 2 also an ̸\in (a − 1 2 , a + 1…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Beispiel 2.2.6 — Strategien zur Grenzwertberechnung

- **Source:** PDF p43; section 2.2. Rechnen mit konvergenten Folgen
- **Context:** Algebra of convergent sequences, comparison principles, squeeze principle, and limit calculation strategies.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(1) Wir untersuchen die Konvergenz der Folge an = 2n + 3 n · Wir umformen zunächst an = 2n + 1 n = 2 + 3 n · Es ist also an = a′ n + a′′ n wobei a′ n = 2 und a′′ n = 3 n . Die Folgen ( a′ n) und ( a′′ n) sind konvergent mit limn→\infty a′ n = 2, limn→\infty a′′ n = 0. Aus Satz 2.2.2 (i) folgt, dass ( an) konvergent ist, und limn→\infty an = limn→\infty a′ n + limn→\infty a′′ n = 2 + 0 = 2. Wir können das auch direkt so schreiben, mit dem Verständnis , dass die Grenzwerte existieren: limn→\infty 2n + 3 n = limn→\infty ( 2 + 3 n ) = limn→\infty 2 + 3 limn→\infty 1 n = 3 + 2 ·0 = 2. (2) Sei a \in R mit | a| < 1. Betrachten wir die Folge an = 1 − an 1 − a · Es ist 1 − an 1 − a = 1 1 − a − an 1 − a · Weil an → 0 gilt: limn→\infty 1 − an 1 − a = limn→\infty 1 1 − a − 1 1 − a limn→\infty an = 1 1 − a · Das zeigt, dass für | a| < 1 gilt: limn→\infty (1 + a + a2 + . . .+ an) = 1 1 − a · (3) Wir betrachten hier Grenzwerte rationaler Funktionen. Wir verallgemeinern das Beispiel (1). Ein Polynom ist eine Funktion P : R → R der Form P(x) = cm xm + cm− 1xm− 1 + . . .+ c1 x + c0, mit m \in N0 und c0, . . . ,cm \in R, den Koeffizienten von P. Falls cm ̸= 0, so heißt m der Grad und cm der Leitkoef- fizient von P. Das Polynom P mit P(x) = 0 für alle x \in R heisst das Polynom konstant gleich Null. Sein Grad ist als −\infty definiert. Der Grad von P wird mit grad P bezeichnet. In der Algebra beweist man, dass ein Polynom vom Grad m \in N0 höchstens m Nullstellen (das sind Lösungen x der Gleich…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Beispiel 2.4.2 — example in 2.4

- **Source:** PDF p46; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Context:** Accumulation values, subsequences, Bolzano-Weierstrass, limsup/liminf, and the Cauchy criterion.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) Teilfolgen von ( 1, 1 2 , 1 3 , . . . ,1 n , . . . ) : (1 2 , 1 4 , 1 6 , . . . , 1 2n , . . . ) wobei nk = 2k ist und ( 1, 1 2 , 1 4 , . . . , 1 2n , . . . ) wobei nk = 2k − 1. Aber die Folge (1 4 , 1 2 , 1 6 , 1 8 , . . . , 1 2n , . . . ) ist keine Teilfolge von ( 1 n )n\inN, weil die Reihenordnung geändert ist. (ii) Es ist instruktiv die Definition der Konvergenz für eine Teilfolge zu schreiben: limn→\infty ank = a \Longleftrightarrow \forall \varepsilon > 0 \exists k0 \forall k ≥ k0 : | ank − a| < \varepsilon. (iii) Ist ( an) konvergent, so ist a = lim an ein Häufungswert von ( an), und zwar der einzige. (Beweis identisch zum Beweis von Übung 2.7.1.) (iv) Es gilt: ( an) ist konvergent mit lim n→\infty an = a \Longleftrightarrow Jede Teilfolge (ank ) ist konvergent mit lim n→\infty ank = a. (v) Die Folge ( an) mit an = (− 1)n, an = { 1 , n gerade − 1 , n ungerade hat − 1 und 1 als Häufungswerte und keine weiteren. Denn für a = 1 und beliebiges \varepsilon > 0 gilt | an − a| = 0 < \varepsilon bei allen geraden n, und analog für a = − 1 bei allen ungeraden n. Ist a ̸\in {− 1,1}, so kann man \varepsilon kleiner als die Abstände von a zu 1 und zu − 1 wähhlen: \varepsilon < min{| a − 1| ,| a + 1| }, dann gibt es gar kein n mit | an − a| < \varepsilon, also ist a kein Häufungswert.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 2.5.2 — example in 2.5

- **Source:** PDF p49; section 2.5. Uneigentliche Grenzwerte
- **Context:** Improper limits and the extended real line.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) Ist an > 0 (bzw .< 0) und an → 0, n → \infty , so gilt 1 an → \infty (bzw .−\infty ).
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Beispiel 2.6.2 — example in 2.6

- **Source:** PDF p52; section 2.6. Folgen komplexer Zahlen
- **Context:** Complex sequences and reduction to real and imaginary parts.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) Ist z \in C, | z| < 1, so gilt zn → 0, n → \infty . (ii) Ist z \in C, | z| < 1, so gilt 1 + z + . . .+ zn → 1 1 − z , n → \infty .
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 2.6.9 — example in 2.6

- **Source:** PDF p53; section 2.6. Folgen komplexer Zahlen
- **Context:** Complex sequences and reduction to real and imaginary parts.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) Ist z \in C, | z| > 1, so gilt zn → \infty \in C, n → \infty . (ii) Vorsicht: Falls a < − 1, dann an \to \infty \in C, aber ( an) ist unbestimmt divergent in R (siehe Definition 2.5.3(v) und Beispiel 2.5.2(4)). Wenn aber eine Folge ( an)n\inN in R gegen \infty \in R oder −\infty \in R konvergiert, dann konver- giert sie auch in C gegen \infty \in C. Wenn aber eine Folge ( an)n\inN in R gegen \infty \in R oder −\infty \in R divergiert, dann divergiert sie auch gegen \infty \in C. Ein Modell für C ist die Sphäre S2 = {(x, y, t) \in R3 : x2 + y2 + t2 = 1}. Sei π : S2\setminus{(0,0,1)} \to C die stereographische Projektion bezüglich des „Nordpols“ (0,0,1): Die Abbildung π ordnet dem Punkt ( x, y, t) \in S2 \setminus {(0,0,1} den Schnittpunkt der Geraden durch (0 ,0,1) und ( x, y, t) mit der Ebene xO y ∼ = R2 ∼ = C zu; π ist bijektiv , und daher ist auch die Fortsetzung π : S2 → C von π durch π(0,0,1) = \infty bijektiv und erlaubt es uns, S2 mit C zu identifizieren. ANALYSIS I-III, 2011/2013 52 x y t P(x, y, t)P(x, y, t)P(x, y, t) /Bullet (π(P),0) R2× {0}∼ = C 2.7. Übungen. 2.7.1. Aufgabe. Sei ( a)n eine konvergente Folge. Zeige, dass lim an eindeutig bestimmt ist. 2.7.2. Aufgabe. Zeige: (i) limn→\infty n\sum k= 1 1 k(k + 1) = 1 , (ii) limn→\infty nk n! = 0 , k \in N fest , (iii) limn→\infty an n! = 0 , a \ge 0 fest , (iv) limn→\infty \sqrtn( \sqrt n + 1 − \sqrtn) = 1 2 . 2.7.3. Aufgabe. Die Folge ( xn)n\inN sei rekursiv definiert durch x1 = 1 , xn+ 1 = √ 2 + xn . (a) Beweise…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 3.2.2 — example in 3.2

- **Source:** PDF p58; section 3.2. Konvergenzkriterien
- **Context:** Convergence criteria for series, including Cauchy-type and comparison ideas.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Sei s \in Q, s > 1 und an = 1 ns > 0 für n \ge 1. Dann gilt sn \le 1 1− ( 1 2 )s− 1 . Aus dem Monotoniekriterium folgt, dass \sum n\ge1 1 ns konvergiert. Die Funktion (3.1) \infty\sum n= 1 1 ns = : ζ(s) heißt die Riemannsche Zeta-Funktion. Sei s \in Q, s \le 1. Aus 1 ns \ge 1 n und \sum\infty n= 1 1 n = \infty folgt nach dem Minorantenkriterium \sum\infty n= 1 1 ns = \infty . Die Zeta- Funktion ist also auf (1 ,\infty ) definiert.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 3.2.8 — example in 3.2

- **Source:** PDF p59; section 3.2. Konvergenzkriterien
- **Context:** Convergence criteria for series, including Cauchy-type and comparison ideas.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Die alternierende harmonische Reihe \sum n\ge1 (− 1)n+ 1 n ist konvergent. Ihre Summe ist log 2 (siehe (??)). 3.3. Absolute Konvergenz.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 3.3.5 — example in 3.3

- **Source:** PDF p59; section 3.3. Absolute Konvergenz
- **Context:** Absolute convergence, product rules, exponential series, and related identities.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) Die Reihe (3.2) \sum n\ge0 zn n! heißt Exponentialreihe. Es gilt an = zn n! ·Für z ̸= 0 ist an ̸= 0 und an+ 1 an = z n → 0, n → \infty also konvergiert die Exponentialreihe. Sie konvergiert offensichtlich auc h für z = 0. Die Summe der Exponentialreihe wird Exponentialfunktion und wird bezeichnet durch (3.3) exp : C → C , exp(z) := \infty\sum n= 0 zn n! · Es gilt (3.4) exp(0) = 1 , exp(1) = \infty\sum n= 0 1 n! = e . ANALYSIS I-III, 2011/2013 58 wobei die zweite Gleichcheit aus Beispiel 3.1.2 (iii) folgt . Für x \in R ist exp(x) = limn→\infty n\sum k= 0 xn n! \in R, also definiert Einschränkung der Exponentialfunktion exp a uf R eine Funktion exp : R \to R. Bemerkung. Beim Ausschreiben der Exponentialreihe als \sum n\ge0 zn n! = 1 + z 1! + z1 2! + . . . haben wir nach rein praktischen Gesichtspunkten 0 0 := 1 definiert. (ii) \sum n\ge1 nz n, z \in C; an = nz n, n\sqrt| an| = n\sqrtn| z| n = n\sqrtn| z| \to | z| , n → \infty . Nach dem Wurzelkriterium folgt: Für | z| < 1 ist die Reihe absolut konvergent; für | z| \ge 1 ist die Reihe divergent ( n\sqrtn| z| n = n\sqrtn| z| \ge 1). (iii) \sum n\ge1 zn n , z \in C; an = zn n , lim | an+ 1 an | = lim | z| n+ 1 n+ 1 · n | z| n = | z| . Für | z| < 1 ist die Reihe absolut konvergent und für | z| > 1 divergent. Ist | z| = 1, so gilt: Für z = 1 ist die Reihe divergent, für z ̸= 1 konvergent. (iv) Es reicht für absolute Konvergenz nicht, dass lim sup n\sqrt| an| = 1 oder lim sup | an+ 1 an | = 1 (oder n\sqrt| an| < 1 oder an+ 1 an…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 4.4.7 — example in 4.4

- **Source:** PDF p76; section 4.4. Grenzwerte von Funktionen
- **Context:** Limits of functions and their relation to continuity.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Sei f : R → R definiert durch f (x) := { 0, x < 0, 1, x ≥ 0. Dann gilt lim x→ 0− f (x) = 0 und lim x→ 0+ f (x) = 1. Da 0 ̸= 1, existiert der Grenzwert lim x→ 0 f (x) nicht. Als nächstes betracten wir die Funktion f : R \to R, (4.8) f (x) = { e− 1/x , x > 0 0 , x \le 0 Die Funktion f ist offentsichtlich stetig auf R\{0}. Ausserdem gilt lim x→ 0− f (x) = 0 limx→ 0+ f (x) also limx→ 0 f (x) = f (0). Somit ist f auch in x = 0 stetig. 0 1 2 3-1-2-3 0 -1 1 Genau wie bei Grenzwerten von Folgen gelten die folgenden Re geln:
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 5.2.2 — example in 5.2

- **Source:** PDF p81; section 5.2. Ableitungsregeln
- **Context:** Derivative rules: linearity, product, quotient, chain rule, inverse rule.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(1) Sei c \in C und f sei differenzierbar in x0. Dann ist auch c f differenzierbar in x0 und (c f )′(x0) = c f ′(x0) wegen der Produktregel und c′ = 0. (2) Wegen sin x = 1 2i (eix − e− ix ), cos x = 1 2 (eix + e− ix ) gilt: sin′x = cos x , cos′x = − sin x Analog sinh′x = cosh x , cosh′x = sinh x ANALYSIS I-III, 2011/2013 80 (3) tan x := sin x cos x (wo cos x ̸= 0) ⇝ tan′x = 1 cos2 x = 1 + tan2 x Die Funktion tan erfüllt also die Differentialgleichung (D GL) f ′= 1 + f 2.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 5.4.9 — Kurvendiskussion

- **Source:** PDF p92; section 5.4. Anwendungen des Mittelwertsatzes
- **Context:** Applications of mean value theorem: monotonicity, extrema, convexity, Taylor, and approximation.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Sei f : D → R, wobei D eine Vereinigung von Intervallen sei. Die Kurven- diskussion der Kurve y = f (x) besteht aus den folgenden Schritten: 1 Bestimme die Schnittpunkte mit den Achsen und das Vorzeiche n der Funktion, d.h. die Mengen {x : f (x) > 0} und {x : f (x) < 0}. 2 Studiere die Grenzwerte in Randpunkten (inklusive eventue ll ±\infty ), Asymptoten, Stetigkeit der Funk- tion. 3 Studiere die Differenzierbarkeit, berechne f ′ und bestimme die Mengen {x : f ′(x) = 0}, {x : f ′(x) > 0}, {x : f ′(x) < 0}; bestimme die lokalen und globalen Extrema. 4 Erstelle eine Tabelle mit den wichtigsten Werten und mit den Monotoniebereichen der Funktion f . Schließlich skizziere den Graphen. ANALYSIS I-III, 2011/2013 91 Wir erläutern das Vorgehen am Beispiel der Funktion f : R \to R, f (x) = − (x2 + x − 1)e− x. Die Tabelle lautet: x −\infty − 1− \sqrt 5 2 − 1 0 − 1+ \sqrt 5 2 2 \infty f (x) −\infty ր 0 ր e ց 1 ց 0 ց − 5 e2 ր 0 f ′(x) + + 0 − − − 0 + Wir entnehmen der Tabelle, dass f (x) \le f (− 1) = e für x \in (−\infty ,2] und f (x) \ge f (2) = − 5/e2 für x \in [− 1,\infty ). Die Funktion hat in x = − 1 ein lokales Maximum und in x = 2 ein lokales Minimum. Da lim x→−\infty f (x) = −\infty gilt, besitzt f kein globales Minimum (Beweis?). Wegen f (x) < 0 < e = f (− 1) für x \in [2,\infty ) hat f in x = − 1 ein globales Maximum. 0 1 2 3 4 5 6 7-1-2 0 -1 1 2 3(− 1,e) (2,− 5 e2 ) f ( − 1− \sqrt 5 2 )= 0 f ( − 1+ \sqrt 5 2 )= 0 f (x) = − (x2 + x − 1)e− x Bei der vorigen Kurvendiskussion feh…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 6.3.6 — example in 6.3

- **Source:** PDF p101; section 6.3. Das Integral von Regelfunktionen
- **Context:** Regulated functions and the extension of the integral by uniform approximation.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
f : [0, b] \to R, f (x) = x2. Für n \in N sei Zn = {0 < 1 n b < 2 n b < . . .< n− 1 n b < b}. Für x \in [k− 1 n b, k n b ) wähle \varphi n(x) = ( k n b)2, \varphi n(b) = b2. Dann ist \| f − \varphi n\| = max {⏐ ⏐(k− 1 n b )2 − (k n b )2⏐ ⏐ : k = 1, . . . ,n } = b2 − ( n− 1 n b)2 ANALYSIS I-III, 2011/2013 100 (weil k2 − (k − 1)2 = 2k − 1 \le 2n − 1 = n2 − (n − 1)2). Also \| f − \varphi n\| → 0 für n → \infty . Nach Definition folgt ∫ b 0 x2 dx = limn→\infty ∫ b 0 \varphi n dx = limn→\infty n\sum k= 1 ( k n b )2 ·1 n b = b3 limn→\infty 1 n3 n\sum k= 1 k2 = b3 limn→\infty 1 n3 ·n(n + 1)(2n + 1) 6 = b3 ·2 6 = b3 3 ·
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 6.6.2 — example in 6.6

- **Source:** PDF p107; section 6.6. Höhere Ableitungen. Die Taylorformel
- **Context:** Higher derivatives and Taylor formula.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(1) Jedes Polynom P : R \to R gehört zu C\infty (R), und P(n) = 0 für n > grad(P). (2) Sei s \in R. Die Funktion f : (0,\infty ) \to R, x \mapstoxs ist unendlich oft differenzierbar . Es gilt für alle n \in N und alle x > 0: ( d dx )n xs = n! ( s n ) xs− n . (3) Die Funktionen exp ,sin,cos : R \to R und log : (0,\infty ) \to R sind unendlich oft differenzierbar . Für n \in N und beliebiges c \in R ist ( d dx )n ecx = cn ecx für alle x \in R , ( d dx )n sin x =              sin x, n = 4k cos x, n = 4k + 1 − sin x, n = 4k + 2 − cos x, n = 4k + 3 für alle x \in R , ( d dx )n log x = (− 1)n− 1(n − 1)! 1 xn für alle x > 0 . (4) Die Funktion (5.7) liegt in C\infty (R). Man zeigt nämlich durch Induktion über n \in N, dass f n -mal differen- zierbar ist und dass f (n)(t) = { Pn( 1 t )e− 1/t , x > 0 , 0 , x < 0 , wobei Pn ein Polynom vom Grad 3 n ist. Dabei benutzt man die Folgerung 5.4.6. ANALYSIS I-III, 2011/2013 106 Sind f , g : I → C n-mal differenzierbar , so sind auch f + g und f ·g n -mal differenzierbar , und es gilt: ( f + g)(n) = f (n) + g(n) , ( f ·g)(n) = n\sum k= 0 ( n k ) f (k) g(n− k) . Die letzte Formel heißt Leibnizsche Produktregel. Daraus folgt, dass für jedes Intervall I \subset R und alle k \in N \cup {\infty } die Menge Ck(I) eine C-Algebra ist. Darüber hinaus beweist man durch Induktion die folgenden Va rianten der Sätze 5.2.4 und 5.2.5: • Die Komposition n-mal (stetig) differenzierbarer Funktionen ist n-mal (stetig) differenzierbar . • Ist f : I \…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Beispiel 6.7.8 — Abschätzung für die Zeta-Funktion

- **Source:** PDF p112; section 6.7. Uneigentliche Integrale
- **Context:** Improper integrals and convergence criteria.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
f : [1,\infty ) \to R, f (x) = 1 xs , s > 0 ist monoton fallend. Nach dem Integralkriterium gilt: ∫ \infty 1 1 xs dx konvergiert genau dann, wenn \sum n\ge1 1 ns konvergiert . Wir wussten schon, dass beides genau dann zutrifft, wenn s > 1 ist (siehe Beispiel 3.2.2). Nun außerdem: Mit ζ(s) = \sum\infty n= 1 1 ns gilt 0 \le ζ(s) − ∫ \infty 1 1 xs dx \le f (1) = 1. Daraus folgt ζ(s) \le 1 + 1 s − 1 = s s − 1 . Für s = 1 erhalten wir die Existenz des Limes limn→\infty ( n\sum k= 1 1 k − ∫ n+ 1 1 1 x dx ) = limn→\infty ( n\sum k= 1 1 k − log(n + 1) ) = limn→\infty ( n\sum k= 1 1 k − log n ) = : γ. Dies bedeutet, dass die Partialsummen der harmonischen Rei he wie log n anwachsen. Die Zahl γ heißt Euler- sche Konstante und beträgt approximativ 0 ,57721.... Es ist unbekannt, ob γ eine rationale oder eine irratio- nale Zahl ist. 6.8. Übungen. 6.8.1. Aufgabe. Sei b > 1. Berechnen Sie ∫ b 1 1 x dx aus der Definition des Integrals, ohne den Hauptsatz und Ihre Kenntnis einer Stammfunktion zu f (x) = 1 x vorauszusetzen. Benutzen Sie dazu die Unterteilungen 1 < b 1 n < b 2 n < . . .< b n− 1 n < b des Intervalles [1 , b]. 6.8.2. Aufgabe. Zeigen Sie durch Betrachtung geeigneter Integrale ∫ b a f (x) dx : (a) lim n→\infty 1 nk+ 1 ( 1k + 2k + . . .+ nk) = 1 k+ 1 für k \in N0 (b) lim n→\infty ( 1 n+ 1 + 1 n+ 2 + . . .+ 1 2n ) = log 2 6.8.3. Aufgabe. Sei f \in R([a, b]) (i) Sei ̃f : [a, b] \to C eine Funktion, die mit f außerhalb einer endlichen Menge von Punkten überein- stimmt. Zeigen Sie, das…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 7.2.2 — example in 7.2

- **Source:** PDF p119; section 7.2. Metrische und normierte Räume
- **Context:** Metric and normed spaces, convergence, Cauchy sequences, completeness, and equivalent norms.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(1) X = R oder X = C, d(x, y) = | x − y| . (2) Auf X = Rn oder X = Cn definieren wir die lp-Metrik: d p(x, y) := \| x − y\|p = ( \sum | xi − yi| p)1/p für ein p \ge 1. Dreiecksungleichung: \|x− z\|p = \| x− y+ y− z\|p \le \|x− y\|p +\| y− z\|p für p \ge 1 wegen der Minkowski-Ungleichung. Für p = 2 heißt d2 die euklidische Metrik auf Rn (bzw .Cn). Das ist das wichtigste Beispiel einer Metrik in Analysis II. Die Metrik d1 wird manchmal die Manhattan-Metrik genannt. /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0 /0/0/0…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 7.2.8 — example in 7.2

- **Source:** PDF p121; section 7.2. Metrische und normierte Räume
- **Context:** Metric and normed spaces, convergence, Cauchy sequences, completeness, and equivalent norms.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Konvergenz in ( B(D),\| · \|D ) bedeutet gleichmäßige Konvergenz der Funktionen.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 7.2.22 — example in 7.2

- **Source:** PDF p124; section 7.2. Metrische und normierte Räume
- **Context:** Metric and normed spaces, convergence, Cauchy sequences, completeness, and equivalent norms.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Als weiteres Beispiel betrachten wir A \in Mn× n(K) mit \|A\|2 < 1. Dann konvergiert die geo- metrische Reihe \infty\sum k= 0 Ak = (Id− A)− 1 also (\sum\infty k= 0 Ak)2 = (Id− A)− 2. Wir berechnen das Cauchy-Produkt: ( \infty\sum k= 0 Ak )2 = ( \infty\sum k= 0 Ak )( \infty\sum l= 0 Al ) = \infty\sum n= 0 ( A0 An + . . .+ An A0) = \infty\sum n= 0 (n + 1)An = \infty\sum k= 1 kA k− 1. Der Satz über das Cauchy-Produkt liefert: \infty\sum k= 1 kA k− 1 = (Id− A)− 2. 7.3. Topologie eines metrischen Raumes. Topologische Räume. Unser Ziel ist, bemerkenswerte Teil- mengen eines metrischen Raumes zu beschreiben, die ein tief eres Studium der Funktionen ermöglichen.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 7.4.9 — example in 7.4

- **Source:** PDF p137; section 7.4. Stetige Abbildungen
- **Context:** Continuity between metric/topological spaces, sequential criteria, homeomorphisms, and uniform continuity.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Die n-Sphäre Sn = {x \in Rn+ 1 : x2 1 + . . .+ x2 n+ 1 = 1} ist abgeschlossen, da Sn = f − 1(1), wobei f die stetige Funktion f : Rn \to R, f (x) = x2 1 + . . .+ x2 n+ 1 ist. Wir beschreiben im folgenden zwei Beispielen von Abbildung en, die Polarkoordinaten in der Ebene und die linearen Abbildungen. Wir schreiben C∗ := C \setminus {0}. Mit der Multiplikation von komplexen Zahlen ist C∗ eine Gruppe ( C∗ , ·). Die Kreislinie S1 := {z \in C : | z| = 1} ist bezüglich der Multiplikation von komplexen Zahlen eine Untergruppe der Gruppe (C∗ , ·).
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 7.6.6 — example in 7.6

- **Source:** PDF p146; section 7.6. Zusammenhang
- **Context:** Connectedness, path connectedness, components, and generalized intermediate value ideas.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) Sei ( V ,\| · \|) ein normierter Vektorraum. Eine Teilmenge A \subset V heißt konvex, wenn für alle x, y \in A die Verbindungsstrecke [ x, y] = {(1 − t)x + ty : t \in [0,1]} in A enthalten ist. Zum Beispiel ist eine Kugel Br(x) in einem normierten Vektorraum konvex. Da [0 ,1] ∋ t \mapsto(1− t)x + ty \in V stetig ist, ist jede konvexe Menge auch wegzusammenhängend. Hat man mehrere Punkte x0, x1, . . . ,xk in einem NVR V so bilden die einzelnen Strecken [ x0, x1], [x1, x2], . . . , [xk− 1, xk] zusammen einen Streckenzug: S(x0, x1, . . . ,xk) = [x0, x1] \cup [x1, x2] \cup [xk− 1, xk] . (ii) Für n \ge 2 ist Rn \setminus {0} nicht konvex, aber offensichtlich wegzusammenhängend. Zu x, y \in Rn \setminus {0} gibt es nämlich z \in Rn \setminus {0}, so dass [ x, z] \cup [z, y] \subset Rn \setminus {0}. (iii) Für n \ge 1 ist die n-Sphäre Sn = {x \in Rn+ 1 : x2 1 + . . .+ x2 n+ 1 = 1} wegzusammenhängend.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 8.2.11 — example in 8.2

- **Source:** PDF p157; section 8.2. Richtungsableitungen und partielle Ableitungen
- **Context:** Directional derivatives, partial derivatives, Jacobian, gradient, chain rule in coordinates, and differentiability criterion.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Sei P2 : R+ × R \to R2, f (r, θ) = (r cos θ, r sin θ). Dann gilt ∂P2 ∂r (r, θ) = ( cos θ sin θ ) , ∂P2 ∂θ (r, θ) = ( − r sin θ r cos θ ) , und ∂P2 ∂r , ∂P2 ∂θ sind stetig (sie haben stetige Komponenten). Daher ist P2 differenzierbar und dP 2(r, θ) ·(h, k) = JP2 (r, θ) · ( h k ) = ( cos θ − r sin θ sin θ r cos θ ) ( h k ) = ( h cos θ − kr sin θ h sin θ + kr cos θ ) . 8.3. Mittelwertsatz und Schrankensatz. Sei D \subset Rn offen. Für reellwertige Abbildungen mehrerer Varia- blen f : D → R können wir ein genaues Analogon des MWS für reellwertige Fun ktionen einer Variablen (Satz 5.3.5, Analysis I) beweisen:
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 8.7.1 — example in 8.7

- **Source:** PDF p162; section 8.7. Extremwertbestimmung
- **Context:** Worked extrema determination examples.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Sei f : R2 \to R, f (x, y) = x3 + x2 + y2; grad f (x, y) = (3x2 + 2x,2y) = (0,0) genau dann, wenn (x, y) \in {(0,0),(− 2 3 ,0)}. Die Hesse-Matrix ist: H f (x, y) = ( 6x + 2 0 0 2 ) mit H f (0,0) = ( 2 0 0 2 ) positiv definit und H f (− 2 3 ,0) = ( − 2 0 0 2 ) indefinit. Daraus folgt: Der Punkt (0 ,0) ist ein lokales Minimum, und ( − 2 3 ,0) ist kein lokales Extremum. Punkte ( x, y) \in R2 mit d f (x, y) = 0 und H f (x, y) indefinit heißen Sattelpunkte.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 8.7.2 — example in 8.7

- **Source:** PDF p162; section 8.7. Extremwertbestimmung
- **Context:** Worked extrema determination examples.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Betrachte die Funktion f : R2 \to R, f (x, y) = x4 + y3 − 4x3 − 3y2 + 3y; grad f (x, y) = (4x3 − 12x2,3y2 − 6y + 3) = (0,0) genau dann, wenn ( x, y) \in {(0,1),(3,1)}. Es ist H f (x, y) = ( 12x2 + − 24x 0 0 6 y − 6 ) , H f (0,1) = ( 0 0 0 0 ) , H f (0,1) = ( 36 0 0 0 ) . In beiden Fällen ist 0 ein Eigenwert der Hessematrix und das K riterium 8.6.4 gibt keine Auskunft. Wir studieren daher das Vorzeichen der Differenzen f (x, y) − f (0,1) und f (x, y) − f (3,1). Für ein Polynom P gilt P(x) = Tk,aP(x) für alle k \ge grad P, d.h. wir können das Polynom nach der Potenzen von x1 − a1, . . . ,xn − an entwickeln. Also f (x, y) − f (0,1) = x4 − 4x3 + (y − 1)2 und dieser Ausdruck ist > 0 in allen Punktem (0 ,1 + z) mit z > 0 und < 0 in allen Punktem (0 ,1 + z) mit z < 0. Es folgt, dass (0 ,1) kein Extremum ist. Es gilt f (x, y) − f (3,1) = (x − 3)4 + 8(x − 3)3 + 18(x − 3)2 + (y − 1)2 = (x − 3)2(x2 + 2x + 3) + (y − 1)2 \ge 0 also (3 ,1) ist eine Minimumstelle. 8.8. Übungen. 8.8.1. Aufgabe. (i) Es sei f : R2 → R definiert durch f (x) =      x1 x2 2 x2 1 + x2 2 , x ̸= 0 0 , x = 0 . Zeige, daß f stetig ist und für jedes x \in R2 und jedes y \in R2 (∗ ) lim t→ 0 f (x + ty) − f (x) t = g(x, y) ANALYSIS I-III, 2011/2013 161 existiert, aber daß die Abbildung y \mapstog(0, y) nicht linear ist (so daß f im Punkt 0 nicht differenzierbar sein kann). (ii) Es sei f : R2 → R definiert durch f (x) =      x3 1 x2 x4 1 + x2 2 , x ̸= 0 0 , x = 0 . Zeige, daß der Limes g(x, y) in ( ∗ ) für jede…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Beispiel 9.2.8 — example in 9.2

- **Source:** PDF p170; section 9.2. Der Umkehrsatz
- **Context:** Diffeomorphisms and inverse function theorem.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Der Diffeomorphiesatz vereinfacht die Beweise, dass eine g egebene Abbildung ein Differo- meorphismus ist; es genügt zu zeigen, dass die Abbildung bij ektiv und von der Klasse Ck ist und zusätzlich, dass das Differential in jedem Punkt bijektiv ist. Man brauc ht nicht mehr die Inverse zu berechnen und nach- zuweisen, dass sie Ck ist. Betrachten wir nochmals die Abbildung f : R+ × R \to R2, f (r, \varphi ) = (r cos \varphi , r sin \varphi ). Sie bildet D = R+ × (\varphi 0 − π, \varphi 0 + π) bijektiv auf G = R2 \setminus {te i\varphi 0 : t \le 0} ab. Außerdem gilt für alle ( r, \varphi ) \in D: Jf (r, \varphi ) = ( cos \varphi − r sin \varphi sin \varphi r cos \varphi ) , det Jf (r, \varphi ) = r ̸= 0. Daraus folgt dass d f (r, \varphi ) für jedes ( r, \varphi ) \in R+ × R invertierbar ist. Nach Folgerung 9.2.7 ist f : D → G ein C\infty -Diffeomorphismus. Genauso zeigt man, dass die Kugelkoordinatenabbildung (9. 2) ein C\infty -Diffeomorphismus auf ihr Bild ist (Übungsaufgabe).
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel 9.3.3 — example in 9.3

- **Source:** PDF p171; section 9.3. Der Satz über implizite Funktionen
- **Context:** Implicit function theorem and derivative formula for the implicit map.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(1) f : R2 \to R, f (x, y) = x2 + y2 (hier k = 1, m = 1). Dann ist ∂f ∂y (x, y) = 2y. Für alle y0 ̸= 0 und alle x0 gilt also: x2 + y2 = z0 = x2 0 + y2 0 kann lokal um ( x0, y0) durch eine Gleichung y = g(x) aufgelöst werden. (Klar auch ohne Satz über implizite Funktionen: g(x) := sign y0 · √ z0 − x2 0 .) Analog für x0 ̸= 0. (2) f : R2 \to R, f (x, y) = x2 − y2. Sei z0 = 0, dann ist f − 1(0) die Vereinigung der zwei Winkelhalbierenden y = x und y = − x. Es ist grad f (x, y) = (2x,− 2y). Daraus folgt: Für alle ( x0, y0) ̸= (0,0) in f − 1(0) ist f (x, y) = 0 nahe (x0, y0) sowohl nach x als auch nach y auflösbar . Denn hier ist 2 y0 ̸= 0 \Longleftrightarrow 2x0 ̸= 0 wegen x2 0 = y2 0. Im Nullpunkt ist die Gleichung weder nach x noch nach y auflösbar . (3) Die Lemniskate von Bernoulli ist der Ort der Punkte ( x, y) \in R2, deren Entfernungen von zwei festen Punkten (− 1,0) und (1 ,0) das konstante Produkt 1 haben: ANALYSIS I-III, 2011/2013 170 Die Lemniskate ist also die Menge der Punkte ( x, y) \in R2, für die gilt: | (x, y) − (1,0)| · |(x, y) − (− 1,0)| = 1 ⇐ ⇒ 1 = ((x − 1)2 + y2) ·((x + 1)2 + y2) = (x2 + 1 + y2)2 − 4x2 ⇐ ⇒ 0 = (x2 + 1 + y2)2 − 4x2 − 1 = (x2 + y2)2 − 2x2 + 2y2 = : f (x, y). Der Gradient der Funktion f ist: grad f (x, y) = (4x(x2 + y2) − 4x,4y(x2 + y2) + 4y) = 4(x(x2 + y2 − 1), y(x2 + y2 + 1)) . Ist y0 ̸= 0, so ist die Gleichung f (x, y) = 0 nahe (x0, y0) \in f − 1(0) auflösbar durch y = g(x). Ist x0 ̸= 0 und x2 0+ y2 0 ̸= 1, so ist die Gleichung f (x, y) = 0 au…
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Beispiel 9.4.2 — example in 9.4

- **Source:** PDF p174; section 9.4. Extrema unter Nebenbedingungen
- **Context:** Constrained extrema and Lagrange multiplier rule.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Sei U := {(x1, . . . ,xn) \in Rn : x j > 0 \forall j = 1, . . . ,n} und f : U → R, f (x) = x1 · · ·xn. Wir suchen Extrema von f unter der Nebenbedingung x1+ . . .+ xn = 1, d.h. Extrema von f | \varphi − 1(0) mit \varphi : U → R, \varphi (x) = x1 + . . .+ xn − 1. Es ist grad \varphi (x) = (1,1, . . . ,1) ̸= 0 für jedes x \in \varphi − 1(0), also ( m = 1) ist die Voraussetzung an die lineare Unabhängigkeit der Gradienten der \varphi i erfüllt. Also: Ist x \in U lokales Extremum von f | \varphi − 1(0), so gibt es \lambda \in R mit grad f (x) = \lambda grad \varphi (x) = (\lambda, . . . ,\lambda). Wegen grad f (x) = (x2 · · ·xn, x1 x3 · · ·xn, . . . ,x1 · · ·xn− 1) folgt c x1 = \lambda, c x2 = \lambda, . . . , c xn = \lambda, wobei c = x1 · · ·xn > 0. Daraus folgt x1 = . . .= xn, d.h. x = ( 1 n , . . . ,1 n ); Wert von f dort: 1 nn > 0. Behauptung: f | \varphi − 1(0) hat in ( 1 n , . . . ,1 n ) tatsächlich ein Extremum, und zwar ein globales Maximum.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Beispiel A.1.2 — example in A.1. Aussagenlogik

- **Source:** PDF p177; section A.1. Aussagenlogik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
A: „3 ist eine gerade Zahl.“ f B: „Es gibt unendlich viele Primzahlen.“ w (Satz von Euklid) Die Klasse aller Aussagen zerfällt also in zwei disjunkte Te ilklassen, die Klasse der wahren und die Klasse der falschen Aussagen. Die Zweiwertigkeit besagt dabei ledigl ich, dass man von jeder Aussage entscheiden kann, ob sie wahr oder falsch ist. Aussagen, deren Wahrheitswert n icht bekannt ist, nennt man Vermutungen. So ist z.B. unbekannt, welchen Wahrheitswert die Goldbachsche Vermutung hat: Jede gerade Zahl \ge 4 lässt sich als Summe von zwei Primzahlen darstellen. Aussagenvariablen stehen für nicht weiter spezifizierte Au ssagen, die wahr oder falsch sein können. Wir be- zeichnen wahre Aussagen mit ⊤ und falsche Aussagen mit ⊥ .
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel A.2.2 — example in A.2. Prädikatenlogik

- **Source:** PDF p180; section A.2. Prädikatenlogik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
◦ A(x): „Es gibt eine rationale Zahl x, für die gilt: x2 = 2.“ (falsch) ◦ B(x, y, z): „Für alle reellen Zahlen x, y und z gilt: ( x ·y) ·z = x ·(y ·z).“ (wahr) Eine Quantifizierung von Variablen erzeugt aus einer Aussageform eine solche nie drigerer Stellenzahl. Quantor umgangssprachlich symbolisch Generalisierung für alle x \forall x : A(x, . . .) (für jedes x, für beliebiges x) Partikularisierung es gibt (mindestens) ein x \existsx : A(x, . . .) (es existiert (mindestens) ein x) verstärkte Partikularisierung es gibt genau ein x \exists!x : A(x, . . .) (es existiert genau ein x; es gibt ein und nur ein x)
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel A.2.3 — example in A.2. Prädikatenlogik

- **Source:** PDF p180; section A.2. Prädikatenlogik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Obige Aussagen können dann wie folgt geschrieben werden: ◦ \exists x : x \in Q ∧ x2 = 2 oder \existsx \in Q : x2 = 2. ◦ \forall x \forall y \forall z \in R : (x ·y) ·z = x ·(y ·z). Andere Aussagen, die Quantifizierungen enthalten: Gruppenaxiome: \forall x \forall y \forall z : (x ·y) ·z = x ·(y ·z) \exists e \forall x : e ·x = x ·e = x \forall x \exists y : x ·y = y ·x = e
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel A.3.1 — example in A.3. Beweistechnik

- **Source:** PDF p181; section A.3. Beweistechnik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Beweis von (A.13): Definition: n \in N heißt ungerade genau dann, wenn es k \in N0 gibt mit n = 2k + 1. Ist n \in N ungerade, so gibt es nach Definition k \in N0 mit n = 2k + 1. Dann ist n2 = (2k + 1)2 = 4k2 + 4k + 1 = 2(2k2 + 2) + 1 auch von der Form 2 m + 1 mit m = 2k2 + 2 \in N0, also nach Definition ungerade. □ ANALYSIS I-III, 2011/2013 180 Oder formaler: n \in N ungerade :\Longleftrightarrow \exists k \in N0 : n = 2k + 1 ⇒ n2 = (2k + 1)2 = 4k2 + 4k + 1 = 2(2k2 + 2) + 1 ⇒ \exists m \in N0 : n2 = 2m + 1 \Longleftrightarrow : n2 ungerade .
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel A.3.2 — example in A.3. Beweistechnik

- **Source:** PDF p182; section A.3. Beweistechnik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Dies ist ein komplizierteres Beispiel. Zu zeigen ist: (A.16) Für alle x, y, z \in R mit x < y und y \le z gilt x < z.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel A.3.4 — example in A.3. Beweistechnik

- **Source:** PDF p182; section A.3. Beweistechnik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Beweis von (A.15): Zu zeigen: A ⇒ B, wobei A : „n2 ist ungerade“, B : „n ist ungerade“. Dann ist ¬ B : „n ist gerade“ und ¬ A : „ n2 ist gerade“. Offensichtlich ist ¬ B ⇒ ¬ A wahr . Also gilt auch A ⇒ B.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel A.3.5 — example in A.3. Beweistechnik

- **Source:** PDF p182; section A.3. Beweistechnik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Zu beweisen:
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** Very short extracted statement; verify against PDF.

## Beispiel A.3.7 — example in A.3. Beweistechnik

- **Source:** PDF p183; section A.3. Beweistechnik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Zu beweisen:
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** Very short extracted statement; verify against PDF.

## Beispiel A.3.9 — example in A.3. Beweistechnik

- **Source:** PDF p183; section A.3. Beweistechnik
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Wir beweisen:
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** Very short extracted statement; verify against PDF.

## Beispiel A.3.12 — example in A.4. Mengenlehre

- **Source:** PDF p184; section A.4. Mengenlehre
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
Definition: Eine Primzahl ist eine natürliche Zahl mit genau zwei natürlichen Zahlen als Teiler , nämlich 1 und sich selbst. Primzahlen sind also 2 ,3,5,7,11, . . . Fundamentalsatz der Arithmetik: Jede natürliche Zahl läss t sich als Produkt von Primzahlen schreiben. Diese Produktdarstellung ist bis auf die Reihenfolge der Fa ktoren eindeutig. Wir beweisen:
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Beispiel A.4.16 — example in A.4. Mengenlehre

- **Source:** PDF p187; section A.4. Mengenlehre
- **Context:** See reconstructed table of contents for this section.
- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.
- **Script example transcription:**
```text
(i) f : R → R, x \mapstox2. (ii) Für beliebige X ,Y und y \in Y hat man die konstante Abbildung vom Wert y, nämlich f : X → Y , x \mapstoy. (iii) Für beliebiges X hat man die identische Abbildung Id X : X → X , x \mapstox.
```
- **Step-by-step pattern:**
  1. Identify the object being tested or computed.
  2. Match it to the relevant definition or theorem in the same section.
  3. Check each hypothesis explicitly.
  4. Perform the calculation or logical implication.
  5. State the conclusion using the script's terminology.
- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.
- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.
- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.
- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.
- **Uncertainty:** No major extraction warning detected.

## Supplementary Examples, Not From Script

### Supplementary, not from script — Sequences
To prove $1/n\to0$, given $\varepsilon>0$ choose $n_0>1/\varepsilon$; then $n\ge n_0$ implies $|1/n|<\varepsilon$.

### Supplementary, not from script — Squeeze principle
If $0\le b_n\le 1/n$ for all large $n$, then $b_n\to0$ because both bounds converge to $0$.

### Supplementary, not from script — Contraction
On $[0,1]$, a differentiable map with $\sup |f'|\le q<1$ is a contraction by the mean value estimate.

### Supplementary, not from script — Hessian test
For $f(x,y)=x^2+y^2$, $\nabla f(0,0)=0$ and the Hessian is positive definite, so $(0,0)$ is a strict local minimum.
