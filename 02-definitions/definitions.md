# Definitions Database

This file contains every numbered definition detected in the PDF extraction. German labels are preserved; English explanations are added for study. If exact mathematical symbols matter, verify entries marked with extraction warnings against the PDF.

## Def 1.1.1 — Körperaxiome

- **Original term:** Körperaxiome
- **Source:** PDF p6; section 1.1. Körperaxiome
- **Formal definition / script statement:**
```latex
A field-like structure has operations $+$ and $\cdot$ satisfying associativity, commutativity, distributivity, neutral elements $0,1$, additive inverses, and multiplicative inverses for nonzero elements.
```
- **English explanation:** This is the algebraic rulebook that makes the usual manipulation of numbers legitimate.
- **Intuition:** This is the algebraic rulebook that makes the usual manipulation of numbers legitimate.
- **Why it matters:** Every later calculation assumes these operations behave reliably.
- **Used later:** Basic set/function language from Appendix A. Later entries in and after 1.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.2.1 — total angeordneter Körper

- **Original term:** total angeordneter Körper
- **Source:** PDF p9; section 1.2. Anordnungsaxiome
- **Formal definition / script statement:**
```latex
A field $K$ is totally ordered if a positive cone $P\subset K$ trichotomizes each $x$ into $x\in P$, $x=0$, or $-x\in P$, and is closed under addition and multiplication.
```
- **English explanation:** A compatible order lets algebra and inequalities work together.
- **Intuition:** A compatible order lets algebra and inequalities work together.
- **Why it matters:** Needed for intervals, monotonicity, supremum arguments, convergence estimates, and all epsilon proofs.
- **Used later:** Körperaxiome. Later entries in and after 1.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.2.3 — unnamed definition in 1.2

- **Original term:** not explicitly named in script
- **Source:** PDF p9; section 1.2. Anordnungsaxiome
- **Formal definition / script statement:**
```latex
Sei K ein total angeordneter Körper. Ein Element x \in K wird nichtnega- tiv genannt, geschrieben x \ge 0 ( x größer-gleich 0), wenn x > 0 oder x = 0. Wir definieren eine ANALYSIS I-III, 2011/2013 8 zweistellige Relation \le auf K durch x \le y :⇐ ⇒ y − x \ge 0 ( x kleiner-gleich y). Die Relation \le ist eine Ordnungsrelation, d.h. (a) x \le x (Reflexivität) (b) x \le y und y \le z ⇒ x \le z (Transitivität) (c) x \le y und y \le x ⇒ x = y (Antisymmetrie) Eine ganz wichtige (aber einfache) Ungleichung ist (1.2) x2 + y2 2 \ge x y, für alle x, y \in K, wobei die Gleichheit genau dann auftritt, wenn x = y. Das folgt aus ( x − y)2 \ge 0 mit Gleichheit genau dann, wenn x = y. Die Ungleichung (1.2) ist ein Spezialfall der AGM-Ungleic hung, die wir später beweisen.
```
- **English explanation:** This definition gives precise language for the topic of order axioms, positivity, inequalities, sign, absolute value, and triangle-type estimates.
- **Intuition:** This definition gives precise language for the topic of order axioms, positivity, inequalities, sign, absolute value, and triangle-type estimates.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.2.4 — Vorzeichen und Absolutbetrag

- **Original term:** Vorzeichen und Absolutbetrag
- **Source:** PDF p10; section 1.2. Anordnungsaxiome
- **Formal definition / script statement:**
```latex
Sei K ein total angeordneter Körper. Sei x \in K . Man nennt sgn(x) =        1 x > 0 0 x = 0 − 1 x < 0 das Vorzeichen von x. Der Betrag von x ist | x| := x ·sgn(x) =        x x > 0 0 x = 0 − x x < 0 d.h. | x| = { x , x \ge 0 − x , x < 0 . Der Abstand zweier Zahlen x, y \in K ist definiert als | x − y| . Hier ist eine Skizze des Graphen der Funktion f : K → K , f (x) = | x| . x y 0 x− x | x| f (x) = | x|
```
- **English explanation:** This definition gives precise language for the topic of order axioms, positivity, inequalities, sign, absolute value, and triangle-type estimates.
- **Intuition:** This definition gives precise language for the topic of order axioms, positivity, inequalities, sign, absolute value, and triangle-type estimates.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 1.3.1 — induktiv

- **Original term:** not explicitly named in script
- **Source:** PDF p11; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Formal definition / script statement:**
```latex
Sei K ein total angeordneter Körper. Eine Menge M \subset K heißt induktiv, falls (a) 1 \in M, (b) Wenn x \in M, dann gilt auch x + 1 \in M. ANALYSIS I-III, 2011/2013 10 Die Menge K oder die Menge der positiven Zahlen K+ sind induktiv . Es ist klar, dass eine induktive Menge mindestens die Elemente 1 , 2 := 1+ 1 > 1, 3 := 2+ 1 > 2, . . .enthalten muss: Eben die natürlichen Zahlen nach unserem naiven Verständnis. Es gibt viele induk tive Mengen, z.B. M = {x \ge 1}. Uns interessiert die kleinste solche Menge, im Sinne der Inklus ion der Mengen.
```
- **English explanation:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Intuition:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.3.2 — unnamed definition in 1.3

- **Original term:** not explicitly named in script
- **Source:** PDF p12; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Formal definition / script statement:**
```latex
Die Menge der natürlichen Zahlen ist definiert als Durchschnitt aller in- duktiven Teilmengen von K: N := { x \in K : Für jede induktive Menge M \subset K gilt x \in M } = \bigcap { M : M \subset K, M induktiv } . Per Definition für jede induktive Teilmenge M von K gilt N \subset M. Diese Definition erfüllt unsere Vorstellung, dass N besteht aus 1 , 2, 3 . . .und nichts anderes enthält. Zudem ist diese Definition auch mathematisch brauchbar.
```
- **English explanation:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Intuition:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.3.5 — natürlichen Potenzen

- **Original term:** natürlichen Potenzen
- **Source:** PDF p13; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Formal definition / script statement:**
```latex
Sei a \in K. Wir definieren die natürlichen Potenzen an, n \in N, durch (1.4) a1 = a , an+ 1 = an ·a , n \in N . ANALYSIS I-III, 2011/2013 12 In der Tat, die Menge M = {n \in N : an ist definiert} hat die Eigenschaften: 1 \in M, n \in M ⇒ n + 1 \in M, also M = N, nach Satz 1.3.3. Eine sehr nüztliche Ungleichung, die durc h Induktion bewiesen wird, ist die folgende:
```
- **English explanation:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Intuition:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.3.7 — unnamed definition in 1.3

- **Original term:** not explicitly named in script
- **Source:** PDF p14; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Formal definition / script statement:**
```latex
Die Menge der ganzen Zahlen ist definiert durch Z := N \cup {0} \cup { − n : n \in N } = { 0, ± 1, ± 2, . . . } \subset K . (Z, + , ·) ist ein Ring, wobei die Addition und Multiplikation von der entsprechenden Operationen von K induziert sind. Wir setzen N0 := N \cup {0} . Die Menge der rationalen Zahlen ist definiert durch Q := { p q : p \in Z , q \in Z \ {0} } \subset K . Bemerkung. Einen Beweis durch Induktion kann man mit einer beliebigen g anzen Zahl anfangen. Sei q \in Z und Z(\ge q) = {n \in Z : n \ge q}. Seien A(n) Aussagen, die für n \in Z(\ge q) definiert sind. Wenn 1) A(q) richtig ist und 2) A(n) ⇒ A(n + 1) für alle n \in Z(\ge q) gilt, dann gilt A(n) für alle n \in Z(\ge q). Dies folgt leicht aus Satz 1.3.4 durch Indexverschiebung ; die Abbil- dung f : Z(\ge q) → N, f (n) = n + q − 1 ist bijektiv und f (n + 1) = f (n) + 1. Im folgenden führen wir mit Hilfe der rekursiven Definition d ie Addition und Multiplikation für eine beliebige Anzahl von Summanden bzw . Faktoren ein. Dies erlaubt es, n! und die Binomialkoeffi- zienten zu definieren. Die entsprechende Symbole, Summenze ichen und Produktzeichen \sum \prod ANALYSIS I-III, 2011/2013 13 erlauben eine abkürzende Schrei…
```
- **English explanation:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Intuition:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.3.8 — auch eine Familie von Elementen von X

- **Original term:** not explicitly named in script
- **Source:** PDF p15; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Formal definition / script statement:**
```latex
Seien I und X zwei Mengen. Eine Abbildung I → X , i \mapstoxi heißt auch eine Familie von Elementen von X , geschrieben ( xi)i\in I . Die Menge I heißt Indexmenge. Ist I = {1, 2, . . .,n} so heißt ( xi)i\in I = : (x1, . . .,xn) = : (xi)1\lei\len ein n-Tupel.
```
- **English explanation:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Intuition:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.3.9 — Summationsindex

- **Original term:** not explicitly named in script
- **Source:** PDF p15; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Formal definition / script statement:**
```latex
Für alle n \in N und alle n-Tupel ( x1, . . .,xn) von K gibt es Elemente \sumn i= 1 xi,\prodn i= 1 xi von K, rekursiv definiert durch 1\sum i= 1 xi := x1 , n+ 1\sum i= 1 xi := ( n\sum i= 1 xi ) + xn+ 1 , 1\prod i= 1 xi := x1 , n+ 1\prod i= 1 xi := ( n\prod i= 1 xi ) ·xn+ 1 . Sei I eine Indexmenge mit n Elementen, ( xi)i\in I eine Familie von Elementen von K. Sei I = {i1, . . .,i n} eine Aufzählung von I. Wir setzen \sum i\in I xi := n\sum k= 1 xi k = xi1 + . . .+ xi k , \prod i\in I xi := n\prod k= 1 xi k = xi1 + . . .+ xi k . Die Definition ist unabhängig von der Wahl der Aufzählung. Di e Menge I Der Buchstabe i heißt Summationsindex, er kann durch einen anderen Buchsta ben ersetzt werden, z. B. ist n\sum i= 1 xi = n\sum k= 1 xk . Natürlich sollte man hier nicht n als Summationsindex verwenden, da der Buchstabe bereits fü r die Gesamtzahl der Summanden in Gebrauch ist. Wir schreiben auch \sumn i= 1 xi = x1 + . . .+ xn, wenn es übersichtlicher ist. Eine nützliche Vereinbarung, die es uns oft erlaubt, Fallun terschiedungen zu vermeiden, ist die fol- gende: Die leere Summe ist 0 und das leere Produkt ist 1, d.h. (1.5) \sum i\in\emptyset xi := 0 , \prod i\in\emptyset xi := 1. Als Bei…
```
- **English explanation:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Intuition:** This definition gives precise language for the topic of construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.4.1 — unnamed definition in 1.4

- **Original term:** not explicitly named in script
- **Source:** PDF p15; section 1.4. Fakultät, Binomialkoeffizienten und binomischer Lehrsatz
- **Formal definition / script statement:**
```latex
Für n \in N0 wird n! (n Fakultät) definiert durch 0! := 1, n! := 1 ·2 ·. . .·n = n\prod k= 1 k, für n \in N also 0! = 1, 1! = 1, und n! = 1 ·2 ·. . .·n für n > 1. Warum definieren wir 0! : = 1? Weil dann die Rekursion n! = n ·(n − 1)!, die offenbar für n ≥ 2 stimmt, schon für n = 1 gilt. Zudem taucht 0! in zahlreichen Formeln auf. ANALYSIS I-III, 2011/2013 14
```
- **English explanation:** This definition gives precise language for the topic of factorials, generalized binomial coefficients, pascal-type identities, and the binomial theorem.
- **Intuition:** This definition gives precise language for the topic of factorials, generalized binomial coefficients, pascal-type identities, and the binomial theorem.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.4.2 — unnamed definition in 1.4

- **Original term:** not explicitly named in script
- **Source:** PDF p16; section 1.4. Fakultät, Binomialkoeffizienten und binomischer Lehrsatz
- **Formal definition / script statement:**
```latex
Für α \in K und k \in N0 definiert man die Binomialkoeffizienten „α über k“ durch ( α 0 ) = 1, ( α k ) := 1 k! k− 1\prod j= 0 (α − j) = α(α − 1) . . .(α − k + 1) k! für k \in N Es gilt also ( α 0 ) = 1 , ( α 1 ) = α, ( α 2 ) = α(α − 1) 2 · 31.10
```
- **English explanation:** This definition gives precise language for the topic of factorials, generalized binomial coefficients, pascal-type identities, and the binomial theorem.
- **Intuition:** This definition gives precise language for the topic of factorials, generalized binomial coefficients, pascal-type identities, and the binomial theorem.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.5.1 — Supremum/Infimum

- **Original term:** Supremum/Infimum
- **Source:** PDF p18; section 1.5. Vollständigkeitsaxiom
- **Formal definition / script statement:**
```latex
$s=\sup A$ means $s$ is an upper bound of $A$ and every smaller number fails to be an upper bound.
```
- **English explanation:** The supremum is the least ceiling, even if the set never reaches it.
- **Intuition:** The supremum is the least ceiling, even if the set never reaches it.
- **Why it matters:** The central language for completeness and existence proofs.
- **Used later:** Order axioms and boundedness. Later entries in and after 1.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.5.3 — Vollständigkeitsaxiom

- **Original term:** Vollständigkeitsaxiom
- **Source:** PDF p19; section 1.5. Vollständigkeitsaxiom
- **Formal definition / script statement:**
```latex
Every nonempty subset of $K$ that is bounded above has a supremum in $K$.
```
- **English explanation:** The real line has no gaps.
- **Intuition:** The real line has no gaps.
- **Why it matters:** Powers monotone convergence, Bolzano-Weierstrass, Cauchy completeness, IVT, compactness, and extrema.
- **Used later:** Supremum and ordered fields. Later entries in and after 1.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.5.4 — Körper der reellen Zahlen

- **Original term:** not explicitly named in script
- **Source:** PDF p20; section 1.5. Vollständigkeitsaxiom
- **Formal definition / script statement:**
```latex
Ein vollständig angeordneter Körper K heißt Körper der reellen Zahlen , bezeichnet mit R. Um diese Definition zu rechtfertigen müssen wir zwei Fragen b eantworten. Existiert ein Körper mit diesen Eigenschaften? Inwieweit ist er eindeutig bestimmt ?
```
- **English explanation:** This definition gives precise language for the topic of upper/lower bounds, supremum/infimum, completeness, and the axiomatic definition of the real numbers.
- **Intuition:** This definition gives precise language for the topic of upper/lower bounds, supremum/infimum, completeness, and the axiomatic definition of the real numbers.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.6.4 — Gauß-Klammer

- **Original term:** Gauß-Klammer
- **Source:** PDF p21; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Formal definition / script statement:**
```latex
Zu jedem x \in R heißt die ganze Zahl ⌊x⌋:= max { k \in Z : k \le x } die Gauß-Klammer oder ganzzahliger Anteil von x (d. h. die grösste ganze Zahl, die kleiner oder gleich x ist). Wir setzen frac( x) = x − ⌊ x⌋ (fractional part). Ist x ≥ 0, so ist frac( x) der Nachkommaanteil von x. Zum Beispiel ⌊3, 2⌋ = 3, frac(3 , 2) = 0, 2 und ⌊− 3, 2⌋ = − 4, frac(− 3, 2) = 0, 8. Für alle n \in Z gilt ⌊n⌋ = n. /Bullet/Circle /Bullet/Circle /Bullet/Circle /Bullet/Circle n − 1 xn = ⌊ x⌋ n + 1
```
- **English explanation:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Intuition:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 1.6.7 — ganzzahlige und rationale Potenzen

- **Original term:** ganzzahlige und rationale Potenzen
- **Source:** PDF p23; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Formal definition / script statement:**
```latex
Sei a \in R eine reelle Zahl. Wir definieren die ganzzahligen Potenzen an, n \in Z, durch (1.4) falls n \in N und a0 = 1 (auch für a = 0)(1.8) an = (a− 1)− n = (1 a )− n , für a ̸= 0, n \in Z, n < 0 .(1.9) Sei a > 0. Sei (1.10) a k m := m√ ak , für k \in Z, m \in N definiert. Damit ist also aq für jedes q \in Q erklärt. Man beweist durch Induktion die Potenzgesetze: am+ n = am ·an , an ·bn = (ab)n , (am)n = amn für a, b \in K, m, n \in N0 oder a, b \in K∗ , m, n \in Z. Die Definition (1.10) hängt von der Darstellung q = k/m der rationalen Zahl q nicht ab (siehe Aufgabe 1.8.12). Dann gelten die Potenzgesetze: (1.11) aqar = aq+ r , (aq)r = aqr , für a > 0 und q, r \in Q . ANALYSIS I-III, 2011/2013 22
```
- **English explanation:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Intuition:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.6.8 — Intervalle

- **Original term:** Intervalle
- **Source:** PDF p24; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Formal definition / script statement:**
```latex
Eine Teilmenge I \subset R heißt Intervall, wenn I mit je zwei Elemen- ten x \le y auch alle Elemente z mit x \le z \le y enthält. Beispiel. Seien a, b \in R, a ≤ b. Die beschränkten Intervalle sind: (a, b) := {x \in R : a < x < b} offenes Intervall (a, b] := {x \in R : a < x \le b} halboffenes Intervall [a, b) := {x \in R : a \le x < b} halboffenes Intervall [a, b] := {x \in R : a \le x \le b} abgeschlosses Intervall Das Intervall [ a, b] heißt auch kompakt. Später werden wir allgemeine offene, abgeschlossene und kompakte Mengen definieren. Für die obige Intervalle heißt d as Element a der Anfangspunkt und das Element b der Endpunkt des Intervalls. Wie definieren die Länge eines Intervalls I mit An- fangspunkt a und Endpunkt b durch | I| := | b − a| . Die unbeschränkten Intervalle sind: (a, \infty ) := {x \in R : a < x} [a, \infty ) := {x \in R : a \le x} (−\infty , b) := {x \in R : x < b} (−\infty , b] := {x \in R : x \le b}
```
- **English explanation:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Intuition:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.6.9 — Intervallschachtelung

- **Original term:** Intervallschachtelung
- **Source:** PDF p24; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Formal definition / script statement:**
```latex
Eine Familie (I n)n\inN von kompakten Intervallen heißt Intervallschachtelung , falls gilt: (i) I n+ 1 \subset I n für alle n \in N, und (ii) für alle \varepsilon> 0 gibt es n \in N mit | I n| < \varepsilon. a1 b1a2 b2 Beispiel: Die Familie von Intervallen I n = [0, 1 n ], n \in N, bildet eine Intervallschachtelung.
```
- **English explanation:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Intuition:** This definition gives precise language for the topic of consequences of completeness: archimedes, eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and euler's number.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.7.3 — imaginäre Einheit

- **Original term:** not explicitly named in script
- **Source:** PDF p26; section 1.7. Der Körper der komplexen Zahlen
- **Formal definition / script statement:**
```latex
Die (nicht-reelle) Zahl i = (0, 1) heißt imaginäre Einheit . Sei z = (x, y) = y + i y. Dann heißt x Realteil von z, und y heißt Imaginärteil von z, geschrieben Re z := x, Im z := y. Man beachte, dass der Imaginärteil y reell ist. Zahlen der Form i y mit y \in R heißen auch (rein) imaginär. Die konjugierte Zahl zu z = x + i y ist z := x − i y. Die konjugiert komplexe Zahl z wird oft als z quer bezeichnet.
```
- **English explanation:** This definition gives precise language for the topic of complex numbers as a field, real/imaginary parts, conjugation, modulus, and modulus rules.
- **Intuition:** This definition gives precise language for the topic of complex numbers as a field, real/imaginary parts, conjugation, modulus, and modulus rules.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.7 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.7.5 — | z|

- **Original term:** not explicitly named in script
- **Source:** PDF p26; section 1.7. Der Körper der komplexen Zahlen
- **Formal definition / script statement:**
```latex
Für z \in C heißt | z| := \sqrt z ·z = √ x2 + y2 der Betrag von z. Für z \in R ist | z| = \sqrt z2 der übliche Betrag von reellen Zahlen. Die geometrische Bed eutung von Re- alteil, Imaginärteil, Betrag und konjugiert komplexer Zah l wird in der Abbildung 2 skizziert. Nach Pythagoras ist | z| der Abstand des Punktes z vom Nullpunkt, siehe Abbildung 2. ANALYSIS I-III, 2011/2013 25 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /0/0/0/0/0/0/0/0/0/0 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /1/1/1/1/1/1/1/1/1/1 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /0/0/0/0 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /1/1/1/1 /0/0/0 /0/0/0 /0/0/0 /0/0/0 /0/0/0 /1/1/1 /1/1/1 /1/1/1 /1/1…
```
- **English explanation:** This definition gives precise language for the topic of complex numbers as a field, real/imaginary parts, conjugation, modulus, and modulus rules.
- **Intuition:** This definition gives precise language for the topic of complex numbers as a field, real/imaginary parts, conjugation, modulus, and modulus rules.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.7 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 1.9.3 — einfach Permutation von n Ele- menten

- **Original term:** not explicitly named in script
- **Source:** PDF p32; section 1.9. Notizen
- **Formal definition / script statement:**
```latex
Seien n, k \in N. Sei X eine n-elementige Menge. ◦ Eine k-Permutation ohne Wiederholung von n Elementen ist eine Auswahl von k verschiede- nen Elementen von X , bei der es auf die Reihenfolge ankommt. ◦ Eine n-Permutation ohne Wiederholung von n Elementen heißt einfach Permutation von n Ele- menten. ◦ Eine k-Kombination ohne Wiederholung von n Elementen ist eine Auswahl von k verschiede- nen Elementen von X , bei der es auf die Reihenfolge nicht ankommt. ◦ Eine k-Permutation mit Wiederholung von n Elementen ist eine Auswahl von k nicht unbe- dingt verschiedenen Elementen von X , bei der es auf die Reihenfolge ankommt. ◦ Eine k-Kombination mit Wiederholung von n Elementen ist eine Auswahl von k nicht unbe- dingt verschiedenen Elementen von X , bei der es auf die Reihenfolge nicht ankommt. Anstelle von k-Permutation ( k-Kombination) ohne Wiederholung sagt man einfach k-Permutation ( k- Kombination). ◦ Eine k-Permutation ist eine Familie ( x1, . . . ,xk) von verschiedenen Elementen von X , d.h. eine injektive Abbildung {1, . . . ,k} → X . Dabei muss k \le n sein. ◦ Eine Permutation ist eine bijektive Abbildung {1, . . . ,n} → X . ◦ Eine k-Kombination ist eine k-elementige Teilmenge {…
```
- **English explanation:** This definition gives precise language for the topic of notes on counting, pigeonhole principle, permutations/combinations, countability, and cardinality.
- **Intuition:** This definition gives precise language for the topic of notes on counting, pigeonhole principle, permutations/combinations, countability, and cardinality.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Appendix A logic/set language and earlier algebra/order material. Later entries in and after 1.9 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.1.1 — Konvergenz einer Folge

- **Original term:** Konvergenz einer Folge
- **Source:** PDF p35; section 2.1. Definition und Beispiele
- **Formal definition / script statement:**
```latex
$a_n\to a$ means $\forall\varepsilon>0\ \exists n_0\in\mathbb N\ \forall n\ge n_0: |a_n-a|<\varepsilon$.
```
- **English explanation:** Eventually every tail of the sequence lies in every prescribed epsilon-neighborhood of the limit.
- **Intuition:** Eventually every tail of the sequence lies in every prescribed epsilon-neighborhood of the limit.
- **Why it matters:** The basic limit definition behind all of Analysis.
- **Used later:** Absolute value, order, neighborhoods. Later entries in and after 2.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.1.4 — \varepsilon-Umgebung von a

- **Original term:** not explicitly named in script
- **Source:** PDF p37; section 2.1. Definition und Beispiele
- **Formal definition / script statement:**
```latex
Sei a \in R, \varepsilon > 0. Die Menge B\varepsilon(a) = {x \in R : | x − a| < \varepsilon} = (a − \varepsilon, a + \varepsilon) heißt \varepsilon-Umgebung von a. Jede Teilmenge U \subset R, zu der es ein \varepsilon> 0 mit B\varepsilon(a) \subset U gibt, heißt Umgebung von a. Umformulierung der Definition 2.1.1 der Konvergenz: limn→\infty an = a \Longleftrightarrow Zu jeder Umgebung U von a gibt es n0 \in N, so dass für alle n \ge n0 gilt: an \in U. Es ist zweckmäßig, die folgende Sprechweise zu benutzen: Wir sagen, dass fast alle Elemente einer Menge eine Eigenschaft haben, wenn höchstens endlich viele Eleme nte der Menge die betreffende Eigenschaft nicht haben. Neue Umformulierung der Definition 2.1.1 der Konverg enz: limn→\infty an = a \Longleftrightarrow Für jede Umgebung U von a gilt an \in U für fast alle n \in N. Durch Negation erhalten wir auch: (an)n\inN divergent \Longleftrightarrow Jedes a \in R hat eine Umgebung U, so dass an \notin U für unendlich viele n \in N. ANALYSIS I-III, 2011/2013 36 Beispiel: Die Folge 1 ,0,1,0, . . ., d.h. an = { 1, n ungerade 0, n gerade ist divergent. In der Tat, für jedes a \in R wähle U = B1/2(a) = (a − 1 2 , a + 1 2 ). Dann ist entwede…
```
- **English explanation:** This definition gives precise language for the topic of sequences, convergence, neighborhoods, elementary limits, boundedness, monotonicity, and monotone convergence.
- **Intuition:** This definition gives precise language for the topic of sequences, convergence, neighborhoods, elementary limits, boundedness, monotonicity, and monotone convergence.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.1.6 — beschränkt

- **Original term:** not explicitly named in script
- **Source:** PDF p40; section 2.1. Definition und Beispiele
- **Formal definition / script statement:**
```latex
(i) Eine Folge ( an)n\inN heißt beschränkt, wenn es M > 0 gibt, mit | an| \le M für alle n \in N. (ii) Eine reelle Folge ( an)n\inN heißt monoton wachsend (steigend) (bzw .fallend) wenn an \le an+ 1 (bzw . an \ge an+ 1) für alle n \in N gilt. Eine reelle Folge ( an)n\inN heißt streng monoton wachsend (steigend) (bzw .fallend) wenn an < an+ 1 (bzw .an > an+ 1) für alle n \in N gilt. Mit anderen Worten: Die Folge ( an) heißt beschränkt, wenn die Menge {an : n \in N} beschränkt ist. Analog definiert man die Begriffe nach oben und nach unten beschränkt . Wir geben nun ein wichtiges Kriterium, mit dem die Konvergen z einer Folge ohne Kenntnis ihres Grenz- wertes gezeigt werden kann. Es basiert sich am Ende auf dem Vo llständigkeitsaxiom.
```
- **English explanation:** This definition gives precise language for the topic of sequences, convergence, neighborhoods, elementary limits, boundedness, monotonicity, and monotone convergence.
- **Intuition:** This definition gives precise language for the topic of sequences, convergence, neighborhoods, elementary limits, boundedness, monotonicity, and monotone convergence.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.3.1 — endlich

- **Original term:** not explicitly named in script
- **Source:** PDF p44; section 2.3. Einschub: Abzählbare und überabzählbare Mengen
- **Formal definition / script statement:**
```latex
(i) Zwei Mengen X ,Y heißen gleichmächtig (geschrieben X ∼ Y ), wenn es eine bijektive Abbildung \varphi : X \to Y gibt. Die Relation X ∼ Y ist eine Äquivalenzrelation. (ii) Eine Menge X heißt endlich, falls X = \emptysetoder es ein n \in N gibt mit X ∼ {1, . . . ,n}. Die Kardinalzahl | X | (Anzahl der Elemente von X ) ist definiert durch | X | = 0 falls X = \emptysetund | X | = n falls X ∼ {1, . . . ,n}. ANALYSIS I-III, 2011/2013 43 (iii) Eine Menge heißt unendlich, wenn sie nicht endlich ist. (iv) Eine Menge X heißt abzählbar, falls X ∼ N und höchstens abzählbar , wenn sie endlich oder ab- zählbar ist. Ist X höchstens abzählbar , so heißt eine Bijektion f : {1, . . . ,n} → X oder f : N → X Aufzählung von X ; dann ist X = {x1, . . . ,xn, . . .}, xk = f (k). Ist X nicht höchstens abzählbar , so heißtX nicht abzählbar oder überabzählbar. 2.3.2. Beispiele. Die Funktion N0 → N, n \mapston + 1 ist bijektiv , also ist N0 abzählbar . Die Funktion f : Z → N, f (z) = 2z falls z \ge 0 und f (z) = − 2z − 1 falls z < 0 ist bijektiv . Daraus folgt, dass die Menge Z abzählbar ist; dies ist schon erstaunlich, weil es bedeutet, dass N und Z gleich viele Elemente haben, obwohl N eine echte Teilme…
```
- **English explanation:** This definition gives precise language for the topic of countable and uncountable sets, especially countability of rationals and uncountability of reals.
- **Intuition:** This definition gives precise language for the topic of countable and uncountable sets, especially countability of rationals and uncountability of reals.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.4.1 — Häufungswert

- **Original term:** not explicitly named in script
- **Source:** PDF p46; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Formal definition / script statement:**
```latex
Sei ( an)n\inN eine Folge in R. (i) a \in R heißt Häufungswert (HW) von ( an), wenn für jedes \varepsilon > 0 gilt: | an − a| < \varepsilon für unendlich viele n \in N. (ii) Ist ( nk)k\inN, n1 < n2 < n3 < . . .< nk < . . . eine streng monoton wachsende Folge in N, so heißt ( ank )k\inN , d.h. die Folge ( an1 , an2 , an3 , . . .) eine Teilfolge von ( an). Man soll beachten, dass in der Definition des Häufungswert, g efordert sind unendlich viele Indizes n, nicht notwendigerweise unendlich viele Werte an. Dies bedeutet, dass es eine streng monoton wachsende Folge n1 < n2 < n3 < . . .< nk < . . .in N existiert, mit | ank − a| < \varepsilon für alle k \in N. Unabhängig davon, wie weit die Folge läuft, kommen immer wieder Folgenglieder in das Intervall ( a − \varepsilon, a + \varepsilon) hinein. Eine Teilfolge entsteht, indem man aus einer Folge ( an) einzelne Glieder „herausnimmt“, jedoch so, dass die Indizes streng wachsend bleiben. Diese Bedingung stellt si cher , dass eine Teilfolge weiterhin „in der richtigen Reihenfolge“ verläuft und eine echte Folge bleibt. Bei eine r Teilfolge (ank )k\inN ist der Index, der alle natürlichen Werte annimmt, nicht n, sondern k.
```
- **English explanation:** This definition gives precise language for the topic of accumulation values, subsequences, bolzano-weierstrass, limsup/liminf, and the cauchy criterion.
- **Intuition:** This definition gives precise language for the topic of accumulation values, subsequences, bolzano-weierstrass, limsup/liminf, and the cauchy criterion.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.4.6 — unnamed definition in 2.4

- **Original term:** not explicitly named in script
- **Source:** PDF p48; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Formal definition / script statement:**
```latex
Sei ( an)n\inN eine beschränkte Folge in R. Man nennt h∗ den oberen Limes oder Limes superior, h∗ den unteren Limes oder Limes inferior der Folge ( an)n\inN und schreibt dafür h∗ = lim sup n→\infty an = limn→\infty an , h∗ = lim infn→\infty an = limn→\infty an .
```
- **English explanation:** This definition gives precise language for the topic of accumulation values, subsequences, bolzano-weierstrass, limsup/liminf, and the cauchy criterion.
- **Intuition:** This definition gives precise language for the topic of accumulation values, subsequences, bolzano-weierstrass, limsup/liminf, and the cauchy criterion.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.4.8 — Cauchy-Folge

- **Original term:** not explicitly named in script
- **Source:** PDF p48; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Formal definition / script statement:**
```latex
Eine Folge ( an)n\inN heißt Cauchy-Folge (CF), wenn gilt: Zu jedem \varepsilon > 0 gibt es n0 = n0(\varepsilon) \in N mit | am − an| < \varepsilon für alle n, m \ge n0. Locker ausgedrückt bedeutet dies, dass die Folgenglieder i mmer dichter zusammenrücken.
```
- **English explanation:** This definition gives precise language for the topic of accumulation values, subsequences, bolzano-weierstrass, limsup/liminf, and the cauchy criterion.
- **Intuition:** This definition gives precise language for the topic of accumulation values, subsequences, bolzano-weierstrass, limsup/liminf, and the cauchy criterion.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.5.1 — unbestimmt divergent

- **Original term:** not explicitly named in script
- **Source:** PDF p49; section 2.5. Uneigentliche Grenzwerte
- **Formal definition / script statement:**
```latex
Wir sagen, eine Folge ( an) divergiere oder strebe gegen \infty wenn es zu jedem M > 0 ein n0 \in N gibt, sodass für alle n \ge n0 gilt: an > M. Wir schreiben limn→\infty an = \infty oder an → \infty , n → \infty . Wir sagen, eine Folge ( an) divergiere oder strebe gegen −\infty wenn es zu jedem M < 0 ein n0 \in N gibt, so dass für alle n \ge n0 gilt: an < M. Wir schreiben limn→\infty an = −\infty oder an → −\infty , n → \infty . Wenn entweder an → \infty oder an → −\infty gilt, nennen wir die Folge ( an) bestimmt divergent, und die Sym- bole \infty („plus Unendlich“) bzw . −\infty („minus Unendlich“) werden gelegentlich als uneigentlich e Grenz- werte von ( an) bezeichnet. Eine divergente Folge die nicht bestimmt dive rgent ist, heißt unbestimmt divergent.
```
- **English explanation:** This definition gives precise language for the topic of improper limits and the extended real line.
- **Intuition:** This definition gives precise language for the topic of improper limits and the extended real line.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.5.3 — die erweiterte Zahlengerade

- **Original term:** not explicitly named in script
- **Source:** PDF p50; section 2.5. Uneigentliche Grenzwerte
- **Formal definition / script statement:**
```latex
(i) Wir definieren R = R\cup {−\infty ,+\infty }, wobei −\infty \notin R, +\infty \notin R zwei (ideale) Elemente sind. R heißt die erweiterte Zahlengerade. Wir erweitern die Ordnungsrelation in R auf R durch −\infty < x < \infty für alle x \in R . Weiterhin definieren wir: \infty + \infty := \infty , (−\infty ) + (−\infty ) := −\infty , ±\infty + x = x + (±\infty ) := ±\infty für x \in R sowie ±\infty · x = x ·(±\infty ) := { ±\infty für x > 0, x \in R ∓\infty für x < 0, x \in R und x ±\infty := 0 für x \in R. Anbei ist eine Übersicht der Definitionen der Operationen mi t ±\infty : (2.8) + a \in R \infty −\infty b \in R a + b +\infty −\infty +\infty +\infty +\infty ∗ −\infty −\infty ∗ −\infty und · a > 0 0 a < 0 +\infty −\infty b > 0 a ·b 0 a ·b +\infty −\infty 0 0 0 0 ∗ ∗ b < 0 a ·b 0 a ·b −\infty +\infty +\infty +\infty ∗ −\infty +\infty −\infty −\infty −\infty ∗ +\infty −\infty +\infty Hierbei bedeutet ∗ , dass die Addition bzw . die Multiplikation nicht definiert i st, d.h. wir haben \infty + (−\infty ) und (−\infty ) + \infty nicht definiert und wir haben auch 0 ·(±\infty ) nicht definiert (siehe die Bemerkung unten). Die Regel für die Multiplikation kann man kurz auch so sc…
```
- **English explanation:** This definition gives precise language for the topic of improper limits and the extended real line.
- **Intuition:** This definition gives precise language for the topic of improper limits and the extended real line.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.6.1 — konvergent

- **Original term:** not explicitly named in script
- **Source:** PDF p52; section 2.6. Folgen komplexer Zahlen
- **Formal definition / script statement:**
```latex
(i) Eine Folge ( an)n\inN in C heißt konvergent, wenn es a \in C gibt mit der Eigenschaft: Zu jedem \varepsilon > 0 gibt es n0 = n0(\varepsilon) \in N, so dass für alle n \in N mit n \ge n0 gilt: | an − a| < \varepsilon. Eine Zahl a \in C wie in der Definition heißt Grenzwert oder Limes der Folge. Wir schreiben limn→\infty an = lim an = a, oder an → a für n → \infty und sagen, dass ( an)n\inN gegen a konvergiert. (ii) Eine nicht konvergente Folge heißt divergent. Sei a \in C, \varepsilon> 0. Die Menge B\varepsilon(a) = {z \in C : | z − a| < \varepsilon} heißt \varepsilon-Umgebung von a. Jede Teilmenge U \subset C, zu der es ein \varepsilon > 0 mit B\varepsilon(a) \subset U gibt, heißt Umgebung von a. Umformulierung der Definition 2.6.1 der Konvergenz: limn→\infty an = a \Longleftrightarrow Zu jeder Umgebung U von a gibt es n0 = n0(U) \in N, so dass für alle n \ge n0 gilt: an \in U.
```
- **English explanation:** This definition gives precise language for the topic of complex sequences and reduction to real and imaginary parts.
- **Intuition:** This definition gives precise language for the topic of complex sequences and reduction to real and imaginary parts.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.6.5 — unnamed definition in 2.6

- **Original term:** not explicitly named in script
- **Source:** PDF p53; section 2.6. Folgen komplexer Zahlen
- **Formal definition / script statement:**
```latex
Die Definitionen von beschränkten Folgen, von Häufungswert en in C und Cauchy- Folgen übertragen sich wörtlich aus der jeweiligen reellen Version (Definitionen 2.1.6, 2.4.1, 2.4.8).
```
- **English explanation:** This definition gives precise language for the topic of complex sequences and reduction to real and imaginary parts.
- **Intuition:** This definition gives precise language for the topic of complex sequences and reduction to real and imaginary parts.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 2.6.8 — die erweiterte Zahlenebene

- **Original term:** not explicitly named in script
- **Source:** PDF p53; section 2.6. Folgen komplexer Zahlen
- **Formal definition / script statement:**
```latex
(i) Wir ergänzen C durch ein (ideales) Element \infty \notin C und setzten C = C \cup {\infty }. Die Menge C heißt die erweiterte Zahlenebene . Geometrisch handelt es sich um die Menge, die sich aus der Hi nzunahme eines Punktes in der Unendlichkeit zu der komplexen Ebene er gibt. (ii) Eine Menge U \subset C heißt Umgebung von \infty in C , wenn es M > 0 gibt, so dass U \supset {| z| > M}. (iii) Eine Folge ( an)n\inN in C konvergiert in C gegen \infty : \Longleftrightarrow Für jede Umgebung U von \infty gilt an \in U für fast alle n \in N, \Longleftrightarrow limn→\infty | an| = \infty . Schreibweise: an \to \infty oder lim n→\infty an = \infty in C.
```
- **English explanation:** This definition gives precise language for the topic of complex sequences and reduction to real and imaginary parts.
- **Intuition:** This definition gives precise language for the topic of complex sequences and reduction to real and imaginary parts.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Chapter 1 real-number foundations, absolute value, and completeness. Later entries in and after 2.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 3.1.1 — Reihe

- **Original term:** not explicitly named in script
- **Source:** PDF p57; section 3.1. Definitionen und Beispiele
- **Formal definition / script statement:**
```latex
(i) Sei ( an)n\geq eine Folge in C. Dazu definiere ( sn)n\geq durch sq = aq, sq+ 1 = aq + aq+ 1, . . . ,sn = \sumn j= q a j. Das Folgenpaar (( an)n\geq,(sn)n\geq) heißt Reihe mit Gliedern an und wird mit \sum n\geq an bezeichnet. Die Zahl sn heißt n-te Partialsumme der Reihe. (ii) \sum n\geq an heißt konvergent, wenn ( sn)n\geq konvergent ist. Gilt sn \to s \in C, so schreibt man s = \infty\sum n= q an = limn→\infty n\sum k= q ak . Die Zahl s heißt die Summe der Reihe. (iii) Eine nicht konvergente Reihe heißt divergent. Sind die an reell, und gilt sn \to \infty (bzw .−\infty ), so ist\sum n\geq an bestimmt divergent mit \sum\infty n= q an = \infty (bzw .−\infty ). 3.1.2. Beispiele. (i) Die geometrische Reihe 1 + z + z2 + . . .= \sum n\ge0 zn mit z \in C. Für z ̸= 1 gilt sn = 1 + z + z2 + . . .+ zn = 1 − zn+ 1 1 − z . Für | z| < 1 ist lim n→\infty zn+ 1 = 0, also \sum\infty n= 0 zn = 1 1 − z . (ii) Die folgende Reihe ist eine Teleskopreihe: \sum n\ge1 1 n(n + 1) = 1 1 ·2 + 1 2 ·3 + 1 3 ·4 + . . . Das sieht man so: Man verwendet 1 k − 1 k + 1 = (k + 1) − k k(k + 1) = 1 k(k + 1) . Damit ergibt sich sn = (1 1 − 1 2 ) + (1 2 − 1 3 ) + (1 3 − 1 4 ) + · · · + ( 1 n − 1 n + 1 ) = 1 − 1 n…
```
- **English explanation:** This definition gives precise language for the topic of series as limits of partial sums.
- **Intuition:** This definition gives precise language for the topic of series as limits of partial sums.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, Cauchy criteria, and comparison estimates. Later entries in and after 3.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 3.3.1 — Absolute Konvergenz

- **Original term:** Absolute Konvergenz
- **Source:** PDF p59; section 3.3. Absolute Konvergenz
- **Formal definition / script statement:**
```latex
$\sum a_n$ is absolutely convergent if $\sum |a_n|$ converges.
```
- **English explanation:** The series converges even after removing all cancellation.
- **Intuition:** The series converges even after removing all cancellation.
- **Why it matters:** Absolute convergence is stable and supports rearrangements/products in many contexts.
- **Used later:** Series and comparison. Later entries in and after 3.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 3.3.9 — unnamed definition in 3.3

- **Original term:** not explicitly named in script
- **Source:** PDF p62; section 3.3. Absolute Konvergenz
- **Formal definition / script statement:**
```latex
Die komplexen Potenzen ez mit z \in C sind definiert durch (3.7) ez := exp(z) , z \in C . Um Potenzen az mit a > 0, z \in C zu definieren, müssen wir warten, bis das Logarithmus definie rt wird. Als Vorgeschmack lautet die Definition az := ez log a (siehe Definition 4.2.5). 3.4. Potenzreihen.
```
- **English explanation:** This definition gives precise language for the topic of absolute convergence, product rules, exponential series, and related identities.
- **Intuition:** This definition gives precise language for the topic of absolute convergence, product rules, exponential series, and related identities.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, Cauchy criteria, and comparison estimates. Later entries in and after 3.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 3.4.1 — unnamed definition in 3.4

- **Original term:** not explicitly named in script
- **Source:** PDF p62; section 3.4. Potenzreihen
- **Formal definition / script statement:**
```latex
Sei R die Menge der Reihen mit komplexen Gliedern. Eine Potenzreihe ist eine Ab- bildung P : C \to R der Form P(z) = \sum n\ge0 an zn. Die Zahlen an heißen Koeffizienten der Reihe. Gilt an \in R für alle n, so spricht man von einer reellen Potenzreihe P : R \to R, P(x) = \sum n\ge0 an xn. Die Theorie der reellen Potenzreihen ergibt sich aus der Theorie der kom plexen Potenzreihen durch Einschränkung der Variablen z \in C auf R.
```
- **English explanation:** This definition gives precise language for the topic of power series, abel's convergence lemma, radius of convergence, and sine/cosine series.
- **Intuition:** This definition gives precise language for the topic of power series, abel's convergence lemma, radius of convergence, and sine/cosine series.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, Cauchy criteria, and comparison estimates. Later entries in and after 3.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 3.4.5 — Konvergenzradius und BR

- **Original term:** not explicitly named in script
- **Source:** PDF p62; section 3.4. Potenzreihen
- **Formal definition / script statement:**
```latex
Die Zahl R aus (3.8) heißt Konvergenzradius und BR(0) heißt Konvergenzscheibe der Potenzreihe. Wir verabreden, dass BR(0) := C, falls R = \infty . Beispiele. (1) Die geometrische Reihe \sum k\ge0 zk. Dann gilt ak = 1 für alle k \in N0. Wir wissen bereits: Für | x| < 1 konvergiert die Reihe absolut und für | x| > 1 divergiert sie. Daraus folgt: R = 1. (2) Exponentialreihe: \sum n\ge0 zn n! . Die Reihe konvergiert für alle z \in C, also R = \infty . 12.12.25 3.4.6. Definition und Satz. Die Cosinus-Reihe und Sinus-Reihe \sum n\ge0 (− 1)n (2n)! z2n , \sum n\ge0 (− 1)n (2n + 1)! z2n+ 1 ANALYSIS I-III, 2011/2013 61 haben Konvergenzradius R = \infty und definieren die Cosinus- und Sinus-Funktion (3.9) cos : C → C , cos z = \infty\sum n= 0 (− 1)n (2n)! z2n , sin : C → C , sin z = \infty\sum n= 0 (− 1)n (2n + 1)! z2n+ 1
```
- **English explanation:** This definition gives precise language for the topic of power series, abel's convergence lemma, radius of convergence, and sine/cosine series.
- **Intuition:** This definition gives precise language for the topic of power series, abel's convergence lemma, radius of convergence, and sine/cosine series.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, Cauchy criteria, and comparison estimates. Later entries in and after 3.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 4.1.1 — Stetigkeit

- **Original term:** Folgen-Definition der Stetigkeit
- **Source:** PDF p68; section 4.1. Stetige Funktionen
- **Formal definition / script statement:**
```latex
$f$ is continuous at $x_0$ if $x_n\to x_0$ implies $f(x_n)\to f(x_0)$, equivalently by the epsilon-delta condition when stated.
```
- **English explanation:** Inputs close to $x_0$ force outputs close to $f(x_0)$.
- **Intuition:** Inputs close to $x_0$ force outputs close to $f(x_0)$.
- **Why it matters:** Continuity connects limits, topology, IVT, extrema, and compactness.
- **Used later:** Sequences and limits. Later entries in and after 4.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 4.1.6 — monoton steigend

- **Original term:** not explicitly named in script
- **Source:** PDF p70; section 4.1. Stetige Funktionen
- **Formal definition / script statement:**
```latex
Sei I \subset R ein Intervall. Eine Funktion f : I \to R heißt monoton steigend (bzw .fal- lend) :⇐ ⇒ Für alle x, y \in I mit x \le y gilt f (x) \le f (y) (bzw . f (x) \ge f (y)). Eine Funktion f : I \to R heißt streng monoton steigend (bzw .fallend) :⇐ ⇒ Für alle x, y \in I mit x < y gilt f (x) < f (y) (bzw . f (x) > f (y)). Bemerkung: Wenn f streng monoton ist, dann ist f injektiv . Beispiel: Stetigkeit der Wurzelfunktion. Sei k \in N. Seien 0 ≤ a < b. Dann ist f : [ k\sqrta, k\sqrt b ] \to [ a, b ] mit f (x) := xk stetig monoton steigend. Wegen Satz 4.1.4 ist g = f − 1 = k\sqrt·: [ a, b ] \to [ k\sqrta, k\sqrt b ] stetig; es folgt, dass die durch h(x) := k\sqrtx definierte Funktion h : [0,\infty ) \to R stetig ist. 4.2. Der Zwischenwertsatz. Der Zwischenwertsatz bildet die Grundlage vieler Existenz aussagen der Ana- lysis.
```
- **English explanation:** This definition gives precise language for the topic of continuity via sequences and epsilon-delta language, algebra and composition of continuous functions.
- **Intuition:** This definition gives precise language for the topic of continuity via sequences and epsilon-delta language, algebra and composition of continuous functions.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, limits, intervals, and completeness. Later entries in and after 4.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 4.2.5 — Potenzfunktion zum Exponenten z und die Funk- tion C ∋ z \mapstoxz \i…

- **Original term:** not explicitly named in script
- **Source:** PDF p71; section 4.2. Der Zwischenwertsatz
- **Formal definition / script statement:**
```latex
Für x > 0 und z \in C definieren wir (4.1) xz := exp(z ·log x) = ez·log x . Die Funktion R+ ∋ x \mapstoxz \in C (für festes z \in C) heißt Potenzfunktion zum Exponenten z und die Funk- tion C ∋ z \mapstoxz \in C (für festes x > 0) heißt Exponentialfunktion zur Basis x. Für alle x > 0, q \in Q stimmt die obige Definition von xq mit unserer früheren Definition 1.6.7 überein (siehe Übung 4.5.4). Als Komposition stetiger Funktionen sind sow ohl die Potenzfunktionene als auch die Exponen- tialfunktionen stetig. Es gelten die Potenzgesetze (vgl. (1.11)) (4.2) ( x y)z = xz yz , xz+ w = xz xw , (xa)z = xaz , für alle x, y > 0, z, w \in C und a \in R Außerdem gilt für x > 1 und a < b gilt xa < xb; für a > 0 und x < y gilt xa < ya. 08.01.26 ANALYSIS I-III, 2011/2013 70 4.3. Satz vom Maximum und Minimum. Zu den grundlegenden mathematischen Sätzen zählt der folge n- de: 4.3.1. Satz (Satz vom Maximum und Minimum (Weierstraß)) . Eine stetige Funktion auf einem nichtleeren kompakten Intervall ist beschränkt und nimmt ihr Maximum un d ihr Minimum an. Genauer: Seien a, b \in R mit a ≤ b, und sei f : [ a, b] → R eine stetige Funktion. Dann gibt es xmin, xmax \in [a, b] so, dass für alle x \in [a, b…
```
- **English explanation:** This definition gives precise language for the topic of intermediate value theorem, inverse functions, roots, logarithm, and exponential/logarithmic relationships.
- **Intuition:** This definition gives precise language for the topic of intermediate value theorem, inverse functions, roots, logarithm, and exponential/logarithmic relationships.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, limits, intervals, and completeness. Later entries in and after 4.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 4.4.1 — Häufungspunkt einer Menge D \subset C

- **Original term:** not explicitly named in script
- **Source:** PDF p73; section 4.4. Grenzwerte von Funktionen
- **Formal definition / script statement:**
```latex
Ein Punkt z0 \in C = C \cup {\infty } heißt Häufungspunkt einer Menge D \subset C, falls es eine Folge (zn) in D \ {z0} gibt mit lim n→\infty zn = z0. Analog heißt x0 \in R = R\cup {−\infty ,+\infty } Häufungspunkt einer Menge D \subset R, falls es eine Folge ( xn) in D \{ x0} gibt mit lim n→\infty xn = x0. Ein Punkt z0 \in D, der kein Häufungspunkt von D ist, heißt isolierter Punkt von D. Beachten Sie: Ein Häufungspunkt x0 von D muss nicht in D liegen. Falls x0 \in D, so müssen die xn alle ungleich x0 sein. Beachten Sie auch, dass wir \infty \in C und −\infty ,+\infty \in R als Häufungspunkte zulassen. Beispiele. (1) Jedes x0 \in [0,1] ist Häufungspunkt von (0 ,1): Für x0 \in (0,1] kann man zum Beispiel xn = x0 ( 1 − 1 n ) nehmen, für x0 = 0 die Folge xn = 1 n , wobei jeweils n ≥ 2. Weitere Häufungspunkte gibt es offenbar nicht. (2) Z hat keinen Häufungspunkt in R. Eine Teilmenge von R mit dieser Eigenschaft nennt man diskret. Insbe- sondere sind alle Punkte von Z isoliert. In R hat Z die Häufungspunkte ±\infty . (3) Die Menge der Häufungspunkte von Q ist R. Es ist wichtig, Häufungspunkte von Mengen und Häufungswerte von Folgen zu unterscheiden. Zum Beispiel hat die Folge ( xn)n\…
```
- **English explanation:** This definition gives precise language for the topic of limits of functions and their relation to continuity.
- **Intuition:** This definition gives precise language for the topic of limits of functions and their relation to continuity.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, limits, intervals, and completeness. Later entries in and after 4.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 4.4.2 — unnamed definition in 4.4

- **Original term:** not explicitly named in script
- **Source:** PDF p73; section 4.4. Grenzwerte von Funktionen
- **Formal definition / script statement:**
```latex
(i) Sei D \subset C, z0 \in C ein Häufungspunkt von D, a \in C. Wir sagen, dass f : D \to C in z0 den Grenzwert a hat, falls für alle Folgen ( zn) in D \ {z0} gilt: limn→\infty zn = z0 \Rightarrow limn→\infty f (zn) = a Schreibweise: lim z→ z0 f (z) = a. (ii) Sei D \subset R, x0 \in R ein Häufungspunkt von D, a \in R. Wir sagen, dass f : D \to R in x0 den Grenzwert a hat, falls für alle Folgen ( xn) in D \ {x0} gilt: limn→\infty xn = x0 \Rightarrow limn→\infty f (xn) = a ANALYSIS I-III, 2011/2013 72 Schreibweise: lim x→ x0 f (x) = a. Beispiele. (1) Sei D := C\{0}, f : D \to C, f (z) = exp(z)− 1 z . Dann ist z0 = 0 ein Häufungspunkt von D. Wir haben schon gezeigt in 4.3, dass lim z→ 0 exp(z) − 1 z = 1. (2) Für n \in N0 gilt (4.4) limx→\infty ex xn = \infty Dafür benutzen wir die folgende Abschätzung für x > 0: ex = \infty\sum k= 0 xk k! > xn+ 1 (n + 1)! , also ex xn > x (n + 1)! Sei xk → \infty , k → \infty . Wegen exk xn k > xk (n + 1)! , k \in N folgt exk xn k → \infty , k → \infty . (3) Es gilt lim x→\infty log x = \infty . In der Tat, sei xn → \infty . Zu zeigen ist, dass für alle Folgen xn → \infty , gilt log xn → \infty . Sei C \in R beliebig. Weil xn → \infty , existiert ein…
```
- **English explanation:** This definition gives precise language for the topic of limits of functions and their relation to continuity.
- **Intuition:** This definition gives precise language for the topic of limits of functions and their relation to continuity.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, limits, intervals, and completeness. Later entries in and after 4.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 4.4.5 — Einseitige Grenzwerte

- **Original term:** Einseitige Grenzwerte
- **Source:** PDF p75; section 4.4. Grenzwerte von Funktionen
- **Formal definition / script statement:**
```latex
Seien D \subset R, f : D → R und x0 \in D. (1) Angenommen, x0 ist Häufungspunkt von D+ := {x \in D : x > x0}. Falls der Grenzwert limx→ x0 x\in D+ f (x) = a existiert, so heißt a der rechtsseitige Grenzwert von f bei x0. (2) Angenommen, x0 ist Häufungspunkt von D− := {x \in D : x < x0}. Falls der Grenzwert limx→ x0 x\in D− f (x) = a existiert, so heißt a der linksseitige Grenzwert von f bei x0. Man schreibt auch limx→ x0+ f (x), bzw . limx→ x0− f (x) für den rechts- bzw . linksseitigen Grenzwert. ANALYSIS I-III, 2011/2013 74
```
- **English explanation:** This definition gives precise language for the topic of limits of functions and their relation to continuity.
- **Intuition:** This definition gives precise language for the topic of limits of functions and their relation to continuity.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, limits, intervals, and completeness. Later entries in and after 4.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 5.1.1 — Differenzierbarkeit

- **Original term:** Differenzierbarkeit
- **Source:** PDF p79; section 5.1. Definition und erste Eigenschaften
- **Formal definition / script statement:**
```latex
$f$ is differentiable at $x_0$ if $\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$ exists.
```
- **English explanation:** The function has a best linear first-order approximation at the point.
- **Intuition:** The function has a best linear first-order approximation at the point.
- **Why it matters:** Basis for local analysis, monotonicity, optimization, Taylor formulas, and multivariable differentials.
- **Used later:** Function limits and continuity. Later entries in and after 5.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 5.3.1 — innerer Punkt von I

- **Original term:** not explicitly named in script
- **Source:** PDF p84; section 5.3. Mittelwertsätze
- **Formal definition / script statement:**
```latex
Sei I \subset R ein Intervall. Ein Punkt x0 \in I heißt innerer Punkt von I :⇐ ⇒ es gibt eine Umgebung U von x0 in R mit U \subset I \Longleftrightarrow es gibt δ > 0 mit ( x0 − δ, x0 + δ) \subset I \Longleftrightarrow x0 \notin {sup I,inf I}. Die Menge ̊I := {x \in I : x innerer Punkt von I} = (sup I,inf I) heißt das Innere von I.
```
- **English explanation:** This definition gives precise language for the topic of rolle, mean value theorem, cauchy mean value theorem, and l'hospital-type results.
- **Intuition:** This definition gives precise language for the topic of rolle, mean value theorem, cauchy mean value theorem, and l'hospital-type results.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Function limits, continuity, and algebra of limits. Later entries in and after 5.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 5.3.2 — lokales Extremum

- **Original term:** not explicitly named in script
- **Source:** PDF p84; section 5.3. Mittelwertsätze
- **Formal definition / script statement:**
```latex
Sei I \subset R ein Intervall und x0 \in I. (1) Die Funktion f : I \to R hat in x0 ein lokales Maximum (bzw .Minimum) :⇐ ⇒ es gibt eine Umgebung U von x0 in I mit f (x) \le f (x0) (bzw . f (x) \ge f (x0)) für alle x \in U. Ein Punkt heißt lokales Extremum, falls er ein lokales Maximum oder ein lokales Minimum ist. (2) Die Funktion f : I \to R hat in x0 ein globales Maximum (bzw .Minimum) : \Longleftrightarrow es gilt f (x) \le f (x0) (bzw . f (x) \ge f (x0)) für alle x \in I. Ein Punkt heißt globales Extremum , falls er ein globales Maximum oder ein globales Minimum ist. (3) Ein innerer Punkt x0 \in I heißt kritischer Punkt für f : I \to R, falls f in x0 differenzierbar ist und f ′(x0) = 0 gilt. (4) Ein kritischer Punkt x0 \in I heißt Sattelpunkt von f , wenn es ein δ > 0 gibt mit ( x0 − δ, x0 + δ) \subset I und f (x) < f (x0) für x \in (x0 − δ, x0) und f (x) > f (x0) für x \in (x0, x0 + δ) oder umgekehrt. Um die x-Koordinate des globalen/lokalen Maximums bzw . Minimums v om dort angenommenen Funktions- wert zu unterscheiden, spricht man auch von einer globalen/ lokalen Maximumsstelle bzw . Minimumsstel- le.
```
- **English explanation:** This definition gives precise language for the topic of rolle, mean value theorem, cauchy mean value theorem, and l'hospital-type results.
- **Intuition:** This definition gives precise language for the topic of rolle, mean value theorem, cauchy mean value theorem, and l'hospital-type results.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Function limits, continuity, and algebra of limits. Later entries in and after 5.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 5.5.3 — Kreiszahl

- **Original term:** not explicitly named in script
- **Source:** PDF p93; section 5.5. Trigonometrische Funktionen
- **Formal definition / script statement:**
```latex
Setze π := 2x0 (d.h. x0 = π/2 ). Die Zahl π heißt Kreiszahl.
```
- **English explanation:** This definition gives precise language for the topic of trigonometric functions and their analytic properties.
- **Intuition:** This definition gives precise language for the topic of trigonometric functions and their analytic properties.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Function limits, continuity, and algebra of limits. Later entries in and after 5.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 5.6.1 — Landau-Symbole

- **Original term:** Landau-Symbole
- **Source:** PDF p95; section 5.6. Notizen
- **Formal definition / script statement:**
```latex
Seien D \subset C, z0 \in C ein HP von D, f : D \to C, g : D \to C. (i) Wir schreiben f (z) = o(g(z)) für z → z0, z \in D (gelesen: f (z) gleich klein-o von g(z)), falls zu jedem \varepsilon > 0 eine Umgebung U von z0 existiert, so dass | f (z)| \le \varepsilon| g(z)| für alle z \in D \cap U . Ist g(z) ̸= 0 für alle z in einer Umgebung U von z0, so ist diese Bedingung äquivalent zu lim z→ z0 f (z) g(z) = 0. (ii) Gilt zusätzlich lim z→ z0 g(z) = 0, so sagen wir auch: „ f strebt für z → z0 schneller gegen 0 als g“. Ferner schreibt man f = h + o(g) für f − h = o(g). (iii) Wir schreiben f (z) = O(g(z)) für z \in D, wenn eine Konstante C existiert, so dass | f (z)| \le C| g(z)| für alle z \in D . ANALYSIS I-III, 2011/2013 94 (iv) Wir schreiben f (z) = O(g(z)) für z → z0, z \in D, wenn eine Konstante C und eine Umgebung U von z0 existieren, so dass | f (z)| \le C| g(z)| für alle z \in D \cap U .
```
- **English explanation:** This definition gives precise language for the topic of notes around differentiability and related refinements.
- **Intuition:** This definition gives precise language for the topic of notes around differentiability and related refinements.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Function limits, continuity, and algebra of limits. Later entries in and after 5.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.2.1 — Treppenfunktion

- **Original term:** not explicitly named in script
- **Source:** PDF p100; section 6.2. Das Integral von Treppenfunktionen
- **Formal definition / script statement:**
```latex
Eine Funktion \varphi : [a, b] \to C heißt Treppenfunktion, wenn es eine Zerlegung Z = {x0, . . . ,xn} mit a = x0 < x1 < . . .< xn− 1 < xn = b von [ a, b] gibt so, dass \varphi für jedes k = 1, . . . ,n auf ( xk− 1, xk) jeweils konstant ist. Über die Funktionswerte \varphi (xk) in den Teilpunkten wird nichts gefordert. Notation: T([a, b]) := {\varphi : [a, b] \to C : \varphi Treppenfunktion}.
```
- **English explanation:** This definition gives precise language for the topic of step functions and their integral.
- **Intuition:** This definition gives precise language for the topic of step functions and their integral.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.2.4 — Integral von Treppenfunktionen

- **Original term:** Integral von Treppenfunktionen
- **Source:** PDF p100; section 6.2. Das Integral von Treppenfunktionen
- **Formal definition / script statement:**
```latex
For a step function $\varphi$ constant with values $c_k$ on intervals $(x_{k-1},x_k)$, define $\int_a^b\varphi(x)\,dx=\sum_k c_k(x_k-x_{k-1})$.
```
- **English explanation:** Area is built by summing rectangles.
- **Intuition:** Area is built by summing rectangles.
- **Why it matters:** Starting point for regulated and Riemann-type integration.
- **Used later:** Partitions and step functions. Later entries in and after 6.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.3.1 — Regelfunktion

- **Original term:** not explicitly named in script
- **Source:** PDF p101; section 6.3. Das Integral von Regelfunktionen
- **Formal definition / script statement:**
```latex
Eine Funktion f : [a, b] \to C heißt Regelfunktion, wenn es zu jedem \varepsilon > 0 eine Trep- penfunktion \varphi \in T([a, b]) gibt mit \| f − \varphi \| \le \varepsilon, d.h. | f (x)− \varphi (x)| \le \varepsilon für alle x \in [a, b] (\varphi weicht nirgends mehr als \varepsilon von f ab). Dann heißt \varphi eine \varepsilon-approximierende TF zu f . Sei I \in R ein beliebiges Intervall. Eine Funktion f : I \to C heißt Regelfunktion, falls für jedes kompakte Intervall [ a, b] \subset I die Einschränkung f | [a,b] eine Regelfunktion ist. Notation: R(I) = {f : I \to C : f Regelfunktion}. Sei f \in R([a, b]). Eine Folge ( \varphi n)n\inN von TF heißt eine approximierende Folge von TF für f , falls \| f − \varphi n\| → 0 für n → \infty . (Eine solche Folge existiert immer , z.B. \varphi n TF mit \| f − \varphi n\| \le 1 n ·Man sagt auch, die Funktionenfolge (\varphi n) konvergiert gleichmäßig gegen f ). Bemerkung: (i) Jede Regelfunktion f auf einem kompakten Intervall [ a, b] ist beschränkt: Wähle eine TF \varphi \in T([a, b]) mit \| f − \varphi \| \le 1. Jede TF ist beschränkt, also \|\varphi \| < \infty . Nach der Dreiecksungleichung für die Supremumsnorm folgt \| f \| = \| f −…
```
- **English explanation:** This definition gives precise language for the topic of regulated functions and the extension of the integral by uniform approximation.
- **Intuition:** This definition gives precise language for the topic of regulated functions and the extension of the integral by uniform approximation.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.3.5 — unnamed definition in 6.3

- **Original term:** not explicitly named in script
- **Source:** PDF p101; section 6.3. Das Integral von Regelfunktionen
- **Formal definition / script statement:**
```latex
Sei f \in R([a, b]), und sei ( \varphi n)n eine approximierende Folge von TF . Wir definieren das Integral von f über [ a, b] durch ∫ b a f (x) dx := ∫ b a f dx := limn→\infty ∫ b a \varphi n dx . Nach Lemma 6.3.4 ist das Integral von f wohldefiniert. Weil dieses Integral für Regelfunktionen de finiert ist, nennen wir es auch Regelintegral. Das von Leibniz eingeführte Integralzeichen ∫ ist ein stilisiertes S und soll daran erinnern, dass das Integral (d.h. „das Ganze“) der Grenzwert einer Summe ist. Auf einem N otizzettel vom 29. Oktober 1675 schreibt Leib- niz: Utile erit scribi ∫ pro omn. ut ∫ l pro omn. l, id est summa ipsorum l (es wird nützlich sein, ∫ statt alle zu schreiben, wie ∫ l anstatt alle l, das ist die Summe der Werte l).
```
- **English explanation:** This definition gives precise language for the topic of regulated functions and the extension of the integral by uniform approximation.
- **Intuition:** This definition gives precise language for the topic of regulated functions and the extension of the integral by uniform approximation.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.4.1 — Stammfunktion von f

- **Original term:** not explicitly named in script
- **Source:** PDF p103; section 6.4. Der Hauptsatz der Differential- und Integralrechnung
- **Formal definition / script statement:**
```latex
Sei I \subset R ein Intervall und f : I → C. Eine Funktion F : I → C heißt Stammfunktion von f , falls F an jeder Stelle x \in I differenzierbar ist mit F′(x) = f (x). Wir möchten zunächst die folgende Frage beantworten: Wie un terscheiden sich zwei Stammfunktionen? Es gilt F′ 1 = F′ 2 auf I, und nach dem Eindeutigkeitssatz der Differentialrechnun g 5.4.1 existiert C \in C mit F1 = F2 + C.
```
- **English explanation:** This definition gives precise language for the topic of fundamental theorem of calculus and integration rules.
- **Intuition:** This definition gives precise language for the topic of fundamental theorem of calculus and integration rules.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.4.3 — unnamed definition in 6.4

- **Original term:** not explicitly named in script
- **Source:** PDF p103; section 6.4. Der Hauptsatz der Differential- und Integralrechnung
- **Formal definition / script statement:**
```latex
Sei I \subset R ein Intervall und f : I → C eine stetige Funktion. Das unbestimmte Inte- gral ∫ f (x) dx von f bezeichnet entweder die Menge aller Stammfunktionen oder ( repräsentativ) eine bestimmte davon. Sei F0 eine feste Stammfunktion; dann gilt ∫ f (x) dx = { F0 + C : C \in C } = F0 + C . Wir lassen üblicherweise die Mengenklammern fort und schre iben ∫ f (x) dx = F0 + C. ANALYSIS I-III, 2011/2013 102 Funktion Stammfunktion f : R+ \to C, f (x) = xα , ∫ xα dx = xα+ 1 α + 1 + C α \in C \setminus {− 1} f : I \subset R \setminus {0} \to R , f (x) = 1 x ∫ 1 x dx = log | x| + C f : R \to C , f (x) = ecx ∫ ecx dx = 1 c ecx + C c \in C \setminus {0} f : R \to R , f (x) = sin x ∫ sin x dx = − cos x + C f : R \to R, f (x) = cos x ∫ cos x dx = sin x + C f : (− 1,1) \to R , f (x) = 1\sqrt 1 − x2 ∫ 1\sqrt 1 − x2 dx = arcsin x + C f : R \to R , f (x) = 1 1 + x2 ∫ 1 1 + x2 dx = arctan x + C In der Definition des unbestimmtes Integrals ∫ f (x) dx = F0 + C, kann die Konstante C in verschieden Formen geschrieben werden. Wesentlich ist, dass C die ganze Menge C läuft. Die Konstante C kann log C, C \in R+ , oder αC, mit α ̸= 0 fest C \in C, oder C1 + C2, wobei C1, C2 \in C. Wegen der Definition…
```
- **English explanation:** This definition gives precise language for the topic of fundamental theorem of calculus and integration rules.
- **Intuition:** This definition gives precise language for the topic of fundamental theorem of calculus and integration rules.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.6.1 — 0-mal differenzierbar

- **Original term:** not explicitly named in script
- **Source:** PDF p107; section 6.6. Höhere Ableitungen. Die Taylorformel
- **Formal definition / script statement:**
```latex
Sei I ein Intervall, x0 \in I und f : I → C. Sei n \in N0. (i) Wir definieren den Begriff der n-maligen Differenzierbarkeit und die n-te Ableitung f (n)(x0) = dn f d xn (x0) rekursiv , und zwar wie folgt: (0) Jede beliebige Funktion f heißt 0-mal differenzierbar . Die 0-te Ableitung wird durch f (0) := f definiert. (1) Für n = 1 sagen wir , dass f in x0 \in I 1-mal differenzierbar ist, falls f in x0 differenzierbar ist. In diesem Fall ist die erste Ableitung von f in x0 als f (1)(x0) := f ′(x0) definiert. (2) Sei n \in N, n \ge 2; wir nehmen an, dass der Begriff der ( n − 1)-maligen Differenzierbarkeit und die (n − 1)-te Ableitung schon definiert sind. Die Funktion f heißt n-mal differenzierbar in x0, falls es \varepsilon > 0 gibt, so dass f in jedem Punkt von ( x0 − \varepsilon, x0 + \varepsilon) \cap I (n − 1)-differenzierbar ist und die Abbildung f (n− 1) : (x0 − \varepsilon, x0 + \varepsilon) \cap I \to C, x \mapstof (n− 1)(x) in x0 differenzierbar ist. Die n-te Ableitung von f in x0 ist dann durch f (n)(x0) := ( f (n− 1))′(x0) definiert. Klassische Notationen: f (1) = f ′, f (2) = ( f ′)′= : f ′′, f (3) = ( f ′′)′= : f ′′′. (ii) Wenn f n -mal differenzierbar in allen x \in I…
```
- **English explanation:** This definition gives precise language for the topic of higher derivatives and taylor formula.
- **Intuition:** This definition gives precise language for the topic of higher derivatives and taylor formula.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.6.3 — 0-tes Taylorpolynom

- **Original term:** not explicitly named in script
- **Source:** PDF p108; section 6.6. Höhere Ableitungen. Die Taylorformel
- **Formal definition / script statement:**
```latex
Sei n \in N, und sei f : I \to C n-mal differenzierbar . Zu x0 \in I assoziieren wir das n-te Taylorpolynom zu f mit Entwicklungspunkt x0: Tx0,n(x) = f (x0) + 1 1! f ′(x0)(x − x0) + . . .+ 1 n! f (n)(x0)(x − x0)n = n\sum k= 0 f (k)(x0) k! (x − x0)k . Das konstante Polynom Tx0,0(x) = f (x0) heißt 0-tes Taylorpolynom. Um festzustellen, wie gut das Taylorpolynom die Funktion in der Nähe des Punktes x0 approximiert, müssen wir den Fehler oder das n-te Restglied Rx0,n(x) := f (x) − Tx0,n(x) abschätzen. Die Taylorformel ist nichts anderes als die tri viale Gleichheit f (x) = Tx0,n(x)+ Rx0,n(x) zusam- men mit einer nützlichen Formel oder Abschätzung für das Res tglied Rx0,n(x).
```
- **English explanation:** This definition gives precise language for the topic of higher derivatives and taylor formula.
- **Intuition:** This definition gives precise language for the topic of higher derivatives and taylor formula.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.7.1 — uneigentliches Integral

- **Original term:** not explicitly named in script
- **Source:** PDF p109; section 6.7. Uneigentliche Integrale
- **Formal definition / script statement:**
```latex
Sei −\infty \le a < b \le \infty . (i) Ist a > −\infty und f : [a, b) \to C Regelfunktion, so setzen wir ∫ b a f (x) dx := lim βր b ∫ β a f (x) dx , falls dieser Grenzwert existiert. In diesem Fall sagen wir , dass ∫ b a f (x) dx konvergiert; ein Integral dieser Form heißt uneigentliches Integral. (ii) Analog für b < \infty , f : (a, b] \to C Regelfunktion: ∫ b a f (x) dx := lim αց a ∫ b α f (x) dx , falls dieser Grenzwert existiert. (iii) Ist f : (a, b) \to C Regelfunktion, so wählen wir c \in (a, b) und setzen ∫ b a f (x) dx := lim αց a ∫ c α f (x) dx + lim βր b ∫ β c f (x) dx , falls diese beiden Grenzwerte existieren. (iv) Konvergiert ∫ b a | f (x)| dx, so heißt ∫ b a f (x) dx absolut konvergent. Beispiele: (1) ∫ \infty 0 e− x dx = 1, denn ∫ β 0 e− x dx = − e− x⏐ ⏐β 0 = 1 − e− β → 1 für β → \infty . (2) ∫ \infty 0 sin x dx existiert nicht, denn ∫ β 0 sin x dx = − cos x ⏐ ⏐β 0 = 1 − cos β hat keinen Grenzwert für β → \infty . ANALYSIS I-III, 2011/2013 108 (3) ∫ \infty 1 1 xs dx konvergiert genau dann, wenn Re s > 1. In der Tat: ∫ \infty 1 1 xs dx =        − 1 s − 1 · 1 xs − 1 ⏐ ⏐β 1 = 1 s − 1 − β1− s s − 1 , s ̸= 1 , log x ⏐ ⏐β 1 = log β , s = 1 . β1− s = β1− Re s ·ei(lo…
```
- **English explanation:** This definition gives precise language for the topic of improper integrals and convergence criteria.
- **Intuition:** This definition gives precise language for the topic of improper integrals and convergence criteria.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.7 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 6.9.1 — \sumn k= 1 f

- **Original term:** not explicitly named in script
- **Source:** PDF p114; section 6.9. Notizen: Der Riemannsche Integralbegriff
- **Formal definition / script statement:**
```latex
Sei Z = {a = x0 < x1 < . . .< xn− 1 < xn = b} eine Zerlegung von [ a, b]. Sei \xik \in [xk− 1, xk] für k = 1, . . . ,n. (i) Für f : [a, b] \to C heißt \sumn k= 1 f (\xik)(xk − xk− 1) die Riemannsche Summe zu f bezüglich der Zer- legung Z und der Stützstellen \xi1, . . . ,\xik. (ii) Die Feinheit von Z ist definiert als max {| xk − xk− 1| : k = 1, . . . ,n}. (iii) Eine Funktion f : [ a, b] \to C heißt Riemann-integrierbar, wenn es eine Zahl I \in C mit der folgenden Eigenschaft gibt: Zu jedem \varepsilon > 0 gibt es δ > 0 so, dass für jede Zerlegung Z = {x0, . . . ,xn} ANALYSIS I-III, 2011/2013 113 mit Feinheit < δ und für jede Wahl von Stützstellen \xik \in [xk− 1, xk] ( k = 1, . . . ,n) gilt: ⏐ ⏐ ⏐ n\sum k= 1 f (\xik)(xk − xk− 1) − I ⏐ ⏐ ⏐ < \varepsilon. In diesem Fall heißt I := R- ∫ b a f (x) dx das Riemann-Integral von f .
```
- **English explanation:** This definition gives precise language for the topic of notes on the riemann integral.
- **Intuition:** This definition gives precise language for the topic of notes on the riemann integral.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.9 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 6.9.4 — unnamed definition in 6.9

- **Original term:** not explicitly named in script
- **Source:** PDF p115; section 6.9. Notizen: Der Riemannsche Integralbegriff
- **Formal definition / script statement:**
```latex
Sei f \in R([a, b]) und p ≥ 1. Die p-Norm von f ist definiert als \| f \|p := (∫ b a | f | p dx )1/p .
```
- **English explanation:** This definition gives precise language for the topic of notes on the riemann integral.
- **Intuition:** This definition gives precise language for the topic of notes on the riemann integral.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Continuity, differentiability, regulated functions, and estimates. Later entries in and after 6.9 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.1.1 — konvex

- **Original term:** not explicitly named in script
- **Source:** PDF p116; section 7.1. Konvexität und wichtige Ungleichungen
- **Formal definition / script statement:**
```latex
Eine Funktion f : I \to R heißt konvex, wenn für alle Tripel x0, x, x1 aus I mit x0 < x < x1 gilt: (7.1) f (x) \le x1 − x x1 − x0 f (x0) + x − x0 x1 − x0 f (x1) . f heißt streng konvex, falls für alle solchen Tripel die Ungleichung (7.1) streng ist. ANALYSIS I-III, 2011/2013 115 f heißt konkav, wenn − f konvex ist (d.h. (7.1) gilt mit \ge). f heißt streng konkav , wenn − f streng konvex ist (d.h. (7.1) gilt mit >).
```
- **English explanation:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Intuition:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.1.6 — unnamed definition in 7.1

- **Original term:** not explicitly named in script
- **Source:** PDF p117; section 7.1. Konvexität und wichtige Ungleichungen
- **Formal definition / script statement:**
```latex
Sei f : I \to R, und sei x0 \in I ein innerer Punkt. Die Funktion f hat in x0 einen Wende- punkt, wenn f stetig in x0 ist und ( α, β) \subset I existiert, so dass f konvex auf ( α, x0) und konkav auf ( x0, β) ist oder umgekehrt.
```
- **English explanation:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Intuition:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.1.12 — \|z\|p

- **Original term:** not explicitly named in script
- **Source:** PDF p118; section 7.1. Konvexität und wichtige Ungleichungen
- **Formal definition / script statement:**
```latex
Sei z = (z1, . . . ,zn) \in Cn, p \ge 1. Dann heißt \|z\|p := (| z1| p + . . .+ | zn| p)1/p die p-Norm von z. Für p = 1 also: \|z\|1 = \sumn j= 1 | z j| ; für p = 2: \|z\|2 = (\sumn j= 1 | z j| 2)1/2. Letzteres ist die eukli- dische Norm von z.
```
- **English explanation:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Intuition:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.1.13 — Norm

- **Original term:** not explicitly named in script
- **Source:** PDF p118; section 7.1. Konvexität und wichtige Ungleichungen
- **Formal definition / script statement:**
```latex
Sei V ein K-VR ( K = R oder C). Eine Abbildung V \to R, v \mapsto \|v\| heißt Norm, falls gilt: (N1) \|v\| \ge 0 für alle v \in V , und aus \|v\| = 0 folgt v = 0, (N2) \|\lambdav\| = | \lambda|\| v\| für alle \lambda \in K, v \in V , (N3) \|v + w\| \le \|v\| + \| w\| für alle v, w \in V . (Dreiecksungleichung) Unser Ziel ist es nun, zu zeigen, dass \|·\|p eine Norm ist. Dazu brauchen wir die Höldersche Ungleichung .
```
- **English explanation:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Intuition:** This definition gives precise language for the topic of convexity, jensen-type ideas, young, holder, minkowski, and norm inequalities.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.2.1 — Metrik

- **Original term:** Metrik
- **Source:** PDF p118; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
A metric $d:X\times X\to\mathbb R$ is positive definite, symmetric, and satisfies the triangle inequality.
```
- **English explanation:** A metric abstracts distance.
- **Intuition:** A metric abstracts distance.
- **Why it matters:** Foundation for convergence, continuity, compactness, and topology in general spaces.
- **Used later:** Set language and inequalities. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.2.3 — Skalarprodukt

- **Original term:** not explicitly named in script
- **Source:** PDF p120; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
Sei V ein K-Vektorraum ( K = R oder C). Eine Abbildung V × V \to K, ( v, w) \mapsto 〈v, w〉 heißt Skalarprodukt, falls gilt: (i) Die Abbildung 〈·, w〉: V → K ist K-linear für alle w \in V , (ii) 〈v, w〉 = 〈w, v〉 für alle v, w \in V , (iii) 〈v, v〉 >0 für alle v \in V \ {0}. 7.2.4. Beispiele. Beispiele von Skalarprodukträumen: • (Rn,〈·,·〉) mit 〈x, y〉 = \sumxi yi , (Cn,〈·,·〉) mit 〈x, y〉 = \sumxi yi , • (l2,〈·,·〉) mit 〈(xn)n,(yn)n〉 = \sum\infty n= 0 xn yn , • (C0[a, b],〈·,·〉) mit 〈f , g〉 = ∫ b a f (x)g(x) dx .
```
- **English explanation:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Intuition:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 7.2.6 — konvergent

- **Original term:** not explicitly named in script
- **Source:** PDF p121; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
Sei ( X , d) ein metrischer Raum; eine Folge ( xn)n\inN in X heißt konvergent, falls es x \in X gibt so, dass zu jedem \varepsilon > 0 ein n0 = n0(\varepsilon) existiert mit d(xn, x) < \varepsilon für alle n \ge n0(\varepsilon). Dann heißt x Grenzwert der Folge, limn→\infty xn = x. Eine Folge ( xn) heißt Cauchy-Folge, falls gilt: \forall \varepsilon > 0 \existsn0 = n0(\varepsilon) so, dass d(xn, xm) < \varepsilon für alle m, n > n0(\varepsilon). Die Definition ist wortwörtlich die gleiche wie die Konverge nz von reellen Folgen, der einzige Unterschied ist, dass wir den Absolutbetrag | xn − x| durch den Abstand d(xn, x) ersetzt haben. Daher konvergiert ( xn)n in (R, d2) oder ( C, d2) genau dann, wenn ( xn)n im Sinne der Definition 2.1.1 konvergiert. Nachdem der Absta nd die gleichen Eigenschaften wie der Absolutbetrag erfüllt, erhalten wir die gleichen Aussagen. Beispielsweise beweist man wortwörtlich wie im in Analysis I, dass: (i) Der Grenzwert ist eindeutig bestimmt. (ii) Jede konvergente Folge ist eine Cauchy-Folge.
```
- **English explanation:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Intuition:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.2.9 — Vollständigkeit in metrischen Räumen

- **Original term:** Vollständigkeit in metrischen Räumen
- **Source:** PDF p121; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
A metric space is complete if every Cauchy sequence converges in the space.
```
- **English explanation:** The space has no missing Cauchy limits.
- **Intuition:** The space has no missing Cauchy limits.
- **Why it matters:** Needed for Banach fixed point and many analytic existence theorems.
- **Used later:** Metric convergence and Cauchy sequences. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 7.2.13 — beschränkt

- **Original term:** not explicitly named in script
- **Source:** PDF p122; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
Eine Menge A \subset (X , d) heißt beschränkt, wenn es x0 \in A und M = M(x0) > 0 gibt so, dass d(x, x0) \le M für alle x \in A. Bemerkung. (1) Ist ( V ,\| · \|) ein NVR, so ist A \subset V beschränkt (bzgl. der Norm-Metrik) genau dann, wenn es M > 0 gibt so, dass \|x\| \le M für alle x \in A. (2) A \subset (R, d2) ist beschränkt genau dann, wenn A im üblichen Sinne beschränkt ist. (3) Sei pr i : Rn → R, pr i(x) = xi die Projektion auf die i-te Achse. A \subset (Rn, d2) ist beschränkt genau dann, wenn für jedes i = 1, . . . ,n die Menge pr i(A) beschränkt in R ist.
```
- **English explanation:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Intuition:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.2.15 — unnamed definition in 7.2

- **Original term:** not explicitly named in script
- **Source:** PDF p123; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
Zwei Normen \| · \|, \| · \|∗ auf einem Vektorraum V heißen äquivalent , geschrieben \| · \| ∼ \| · \|∗ , wenn es zwei Konstanten c1, c2 > 0 gibt mit c1\|x\| \le \|x\|∗ \le c2\|x\| für alle x \in V . Dies ist eine Äquivalenzrelation. Ist \| · \| ∼ \| · \|∗ , so gilt: ( xn)n ist konvergent gegen x (bzw . Cauchy-Folge) in (V ,\| · \|) genau dann, wenn (xn)n konvergent gegen x (bzw . Cauchy-Folge) in (V ,\| · \|∗ ) ist.
```
- **English explanation:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Intuition:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.2.17 — s = limn→\infty sn die Summe der Reihe

- **Original term:** not explicitly named in script
- **Source:** PDF p123; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
Sei ( V ,\| · \|) ein normierter Vektorraum. Ein Paar ( xn)n\ge0, ( sn)n\ge0 wird eine Reihe genannt, wenn sn = x0 + . . .+ xn. Die Reihe wird durch \sum n\ge0 xn bezeichnet. Wir sagen, dass die Reihe\sum n\ge0 xn konvergiert, wenn ( sn)n\ge0 konvergiert. Dann heißt s = limn→\infty sn die Summe der Reihe. Wir schreiben s = \sum\infty n= 0 xn. Eine Reihe \sum n\ge0 xn heißt absolut konvergent, wenn \sum n\ge0 \|xn\| in R konvergiert.
```
- **English explanation:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Intuition:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.2.19 — normierte K-Algebra

- **Original term:** not explicitly named in script
- **Source:** PDF p123; section 7.2. Metrische und normierte Räume
- **Formal definition / script statement:**
```latex
Ein normierter K-Vektorraum (V ,\| · \|) heißt normierte K-Algebra, wenn es eine as- soziative Verknüpfung V × V \to V , ( x, y) \mapstox y gibt so, dass \|x y\| \le \|x\| · \|y\| für alle x, y \in V . Ist ( V ,\| · \|) zugleich ein Banachraum, so heißt ( V ,\| · \|) eine Banachalgebra. Beispiele: V = Mn× n(K) mit der Multiplikation der Matrizen und Norm \|A\|2 = (\sumn i, j= 1 | ai j| 2)1/2 i st eine Bana- chalgebra. Auch ( B(D),\| · \|D ) und ( C0([a, b]),\| · \|[a,b]) sind Banachalgebren. ANALYSIS I-III, 2011/2013 122
```
- **English explanation:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Intuition:** This definition gives precise language for the topic of metric and normed spaces, convergence, cauchy sequences, completeness, and equivalent norms.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.1 — Offene Menge

- **Original term:** Offene Menge
- **Source:** PDF p124; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
A set is open if every point has an epsilon-ball contained in the set.
```
- **English explanation:** Every point has local room to move without leaving the set.
- **Intuition:** Every point has local room to move without leaving the set.
- **Why it matters:** Core topological language for continuity and differentiability domains.
- **Used later:** Metric balls. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.2 — offen

- **Original term:** not explicitly named in script
- **Source:** PDF p125; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
Sei ( X , d) ein metrischer Raum. Eine Teilmenge U \subset X heißt offen (bezüglich d) : \Longleftrightarrow für jedes a \in U gibt es r > 0 mit Br(a) \subset U. Eine Teilmenge F \subset X heißt abgeschlossen :\Longleftrightarrow X \setminus F ist offen. M a r offen b r nicht offen In der rechten Skizze ist eine offene Menge dargestellt. In d er rechten Skizze liegt der Punkt b \in M auf dem “Rand” von M. Jede Kugel um b enthält Punkte ausserhalb von M. Daher ist M nicht offen. Beispiele: (1) Offene Intervalle in ( a, b) \subset R, mit −\infty ≤ a < b ≤ \infty , sind offen in ( R, d2).
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.6 — topologischer Raum

- **Original term:** not explicitly named in script
- **Source:** PDF p128; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
Sei X eine Menge. Eine Topologie auf X ist eine Teilmenge O \subset P(X ) von Teilmengen von X mit den Eigenschaften: (1) X ,\emptyset \inO. (2) Die Vereinigung beliebig vieler Mengen aus O gehört zu O. (3) Der Durchschnitt endlich vieler offener Mengen aus O gehört zu O. Das Paar ( X ,O) heißt topologischer Raum . Eine Teilmenge U \subset X heißt offen, falls U \in O. Eine Teil- menge F \subset X heißt abgeschlossen, falls X \setminus F offen ist. 7.3.7. Beispiele. (1) Ist ( X , d) ein metrischer Raum, so ist O := O(d) := {U \subset X : U offen bezüglich d} (siehe Def. 7.3.2) eine Topologie auf X , genannt die induzierte Topologie von d. Dies folgt aus Satz 7.3.3. (2) Ein topologischer Raum ( X ,O) heißt metrisierbar, falls es eine Metrik gibt mit O(d) = O. Nicht alle topo- logischen Räume sind metrisierbar . Sei X eine Menge. Die Familie O = {\emptyset, X } bilden eine Topologie, genannt grobe Topologie. Die einzigen offenen Teilmengen sind \emptysetund X , und die sind auch die einzigen abgeschlos- senen Teilmengen. Nehmen wir an, X hat mindestens zwei Punkte. Dann is ( X ,O) nicht metrisierbar . Wäre (X ,O) metrisierbar , so wäre {a} abgeschlossen für a \in X , also {a} = \emp…
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.8 — Umgebung von a

- **Original term:** not explicitly named in script
- **Source:** PDF p128; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
Sei ( X ,O) ein metrischer Raum, a \in X . Eine Teilmenge U \subset X heißt Umgebung von a, wenn es eine offene Menge V gibt mit a \in V \subset U. Die Menge aller Umgebungen von a wird mit Ua bezeichnet. Es gilt: U \in Ua \Longleftrightarrow \exists \varepsilon > 0 : B\varepsilon(a) \subset U. Dieselbe Definition kann man für allgemeine topologische Rä ume geben.
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.10 — unnamed definition in 7.3

- **Original term:** not explicitly named in script
- **Source:** PDF p129; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
Sei (X ,O) ein metrischer (oder allgemeiner topologischer) Raum und A \subset X . Ein Punkt x \in X heißt: (i) innerer Punkt von A, wenn A eine Umgebung von x ist. (ii) Berührpunkt von A, wenn jede Umgebung von x (mindestens) einen Punkt aus A enthält. (iii) Randpunkt von A, wenn x Berührpunkt von A und X \setminus A ist. (iv) Häufungspunkt von A, wenn jede Umgebung von x unendlich viele Punkte aus A enthält. (v) isolierter Punkt von A, wenn es eine Umgebung U von x gibt mit U \cap A = {x}. (vi) äußerer Punkt von A, wenn es eine Umgebung U von x gibt mit U \cap A = \emptyset.
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.12 — unnamed definition in 7.3

- **Original term:** not explicitly named in script
- **Source:** PDF p129; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
Sei ( X ,O) ein topologischer Raum, A \subset X . Wir führen ein: (i) ̊A, die Menge aller inneren Punkte von A, genannt das Innere von A. (ii) A, die Menge aller Berührpunkte von A, genannt der Abschluss von A. (iii) ∂A, die Menge aller Randpunkte, genannt der Rand von A. (iv) A′, die Menge der Häufungspunkte von A. Beispiele: (1) Sei A = (a, b) \subset R mit a, b \in R, a < b. a b (a, b) Die Menge A ist offen, also ̊A = A = (a, b). Alle Punkte aus ( a, b) sind Berührpunkte. Zusätzlich sind auch a, b Berührpunkte: Für alle \varepsilon > 0 gilt A \cap (a − \varepsilon, a + \varepsilon) = (a,min(\varepsilon, b − a)) und A \cap (b − \varepsilon, b + \varepsilon) = (min(\varepsilon, b − a), b). Somit ist A = [a, b]. Die Punkte a, b sind auch Randpunkte: Für alle \varepsilon > 0 gilt (R\ A)\cap (a− \varepsilon, a+ \varepsilon) = (a− \varepsilon, a] und (R\ A)\cap (b− \varepsilon, b+ \varepsilon) = [b, b + \varepsilon). Somit ist ∂A = {a, b}. (2) Sei A = [0,1) \cup {2} \subset (R, d2). 0 1 2 [0,1) {2} Die Menge A ist weder offen noch abgeschlossen. Das Innere besteht aus a llen Punkten des offenen Intervalls: ̊A = (0,1). Alle Punkte aus [0 ,1) sind Berührpunkte von A. Zusätzlich ist auc…
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.14 — Hausdorffraum

- **Original term:** not explicitly named in script
- **Source:** PDF p131; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
Ein topologischer Raum ( X ,O) heißt Hausdorffraum, wenn es zu jedem Paar x, y \in X mit x ̸= y Umgebungen U von x und V von y gibt mit U \cap V = \emptyset. Sei ( X , d) ein metrischer Raum. Dann ist ( X ,O(d)) ein Hausdorffraum: Für x ̸= y gilt B ( x, r 2 ) \cap B ( y, r 2 ) = \emptyset, wobei r = d(x, y) > 0 . In einem Hausdorffraum sind die einpunktigen Mengen {p} mit p \in X abgeschlossen: Zu jedem x \in X \setminus {p} wähle eine offene Umgebung Uq von q mit Uq \subset X \setminus{p}. Dann gilt X \setminus{p} = \bigcup q\in X \setminus{p} Uq und X \setminus{p} ist offen als Vereinigung von offenen Mengen.
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.15 — dicht in X

- **Original term:** not explicitly named in script
- **Source:** PDF p131; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
Sei (X ,O) ein topologischer Raum. Eine Teilmenge A \subset X heißt dicht in X falls A = X . Zum Beispiel, eine Teilmenge A \subset R ist dicht in R, genau dann, wenn für alle Intervalle ( a, b) in R mit a < b gilt A \cap (a, b) ̸= \emptyset. Daher sind Q und R \ Q dicht in R. Siehe dazu Satz 1.6.5; wir haben also in Definition 7.3.15 ei ne Verallgemeinerung der Dichtheit in R. Ein Beispiel in Rn: die Menge Qn liegt dicht in Rn.
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.3.16 — unnamed definition in 7.3

- **Original term:** not explicitly named in script
- **Source:** PDF p131; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Formal definition / script statement:**
```latex
(i) Sei ( X ,O) ein topologischer Raum, A \subset X . Dann ist OA := {U \cap A : U \in O} eine Topologie auf A, genannt induzierte Topologie oder Teilraumtopologie. (ii) Sind ( X1,O1), . . . ,(X n,On) topologische Räume, so ist O := {U \subset X1 × . . .× X n : \forall x \in U \exists Ui \in Oi, i = 1, . . . ,n : x \in U1 × . . .× Un \subset U} eine Topologie auf X1 × . . .× X n, genannt Produkttopologie von O1, . . . ,On.
```
- **English explanation:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Intuition:** This definition gives precise language for the topic of open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.3 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.4.1 — Stetige Abbildungen zwischen metrischen Räumen

- **Original term:** Stetige Abbildungen zwischen metrischen Räumen
- **Source:** PDF p132; section 7.4. Stetige Abbildungen
- **Formal definition / script statement:**
```latex
$f:X\to Y$ is continuous at $a$ if $\forall\varepsilon>0\ \exists\delta>0: d_X(x,a)<\delta\Rightarrow d_Y(f(x),f(a))<\varepsilon$.
```
- **English explanation:** Small input-distance implies small output-distance.
- **Intuition:** Small input-distance implies small output-distance.
- **Why it matters:** Generalizes continuity beyond real functions.
- **Used later:** Metrics, balls, neighborhoods. Later entries in and after 7.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.4.11 — die Standardparametrisierung der Kreislinie S1

- **Original term:** not explicitly named in script
- **Source:** PDF p138; section 7.4. Stetige Abbildungen
- **Formal definition / script statement:**
```latex
(a) Die Funktion p : R \to S1, p(\varphi ) = ei\varphi heißt die Standardparametrisierung der Kreislinie S1. (b) Für z \in S1 heißt Arg( z) = {\varphi \in R : ei\varphi = z} = arg z + 2πZ die Menge der Argumente von z. Die Abbildung Arg : S1 \to R/2πZ ist mehrdeutig, d.h. sie assoziiert zu z \in S1 eine Menge von Werten in R. (c) Sei I \subset R ein halboffenes Intervall der Länge 2 π. Die Umkehrung ( p| I )− 1 : S1 \to I heißt ein Zweig der Argument-Abbildung. (d) Die Funktion arg = (p| (− π,π])− 1 heißt Hauptzweig von Arg. (e) Wir erweitern nun den Definitionsbereich von Arg: Setze Arg : C∗ \to R/2πZ , Arg(z) := Arg ( z | z| ) = {\varphi \in R : ei\varphi = z | z| } Für z \in C∗ heißt Arg( z) die Menge der Argumente von z. (f) Die Funktion (7.7) arg : C∗ \to (− π, π] , arg(z) := arg ( z | z| ) heißt Hauptzweig von Arg. (g) Für z \in C∗ in der Form z = re i\varphi = r(cos \varphi + i sin \varphi ) mit r = | z| und \varphi \in Arg(z) (Polarkoordinaten- darstellung von z (??)) heißen ( r, \varphi ) die Polarkoordinaten von z. Die Abbildung R+ × R \mapstoC∗ , (r, \varphi ) \mapstore i\varphi heißt Polarkoordinatenabbildung. Sei R− = {x \in R : x < 0} die negative reele Achse. Die Me…
```
- **English explanation:** This definition gives precise language for the topic of continuity between metric/topological spaces, sequential criteria, homeomorphisms, and uniform continuity.
- **Intuition:** This definition gives precise language for the topic of continuity between metric/topological spaces, sequential criteria, homeomorphisms, and uniform continuity.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.4.14 — unnamed definition in 7.4

- **Original term:** not explicitly named in script
- **Source:** PDF p139; section 7.4. Stetige Abbildungen
- **Formal definition / script statement:**
```latex
Seien X ,Y topologische Räume, A \subset X und a ein HP von A. Eine Funktion f : A \to Y hat in a den Grenzwert b \in Y , wenn es zu jeder Umgebung V von b eine Umgebung U von a gibt so, dass f (A \cap U \setminus {x0}) \subset V . Schreibweise: lim x→ a f (x) = b.
```
- **English explanation:** This definition gives precise language for the topic of continuity between metric/topological spaces, sequential criteria, homeomorphisms, and uniform continuity.
- **Intuition:** This definition gives precise language for the topic of continuity between metric/topological spaces, sequential criteria, homeomorphisms, and uniform continuity.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.5.1 — Kompaktheit

- **Original term:** Kompaktheit
- **Source:** PDF p140; section 7.5. Kompaktheit
- **Formal definition / script statement:**
```latex
In the script's metric/topological setting, compactness is tied to sequence compactness and finite subcover behavior as stated.
```
- **English explanation:** Compact sets are small enough for infinite processes to have finite/convergent structure.
- **Intuition:** Compact sets are small enough for infinite processes to have finite/convergent structure.
- **Why it matters:** Explains max/min theorems, uniform continuity, and existence results.
- **Used later:** Topology, sequences, closed/bounded behavior. Later entries in and after 7.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.6.1 — zusammenhängend

- **Original term:** not explicitly named in script
- **Source:** PDF p142; section 7.6. Zusammenhang
- **Formal definition / script statement:**
```latex
Sei X ein metrischer Raum. (i) X heißt zusammenhängend, wenn es keine Zerlegung von X in zwei nichtleere disjunkte offene Teilmengen U,V gibt. (ii) A \subset X heißt zusammenhängend, falls der metrische ( A, d| A ) zusammenhängend ist. X zusammenhängend \Longleftrightarrow für alle offenen Teilmengen U,V \subset X mit U \cap V = \emptysetund U \cup V = X gilt U = \emptysetoder V = \emptyset \Longleftrightarrow \emptysetund X sind die einzigen zugleich offen und abgeschlossen Teilmen gen von X . A \subset X zusammenhängend \Longleftrightarrow für alle offenen Teilmengen U,V \subset X mit A \subset U \cup V und A \cap U \cap V = \emptysetgilt A \cap U = \emptysetoder A \cap V = \emptyset. zusammenhängend nicht zusammenhängend ANALYSIS I-III, 2011/2013 141 zusammenhängend zusammenhängend nicht zusammenhängend wegzusammenhängend zusammenhängend R2 \ {0} ANALYSIS I-III, 2011/2013 142 zusammenhängend Beispiele: (i) Sei f : R \setminus {0} \to R, f (x) = 1 x . Graph( f ) ist nicht zusammenhängend. (ii) Q \subset R ist nicht zusammenhängend. Sogar: Für alle x, y \in Q mit x ̸= y gibt es z \notin Q zwischen x und y. Eine Teilmenge von R mit dieser Eigenschaft heißt Diskontinuum. Die Cantor…
```
- **English explanation:** This definition gives precise language for the topic of connectedness, path connectedness, components, and generalized intermediate value ideas.
- **Intuition:** This definition gives precise language for the topic of connectedness, path connectedness, components, and generalized intermediate value ideas.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.6.5 — wegzusammenhängend

- **Original term:** not explicitly named in script
- **Source:** PDF p145; section 7.6. Zusammenhang
- **Formal definition / script statement:**
```latex
Sei X ein metrischer Raum. (i) X heißt wegzusammenhängend, wenn es zu allen x, y \in X eine stetige Abbildung γ : [a, b] \to X mit γ(a) = x, γ(b) = y gibt (solch ein γ heißt stetige Kurve). (ii) A \subset X heißt wegzusammenhängend, wenn ( A, d| A ) wegzusammenhängend ist. X x y γ ANALYSIS I-III, 2011/2013 144
```
- **English explanation:** This definition gives precise language for the topic of connectedness, path connectedness, components, and generalized intermediate value ideas.
- **Intuition:** This definition gives precise language for the topic of connectedness, path connectedness, components, and generalized intermediate value ideas.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 7.6.13 — Zusammenhangskomponente, Wegekomponente

- **Original term:** Zusammenhangskomponente, Wegekomponente
- **Source:** PDF p147; section 7.6. Zusammenhang
- **Formal definition / script statement:**
```latex
Sei X ein topologischer Raum. Die Vereinigung aller zusammenhängenden Teilmengen A von X , die x \in X enthalten, heißt Zusammen- hangskomponente X (x) von x. Wir sprechen auch kurz von Komponenten. Die Vereinigung aller weg- zusammenhängenden Teilmengen A von X , die x \in X enthalten, heißt Wegekomponente von x. Ein Raum X heißt lokal (weg-) zusammenhängend, wenn zu jedem x \in X und jeder Umgebung U von x eine (weg-) zusammenhängendende Umgebung V \subset U existiert.
```
- **English explanation:** This definition gives precise language for the topic of connectedness, path connectedness, components, and generalized intermediate value ideas.
- **Intuition:** This definition gives precise language for the topic of connectedness, path connectedness, components, and generalized intermediate value ideas.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Sequences, convergence, inequalities, and set/topology language. Later entries in and after 7.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.1.1 — Differenzierbarkeit in normierten Räumen

- **Original term:** Differenzierbarkeit in normierten Räumen
- **Source:** PDF p151; section 8.1. Definition und einfache Regeln
- **Formal definition / script statement:**
```latex
$f$ is differentiable at $a$ if there is a linear map $T$ with $\|f(a+h)-f(a)-T(h)\|/\|h\|\to0$ as $h\to0$.
```
- **English explanation:** The derivative is the best linear approximation in all directions at once.
- **Intuition:** The derivative is the best linear approximation in all directions at once.
- **Why it matters:** Foundation of multivariable calculus.
- **Used later:** Normed spaces, one-variable differentiability. Later entries in and after 8.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.2.1 — ∂v f

- **Original term:** not explicitly named in script
- **Source:** PDF p154; section 8.2. Richtungsableitungen und partielle Ableitungen
- **Formal definition / script statement:**
```latex
Sei D \subset V offen, a \in D und f : D \to W. Sei v \in V . Existiert der Limes ∂v f (a) = lim t→ 0 f (a + tv) − f (a) t \in W, so heißt ∂v f (a) die Richtungsableitung von f in a in Richtung v \in V . Sei nun V = Rn und {e1, . . . ,en} die Standardbasis. f heißt partiell differenzierbar in a bzgl. der i-ten Koordinatenrichtung, falls die Richtungsableitung ∂f ∂xi (a) := ∂i f (a) := ∂e i f (a) , existiert und ∂i f (a) heißt die i-te partielle Ableitung von f in a. Die Funktion f heißt partiell differenzierbar, falls ∂i f (x) für jedes x \in D und jedes 1 \le i \le n existiert.
```
- **English explanation:** This definition gives precise language for the topic of directional derivatives, partial derivatives, jacobian, gradient, chain rule in coordinates, and differentiability criterion.
- **Intuition:** This definition gives precise language for the topic of directional derivatives, partial derivatives, jacobian, gradient, chain rule in coordinates, and differentiability criterion.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.2.5 — unnamed definition in 8.2

- **Original term:** not explicitly named in script
- **Source:** PDF p155; section 8.2. Richtungsableitungen und partielle Ableitungen
- **Formal definition / script statement:**
```latex
Seien V = Rn, W = Rm, D \subset Rn offen, a \in D und f : D \to Rm. Die Jacobi-Matrix Jf (a) \in Mm× n(R) von f in a ist die assoziierte Matrix zu d f (a) \in L(Rn,Rm) bzgl. der kanonischen Basen B, C von Rn, Rm, also: Jf (a) = MB C (d f (a)). Aus der linearen Algebra wissen wir , dass die Spalten der Mat rix MB C (d f (a)) die Vektoren d f (a) ·e i = ∂e i f (a) = ∂f ∂xi (a) sind. Also Jf (a) = ( ∂f ∂x1 (a), . . . ,∂f ∂xn (a) ) =        ∂f1 ∂x1 (a) . . . ∂f1 ∂xn (a) . . . . . . ∂f m ∂x1 (a) . . . ∂f m ∂xn (a)        und d f (a) ·v = Jf (a) ·v =        ∂f1 ∂x1 (a) . . . ∂f1 ∂xn (a) . . . . . . ∂f m ∂x1 (a) . . . ∂f m ∂xn (a)        ·     v1 . . . vn     . ANALYSIS I-III, 2011/2013 154 Merkregel zur Bildung der Jacobi-Matrix: Komponenten unte reinander , Ableitungen von links nach rechts. Beispiel: Für f : R+ × R \to R2, f (r, θ) = ( r cos θ r sin θ ) gilt Jf (r, θ) = ( cos θ − r sin θ sin θ r cos θ ) . Betrachten wir einige Spezialfälle: • Falls n = m = 1, so ist Jf (a) = f ′(a) \in M1× 1(R) = R die Ableitung einer reellen Funktion von einer reellen Variablen. • Falls n = 1, f =     f1 . . . f m     , so ist Jf (a) =     f ′ 1(a) . .…
```
- **English explanation:** This definition gives precise language for the topic of directional derivatives, partial derivatives, jacobian, gradient, chain rule in coordinates, and differentiability criterion.
- **Intuition:** This definition gives precise language for the topic of directional derivatives, partial derivatives, jacobian, gradient, chain rule in coordinates, and differentiability criterion.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 8.2.6 — grad f

- **Original term:** not explicitly named in script
- **Source:** PDF p156; section 8.2. Richtungsableitungen und partielle Ableitungen
- **Formal definition / script statement:**
```latex
Sei f : D → R differenzierbar in a \in D. Dann heißt grad f (a) :=        ∂f ∂x1 (a) . . . ∂f ∂xn (a)        = Jf (a)T \in Rn der Gradient von f in a. Für alle v \in Rn gilt nach Satz 8.2.4 (8.4) d f (a) ·v = (∂1 f (a), . . . ,∂n f (a)) ·     v1 . . . vn     = ⟨ grad f (a), v ⟩ . Der Gradient grad f (a) ist derjenige Vektor in Rn, der bzgl. des euklidischen Skalarprodukts 〈·,·〉dual zur Linearform d f (a) : Rn \to R ist. Da grad f (a) hierdurch eindeutig bestimmt ist, kann (8.4) gut als basis freie Definition des Gradienten dienen. Die Gradientenabbildung (auch Gradient genannt) D → Rn, x \mapstograd f (x) ist ein Speziallfall eines Vektor- feldes (im Sinne des Mathematikers), d.h. einer Abbildung F : D → Rn, oder Feldes (im Sinne des Physikers), d.h. jedem Punkt x \in D wird der Vektor grad f (x) angeheftet. Beispiel: Für f : Rn \to R, f (x) = \| x\|2 = 〈 x, x〉 = x2 1 + . . .+ x2 n ist ∂j f (x) = 2x j und grad f (x) = 2x.
```
- **English explanation:** This definition gives precise language for the topic of directional derivatives, partial derivatives, jacobian, gradient, chain rule in coordinates, and differentiability criterion.
- **Intuition:** This definition gives precise language for the topic of directional derivatives, partial derivatives, jacobian, gradient, chain rule in coordinates, and differentiability criterion.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 8.4.1 — unnamed definition in 8.4

- **Original term:** not explicitly named in script
- **Source:** PDF p158; section 8.4. Höhere Ableitungen und der Satz von Schwarz
- **Formal definition / script statement:**
```latex
Sei f : D \subset Rn \to Rm eine Abbildung, und seien i, j \in {1, . . . ,n}. Die partielle Ableitung ∂j f existiere auf ganz U. Falls die i-te partielle Ableitung zu ∂j f in a existiert, so heißt ∂i(∂j f )(a) eine partielle Ableitung 2. Ordnung in a. Schreibweisen: ∂2 f ∂xi∂x j (a) := ∂i j f (a) := ∂i(∂j f )(a) , ∂2 f ∂x2 i (a) := ∂2 i f (a) := ∂i(∂i f )(a) . Beispiel: Seien D := R+ × R \subset R2 und f : D \to R definiert durch f (x, y) := x y. Dann ∂f ∂x (x, y) = yx y− 1 , ∂2 f ∂y∂x (x, y) = x y− 1 + y log x − x y− 1 , ∂f ∂y (x, y) = log x ·x y , ∂2 f ∂x∂y (x, y) = x y− 1 + yx y− 1 log x , ∂2 f ∂x2 (x, y) = y(y − 1)x y− 2 , ∂f ∂y2 (x, y) = log x ·log x ·x y . ANALYSIS I-III, 2011/2013 157
```
- **English explanation:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Intuition:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.4.4 — unnamed definition in 8.4

- **Original term:** not explicitly named in script
- **Source:** PDF p159; section 8.4. Höhere Ableitungen und der Satz von Schwarz
- **Formal definition / script statement:**
```latex
Für i1, . . . ,i k \in {1, . . . ,n} definieren wir eine partielle Ableitung k-ter Ordnung in Richtungen xi1 , xi2 , . . . ,xik durch ∂i1···ik f = ∂i1 (· · ·(∂ik− 1 (∂ik f )) · · ·), falls f auf U in Richtung xik differen- zierbar ist, ∂ik f auf U in Richtung xik− 1 differenzierbar ist etc. Schreibweisen: ∂k f ∂xi1 . . .∂xik := ∂i1···ik f := ∂i1 (· · ·(∂ik− 1 (∂ik f )) · · ·) , ∂l f ∂xl i := ∂l i f := ∂i∂i . . .∂i   l− mal f , für l \in N0 (wobei ∂0 i f := f ), ∂k f ∂xl1 1 . . .∂xln n := ∂l1 1 · · ·∂ln n f , für l \in N0, l1 + . . .+ ln = k .
```
- **English explanation:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Intuition:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.4.5 — k-mal stetig differenzierbar

- **Original term:** not explicitly named in script
- **Source:** PDF p159; section 8.4. Höhere Ableitungen und der Satz von Schwarz
- **Formal definition / script statement:**
```latex
Sei D \subset Rn offen und k \in N. (i) Eine Abbildung f : D \to Rm heißt k-mal stetig differenzierbar , wenn alle partiellen Ableitun- gen bis zur Ordnung k von f existieren und stetig sind. Wir bezeichnen mit Ck(D,Rm) den Raum der k-mal stetig differenzierbaren Abbildungen von U nach Rm. (ii) Eine Abbildung f : D \to Rm heißt unendlich oft differenzierbar oder glatt, wenn für alle k \in N alle partiellen Ableitungen ∂i1···ik f existieren und stetig sind. Wir bezeichnen mit C\infty (D,Rm) der Raum der unendlich oft differenzierbaren Abbildungen von U nach Rm. Offensichtlich gilt C0(D,Rm) \supset C1(D,Rm) \supset C2(D,Rm) \supset . . .\supset Ck(D,Rm) \supset Ck+ 1(D,Rm) \supset . . . und C\infty (D,Rm) = \cap k\inNCk(D,Rm).
```
- **English explanation:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Intuition:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.4.7 — die Matrix H f

- **Original term:** not explicitly named in script
- **Source:** PDF p160; section 8.4. Höhere Ableitungen und der Satz von Schwarz
- **Formal definition / script statement:**
```latex
Sei f \in C2(D,R), D \subset Rn offen, a \in D. Dann heißt die Matrix H f (a) :=     ∂11 f (a) . . . ∂1n f (a) . . . . . . ∂n1 f (a) . . . ∂nn f (a)     Hesse-Matrix zu f in a . Die Bilinearform d2 f (a) : Rn × Rn \to R , (u, v) \mapsto∂u(∂v f )(a) . heißt Hesse-Form oder Differential zweiter Ordnung zu f in a . Wegen des Satzes von Schwarz ist H f (a) symmetrisch, d.h. ∂i j f (a) = ∂ji f (a). Daher ist die Hesse-Matrix die Jacobi-Matrix des Gradienten: H f (a) = Jgrad f (a). Die Hesse-Form ist wohldefiniert, da ∂v f = v1∂1 f + . . .+ vn∂n f differenzierbar ist; daher ist ∂u(∂v f )(a) linear in u und v. Es gilt d2 f (a)(u, v) = n\sum i, j= 1 ui v j d2 f (a)(e i, e j) = n\sum i, j= 1 ui v j∂i j f (a) = uT H f (a)v. Also hat die Bilinearform d2 f (a) bezüglich der Standardbasis {e1, . . . ,en} die Matrix H f (a). Insbesondere ist d2 f (a) symmetrisch. Wir werden sehen, dass die Hesse-Matrix bei d er Extremwertbestimmung eine wesentli- che Rolle spielt.
```
- **English explanation:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Intuition:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def 8.4.9 — Differential k-ter Ordnung zu f in a

- **Original term:** not explicitly named in script
- **Source:** PDF p160; section 8.4. Höhere Ableitungen und der Satz von Schwarz
- **Formal definition / script statement:**
```latex
Sei f \in Ck(D,Rm) und a \in D. Die multilineare Abbildung dk f (a) : Rn × . . .× Rn \to Rm , (v1, v2, . . . ,vk) \mapsto∂v1 v2...vk f (a) = n\sum i1,i2,...,ik = 1 v1i1 v2i2 . . .vki k ∂i1 i2...ik f (a) heißt Differential k-ter Ordnung zu f in a . Nach Bemerkung 8.4.6 ist dk f (a) symmetrisch. 8.5. Die Taylorformel. Sei D \subset Rn offen, f \in Ck(D,Rm), a \in D. Für 1 \le r \le k betrachte die multilineare Abbil- dung dr f (a). Für v1 = v2 = . . .= vr = v setzen wir dr f (a) ·v(r) := dr f (a)(v, v, . . . ,v) .
```
- **English explanation:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Intuition:** This definition gives precise language for the topic of higher partial derivatives, schwarz theorem, hessian, and higher differentials.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.4 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.5.1 — p-tes Taylorpolynom zu f in a \in D

- **Original term:** not explicitly named in script
- **Source:** PDF p160; section 8.5. Die Taylorformel
- **Formal definition / script statement:**
```latex
Sei f \in Cp+ 1(D,R) und a \in D. Das Polynom T p,a f (x) = f (a) + 1 1! d f (a)(x − a) + 1 2! d2 f (a)(x − a)(2) + . . .+ 1 p! d p f (a)(x − a)(p) heißt p-tes Taylorpolynom zu f in a \in D. Für α = (α 1, . . . ,α n) \in Nn 0 und v \in Rn schreibe | α| := α 1 + . . .+ α n, α! := α 1! · · ·α n!, vα = vα 1 1 · · ·vα n n , und setze: ∂μ i f := ∂μ ∂xμ i , ∂α f := ∂α 1 1 · · ·∂α n n f = ∂α 1 ∂xα 1 1 · · ·∂α n ∂xα n n f = ∂| α| f ∂xα 1 1 · · ·∂xα n n ·
```
- **English explanation:** This definition gives precise language for the topic of multivariable taylor formula.
- **Intuition:** This definition gives precise language for the topic of multivariable taylor formula.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.5 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.6.1 — unnamed definition in 8.6

- **Original term:** not explicitly named in script
- **Source:** PDF p161; section 8.6. Lokale Extrema
- **Formal definition / script statement:**
```latex
Sei X ein topologischer Raum (z.B. X \subset Rn mit der induzierten Topologie). (i) f : X \to R hat in a \in X ein Maximum (bzw .Minimum), wenn f (x) \le f (a) für alle x \in X (bzw . f (x) \ge f (a) für alle x \in X ). Man bezeichnet a auch als globales Maximum (bzw .globales Mini- mum ). (ii) f : X \to R hat in a ein lokales Maximum (bzw .lokales Minimum ), wenn es eine Umgebung U von a in X gibt mit f (x) \le f (a) (bzw . f (x) \ge f (a)) für alle x \in U. (iii) f : X \to R hat in a ein strenges Maximum (bzw .strenges Minimum ), wenn f (x) < f (a) (bzw . f (x) > f (a)) für alle x \in X \setminus {a}. (iv) f : X \to R hat in a ein strenges lokales Maximum (bzw .strenges lokales Minimum ), wenn es eine Umgebung U von a gibt mit f (x) < f (a) (bzw . f (x) > f (a)) für alle x \in U \setminus {a}. (v) f : X \to R hat in a ein lokales Extremum , wenn f in a ein lokales Maximum oder ein lokales Minimum hat.
```
- **English explanation:** This definition gives precise language for the topic of local extrema, critical points, and hessian tests.
- **Intuition:** This definition gives precise language for the topic of local extrema, critical points, and hessian tests.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.6.2 — kritisch oder stationär

- **Original term:** not explicitly named in script
- **Source:** PDF p161; section 8.6. Lokale Extrema
- **Formal definition / script statement:**
```latex
Seien D \subset (V ,\|·\|) offen und f : D \to R differenzierbar . Ein Punkt a \in D mit d f (a) = 0 \in L(V ,R) heißt kritisch oder stationär .
```
- **English explanation:** This definition gives precise language for the topic of local extrema, critical points, and hessian tests.
- **Intuition:** This definition gives precise language for the topic of local extrema, critical points, and hessian tests.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.6 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 8.9.1 — komplex differenzierbar in z0 \in D

- **Original term:** not explicitly named in script
- **Source:** PDF p164; section 8.9. Notizen: Komplexe Differenzierbarkeit
- **Formal definition / script statement:**
```latex
Sei D \subset C offen. Eine Funktion f : D \to C heißt komplex differenzierbar in z0 \in D, wenn (8.7) f ′(z0) := d f dz (z0) := limz→ z0 f (z) − f (z0) z − z0 in C existiert. Diese Zahl heißt dann die (komplexe) Ableitung von f in z0. Die Funktion f : D \to C heißt holomorph in D, falls f komplex differenzierbar in allen Punkten z \in D ist; f heißt holomorph in z0 \in D, wenn f holomorph in einer offenen Umgebung von z0 ist. Jedes Polynom P : C \to C, P(z) = an zn + . . .+ a0 ist komplex differenzierbar , und P′(z) = nan zn− 1 + . . .+ 2a2 z + a1. Diese Definition erhalten wir durch Übertragung der Definiti on der Differenzierbarkeit in einer reellen Verän- derlichen. Auf gleiche Weise wie in Satz 5.2.3 zeigt man:
```
- **English explanation:** This definition gives precise language for the topic of notes on complex differentiability and cauchy-riemann style equivalences.
- **Intuition:** This definition gives precise language for the topic of notes on complex differentiability and cauchy-riemann style equivalences.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Metric/normed spaces, one-variable differentiability, and linear algebra. Later entries in and after 8.9 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 9.1.1 — Kontraktion

- **Original term:** Kontraktion
- **Source:** PDF p166; section 9.1. Banachscher Fixpunktsatz
- **Formal definition / script statement:**
```latex
A map $f:X\to X$ is a contraction if $d(f(x),f(y))\le qd(x,y)$ for some $q\in[0,1)$.
```
- **English explanation:** The map strictly shrinks distances.
- **Intuition:** The map strictly shrinks distances.
- **Why it matters:** Hypothesis of Banach fixed point theorem.
- **Used later:** Metric spaces and Lipschitz estimates. Later entries in and after 9.1 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def 9.2.1 — Ck-Diffeomorphismus

- **Original term:** not explicitly named in script
- **Source:** PDF p166; section 9.2. Der Umkehrsatz
- **Formal definition / script statement:**
```latex
Seien D \subset Rn, G \subset Rm offen, und sei k \in N \cup {\infty }. f : D \to G heißt Ck-Diffeomorphismus, wenn f \in Ck(D,G), f bijektiv und f − 1 \in Ck(G, D) ist. f heißt lokaler Ck-Diffeomorphismus in a \in D, wenn offene Umgebungen U von a und V von f (a) existieren so, dass f : U \to V ein Ck-Diffeomorphismus ist. f heißt lokaler Ck-Diffeomorphismus, wenn f ein lokaler Ck-Diffeomorphismus in jedem x \in D ist. 9.2.2. Beispiele. (1) exp : R \to R+ ist ein C\infty -Diffeomorphismus mit der Inversen log : R+ \to R. (2) Polarkoordinaten in R2. Die (Einschränkung der) Polarkoordinatenabbildung P : R+ × (− π, π) \to R2 \ {(x, y) : x \le 0, y = 0} = : R2 − , P(r, θ) = (r cos θ, r sin θ) ANALYSIS I-III, 2011/2013 165 ist ein C\infty -Diffeomorphismus. Laut Satz 7.4.12 ist die Inverse von P gegeben durch P− 1 : R2 \to R+ × (− π, π) , (x, y) \mapsto (√ x2 + y2,arg(x, y) ) wobei (siehe (7.6) und (7.7)) arg : R2 \to (− π, π) , arg(x, y) =      arccos x \sqrt x2+ y2 , x \ge 0 , − arccos x\sqrt x2+ y2 , x < 0 . Die Funktion R2 \to R+ , ( x, y) \mapsto √ x2 + y2 ist glatt, als Zusammensetzung von R2 \to R+ , ( x, y) \mapstox2 + y2 und R+ → R+ , t \mapsto \sqrt t. Wir beweisen, das…
```
- **English explanation:** This definition gives precise language for the topic of diffeomorphisms and inverse function theorem.
- **Intuition:** This definition gives precise language for the topic of diffeomorphisms and inverse function theorem.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** Complete metric spaces, differential estimates, inverse/differential calculus. Later entries in and after 9.2 reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Def A.1.1 — unnamed definition in A.1. Aussagenlogik

- **Original term:** not explicitly named in script
- **Source:** PDF p177; section A.1. Aussagenlogik
- **Formal definition / script statement:**
```latex
Eine Aussage ist ein sprachlich und grammatisch richtiger Ausdruck, von dem ein- deutig feststeht, ob er wahr (richtig), bezeichnet w , oder f alsch, bezeichnet f, ist. Wahre Aussagen nennen wir Sätze. Wahr und falsch heißen auch Wahrheitswerte.
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.1. Aussagenlogik reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.1.3 — logische Verknüpfungen, Formel

- **Original term:** logische Verknüpfungen, Formel
- **Source:** PDF p177; section A.1. Aussagenlogik
- **Formal definition / script statement:**
```latex
Aus den Aussagenvariablen werden mit Hilfe von logischen Verknüpfungen kompliziertere Aussagen, genannt Formeln, aufgebaut. Die logischen Ver- knüpfungen sind: Verknüpfung symbolisch umgangssprachlich Verneinung ¬ non ; nicht Konjunktion ∧ und Disjunktion ∨ oder Implikation ⇒ wenn , dann Äquivalenz \Longleftrightarrow genau dann, wenn Im folgenden bezeichnen wir Aussagenvariablen mit A, B, . . .und definieren die folgenden Formeln: Formel symbolisch umgangssprachlich Verneinung ¬ A non ( A); nicht A Konjunktion A ∧ B A und B Disjunktion A ∨ B A oder B Implikation A ⇒ B aus A folgt B; wenn A, dann B Äquivalenz A \Longleftrightarrow B A äquivalent mit B; A genau dann, wenn B (i) Die Formel ¬ A bezeichnet die Negation (das Gegenteil) von A. Wenn A eine wahre Aussage ist, dann ist ¬ A eine falsche Aussage; ist A eine falsche Aussage, so ist ¬ A eine wahre Aussage. (ii) Die Formel A ∧ B bezeichnet die Konjunktion der beiden Aussagen A und B. Die Formel A ∧ B ist dann und nur dann wahr , wenn A und B beide wahr sind. ANALYSIS I-III, 2011/2013 176 (iii) Die Formel A∨ B bezeichnet die Disjunktion von A und B. Die Formel A∨ B ist dann und nur dann wahr , wenn mindestens eine der beiden Aus…
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.1. Aussagenlogik reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.1.7 — eine Belegung dieser Variablen

- **Original term:** not explicitly named in script
- **Source:** PDF p178; section A.1. Aussagenlogik
- **Formal definition / script statement:**
```latex
Die Zuordnung von Wahrheitswerten wahr oder falsch zu Aussa genvariablen A, B, . . . heißt eine Belegung dieser Variablen. Die Wahrheitswerttabelle einer Formel gibt für alle Belegungen der Eingänge A, B, . . .die Belegung des Ausgangs an. Eine Wahrheitswerttabelle fü r eine Formel enthält für jede Aussagenvariable, die in der Formel vorkommt, eine Kolonne, und in den Kolonnen werden alle möglichen Kombinationen von Wahrheitswerten eingetragen . Aus den Definitionen können wir die folgenden Wahrheitswert tabellen bilden: A ¬ A w f f w A B A ∧ B A ∨ B A ⇒ B A \Longleftrightarrow B w w w w w w w f f w f f f w f w w f f f f f w w ANALYSIS I-III, 2011/2013 177
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.1. Aussagenlogik reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.1.8 — Kontradiktion

- **Original term:** not explicitly named in script
- **Source:** PDF p179; section A.1. Aussagenlogik
- **Formal definition / script statement:**
```latex
Eine Formel, deren Wahrheitswert für alle Belegungen der Au ssagenvariablen immer falsch ist, heißt Kontradiktion. Eine Formel, deren Wahrheitswert für alle Belegungen der A ussagenva- riablen immer wahr ist, heißt Tautologie oder allgemeingültige Formel. Zwei Formeln A und B heißen logisch äquivalent, wenn die Formel A \Longleftrightarrow B eine Tautologie ist.
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.1. Aussagenlogik reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.2.1 — unnamed definition in A.2. Prädikatenlogik

- **Original term:** not explicitly named in script
- **Source:** PDF p180; section A.2. Prädikatenlogik
- **Formal definition / script statement:**
```latex
Seien X1, . . . ,X k Mengen. Eine k-stellige Aussageform oder Prädikat mit freien Varia- blen aus X1, . . . ,X k ist ein sprachlicher Ausdruck A(x1, . . . ,xk), der endlich viele Variablen x1 \in X1 . . . ,xk \in X k enthält und zu einer Aussage wird, wenn alle Variablen mit We rten belegt werden. Eine Aussage ist per definitionem eine 0-stellige Aussageform.
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.2. Prädikatenlogik reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.1 — Inklusion

- **Original term:** not explicitly named in script
- **Source:** PDF p184; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Sind X und Y Mengen, so bedeutet X \subset Y , dass jedes Element von X Element von Y ist. Ist X \subset Y , so sagt man, X sei eine Teilmenge von Y oder X sei in Y enthalten oder Y umfasse X ; man schreibt auch Y \supset X . Die „ \subset “–Beziehung heißt Inklusion. Für die Negation von X \subset Y schreibt man X ̸\subset Y . Wenn X und Y Mengen sind, für die X \subset Y und X ̸= Y gilt, so spricht man von einer echten Teilmenge (X ist echt enthalten in Y ). Offenbar gilt X \subset X , (X \subset Y undY \subset Z) \Rightarrow X \subset Z A.4.2. Extensionalitätsaxiom. Umfangsgleiche Mengen sind gleich; mit anderen Worten: Zwe i Mengen sind genau dann gleich, wenn sie aus denselben Elementen bestehe n. Daraus folgt (X \subset Y und Y \subset X ) \Longleftrightarrow X = Y ANALYSIS I-III, 2011/2013 183 Dementsprechend zerfallen fast alle Beweise von Gleichhei ten zwischen zwei Mengen X und Y in zwei Teile; zuerst hat man X \subset Y und dann Y \subset X zu zeigen. Wir geben nun ein wichtiges Mittel zum Bilden von neuen Menge n aus gegebenen Mengen an. Das nächste Axiom besagt, dass eine Aussage über Elemente einer gewisse n Menge aus dieser eine Teilmenge aussondert, nämlich die Tei…
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.4 — unnamed definition in A.4. Mengenlehre

- **Original term:** not explicitly named in script
- **Source:** PDF p185; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Sind X , Y zwei Mengen und gilt Y \subset X , so ist die Menge {x \in X : x ̸\in Y } eine Teilmenge von X , die sogenannte Differenz von X und Y oder das Komplement von Y bezüglich X , in Zeichen X \setminus Y oder ∁X Y (oder auch ∁Y , wenn kein Missverständnis zu befürchten ist). Sind zwei Mengen X ,Y gegeben, so existiert eine Menge, die genau aus denjenigen E lementen besteht, die sowohl zu X als auch zu Y gehören, nämlich {x \in X : x \in Y }; sie wird Durchschnitt von X und Y genannt und mit X \cap Y bezeichnet. Ist X eine Menge und x \in X , so bedeutet {x} die Menge, deren einziges Element x ist. Um unserem Vorgehen Substanz zu geben, setzen wir voraus: A.4.5. Existenzaxiom. Es gibt eine Menge. Als logische Folgerung ergibt sich aus diesem Axiom, dass ei ne Menge ohne irgendein Element existiert. Hat man nämlich eine Menge X , so wende man das Aussonderungsaxiom mit der Aussage „ x ̸= x“. Das Ergebnis ist die Menge (A.23) \emptysetX = {x \in X : x ̸= x}, gennant die leere Teilmenge von X . Es ist bemerkenswert, dass jede beliebige Eigenschaft auf Elemente von \emptysetX zutrifft. A.4.6. Aufgabe. Betrachte die Aussage: “Alle Menschen über 200 Jahre sind Ho chleistungssportle…
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.7 — die leere Menge

- **Original term:** not explicitly named in script
- **Source:** PDF p185; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Die Menge \emptysetheißt die leere Menge . Zwei Mengen X und Y heißen disjunkt falls X \cap Y = \emptyset. Das Paarmengenaxiom stellt sicher , dass jede Menge auch als Element einer Menge vorkommt und dass es zu je zwei Mengen stets eine dritte gibt, in der sie beide als E lemente enthalten sind. Das Axiom hat einen technischen Charakter . A.4.8. Paarmengenaxiom. Zu je zwei Mengen X , Y gibt es eine Menge Z, welche genau X und Y als Elemente besitzt. Wir schreiben Z = {X ,Y } und für {X , X }, die Einermenge von X , abkürzend {X }. Nach dem Extensionali- tätsaxiom ist stets {X ,Y } = {Y , X }; {X ,Y } hat also nicht die Eigenschaft eines geordneten Paares von X und Y . Eine Menge Z, deren Elemente Mengen sind, wird Mengensystem gennant. A.4.9. Vereinigungsmengenaxiom. Zu jedem Mengensystem Z gibt es die Menge Y der Elemente der Ele- mente von Z.
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.10 — Vereinigung von Z

- **Original term:** not explicitly named in script
- **Source:** PDF p185; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Die Menge Y heißt Vereinigung von Z. Schreibweise: Y = \bigcup z\in Z z = \bigcup {z : z \in Z}. ANALYSIS I-III, 2011/2013 184 Sind X und Y zwei Mengen und Z = {X ,Y } so wird \cup {z : z \in {X ,Y }} durch X \cup Y bezeichnet. Folglich ist X \cup Y = {a : a \in X oder a \in Y }. Sei x, y \in X . Die Vereinigung {x}\cup {y} wird mit {x, y} bezeichnet; ähnlich schreibt man {x, y, z} für {x}\cup {y}\cup {z} usw . A.4.11. Potenzmengenaxiom. Zu jeder Menge X gibt es die Menge Y aller Teilmengen von X , die sogenannte Potenzmenge von X ; wir bezeichnen diese mit P(X ). Offenbar ist \emptyset \inP(X ) sowie X \in P(X ). Die Relationen x \in X und {x} \in P(X ) sind äquivalent, ebenso Y \subset X und Y \in P(X ). Beispiel: Für X = {1,2,3} ist P(X ) = { \emptyset,{1},{2},{3},{1,2},{1,3},{2,3}, X } .
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.12 — die erste

- **Original term:** not explicitly named in script
- **Source:** PDF p186; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Je zwei Objekten x, y entspricht ein neues Objekt, das geordnete Paar (x, y); die Relation ( x, y) = (x′, y′) ist äquivalent der Relation ( x = x′ und y = y′); insbesondere gilt ( x, y) = (y, x) genau dann, wenn x = y ist. Das erste (bzw . zweite) Element eines geordneten Paare s z = (x, y) heißt die erste (bzw .zweite) Projektion von z, in Zeichen x = pr1 z (bzw .y = pr2 z). Sind X ,Y zwei (nicht notwendig verschiedene) Mengen, so gibt es eine (eindeutig bestimmte) Men- ge, deren Elemente genau die geordneten Paare ( x, y), x \in X und y \in Y sind. Sie wird das kartesische Produkt (oder einfach Produkt) von X und Y genannt und mit X × Y bezeichnet.
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.14 — unnamed definition in A.4. Mengenlehre

- **Original term:** not explicitly named in script
- **Source:** PDF p186; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Seien X und Y Mengen. Eine Abbildung f : X → Y von der Menge X in die Menge Y ist eine Vorschrift, die jedem Element x \in X genau ein Element f (x) \in Y zuordnet. Wir schreiben auch f : X → Y , x \mapstof (x). Der Graph der Funktion f : X → Y ist die folgende Teilmenge von X × Y : (A.24) Graph( f ) = {(x, y) \in X × Y : y = f (x)}. Zwei Abbildungen f , g : X → Y sind gleich, wenn f (x) = g(x) für alle x \in X , d.h. Graph( f ) = Graph(g). Der Graph einer Abbildung charakterisiert die Abbildung vo llständig. Eigentlich ist es korrekt zu denken, dass die Abbildung ein Graph ist! Eine formalere Definition einer Abbildung verläuft daher so: ANALYSIS I-III, 2011/2013 185
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.15 — unnamed definition in A.4. Mengenlehre

- **Original term:** not explicitly named in script
- **Source:** PDF p187; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Seien X , Y Mengen. Eine Abbildung von X in Y ist eine Teilmenge G \subset X × Y , gennant funktionaler Graph, mit folgender Eigenschaft: Zu jedem x \in X gibt es ein und nur ein y \in Y , so dass ( x, y) \in G. Dieses y bezeichnet man dann als f (x) und erhält eine „Abbildungsvorschrift“ f : X → Y , x \mapstof (x).
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.17 — der Definitionsbereich

- **Original term:** not explicitly named in script
- **Source:** PDF p187; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Sei f : X → Y eine Abbildung. (i) Die Menge X heißt der Definitionsbereich, die Menge Y der Wertebereich von f . (ii) Für x \in X heißt f (x) das Bild von x unter f oder , wenn f klar ist, einfach das Bild von x. Es heißt auch der Wert von f auf x oder an der Stelle x. (iii) Die Menge {f (x) : x \in X } \subset Y heißt das Bild oder die Bildmenge von f . (iv) Für A \subset X heißt f (A) = {f (x) : x \in A} das Bild von A unter f . (v) Für B \subset Y heißt f − 1(B) = {x : f (x) \in B} \subset X das Urbild von B unter f . (Es kann f − 1(B) = \emptysetsein.)
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.18 — Einschränkung

- **Original term:** Einschränkung
- **Source:** PDF p187; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Sei f : X \to Y eine Abbildung und A \subset X . Dann bezeichnen wir mit f | A : A \to Y die Abbildung, die jedem x \in A den Wert f (x) \in Y zuordnet. Also f | A : A \to Y , x \mapstof (x). f | A heißt die Einschränkung (oder Restriktion) von f auf A. Ist A ̸= X , so gelten f und f | A also als verschiedene Abbildungen, obwohl sie mit jedem x \in A „dasselbe machen“.
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.19 — injektiv , surjektiv , bijektiv

- **Original term:** injektiv , surjektiv , bijektiv
- **Source:** PDF p187; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Sei f : X \to Y eine Abbildung. (i) f heißt injektiv, wenn eine der folgenden, zueinander äquivalenten Bedingu ngen erfüllt ist: a) \forall x1, x2 \in X (x1 ̸= x2 ⇒ f (x1) ̸= f (x2)), b) \forall x1, x2 \in X ( f (x1) = f (x2) ⇒ x1 = x2). (ii) f heißt surjektiv, wenn f (X ) = Y . (iii) f heißt bijektiv, wenn es injektiv und surjektiv ist, d.h. wenn jedes y \in Y das Bild genau eines x \in X ist.
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.

## Def A.4.20 — Umkehrabbildung

- **Original term:** Umkehrabbildung
- **Source:** PDF p187; section A.4. Mengenlehre
- **Formal definition / script statement:**
```latex
Sei f : X \to Y bijektiv . Zu jedem y \in B gibt es also genau ein x \in X mit f (x) = y. Wir bezeichnen dieses x mit f − 1(y) und haben damit eine Abbildung f − 1 : Y \to X definiert, welche Umkehrabbildung von f heißt. Die Umkehrabbildung existiert nur für bijektive Abbildungen f : X \to Y . ANALYSIS I-III, 2011/2013 186 LITERATUR [1] N. H. Abel. Untersuchungen über die Reihe 1 + m 1 x + m(m− 1) 1·2 x2 + m(m− 1)(m− 2) 1·2·3 x3 + . . .. Crelles Journal, 1:311–339. [2] E. Behrends. Maß- und Integrationstheorie. Springer, 1987. [3] A. Beutelspacher . “Das ist o. B. d. A. trivial!” . Vieweg. Braunschweig. iv+96, 1997. Eine Gebrauchsanleit ung zur For- mulierung mathematischer Gedanken mit vielen praktischen Tips für Studierende der Mathematik und Informatik. [4] P . Cohen. Set Theory and the Continuum Hypothesis . New Y ork-Amsterdam: W .A. Benjamin, Inc. VI, 154 p., 1966. [5] J. Dieudonné. Grundzüge der modernen Analysis. Band 1. (Übers. aus dem Eng lischen: Ludwig Boll und Klaus Matt- hes. Übers. d. Berichtigungen u. Erg. aus d. Französ.: Ludwi g Boll). 3., berichtigte u. erg. Aufl. Logik und Grundlagen der Mathematik, Bd. 8. Braunschweig-Wiesbaden: Friedr . Vi eweg & Sohn. 369 S.…
```
- **English explanation:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Intuition:** This definition gives precise language for the topic of see reconstructed table of contents for this section.
- **Why it matters:** Later statements rely on this term being used exactly, especially in proofs and exercise wording.
- **Used later:** None beyond ordinary mathematical language. Later entries in and after A.4. Mengenlehre reuse this vocabulary.
- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.
- **Simple example:** Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood.
- **Uncertainty:** No major extraction warning detected.
