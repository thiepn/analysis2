# Proof Database

This database focuses on important proofs and every numbered result whose extracted block contains `Beweis:`. OCR artifacts are marked; use the PDF for exact symbol verification.

## Proof A.3.10 — 1.1. Körperaxiome

- **Theorem name:** Satz A.3.10 
- **Source:** PDF p5; section 1.1. Körperaxiome
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir beweisen die Behauptung durch Widerspruch. Die Konklus ion ist B :“ \sqrt 2 ist irrational.“ Das Gegenteil ist ¬ B :“ \sqrt 2 ist rational.“ Die folgende Schlusskette gilt: x = \sqrt 2 ist rational : \Longleftrightarrow \exists p, q \in Z, q ̸= 0 : x = p/q = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : x = p/q = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : 2 = x2 = p2/q2 = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : 2q2 = p2 = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : 2| p und 2| q . (1.1) Die letzte Implikation zeigt man so: 2q2 = p2 \Rightarrow 2| p2 \Rightarrow 2| p \Rightarrow \exists k \in Z : p = 2k = ⇒ p2 = 4k2 \Rightarrow 4k2 = q2 = 2p2 \Rightarrow 2k2 = q2 \Rightarrow 2| q2 \Rightarrow 2| q = ⇒ 2| q und 2| p . Die letzte Behauptung von (1.1), nämlich F: “ \exists p, q \in Z, q ̸= 0 und ( p, q) = 1 : 2| p und 2| q”, ist offen- sichtlich falsch. Wir haben also gezeigt, dass ¬ B \Rightarrow F wahr ist. Das ist aber nur möglich, wenn ¬ B falsch ist (siehe Wahrheitswerttabelle der Implikation), d.h. wenn B wahr ist. □ Sie hat auch eine unendlich nicht-periodische Dezimalbruc hzerlegung, wir können sie nicht als Bruch darstellen, z. B. in einem Computer speichern. Wir kön nen sie nur approximieren. 17.10.25 Wir wollen einen neuen Zahlenbereich definieren, der die Lös ung von x2 = 2 enthält und noch mehr, die Grundlage für die Analysis, Physik und andere Wiss enschaften ist. Diesen Bereich heißt Bereich der reellen Zahlen. Was ist unsere Intuition über die reellen Zahlen R? (1) Reelle Zahlen können addiert und multipliziert werden wie r ationale Zahlen. (2) Reelle Zahlen können geordnet werden, d. h. der Größenvergl eich ist möglich: x < y Daher entsprechen die reellen Zahlen den Punkten auf der Zah lengeraden. (3) Die reelle Gerade ist ein Kontinuum, sie…
```
- **Key idea:** This result packages a reusable fact from 1.1. Körperaxiome; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz A.3.10 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.1.2 — 1.1. Körperaxiome

- **Theorem name:** Satz 1.1.2 
- **Source:** PDF p7; section 1.1. Körperaxiome
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(a) Seien 0 und 0 ′ zwei Nullelemente. Da 0 ein Nullelelment ist, gilt 0 ′+ 0 = 0′. Da 0 ′ ein Nullelelment ist, gilt 0 ′+ 0 = 0′. Insgesamt gilt 0 = 0 + 0′= 0′ also 0 = 0′. (b) Aus x + a = b folgt (x + a) + (− a) = b + (− a) Addition von − a ⇒ x + (a + (− a)) = b + (− a) Assoziativität ⇒ x + 0 = b + (− a) Addition des Inverses ⇒ x = b + (− a) Addition des Nullelements Wegen a ̸= 0 existiert das multiplkative Inverse a− 1. Aus ax = b folgt a− 1(ax) = a− 1b Multiplikation von a− 1 ⇒ (a− 1a)x = a− 1b Assoziativität ⇒ 1 ·x = a− 1b Multiplikation des Inverses ⇒ x = a− 1b Multiplikation des Einselements Seien ̃a und ̃ ̃a zwei additive Inverse von a, d.h. ̃a + a = 0 und ̃ ̃a + a = 0. Somit sind ̃a und ̃ ̃a Lösungen der Gleichung x + a = 0. Wegen der Eindeutigkeit der Lösung folgt ̃a = ̃ ̃a. Analog zeigt man dass, das multiplikative Inverse eindeutig ist. (c) Die Elemente a und − (− a) sind Lösungen der Gleichung x + (− a) = 0, da a + (− a) = 0. Wegen der Eindeutigkeit der Lösung folgt a = − (− a). Man kann auch so argumentiren: Per Definition ist a + (− a) = 0. Wegen der Kommutativität der Addition folgt ( − a) + a = 0. Nach Definition des Inversen der Addition ist also a das additive Inverse von − a, d. h. − (− a) = a. Es gilt (a + b) + ((− a) + (− b)) = a + b + (− a) + (− b) = a + (− a) + b + (− b) = (a + (− a)) + (b + (− b)) = 0 + 0 = 0. Mit der Definition des Inversen der Addition folgt schließli ch, dass ( − a) + (− b) das additive Inverse von a + b ist, also ( − a) + (− b) = − (a + b). Sei a ̸= 0. Per Definition ist a ·a− 1 = 1. Wegen der Kommutativität der Multiplikation folgt a− 1 ·a = 1. Nach Definition des Inversen der Multiplikation ist also ( a− 1)− 1 = a. ANALYSIS I-III, 2011/2013 6 Seien a ̸= 0 und b ̸= 0. Dann existieren a− 1 und b− 1, und es ist: (a ·b) ·(a−…
```
- **Key idea:** This result packages a reusable fact from 1.1. Körperaxiome; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.1.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.2.2 — Rechenregeln für Ungleichungen

- **Theorem name:** Satz 1.2.2 Rechenregeln für Ungleichungen
- **Source:** PDF p9; section 1.2. Anordnungsaxiome
- **Proof strategy in one sentence:** Start from the defining inequality or a known inequality, then estimate term by term.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(a) Es gilt x < y \Longleftrightarrow y − x \in P und y < z \Longleftrightarrow z − y \in P. Es folgt mit (O2), dass (z − y) + (y − x) \in P \Longleftrightarrow x < z (b) ( y + z) − (x + z) = y + z − x − z = y − x \in P ⇒ y + z > x + z (c) (− x) − (− y) = y − x \in P ⇒ − y < − x (d) yz − xz = (y − x)z \in P (e) Sei x ̸= 0. Falls x > 0 ⇒ x2 = x ·x \in P. Falls x < 0 ⇒ − x \in P ⇒ (− x)(− x) = x2 \in P (Satz 1.1.2 (c)). Da 1 = 1 ·1 = 12 und 1 ̸= 0, so ist 1 > 0. (j) \lambda > 0 ⇒ \lambdax < \lambda y und 1 − \lambda > 0 ⇒ (1 − \lambda)x < (1 − \lambda)y. Durch Addition gilt x = 1 ·x = (\lambda + 1 − \lambda)x = \lambdax + (1 − \lambda)x < \lambdax + (1 − \lambda)y < \lambda y + (1 − \lambda)y = (\lambda + 1 − \lambda)y = 1 ·y = y. Jetzt können wir zeigen, dass ein total angeordneter Körper außer 0 und 1 noch weitere Elemente hat! Denn 0 < 1 ⇒ 0 + 1 < 1 + 1 = : 2 ⇒ 0 < 1 < 2 usw . In einem beliebigen Körper (z.B. in Z/2Z) kann es passieren, dass 1 + 1 = 0 ! Wenn wir \lambda = 1 2 in (j) betrachten, ergibt sich x < x+ y 2 < y. Für zwei (nicht unbedingt verschiedene) Elemente x, y \in K heißt x+ y 2 das arithmetische Mittel von x und y. 24.10.25
```
- **Key idea:** This result packages a reusable fact from 1.2. Anordnungsaxiome; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Start from the defining inequality or a known inequality, then estimate term by term.
- **Active recall prompts:**
  1. State Satz 1.2.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.2.5 — Rechenregeln

- **Theorem name:** Satz 1.2.5 Rechenregeln
- **Source:** PDF p10; section 1.2. Anordnungsaxiome
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Zu (a): Wegen der Definition von | x| durch zwei Fälle, machen wir eine Fallunterscheidung. Ist x ≥ 0, so ist | x| = x ≥ 0. Ist x < 0, so ist | x| = − x > 0. Insgesamt, für alle x \in K gilt | x| ≥ 0. Zu (b): Für alle x \in K gilt | x| ≥ 0. Laut Definition 1.2.4 gilt dann ⏐ ⏐| x| ⏐ ⏐ ≥ 0. Zu | − x| = | x| : Ist x ≥ 0 so ist − x ≤ 0. Laut Definition 1.2.4 gilt | x| = x und | − x| = − (− x) = x. Somit ist | − x| = | x| . Ist nun x < 0, so ist − x > 0. Laut Definition 1.2.4 gilt | x| = − x und | − x| = − x. Somit ist | − x| = | x| . Zu (c): Zunächst zeigen wir die Vorwärtsrichtung ( ⇒ ) der ersten äquivalenz: Sei | x| ≥ 0. Wegen | x| ≥ 0 ist dann y ≥ 0. Fallunterscheidung: (a) Sei x ≥ 0. Dann gilt x = | x| ≤ y, also x ≤ y, und − y ≤ 0 ≤ x, also − y ≤ x. Insgesamt − y \le x \le y. 0 x = | x|− x− y y (b) Sei x < 0. Dann gilt x < 0 ≤ y, also x < y, und − x = | x| ≤ y, also − y ≤ x, also − y \le x \le y. 0 − x = | x|x− y y Nun die Rückrichtung ( ⇐ ): Sei − y \le x \le y. Fallunterscheidung: (a) Sei x ≥ 0. Dann ist x = | x| , und da per Voraussetzung x ≤ y gilt, folgt | x| ≤ y. (b) Sei x < 0. Dann ist − x = | x| , und da per Voraussetzung − y ≤ x, also y ≥ − x gilt, folgt | x| ≤ y. Die zweite äquivalenz folgt aus − y ≤ x \Longleftrightarrow y ≥ − x. Zu (d): Wenn man in (c) y = | x| nimmt, so folgt, dass x ≤ | x| und − x ≤ | x| . Aus x ≤ | x| und y ≤ | y| folgt durch Addition x + y ≤ | x| + | y| . Aus − x ≤ | x| und − y ≤ | y| folgt durch Addition ( − x) + (− y) ≤ | x| + | y| und wegen ( − x) + (− y) = − (x + y), gilt − (x + y) ≤ | x| + | y| . Insgesamt ist dann x + y ≤ | x| + | y| und − (x + y) ≤ | x| + | y| . Nach (c) folgt | x + y| ≤ | x| + | y| . □ Die Dreiecksungleichungen sind ein wichtiges Mittel in der Analysis. Die Gleichheit in der Drei- ecksungleichung | x + y| \le |…
```
- **Key idea:** This result packages a reusable fact from 1.2. Anordnungsaxiome; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.2.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.3.3 — 1.3. Natürliche Zahlen und vollständige Induktion

- **Theorem name:** Satz 1.3.3 
- **Source:** PDF p12; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(i) Zu zeigen sind die Eigenschaften (a) und (b) aus Definitio n 1.3.1 für M = N: (a) Zu zeigen: 1 \in N. Da für jede induktive Menge M gilt: 1 \in M, folgt aus der Definition von N, dass 1 \in N. (b) Zu zeigen: x \in N ⇒ x + 1 \in N. Sei x \in N. Per Definition ist x \in M für jedes induktive M. Also ist x + 1 \in M für jedes induktive M. Nach der Definition folgt x + 1 \in N. (ii) Nach Annahme ist M induktiv . Damit folgt nach der Definition von N, dass N \subset M. Mit M \subset N folgt dann M = N. □ Der Satz 1.3.3 besagt, dass die Menge N die kleinste induktive Menge ist.
```
- **Key idea:** This result packages a reusable fact from 1.3. Natürliche Zahlen und vollständige Induktion; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.3.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.3.4 — Induktionsprinzip

- **Theorem name:** Satz 1.3.4 Induktionsprinzip
- **Source:** PDF p12; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Proof strategy in one sentence:** Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.
- **Full proof rewritten clearly:**
  Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei M := {n \in N : A(n) ist wahr }. Aus (a) folgt, dass 1 \in M, und (b) zeigt, dass aus n \in M auch n + 1 \in M folgt. Nach Definition 1.3.1 ist M somit induktiv . Ausserdem ist M eine Teilmenge von N. Aus Teil (ii) des Satzes 1.3.3 folgt dann, dass M gleich N ist, d. h. A(n) ist wahr für alle n \in N. □ 28.10 Der Induktionsanfang besteht aus A(1) und dessen Beweis. Die Induktionsvoraussetzung ist „A(n) ist wahr “, die Induktionsbehauptung ist „ A(n + 1) ist wahr “. Der Induktionsschritt ist der Beweis von „ A(n) \Rightarrow A(n + 1)“. Induktionsbeweise strukturiert man so: (i) Induktionsanfang ( n = 1): Beweis von A(1). (ii) Induktionsannahme: Sei n \in N beliebig. Angenommen, A(n) gilt. (iii) Induktionsbehauptung: Es ist zu zeigen, dass A(n + 1) gilt. (iv) Induktionsschritt ( n ⇝ n + 1): Beweis von „ A(n) \Rightarrow A(n + 1)“ d. h., dass aus der Wahrheit von A(n) die Wahrheit von A(n + 1) folgt. Einen Induktionsbeweis könnte man sich als eine unendliche Reihe von Dominosteinen vorstellen, die man zu Fall bringen möchte. Jeder Dominostein steht für e in A(n). Um alle Steine umzustoßen, muss man den ersten Stein umschubsen (Beweis von A(1)), und der Stein A(n+ 1) muss nah genug zu A(n) stehen, so dass jeder Stein durch seinen Vorgänger mit umge rissen wird (Beweis von „ A(n) = ⇒ A(n + 1)“). Beispiel: Wir wollen beweisen, dass für alle n \in N gilt (1.3) Sn := 1 + 2 + . . .+ n = n(n + 1) 2 · ANALYSIS I-III, 2011/2013 11 Beweis: Die Aussage ist A(n) : 1+ 2+ . . .+ n = 1 2 n(n + 1). Wir beweisen dies durch vollständige Induk- tion nach n. Induktionsanfang: Wir müssen also zeigen, dass die Aussage A(1) wahr ist. Es gilt S1 = 1 und für n = 1 ist n(n+ 1) 2 = 1·2 2 = 1. Die Aussage A(1) : 1 = 1·2 2 ist wahr. Induktionsannahme: Wir nehmen an, dass A(n) für ein n \in N wahr…
```
- **Key idea:** A first domino plus a rule that every domino knocks over the next one proves the whole infinite chain.
- **Dependency list:** Inductive subsets and the definition of $\mathbb N$.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.
- **Active recall prompts:**
  1. State Satz 1.3.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.3.6 — Bernoulli-Ungleichung

- **Theorem name:** Satz 1.3.6 Bernoulli-Ungleichung
- **Source:** PDF p14; section 1.3. Natürliche Zahlen und vollständige Induktion
- **Proof strategy in one sentence:** Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.
- **Full proof rewritten clearly:**
  Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es sei x ≥ − 1. Für n \in N sei A(n) die Aussage, dass (1 + x)n ≥ 1 + nx. Induktionsanfang. Die Aussage A(1) lautet: (1 + x)1 ≥ 1 + 1 ·x. Sie ist offentsichtlich wahr. Induktionsannahme. Wir nehmen an, dass A(n) für ein n \in N gilt, d.h. wir nehmen an, dass (1 + x)n ≥ 1 + nx. Induktionsbehauptung. Zu zeigen: (1 + x)n+ 1 ≥ 1 + (n + 1)x. Induktionsschritt. Es gilt (1 + x)n+ 1 = (1 + x)n(1 + x) Induktionsannahme und 1 + x ≥ 0 ≥ (1 + nx)(1 + x) = 1 + (n + 1)x + nx2 nx2 ≥ 0) ≥ 1 + (n + 1)x. Die Behauptung gilt somit nach dem Prinzip der vollständige n Induktion für alle n \in N. □ Beachten Sie, dass wir im 2. Schritt verwendet haben, dass 1 + x ≥ 0. Bei Beweisen in der Mathe- matik ist es immer eine gute Übungsaufgabe, sich zu überlege n, ob in der Tat alle Voraussetzungen verwendet wurden.
```
- **Key idea:** The first-order linear term underestimates the power for admissible $x$.
- **Dependency list:** Induction and order rules.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.
- **Active recall prompts:**
  1. State Satz 1.3.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.4.4 — Binomischer Lehrsatz

- **Theorem name:** Satz 1.4.4 Binomischer Lehrsatz
- **Source:** PDF p16; section 1.4. Fakultät, Binomialkoeffizienten und binomischer Lehrsatz
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Seien x, y \in K. Für n \in N sei A(n) die Aussage: (x + y)n = n\sum k= 0 ( n k ) xn− k yk. Induktionsanfang. Die Aussage A(1) lautet: (x + y)1 = ( 1 0 ) x1 y0 + ( 1 1 ) x0 y1 Da ( 1 0 ) = ( 1 0 ) = 1 sind beide Seiten gleich x + y, also ist A(1) wahr. Induktionsannahme. Wir nehmen an, dass A(n) gilt, d.h. wir nehmen an, dass (x + y)n = n\sum k= 0 ( n k ) xn− k yk. Induktionsbehauptung. Wir sollen zeigen, dass A(n + 1) gilt (wir ersetzen n durch n + 1): (x + y)n+ 1 = n+ 1\sum k= 0 ( n + 1 k ) xn+ 1− k yk. Induktionsschritt. Mithilfe der Induktionsannahme berechnen wir (x + y)n+ 1 = (x + y)(x + y)n = = (x + y) · n\sum k= 0 ( n k ) xn− k yk = = x · n\sum k= 0 ( n k ) xn− k yk + y · n\sum k= 0 ( n k ) xn− k yk = = n\sum k= 0 ( n k ) xn− k+ 1 yk + n\sum k= 0 ( n k ) xn− k yk+ 1. Wir wenden jetzt die Indexverschiebung an: n\sum k= 0 ck = n+ 1\sum k= 1 ck− 1. Die zweite Summe kann man mit Indexverschiebung so umschrei ben: n\sum k= 0 ( n k ) xn− k yk+ 1 = n+ 1\sum k= 1 ( n k − 1 ) xn− (k− 1) y(k− 1)+ 1 = n+ 1\sum k= 1 ( n k − 1 ) xn+ 1− k yk. Mit dieser Indexverschiebung und mit der Additionsformel f ür Binomialkoeffizienten erhalten wir nun (x + y)n+ 1 = n\sum k= 0 ( n k ) xn− k+ 1 yk + n+ 1\sum k= 1 ( n k − 1 ) xn+ 1− k yk = ( n 0 ) xn+ 1 y0 + n\sum k= 1 (( n k − 1 ) + ( n k )) xn− k+ 1 yk + ( n 0 ) x0 yn+ 1 = ( n + 1 0 ) xn+ 1 y0 + n\sum k= 1 ( n + 1 k ) akbn− k+ 1 + ( n + 1 n + 1 ) y0 yn+ 1 = n+ 1\sum k= 0 ( n + 1 k ) xn+ 1− k yk. Die Behauptung gilt somit nach dem Prinzip der vollständige n Induktion für alle n \in N. □ ANALYSIS I-III, 2011/2013 16 1.5. Vollständigkeitsaxiom. Dieses Axiom bringt die geometrische Anschauung zum Ausdru ck, dass die Zahlengerade ein Kontinuum ist. Die Vollständigke it ist eine der wichtigsten Eigenschaften von R. Ohne sie könnten wir z.B.…
```
- **Key idea:** This result packages a reusable fact from 1.4. Fakultät, Binomialkoeffizienten und binomischer Lehrsatz; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.4.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.6.1 — Prinzip von Archimedes

- **Theorem name:** Satz 1.6.1 Prinzip von Archimedes
- **Source:** PDF p20; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Proof strategy in one sentence:** Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.
- **Full proof rewritten clearly:**
  Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Andernfalls hätte die Menge N ein Supremum s = sup N \in R. Weil s− 1 keine obere Schranke von A ist, gäbe es ein Element n \in N mit s − 1 < n, also sup N = s < n + 1 \in N, ein Widerspruch zur Annahme, dass s eine obere Schrank von N ist. □ Dies zeigt auch, dass N unendlich ist (da jede endliche Menge in R ein Maximum besitzt). Eine Umformulierung des archimedischen Prinzips lautet: Für alle x \in R, y \in R+ gibt es n \in N mit n y> x.
```
- **Key idea:** Natural numbers eventually exceed any fixed real number.
- **Dependency list:** Completeness and supremum.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.
- **Active recall prompts:**
  1. State Satz 1.6.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.6.2 — Satz von Eudoxus

- **Theorem name:** Satz 1.6.2 Satz von Eudoxus
- **Source:** PDF p20; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Nach dem Satz 1.6.1 gibt es n \in N mit n > 1 \varepsilon, also 1 n < \varepsilon. □ Die Aussage ist klar für \varepsilon ≥ 1 (man kann n = 2 nehmen). Sie ist interessant für \varepsilon “klein”. Die griechischen Buchstaben \varepsilon und δ (epsilon und delta) werden in der Mathematik oft für kleine p ositive Zahlen verwendet. Eine Umformulierung des Satzes von Eudoxus ist inf { 1 n : n \in N } = 0 . ANALYSIS I-III, 2011/2013 19 In der Tat, sei A = {1 n : n \in N } . Dann gilt: (a) 0 ist untere Schranke für A. (b) Für \varepsilon> 0 wähle n \in N mit 1 n < \varepsilon. Wegen 1 n \in A ist \varepsilon keine untere Schranke für A. Es bleibt, dass 0 die größte untere Schranke von A ist.
```
- **Key idea:** This result packages a reusable fact from 1.6. Folgerungen des Vollständigkeitsaxioms; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.6.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.6.3 — Wohlordnungsprinzip

- **Theorem name:** Satz 1.6.3 Wohlordnungsprinzip
- **Source:** PDF p21; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
In der Tat, sei A \subset Z nach oben beschränkt. Laut Axiom (V) gibt es s = sup A \in R. Da s − 1 keine obere Schranke von A ist, existiert n \in A mit s − 1 < n ≤ s, also s < n + 1. Daher gilt s < m und somit m ̸\in A für alle m ≥ n + 1. Da zwischen n und n + 1 keine ganze Zahl existiert, so gilt a ≤ n für alle a \in A also n ist das Maximum von A (und natürlich s = n). □
```
- **Key idea:** This result packages a reusable fact from 1.6. Folgerungen des Vollständigkeitsaxioms; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.6.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.6.5 — Dichtheit von Q in R

- **Theorem name:** Satz 1.6.5 Dichtheit von Q in R
- **Source:** PDF p21; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wähle n \in N mit 1 n < b − a (Satz 1.6.2). Dann gilt na + 1 < nb. Aber ⌊na⌋ ≤ na < ⌊ na⌋ + 1, also na < ⌊ na⌋ + 1 ≤ na + 1 < nb. Durch Division mit n folgt: a < ⌊na⌋ + 1 n < b. Die rationale Zahl x = ⌊na⌋ + 1 n erfüllt somit a < x < b. □ 7.11.25 Mehr zum Wohlordnungsprinzip finden Sie in §1.9. Eine weiter e wichtige Anwendung des Vollstän- digkeitsaxioms ist die Existenz der Wurzeln. ANALYSIS I-III, 2011/2013 20
```
- **Key idea:** Between any two real numbers sits a rational number.
- **Dependency list:** Archimedean principle and floor function.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.6.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 1.6.6 — Existenz der k-ten Wurzel

- **Theorem name:** Satz 1.6.6 Existenz der k-ten Wurzel
- **Source:** PDF p22; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Der Satz ist klar für k = 1. Wir betrachten den Fall k ≥ 2. Wir zeigen zuächst die Eindeutig- keit. Zu zeigen ist, dass für reelle Zahlen x, y > 0 mit xk = a = yk folgt x = y. Vorbemerkung: Es gilt die folgende Äquivalenz. Für alle x, y ≥ 0 gilt: x < y \Longleftrightarrow xk < yk . “= ⇒ ” Nehmen wir an, dass x < y. Dann x2 = x ·x ≤ x ·y (da x ≥ 0) und x ·y < y ·y = y2 (da y > 0) also x2 < y2. Durch Induktion zeigt man, dass xn < yn für alle n \in N. “⇐ = ” Seien x, y ≥ 0 mit xn < yn. Falls x ≥ y, folgt wie oben, dass xn ≥ yn, Widerspruch zu xn < yn. Es muss also x < y sein. Seien nun x, y > 0 mit xk = a = yk. Falls x < y wäre, so folgte nach der obigen Ungleichung dass xk < yk, im Widerspruch zur Annahme. Ähnlich schließt man die Mögli chkeit x > y aus. Wegen der Trichotomie (erstes Anordnungsaxiom) bleibt nur die Mögli chkeit x = y. Für die Existenz betrachten wir die Menge A := { x \in R : x ≥ 0, xk < a } . Die Menge A ist nicht leer, denn 0 \in A. Die Menge A ist nach oben beschänkt, da 1 + a eine obere Schranke von A ist: Für alle x \in A gilt xk < a < 1 + ka < (1 + a)k , nach der Bernoullischen Ungleichung. Nach der obigen Vorbe merkung gilt dann x < 1 + a für alle x \in A. Das Vollständigkeitaxiom besagt, dass A ein Supremum s = sup A hat. Es gibt nun drei Mög- lichkeiten: (i) sk < a, (ii) sk = a, (iii) sk > a. Wir zeigen, dass (i) und (iii) zu Widerspruch führen. Zu (i). Angenommen sk < a. Die Idee des Beweises ist, eine Zahl t zu suchen, so dass s < t und tk < a. Das führt zu einem Widerspruch. Aber wie finden wir einen sol chen t ? Wir haben bessere Chancen, wenn t sehr nah an s liegt. Wir wählen also t = s + 1 n , da wir wissen, dass 1 n beliebig klein wird, wenn n groß genug ist (Satz von Eudoxus). Der binomische Lehrsatz l iefert für alle n \in N: ( s + 1 n…
```
- **Key idea:** This result packages a reusable fact from 1.6. Folgerungen des Vollständigkeitsaxioms; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.6.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 1.6.10 — Intervallschachtelungsprinzip

- **Theorem name:** Satz 1.6.10 Intervallschachtelungsprinzip
- **Source:** PDF p24; section 1.6. Folgerungen des Vollständigkeitsaxioms
- **Proof strategy in one sentence:** Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.
- **Full proof rewritten clearly:**
  Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei I n = [an, bn]. Wir definieren die Menge A := {an : n \in N}. Die Menge A ist nicht leer und für jedes m \in N ist bm eine obere Schranke von A. Angenommen, bm ist keine obere Schanke von A, so existiert ein n \in N mit bm < an. Dann sind die Intervalle I n und I m disjunkt. Das ist aber ein Widerspruch zur Eigenschaft (i) der Definition 1.6.9. Diese Voraussetzung impliziert, dass I n \subset I m (falls n > m) oder I m \subset I n (falls m > n). Sei x := sup A. Weil s eine obere Schanke von A ist, folgt, dass für alle n \in N gilt an ≤ x. Weil s die kleinste obere Schanke von A ist, folgt, dass für alle n \in N gilt x ≤ bn. Insgesamt, an ≤ x ≤ bn also x \in [an, bn] = I n für alle n \in N. ANALYSIS I-III, 2011/2013 23 Wir zeigen, dass der Durchschnitt der Intervallen I n nur ein Element enthält. Seien x, y \in [an, bn] für alle n \in N. Dann gilt | x − y| ≤ bn − an = | I n| für alle n \in N. Angenommen, x ̸= y. Dann ist | x − y| > 0. Sei \varepsilon := | x− y| 2 . Die Eigenschaft (ii) der Definition 1.6.9 besagt, dass es ei n n \in N gibt, mit | I n| < \varepsilon. Für dieses n gilt | x − y| ≤ bn − an = | I n| < | x − y| 2 Daraus folgt, dass 1 < 1 2 . Widerspruch. Es muss also | x − y| = 0 sein, und somit x = y. □ 11.11.25
```
- **Key idea:** Nested closed intervals that shrink indefinitely trap one real number.
- **Dependency list:** Completeness, compact intervals, supremum/infimum.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.
- **Active recall prompts:**
  1. State Satz 1.6.10 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.7.1 — 1.7. Der Körper der komplexen Zahlen

- **Theorem name:** Satz 1.7.1 
- **Source:** PDF p25; section 1.7. Der Körper der komplexen Zahlen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Die Körperaxiome sind leicht nachzuprüfen. Die neutralen E lemente sind (0 , 0) für die Ad- dition und (1 , 0) für die Multiplikation. Der einzige schwierige Punkt ist , zu zeigen, dass es für jedes z ̸= 0 ein w gibt, so dass z ·w = 1 gilt. Sei z = x + i y. Wir betrachten die Formel (x + i y)(x − i y) = x2 − ix y + i yx + y2 = x2 + y2. ANALYSIS I-III, 2011/2013 24 Es ist z ̸= 0 genau dann, wenn x2 + y2 ̸= 0. Setze w = x x2 + y2 − i x x2 + y2 Dann gilt z ·w = 1. □
```
- **Key idea:** This result packages a reusable fact from 1.7. Der Körper der komplexen Zahlen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.7.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.7.4 — Rechenregeln

- **Theorem name:** Satz 1.7.4 Rechenregeln
- **Source:** PDF p26; section 1.7. Der Körper der komplexen Zahlen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es seien also z = x + yi und w = u + vi komplexe Zahlen. Dann gilt in der Tat z + w = x + u + i(y + v) = x + u − (i y+ iv) = z + w zw = xu − yv + i(yu + xv) = xu − yv − i(yu + xv) = (x − i y)(u − iv) = z ·w. Re(z) = 1 2 ( x + i y+ x + i y ) = 1 2 (x + i y+ x − i y) = x Im(z) = 1 2i (z − z) = 1 2i ( x + i y− (x + i y) ) = 1 2i (x + i y− x + i y) = y z ·z = (x + i y)(x − i y) = x2 − ix y + i yx + y2 = x2 + y2 ( z ) = x − i y = x + (− i y) = x − (− i y) = x + i y □
```
- **Key idea:** This result packages a reusable fact from 1.7. Der Körper der komplexen Zahlen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.7.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 1.7.6 — Rechenregeln für den Betrag

- **Theorem name:** Satz 1.7.6 Rechenregeln für den Betrag
- **Source:** PDF p27; section 1.7. Der Körper der komplexen Zahlen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es seien z = x + i y und w = u + iv und komplexe Zahlen. (i) Es ist | z| = √ x2 + y2 ≥ 0, und wenn | z| = 0, dann ist auch x2 + y2 = 0, d.h. x = 0 und y = 0. (ii) Es ist Es ist \sqrt z ·z = √ (x + i y)(x − i y) = √ x2 + y2 = | z| . Dann gilt z · 1 | z| 2 z = 1 zz zz = 1, also ist z− 1 = 1 | z| 2 z. (iii) Es ist | z| = √ x2 + y2 = √ x2 + (− y)2 = | z| . (iv) Es ist | z| = √ x2 + y2 ≥ \sqrt x2 = | x| = | Re(z)| . Die zweite Ungleichung wird ganz analog bewiesen. (v) Aus Satz 1.7.4 (i) folgt, dass | w ·z| = √ wz ·wz = √ w ·w ·z ·z = √ ww · √ zz = | w| · |z| . (vi) Es gilt | z + w| 2 = (z + w)(z + w) = (z + w)(z + w) = zz + zw + wz + ww = | z| 2 + zw + zw + | w| 2 = | z| 2 + 2 Re(zw) + | w| 2 (iv) ≤ | z| 2 + 2| zw| + | w| 2 = | z| 2 + 2| z|| w| + | w| 2 = | z| 2 + 2| z|| w| + | w| 2 = (| z| + | w| )2. Für reelle Zahlen a, b ≥ 0 gilt: a ≤ b \Longleftrightarrow a2 ≤ b2. Aslo folgt die Dreiecksungleichung | z + w| ≤ | z| + | w| aus | z + w| 2 ≤ (| z| + | w| )2. □ ANALYSIS I-III, 2011/2013 26 Zur Dreiecksungleichung: In dem Dreieck mit Ecken die Punkt e 0, w und z + w ist eine Dreiecksseite höchstens so lang wie die Summe der beiden anderen Seiten. (0, 0) →→ ↑↑ x-Achse y-Achse •↗↗✡✡✡✡✡✡✡✡✡✡✡✡✡✡✡✡✡✡✡✡✡ z •→→❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥ w •↗↗2222222222222222222222222222222222222 • ✡✡✡✡✡✡✡✡✡✡✡ • ❥❥❥❥❥❥❥❥❥ z + w | w| | z| | z + w| Bemerkung (Zur quadratische Gleichungen) . Neben i2 = − 1 gilt auch ( − i)2 = − 1. Genauer hat die Gleichung z2 = − 1 die Lösungen z1 = i und z2 = − i und keine weiteren. In der Tat, z2 = − 1 ist äquiva- lent zu 0 = z2 + 1 = z2 − (− 1) = z2 − i2 = (z− i)(z+ i). Deshalb verwenden wir nicht die Bezeichnung \sqrt − 1 für i. Für reelle Zahlen a > 0 gibt es auch zwei Lösungen der Gleichung x2 = a. In diesem Fall können wir aber die positive Lösung mit \sqrta bezeichnen…
```
- **Key idea:** This result packages a reusable fact from 1.7. Der Körper der komplexen Zahlen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Appendix A logic/set language and earlier algebra/order material.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 1.7.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.1.3 — 2.1. Definition und Beispiele

- **Theorem name:** Lemma 2.1.3 
- **Source:** PDF p37; section 2.1. Definition und Beispiele
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir nehmen an, dass gilt: \existsM > 0 \forall \varepsilon > 0 \exists n0 \in N \forall n \ge n0 : | an − a| < M ·\varepsilon, Dies können wir auch als \existsM > 0 \forall \varepsilon′> 0 \exists n0 \in N \forall n \ge n0 : | an − a| < M ·\varepsilon′, schreiben. Wir wollen dann \forall \varepsilon > 0 \exists n0 \in N \forall n \ge n0 : | an − a| < \varepsilon, zeigen. Dazu sei ein beliebiges \varepsilon > 0 gege- ben.Wir setzen \varepsilon′= \varepsilon M . und verwenden die Annahme. Dies ergibt \exists n0 \in N \forall n \ge n0 : | an − a| < M ·\varepsilon′= M · \varepsilon M = \varepsilon, was zu zeigen war . Die anderen Aussagen lassen sich ähnlich z eigen. □ 18.11.25
```
- **Key idea:** This result packages a reusable fact from 2.1. Definition und Beispiele; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Lemma 2.1.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.1.5 — 2.1. Definition und Beispiele

- **Theorem name:** Satz 2.1.5 
- **Source:** PDF p38; section 2.1. Definition und Beispiele
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Um die Konvergenz von ( an) gegen a zu beweisen, muss man für beliebig vorgegebenes \varepsilon > 0 ein n0 = n0(\varepsilon) angeben, so dass | an− a| < \varepsilon für alle n \ge n0 gilt. Im Prinzip muss man also die Ungleichung | an− a| < \varepsilon nach der Unbekannten n \in N auflösen und eine Menge {n \in N : n \ge n0} von Lösungen finden. Falls an eine einfache Funktion von n ist, kann die Lösung der Ungleichung leicht sein. Falls nich t, muss man zunächst eine Abschätzung | an − a| \le bn finden, wobei bn eine einfache Form hat. Danach löst man die Ungleichung bn < \varepsilon. Wir gehen in zwei Etappen vor . Zunächst kommt eine heuristis che Phase (Laborphase), in der man eine geeignete Vorausabschätzung (Ansatz) für | an − a| sucht und die Ungleichung | an − a| (\le bn) < \varepsilon löst. Diese Etappe erscheint normalerweise nicht in Schriftform, und w enn, dann nur in Büchern über das Lösen von Problemen (ein berühmtes Beispiel ist das Buch [18] von G. Po lya). Man benutzt aber die Ergebnisse der Laborphase, um anschließend einen formalen Beweis niederz uschreiben. Zu (2.1). Laborphase: Wir lösen | an| = 1 ns < \varepsilon nach n für gegebenes \varepsilon > 0. Es gilt 1 ns < \varepsilon \Longleftrightarrow 1 \varepsilon < ns \Longleftrightarrow 1 \varepsilon1/s < n \Longleftrightarrow n \ge ⌊ 1 \varepsilon1/s ⌋ + 1 . Wir könnten es also mit einem n0 > 1 \varepsilon1/s versuchen. Und in der Tat, für n \ge n0 gilt ns \ge ns 0 (weil s > 0), also 1 ns \le 1 ns 0 < \varepsilon.Formaler Beweis: Sei \varepsilon > 0 vorgegeben. Wähle n0 = ⌊ 1 \varepsilon1/s ⌋ + 1 Dann gilt für alle n \ge n0: ⏐ ⏐ ⏐ 1 ns − 0 ⏐ ⏐ ⏐ = 1 ns \le 1 ns 0 < \varepsilon. Nach der Definition folgt lim n→\infty 1 ns = 0. Zu (2.2). Sei zunächst a \ge 1 (1. Fall). Laborphase: Die Ungleichung | n…
```
- **Key idea:** This result packages a reusable fact from 2.1. Definition und Beispiele; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.1.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 2.1.7 — Monotonieprinzip

- **Theorem name:** Satz 2.1.7 Monotonieprinzip
- **Source:** PDF p40; section 2.1. Definition und Beispiele
- **Proof strategy in one sentence:** Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.
- **Full proof rewritten clearly:**
  Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Nach Annahme ist die Menge A nach oben beschränkt. Aus dem Vollständigkeitsaxiom folgt , dass a := sup A existiert. Wir zeigen, dass an → a. Da a eine obere Schranke von A ist, gilt an ≤ a für alle n \in N. Sei \varepsilon > 0. Da a die kleinste obere Schranke von A ist, gibt es n0 mit a − \varepsilon < an0 ≤ a, , denn andernfalls wäre a − \varepsilon obere Schranke im Widerspruch zur Supremumeigenschaft von a. R a = sup an a − \varepsilon an0 an (a − \varepsilon, a) Wegen der Monotonie gilt für alle n ≥ n0, dass an0 ≤ an. Es folgt, dass a − \varepsilon < an0 ≤ an ≤ a für alle n ≥ n0 und somit | an − a| < \varepsilon. □ 2.1.8. Beispiele. (i) Sei ( In) eine Intervallschachtelung mit In = [an, bn] und \cap In = {x}. Dann sind ( an) und ( bn) konvergent und an → x, bn → x, n → \infty . In der Tat, wegen der Definition der Intervallschachtelung , ist ( an) monoton steigend und ( bn) monoton fallend. Im Satz 1.6.10 (Intervallschachtelungs prinzip) haben wir gesehen, dass ( an) nach ANALYSIS I-III, 2011/2013 39 oben beschränkt ist (jedes bn ist eine obere Schranke) und x wurde als sup {an} definiert. Da auch x = inf{bn}, die Aussage folgt aus dem Monotonieprinzip. Aus Satz 1.6.11 erhalten wir (2.6) ( 1 + 1 n )n \to e , ( 1 + 1 n )n+ 1 \to e , n \to \infty . (ii) Sei an = n\sum k= 0 1 n! = 1 + 1 1! + 1 2! + . . .+ 1 n! , für n \in N0; ( an) ist monoton wachsend und beschränkt, 2 1 2 < an < 3 für n \ge 2, also konvergent gegen eine Zahl in (2 ,3]. Der Grenzwert ist die Eulersche Zahl e = lim an. (iii) Sei a > 0, k \in N, k \ge 2. Wähle x1 > 0 mit xk 1 > a; definiere rekursiv für n \in N : xn+ 1 := xn − xk n − a kx k− 1n = (k − 1)xk n + a kx k− 1n > 0 . (xn) ist monoton fallend, nach unten durch k\sqrta beschränkt ⇒ (xn) konvergent.
```
- **Key idea:** A one-directional bounded sequence cannot wander forever; completeness forces a limit.
- **Dependency list:** Completeness, supremum, sequence convergence.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.
- **Active recall prompts:**
  1. State Satz 2.1.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.1.9 — 2.1. Definition und Beispiele

- **Theorem name:** Satz 2.1.9 
- **Source:** PDF p41; section 2.1. Definition und Beispiele
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei ( an) eine Folge mit an → a. Dann existiert zu \varepsilon = 1 ein n0 \in N, so dass | an − a| < 1 für alle n ≥ n0. Es folgt | an| = | (an − a)+ a| ≤ | an − a|+| a| < 1+| a| für alle n ≥ n0. Man setzt nun M := max{1+| a| ,| a1| , . . . ,| an0− 1| }. Dann ist | an| ≤ M für alle n ≥ n0. □ Ra − 1 a + 1 a = lim ana1 a2 a3 an0− 1 { an : n ≥ n0 } \subset (a − 1, a + 1) Bemerkung: (i) ( an)n\inN unbeschränkt \Rightarrow (an)n\inN divergent. Z.B. an = n ist divergent, ebenso an = (− 1)nn = { n, n gerade − n, n ungerade (ii) ( an)n\inN beschränkt ̸= ⇒ (an)n\inN konvergent. Z.B. ist die Folge 1 ,0,1,0, . . .beschränkt, aber divergent. 21.11.25 2.2. Rechnen mit konvergenten Folgen. Wir untersuchen nun, wie gut sich Konvergenz von Folgen mit algebraischen Operationen und mit Ungleichungen „verträgt“. Wir arbeiten nun mit mehrere Folgen und daher müssen wir zunächst bemerken, dass n0 in der Definition der Konvergenz auch von der Folge abhängt. A ls Beispiel, für die Folge an = 1 n kann man optimal n0 = ⌊1 \varepsilon ⌋ + 1 wählen und für die Folge an = 1 n2 kann man optimal n0 = ⌊ 1\sqrt\varepsilon ⌋ + 1 wählen. Wir zeigen nun, dass man zu \varepsilon ein n0 finden kann, das für ( an) und ( bn) gleichzeitig funktioniert.
```
- **Key idea:** This result packages a reusable fact from 2.1. Definition und Beispiele; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.1.9 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 2.2.1 — 2.2. Rechnen mit konvergenten Folgen

- **Theorem name:** Lemma 2.2.1 
- **Source:** PDF p41; section 2.2. Rechnen mit konvergenten Folgen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei \varepsilon > 0 beliebig. Wegen lim n→\infty an = a existiert ein n1 \in N, so dass für alle n ≥ n1 gilt | an − a| < \varepsilon und wegen und lim n→\infty bn = b existiert ein n2 \in N, so dass für alle n ≥ n2 gilt | bn − b| < \varepsilon. Setzt man n0 := max{n1, n2}, dann gelten für n ≥ n0 sowohl | an − a| < \varepsilon als auch | bn − b| < \varepsilon. □
```
- **Key idea:** This result packages a reusable fact from 2.2. Rechnen mit konvergenten Folgen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Lemma 2.2.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.2.2 — Konvergenz und algebraische Operationen

- **Theorem name:** Satz 2.2.2 Konvergenz und algebraische Operationen
- **Source:** PDF p41; section 2.2. Rechnen mit konvergenten Folgen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei \varepsilon > 0 und wähle dazu n0 wie im Lemma. Zu (1): Vorüberlegung: Wir müssen also | (an + bn) − (a + b)| ‘beliebig klein kriegen’. Nachdem an → a und bn → b, können wir | an − a| und | bn − b| ‘beliebig klein kriegen’. Wir müssen daher | (an + bn)− (a+ b)| so umschreiben, dass | an − a| und | bn − b| auftauchen. Wir schreiben | (an + bn)− (a+ b)| = | (an − a)+ (bn − b)| und kommen sofort auf die Idee, die Dreiecksungleichung anz uwenden. Die Aussage (1) folgt aus der Dreiecksungleichung und der Ta tsache, dass für alle n ≥ n0 gilt: | (an + bn) − (a + b)| = | (an − a) − (b − bn )| ≤ | an − a| + | bn − b| ≤ \varepsilon+ \varepsilon= 2\varepsilon. Zu (2): Vorüberlegung: Wir suchen also einen Brücke von an − a, bn − b zu anbn − ab. Wie können wir zunächst anbn mit an − a oder bn − b in Verbindung bringen? über den Ausdruck an(bn − b) = anbn − anb. Was benötigen wir , um von hier nach anbn − ab zu gelangen? Wir müssen anb − ab dazu addieren, also (an − a)b. Nach Satz 2.1.9 existiert ein C > 0, so dass | an| ≤ C für alle n \in N. Es folgt aus der Dreiecksungleichung, dass für alle n ≥ n2 gilt: | an bn − ab| = | anbn − anb + an b − ab| = | (anbn − anb) + (an b − ab)| ≤ | an(bn − b)| + | (an − a)b| = | an| · |bn − b| + | b| · |an − a| ≤ (C + | b| )\varepsilon. Dabei ist C + | b| unabhängig von \varepsilon. Aus Lemma 2.1.3 folgt die Behauptung. Zu (3): Aus bn → b folgt mit \varepsilon:= | b| 2 , dass n0 \in N existiert mit | bn − b| < | b| 2 für alle n ≥ n0. Daraus folgt | b| = | (b − bn) + bn| ≤ | b − bn| + | bn| < | bn| − | b| 2 , also also | bn| ≥ | b| 2 , insbesondere bn ̸= 0 für n ≥ n0. Wir zeigen nun 1 bn → 1 b : Sei \varepsilon > 0 gegeben und n1 derart gewählt, dass | bn − b| < \varepsilon für n ≥ n1. Für n ≥ n0 ist | bn| ≥ | b| 2 , also folgt für n ≥ n2 := max…
```
- **Key idea:** Limits respect ordinary algebra when the expressions are well-defined.
- **Dependency list:** Epsilon definition, boundedness of convergent sequences.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.2.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.2.3 — Vergleichsprinzip

- **Theorem name:** Satz 2.2.3 Vergleichsprinzip
- **Source:** PDF p42; section 2.2. Rechnen mit konvergenten Folgen
- **Proof strategy in one sentence:** Start from the defining inequality or a known inequality, then estimate term by term.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei \varepsilon > 0. Wähle n0 \in N, so dass | an − a| < \varepsilon und | bn − b| < \varepsilon für alle n ≥ n0 gilt. Aus | an − a| < \varepsilon folgt a − \varepsilon < an, also a < an + \varepsilon. Aus | bn − b| < \varepsilon folgt bn < b + \varepsilon. Damit folgt für n ≥ n0 a < an + \varepsilon ≤ bn + \varepsilon< b + 2\varepsilon. Also gilt a < b + 2\varepsilon für alle \varepsilon > 0. Daraus folgt a − b ≤ inf { 2\varepsilon: \varepsilon > 0 } = inf R+ = 0 also a ≤ b. □
```
- **Key idea:** This result packages a reusable fact from 2.2. Rechnen mit konvergenten Folgen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Start from the defining inequality or a known inequality, then estimate term by term.
- **Active recall prompts:**
  1. State Satz 2.2.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.2.4 — 2.2. Rechnen mit konvergenten Folgen

- **Theorem name:** Folgerung 2.2.4 
- **Source:** PDF p42; section 2.2. Rechnen mit konvergenten Folgen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir wenden Satz 2.2.3 auf die Folgen ( an) und ( cn) mit cn = c für alle n \in N an, das ergibt a ≤ c. Analog folgt b ≤ a. □ ANALYSIS I-III, 2011/2013 41
```
- **Key idea:** This result packages a reusable fact from 2.2. Rechnen mit konvergenten Folgen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Folgerung 2.2.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.2.5 — Einschließungsprinzip

- **Theorem name:** Satz 2.2.5 Einschließungsprinzip
- **Source:** PDF p43; section 2.2. Rechnen mit konvergenten Folgen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei \varepsilon > 0. Wähle n0 \in N, so dass | an − a| < \varepsilon und | cn − a| < \varepsilon für alle n ≥ n0. Aus | an − a| < \varepsilon folgt a − \varepsilon < an und aus | cn − a| < \varepsilon folgt cn < a + \varepsilon. Also gilt für n ≥ n0 a − \varepsilon < an ≤ bn ≤ cn < a + \varepsilon, also | bn − a| < \varepsilon, was zu zeigen war . □ Bemerkung. Die Konvergenz von ( bn) wird im Satz nicht vorausgesetzt, sondern abgeleitet.
```
- **Key idea:** A squeezed sequence must follow the common limit of the bounds.
- **Dependency list:** Comparison principle.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.2.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.3.3 — 2.3. Einschub: Abzählbare und überabzählbare Mengen

- **Theorem name:** Satz 2.3.3 
- **Source:** PDF p45; section 2.3. Einschub: Abzählbare und überabzählbare Mengen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Jede rationale Zahl m n mit m, n \in Z, n ̸= 0, und gcd( m, n) = 1 kann eindeutig dargestellt werden. Wir ordnen die Brüche m n , m, n \in Z, n ̸= 0, in ein quadratisch unendliches Schema, aus dem man die ungek ürzten Brüche herausstreicht, um „Mehrfachaufzählung“ zu vermei den. Dabei bleiben nur die ungekürtze Brüche m n mit m, n \in Z, n ̸= 0, und gcd( m, n) = 1 0 \to 1 1 \to − 1 1 2 1 \to − 2 1 3 1 \to − 3 1 . . . ւ ր ւ ր ւ 1 2 − 1 2 2 2 − 2 2 ↓ ր ւ ր 1 3 − 1 3 2 3 .. . ւ ր ւ 1 4 − 1 4 2 4 . . . .. . Es ist klar , dass jede rationale Zahl genau einmal in diesem S chema auftaucht. Dieses Schema kann man auf dem durch die „Pfeile“ angegebenen Wege durchwandern un d dadurch die Abzählung {rk : k \in N} von Q herstellen. □ Wir können dagegen die reellen Zahlen nicht abzählen:
```
- **Key idea:** This result packages a reusable fact from 2.3. Einschub: Abzählbare und überabzählbare Mengen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.3.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.4.3 — 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium

- **Theorem name:** Satz 2.4.3 
- **Source:** PDF p46; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
„= ⇒ “ Sei a Häufungswert von ( an). Wähle n1 so, dass | an1 − a| < 1 (\varepsilon = 1 in Häufungswertdefinition). Wähle n2 > n1 so, dass | an2 − a| < 1 2 (\varepsilon = 1 2 in Häufungswertdefinition). Wähle n3 > n2 so, dass | an3 − a| < 1 3 , usw . Die Teilfolge ( ank )k\inN konvergiert gegen a, da | ank − a| ≤ 1 k , also | ank − a| → 0, k → \infty . „⇐ = “ Sei ank → a, für k → \infty und \varepsilon> 0 beliebig. Dann gibt es ein k0 mit | ank − a| < \varepsilon für k ≥ k0. Da dies unendlich viele Indizes n = nk sind, ist a Häufungswert von ( an). □ Wir können nun einen der wichtigsten Sätze der Analysis bewe isen. Der Satz von Bolzano-Weierstraß zeigt, dass jede beschränkte Folge in R eine konvergente Teilfolge besitzt. Er macht sichtbar , wie die Ord- nung und Vollständigkeit der reellen Zahlen zusammenwirke n, um aus unübersichtlichen Folgen geordnete Grenzwerte herauszufiltern. Damit bildet er eine zentrale G rundlage für viele spätere Existenzbeweise in der Analysis, insbesondere für Kompaktheits- und Extremwerts ätze.
```
- **Key idea:** This result packages a reusable fact from 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.4.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.4.4 — Satz von Bolzano-Weierstraß

- **Theorem name:** Satz 2.4.4 Satz von Bolzano-Weierstraß
- **Source:** PDF p47; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Proof strategy in one sentence:** Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.
- **Full proof rewritten clearly:**
  Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Vorbemerkung. Seien A \subset B beschränkte Teilmengen von R. Dann gilt inf B ≤ inf A ≤ sup A ≤ sup B. In der Tat: sup B ist eine obere Schranke für B, also auch für A, also sup A ≤ sup B, denn sup A ist die kleinste obere Schranke von A. Analog zeigt man, dass inf B ≤ inf A (Fig. 6). ABBILDUNG 6. Bolzano-Weierstrass inf B inf A sup A sup B A B x − 1 an1 x x1 = sup { a1, a2, . . . } x − 1 2 an2 x xn1+ 1 = sup { an1+ 1, an1+ 2, . . . } Betrachten wir nun die Mengen An := {ak : k ≥ n}. Die Folge ( an) ist beschränkt, also existiert M > 0, sodass für alle n \in N gilt | an| ≤ M. Es folgt, dass für alle n \in N auch An beschränkt ist, An \subset [− M, M]. Das Vollständigkeitsaxiom impliziert, dass xn := sup An, yn := inf An existieren. Da M eine obere Schranke für An ist, folgt xn ≤ M. Analog yn ≥ − M. Es ist An+ 1 \subset An, also nach der Vorbemerkung gilt: yn ≤ yn+ 1 ≤ xn+ 1 ≤ xn. Die Folge (xn) ist also monoton fallend und ( yn) ist monoton wachsend. Diese Folgen sind auch beschränkt. D as Monotonieprinzip impliziert, dass ( xn) und ( yn) konvergent sind. Es gilt: x := limn→\infty xn = inf{xn : n \in N}, y := limn→\infty yn = sup{yn : n \in N}. Wir zeigen, dass x ein Häufungswert der Folge ( an) ist. Wir definieren n1 < n2 < . . . wie folgt. Wegen x1 = sup{a1, a2, . . .} und x − 1 < x ≤ x1 existiert n1 derart, dass x − 1 < an1 ≤ x1 (Fig. 6). ANALYSIS I-III, 2011/2013 46 Wegen xn1+ 1 = sup{an1+ 1, an1+ 2, . . .} und x − 1 2 < x ≤ xn1+ 1 existiert n2 > n1 derart, dass x − 1 2 < an2 ≤ xn1+ 1 (Fig. 6). Wegen xn2+ 1 = sup{an2+ 1, an2+ 2, . . .} und und x − 1 3 < x ≤ xn2+ 1 existiert n3 > n2 derart, dass x − 1 3 < an3 ≤ xn2+ 1. Dann ist für alle k x − 1 k < ank ≤ xnk+ 1 Da xnk+ 1 → x für k → \infty , folgt aus dem Einschließungsprinzip, dass ank → x für k → \infty . □ Bemerk…
```
- **Key idea:** Bounded infinite data in the real line contains a convergent pattern.
- **Dependency list:** Completeness, monotone convergence, subsequences, accumulation values.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.
- **Active recall prompts:**
  1. State Satz 2.4.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.4.5 — 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium

- **Theorem name:** Satz 2.4.5 
- **Source:** PDF p48; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei a ein Häufungswert von ( an) und sei ( ank ) eine Teilfolge von ( an) mit ank → a für k → \infty . Dann gilt ank \in Ank für alle k \in N. Somit ist ynk = inf Ank ≤ ank ≤ sup Ank = xnk . Mit dem Vergleichsprinzip folgt h∗ = lim k→\infty ynk ≤ lim k→\infty ank ≤ lim k→\infty xnk = h∗ , also h∗ ≤ a ≤ h∗ . □
```
- **Key idea:** This result packages a reusable fact from 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.4.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.4.9 — Cauchy-Kriterium

- **Theorem name:** Satz 2.4.9 Cauchy-Kriterium
- **Source:** PDF p48; section 2.4. Der Satz von Bolzano-Weierstraß und das Cauchy-Kriterium
- **Proof strategy in one sentence:** Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.
- **Full proof rewritten clearly:**
  Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei ( an) eine Cauchy-Folge. Wir zeigen zunächst, dass ( an) beschränkt ist. Sei \varepsilon = 1. Es gibt n0 mit | an − am| < 1 für n, m ≥ n0. Wähle m = n0, dann folgt: n ≥ n0 ⇒ | an − an0 | ≤ 1 ⇒ | an| ≤ | an0 | + 1. ANALYSIS I-III, 2011/2013 47 Also ist max {| a1| ,| a2| , . . . ,| an0 | } + 1 eine Schranke für ( an). Nach Bolzano–Weierstraß hat ( an) einen Häufungs- wert a. Sei ( ank ) eine Teilfolge mit ank → a für k → \infty . Es bleibt zu zeigen, dass an → a für n → \infty . Sei \varepsilon > 0. Wähle N mit | am − an| < \varepsilon für n, m ≥ N. Wähle k mit nk ≥ N und | ank − a| < \varepsilon. Für m ≥ N ist dann | am − a| ≤ | am − ank |   < \varepsilon + | ank − a|   < \varepsilon < \varepsilon+ \varepsilon = 2\varepsilon. Somit an → a. □
```
- **Key idea:** In $\mathbb R$, terms becoming mutually close is enough to guarantee an actual limit.
- **Dependency list:** Completeness, boundedness, Bolzano-Weierstrass.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.
- **Active recall prompts:**
  1. State Satz 2.4.9 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.5.4 — 2.5. Uneigentliche Grenzwerte

- **Theorem name:** Satz 2.5.4 
- **Source:** PDF p50; section 2.5. Uneigentliche Grenzwerte
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir beweisen die Regel, die \infty + x = \infty entspricht, die anderen Beweise verlaufen ähnlich (übung! ). Es ist zu zeigen: limn→\infty an = \infty , limn→\infty bn = x \in R ⇒ limn→\infty (an + bn) = \infty Zum Beweis von lim n→\infty (an + bn) = \infty sei M \in R beliebig. Da die Folge ( bn) konvergiert, ist sie beschränkt, also existiert C \in R mit | bn| ≤ C, insbesondere bn ≥ − C für alle n. Vorüberlegung: Wir wollen an + bn > M und wissen bn ≥ − C. Welche Bedingung an an brauchen wir? Die Bedingung an > M + C genügt, da dann an + bn > (M + C) + (− C) = M. Wegen lim n→\infty an = \infty gibt es ein n0 \in N, so dass an > M + C für alle n ≥ n0. Für diese n gilt dann an + bn > M. Wir haben gezeigt, dass es für alle M \in R ein n0 \in N gibt mit an + bn > M für alle n ≥ n0. Das bedeutet limn→\infty (an + bn) = \infty . □ Als Beispiel betrachten wir den Grenzwert der rationalen Fu nktionen. Seien P(x),Q(x) Polynome, die nicht konstant gleich Null sind. Dann gilt: (2.9) lim n→\infty P(n) Q(n) =            0 falls grad P < gradQ, c d falls grad P = gradQ und c, d die Leitkoeffizienten von P bzw .Q sind. sgn ( c d ) · \infty falls grad P > gradQ und c, d die Leitkoeffizienten von P bzw .Q sind. ANALYSIS I-III, 2011/2013 49 Die ersten zwei Gleichungen haben wir in (2.9) bewiesen. Die dritte Gleichung behandeln wir ähllich. Die Stra- tegie ist, den dominanten Term im Zähler und Nenner identifizieren und ihn auszuklammern. D ie dominanten Terme in P(n), Q(n) sind nm bzw .nk. Wir klammern diese aus: P(n) Q(n) = nm ( cm + cm− 1n− 1 + . . .+ c0n− m) nk ( dk + dk− 1n− 1 + . . .+ d0n− k) = nm− k ·cm + cm− 1n− 1 + . . .+ c0n− m dk + dk− 1n− 1 + . . .+ d0n− k · Wegen m > k gilt nm− k → \infty und der Bruch konvergiert gengen cm dk . Es folgt nach Satz 2.5.4: limn→\i…
```
- **Key idea:** This result packages a reusable fact from 2.5. Uneigentliche Grenzwerte; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.5.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 2.6.3 — 2.6. Folgen komplexer Zahlen

- **Theorem name:** Satz 2.6.3 
- **Source:** PDF p52; section 2.6. Folgen komplexer Zahlen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Für z \in C gilt laut Satz 1.7.6 (iii) und (v): (2.10) max { | Re z| ,| Im z| } \le | z| \le | Re z| + | Im z| . ANALYSIS I-III, 2011/2013 51 Dies zeigt, dass für Folgen ( zn) in C dieAussage zn → 0 äquivalent zur Aussage Re zn → 0 und Im zn → 0 ist. Wendet man dies auf zn − z an, folgt die Behauptung. □
```
- **Key idea:** This result packages a reusable fact from 2.6. Folgen komplexer Zahlen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.6.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.6.4 — Rechenregeln

- **Theorem name:** Satz 2.6.4 Rechenregeln
- **Source:** PDF p53; section 2.6. Folgen komplexer Zahlen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Die Rechenregeln wurden mit Dreiecksungleichung und algeb raischen Umformungen bewiesen, bei- des gilt genauso in C. □
```
- **Key idea:** This result packages a reusable fact from 2.6. Folgen komplexer Zahlen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.6.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.6.6 — Cauchy-Kriterium in C

- **Theorem name:** Satz 2.6.6 Cauchy-Kriterium in C
- **Source:** PDF p53; section 2.6. Folgen komplexer Zahlen
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Mit den Abschätzungen (2.10) sieht man: Ist ( zn) eine Cauchy-Folge in C und zn = xn + i yn, so sind (xn) und ( yn) Cauchy-Folgen in R. Da R vollständig ist, existieren x = limn→\infty xn und y = limn→\infty yn. Dann folgt limn→\infty zn = limn→\infty (xn + i yn) = x + i y. □ Die Aussage von Satz 2.6.6 nennt man auch die Vollständigkei t der komplexen Zahlen.
```
- **Key idea:** This result packages a reusable fact from 2.6. Folgen komplexer Zahlen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 2.6.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 2.6.7 — Bolzano-Weierstraß in C

- **Theorem name:** Satz 2.6.7 Bolzano-Weierstraß in C
- **Source:** PDF p53; section 2.6. Folgen komplexer Zahlen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir betrachten die Folgen der Real- und Imaginärteile. Beze ichnet man deren Häufungspunkte mit x bzw .y, dann ist x + i y ein Häufungspunkt der Ausgangsfolge. □
```
- **Key idea:** This result packages a reusable fact from 2.6. Folgen komplexer Zahlen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Chapter 1 real-number foundations, absolute value, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 2.6.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.1.3 — Rechenregeln

- **Theorem name:** Satz 3.1.3 Rechenregeln
- **Source:** PDF p58; section 3.1. Definitionen und Beispiele
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sind sn und tn die Partialsummen der Reihen \sum n≥ 0 an, \sum n≥ 0 bn, so gilt n\sum k= 0 (\lambdaak + μ bk) = \lambda n\sum k= 0 ak + μ n\sum k= 0 bk = \lambdasn + μ tn \to \lambdaa + μ b . Analog beweist man die anderen Behauptungen. □ Vorsicht: Aus der Konvergenz von \sum n\ge1 an, \sum n\ge1 bn folgt nicht die Konvergenz von \sum n\ge1 anbn! Beispiel: Die Reihe \sum n\ge1 (− 1)n \sqrtn konvergiert nach Leibniz-Kriterium, aber \sum n\ge1 (− 1)n \sqrtn ·(− 1)n \sqrtn = \sum n\ge1 1 n divergiert. 3.2. Konvergenzkriterien. Wie kann man entscheiden, ob eine Reihe konvergiert? Dies is t vor allem deswe- gen eine wichtige Frage, weil wir oft Reihen verwenden werde n, um Zahlen oder Funktionen zu definieren, z. B. die Exponentialfunktion. Das ergibt jedoch nur Sinn, wenn d ie Reihen konvergieren. Im Folgenden werden wir einige Sätze kennenlernen, die es ermöglichen, ihr Konverg enzverhalten zu bestimmen. Wir haben zwei Sätze kennengelernt, mit denen sich die Konve rgenz einer Folge aus deren Eigenschaften folgern lässt: Satz 2.1.7 über die Konvergenz monotoner , be schränkter Folgen und Satz 2.4.9 über die Kon- vergenz von Cauchy-Folgen. Wenden wir diese auf die Partial summenfolge einer Reihe an, so erhalten wir die beiden folgenden Sätze.
```
- **Key idea:** This result packages a reusable fact from 3.1. Definitionen und Beispiele; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, Cauchy criteria, and comparison estimates.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 3.1.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.2.3 — Cauchy-Kriterium für Reihen

- **Theorem name:** Satz 3.2.3 Cauchy-Kriterium für Reihen
- **Source:** PDF p58; section 3.2. Konvergenzkriterien
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es ist sn − sm = am+ 1 + . . .+ an, also ist dies einfach das schon bekannte Cauchy-Kriterium für Folgen: (sn) konvergiert \Longleftrightarrow (sn) ist Cauchy-Folge. □
```
- **Key idea:** A series converges exactly when distant tail sums carry no mass.
- **Dependency list:** Cauchy criterion for sequences and partial sums.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 3.2.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.2.7 — Leibniz-Kriterium

- **Theorem name:** Satz 3.2.7 Leibniz-Kriterium
- **Source:** PDF p59; section 3.2. Konvergenzkriterien
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Aus an → 0 und an ≥ an+ 1 folgt zunächst an ≥ 0 für alle n \in N. Setze s2k = (a1 − a2) + (a3 − a4) + . . .+ (a2k− 1 − a2k), s2k+ 1 = a1 − (a2 − a3) − . . .− (a2k − a2k+ 1). Dann gilt s2k ≤ s2k+ 2, s2k+ 1 ≤ s2k− 1, 0 ≤ s2k ≤ s2k+ 1 ≤ a1. Die Folgen (s2k) und ( s2k+ 1) sind also monoton und beschränkt und daher konvergent, und wegen | s2k+ 1 − s2k| = a2k+ 1 → 0 haben sie den gleichen Limes s. Hieraus schließt man, dass sn := a1 − a2 + a3 − ... + (− 1)n− 1an → s gilt. □
```
- **Key idea:** This result packages a reusable fact from 3.2. Konvergenzkriterien; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, Cauchy criteria, and comparison estimates.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 3.2.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.3.6 — Cauchy-Produkt

- **Theorem name:** Satz 3.3.6 Cauchy-Produkt
- **Source:** PDF p60; section 3.3. Absolute Konvergenz
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Zum Beweis betrachten wir zunächst den Fall, dass beide Reih en nur nichtnegative Glieder besitzen. Die Teilsummen der vorkommenden Reihen seien bezeichnet mi t sn := n\sum k= 0 ak, , tn := n\sum k= 0 bk, un := n\sum k= 0 ck. Wir bilden nun das Produkt sn ·tn sowie das Produkt s2n ·t2n und wir zeigen: (3.5) sn ·tn ≤ u2n ≤ s2n ·t2n Es gilt sn tn = ( n\sum k= 0 ak )( n\sum l= 0 bl ) = \sum 0≤ k,l≤ n ak bl, s2n t2n = \sum 0≤ k,l≤ 2n ak bl . Weiter gilt u2n := 2n\sum j= 0 j\sum k= 0 ak b j− k = \sum k+ l≤ 2n k,l≥ 0 ak bl. Für die Indexmengen der Summen gilt { (k, l) : 0 ≤ k, l ≤ n } \subset { (k, l) : k + l ≤ 2n } \subset { (k, l) : 0 ≤ k, l ≤ 2n } . Wegen der Nichtnegativität der Terme folgt (3.5). Sei s = \infty\sum k= 0 ak, t = \infty\sum k= 0 bk. Aus (3.5) und aus dem Einschließungsprinzip folgt: limn→\infty u2n = s t. Da die Folge ( un) monoton wachsend ist, existiert auch lim n→\infty un und es gilt limn→\infty un = limn→\infty u2n = st. Für den Fall, dass beide Reihen nur nichtnegative Glieder be sitzen, ist damit unser Satz bewiesen. Hat nun eine der Reihen – etwa \sum\infty k= 0 ak – Glieder verschiedenen Vorzeichens, so können wir diese Re ihe als Differenz zweier absolut konvergenter Reihen mit nichtneg ativen Gliedern darstellen: ak = a+ k − a− k mit a+ k = ak + | ak| 2 , a− k = | ak| − ak 2 . ANALYSIS I-III, 2011/2013 59 Mit den Bezeichnungen c+ n = n\sum k= 0 a+ k bn− k, c− n = n\sum k= 0 a− k bn− k folgt nun aus den schon bewiesenen Gleichungen ( bk ≥ 0 wird vorausgesetzt ) \infty\sum k= 0 a+ k · \infty\sum k= 0 bk = \infty\sum n= 0 c+ n , \infty\sum k= 0 a− k · \infty\sum k= 0 bk = \infty\sum n= 0 c− n durch Summenbildung die Behauptung. Durch nochmalige Anwe ndung dieses Verfahrens kann man sich schließlich auch von der Voraussetzung bk ≥ 0 befreien. Betra…
```
- **Key idea:** This result packages a reusable fact from 3.3. Absolute Konvergenz; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, Cauchy criteria, and comparison estimates.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 3.3.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.3.8 — 3.3. Absolute Konvergenz

- **Theorem name:** Satz 3.3.8 
- **Source:** PDF p61; section 3.3. Absolute Konvergenz
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir wissen, dass exp(0) = 1 und exp(1) = e. • exp(− z) exp(z) = exp(z − z) = exp(0) = 1. Insbesondere gilt exp( z) ̸= 0 und exp(z)− 1 = 1 exp(z) = exp(− z). • Für m \in N gilt exp(mz) = exp(z)m, exp(− mz) = exp(z)− m. Damit folgt für n \in Z: exp(nz) = exp(z)n. • Für q \in N gilt e = exp(1) = exp ( q q ) = exp ( 1 q )q , also exp ( 1 q ) = e1/q. • Für p \in Z, q \in N folgt exp ( p q ) = exp ( 1 q )p = e p/q. Dies inspiriert zur folgenden Definition der Potenz mit beli ebigem komplexem Exponenten. ANALYSIS I-III, 2011/2013 60
```
- **Key idea:** This result packages a reusable fact from 3.3. Absolute Konvergenz; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, Cauchy criteria, and comparison estimates.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 3.3.8 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.4.2 — Abelsches Konvergenzlemma

- **Theorem name:** Lemma 3.4.2 Abelsches Konvergenzlemma
- **Source:** PDF p62; section 3.4. Potenzreihen
- **Proof strategy in one sentence:** Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.
- **Full proof rewritten clearly:**
  Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es gilt | an zn| = ⏐ ⏐ ⏐ansn (z s )n⏐ ⏐ ⏐ ≤ M ⏐ ⏐ ⏐ z s ⏐ ⏐ ⏐ n . Für | z| < s ist ⏐ ⏐ z s ⏐ ⏐ < 1, also konvergiert die Reihe \infty\sum n= 0 M ⏐ ⏐ ⏐ z s ⏐ ⏐ ⏐ n , und daraus folgt die absolute Konvergenz der Reihe \infty\sum n= 0 an zn mit Hilfe des Majorantenkriteriums. □
```
- **Key idea:** A power series that is controlled at one radius is dominated inside that radius by a geometric series.
- **Dependency list:** Majorant criterion and geometric series.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.
- **Active recall prompts:**
  1. State Lemma 3.4.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.4.4 — Konvergenzradius

- **Theorem name:** Satz 3.4.4 Konvergenzradius
- **Source:** PDF p62; section 3.4. Potenzreihen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(i) Sei | z| < R. Dann existiert z0 mit | z| < z0 < R. Nach Definition von R konvergiert die Reihe für z0. Verwende nun das Abelsches Konvergenzlemma 3.4.2. (ii) Sei | z| > R. Angenommen, \sum\infty n= 0 an zn konvergiert. Dann folgt nach Lemma 3.4.2, dass \sum\infty n= 0 anwn für alle w mit | w| < | z| absolut konvergent ist. Wählt man ein w mit R < w < | z| , so ergibt sich ein Widerspruch zur Definition von R. □
```
- **Key idea:** Power series have circular domains of guaranteed convergence.
- **Dependency list:** Abel lemma, supremum, absolute convergence.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 3.4.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 3.4.7 — Eulersche Formel

- **Theorem name:** Satz 3.4.7 Eulersche Formel
- **Source:** PDF p63; section 3.4. Potenzreihen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Für die Patialsummen der Reihe eiz = \infty\sum k= 0 (iz )k k! gilt wegen i2l = (− 1)l, i2l+ 1 = i(− 1)l: 2n+ 1\sum k= 0 (iz )k k! = n\sum l= 0 (iz )2l (2l)! + n\sum l= 0 (iz )2l+ 1 (2l + 1)! = n\sum l= 0 (− 1)l (2l)! z2l + i n\sum l= 0 (− 1)l (2l + 1)! (iz )2l+ 1 Durch Limesübergang gilt eiz = \infty\sum k= 0 (iz )k k! = limn→\infty n\sum l= 0 (− 1)l (2l)! z2l + i limn→\infty n\sum l= 0 (− 1)l (2l + 1)! (iz )2l+ 1 = \infty\sum l= 0 (− 1)l (2l)! z2l + i \infty\sum l= 0 (− 1)l (2l + 1)! (iz )2l+ 1 = cos z + i sin z □ Die Cosinus-Funktion ist gerade d. h. cos(− z) = cos z und ie Sinus-Funktion ist ungerade d. h. sin(− z) = − sin z. So gilt cos z − i sin z = e− iz . Durch Addition mit (3.10) und Subtraktion aus (3.10) folge n weiteren Eulerschen Formeln: cos z = 1 2 (eiz + e− iz ) , sin z = 1 2i (eiz − e− iz ) . Für x \in R gilt cos x \in R und sin x \in R, wegen der Reihendefinition von Cosinus und Sinus. Es gilt al so mit der Eulersche Formel: (3.11) eix = cos x + i sin x, cos x = Re eix , sin x = Im eix , für x \in R. Da cos z und sin z für nicht-reelles z auch nicht-reelle Werte annehmen, ist i.A. cos z nicht notwendig der Realteil von eiz , obwohl die Eulersche Formel (3.11) gilt. Bemerkung (Geometrische Bedeutung von Sinus und Cosinus ). In der Schule werden die trigonometrischen Funktionen mit Hilfe eines rechtwinkligen Dreiecks eingef ührt, siehe Abbildung 7. Aus dem Strahlensatz folgt, dass die Seitenverhältnisse a c und b c nur vom Winkel α, nicht aber von der Größe des Dreiecks abhängen, und man definiert sin α = a c , cos α = b c . Dabei muss der Winkel α zwischen 0 und 90 ◦ liegen. Die Seite (der Länge) a heißt Gegenkathete des Winkels α b a c ABBILDUNG 7. Rechtwinkliges Dreieck ANALYSIS I-III, 2011/2013 62 α, die Seite b Ankathete, die Seite c Hypothenuse. W…
```
- **Key idea:** This result packages a reusable fact from 3.4. Potenzreihen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, Cauchy criteria, and comparison estimates.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 3.4.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 4.1.2 — Rechenregeln

- **Theorem name:** Satz 4.1.2 Rechenregeln
- **Source:** PDF p68; section 4.1. Stetige Funktionen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei ( zn)n\inN eine Folge in D mit lim n→\infty zn = z0. Die Stetigkeit von f und g in x0 bedeutet Die Stetig- keit von f und g in x0 bedeutet limn→\infty f (zn) = f (z0) und lim n→\infty g(zn) = g(z0), und mit den Grenzwertregeln (Satz 2.2.2) folgt lim n→\infty ( f (zn) + g(xz n) ) = f (z0) + g(z0). Also ist f + g stetig. Die Stetigkeit von f ·g folgt analog. Zu (ii): Wir zeigen, dass ein δ > 0 existiert, so dass für alle z \in D mit | z − z0| < δ gilt g(z) ̸= 0. Angenommen, das ist nicht wahr . Dann für alle δ > 0 existiert zδ \in D mit | zδ − z0| < δ und g(zδ) = 0. Wende dies an auf δ = 1 n , n \in N. | zn − z0| < 1 n , also lim n→\infty zn = z0. Wegen der Stetigkeit von g gilt lim n→\infty g(zn) = g(z0). Weil g(zn) = 0 für alle n \in N folgt g(z0) = 0, Widerspruch. Die Stetigkeit von f g folgt nun aus den Grenzwertregeln (Satz 2.2.2 (iii)). □ ANALYSIS I-III, 2011/2013 67 Beispiele: (i) Polynome C ∋ z \mapstoan zn + an− 1 zn− 1 + . . .+ a1 z + a0 \in C sind stetig. Denn beginnend mit f (z) = z und den Konstanten kann man jedes Polynom durch wiederholtes Multi plizieren und Addieren erhalten. (ii) Rationale Funktionen D ∋ z \mapstoP(z) Q(z) \in C mit Polynomen P und Q sind stetig auf D = {z \in C : Q(z) ̸= 0}. 15.12.25
```
- **Key idea:** This result packages a reusable fact from 4.1. Stetige Funktionen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, limits, intervals, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 4.1.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.1.3 — Kompositionsregel

- **Theorem name:** Satz 4.1.3 Kompositionsregel
- **Source:** PDF p69; section 4.1. Stetige Funktionen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Zu zeigen: Für jede Folge ( xn)n\inN in D gilt: xn → x0 \Rightarrow (g ◦ f )(xn) → (g ◦ f )(x0). Sei also ( xn) eine beliebige Folge mit xn → x0. Da f stetig in x0 ist, folgt f (xn) → f (x0). Da g stetig in f (x0) ist, folgt weiter g( f (xn)) → g( f (x0)). □ Beispiel: Ist f : D \to C stetig, so sind | f | , f ,Re f ,Im f : D \to C stetig.
```
- **Key idea:** This result packages a reusable fact from 4.1. Stetige Funktionen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, limits, intervals, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 4.1.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.1.4 — Stetigkeit der Umkehrfunktion

- **Theorem name:** Satz 4.1.4 Stetigkeit der Umkehrfunktion
- **Source:** PDF p69; section 4.1. Stetige Funktionen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es gilt nach Definition der Umkehrfunktion y = f (x) \Longleftrightarrow x = g(y) für x \in [a, b], y \in E. Sei y0 \in E und yn → y0, n → \infty , yn \in E. Sei xn = g(yn) \in [a, b], also f (xn) = yn. Nach dem Satz von Bolzano-Weierstass 2.4.4 existiert L = lim supxn \in [a, b] und eine Teilfolge xnk → L, k → \infty . Da f stetig in L ist, gilt ynk = f (xnk ) → f (L), k → \infty . Wegen ynk → y0, k → \infty folgt, dass y0 = f (L) und deshalb L = g(y0). Analog zeigt man, dass für l = lim infxn \in [a, b] gilt l = g(y0). Insgesamt lim inf xn = lim supxn = g(y0) und somit g(yn) → g(y0), n → \infty . □ Eine Version des Satzes 4.1.4 nur für die Stetigkeit in einem Punkt findet man in Übung 4.5.6.
```
- **Key idea:** This result packages a reusable fact from 4.1. Stetige Funktionen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, limits, intervals, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 4.1.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.1.5 — \varepsilon-δ-Kriterium für Stetigkeit

- **Theorem name:** Satz 4.1.5 \varepsilon-δ-Kriterium für Stetigkeit
- **Source:** PDF p69; section 4.1. Stetige Funktionen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir müssen die Äquivalenz der folgenden beiden Aussagen nac hweisen: (i) Für jede Folge ( xn)n\inN \subset D mit lim n→\infty xn = x0 gilt lim n→\infty f (xn) = f (x0). (ii) Für alle \varepsilon > 0 existiert ein δ > 0, so dass für alle x \in D mit | x − x0| < δ gilt: | f (x) − f (x0)| < \varepsilon. (ii) ⇒ (i): Sei \varepsilon > 0 und sei ( xn)n\inN \subset D mit lim n→\infty xn = x0. Wähle δ > 0 wie in (ii). Dann existiert ein n0 \in N, so dass für alle n ≥ n0 gilt | xn − x0| < δ. Nach (ii) folgt damit für alle n ≥ n0: | f (xn) − f (x0)| < \varepsilon. Also gilt limn→\infty f (xn) = f (x0). ANALYSIS I-III, 2011/2013 68 (i) ⇒ (ii): Wir führen einen indirekten Beweis. Angenommen, (ii) gilt n icht. Dann existiert ein \varepsilon > 0, so dass für alle δ > 0 ein x \in D existiert mit | x − x0| < δ und f (x) − f (x0)| ≥ \varepsilon. Wende dies auf δ = 1 n , n \in N, an und bezeichne das entsprechende Element mit xn. Dann gilt | xn − x0| < 1 n , alsolimn→\infty xn = x0, aber zugleich | f (xn) − f (x0)| ≥ \varepsilon für alle n \in N. Damit folgt lim n→\infty f (xn) ̸= f (x0), im Widerspruch zu (i). Also gilt (ii). □
```
- **Key idea:** This result packages a reusable fact from 4.1. Stetige Funktionen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, limits, intervals, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 4.1.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.2.1 — Zwischenwertsatz

- **Theorem name:** Satz 4.2.1 Zwischenwertsatz
- **Source:** PDF p70; section 4.2. Der Zwischenwertsatz
- **Proof strategy in one sentence:** Use a supremum/nested interval argument on the set where the function lies below the target.
- **Full proof rewritten clearly:**
  Use a supremum/nested interval argument on the set where the function lies below the target.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** A continuous graph cannot jump over intermediate heights.
- **Dependency list:** Continuity, intervals, completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use a supremum/nested interval argument on the set where the function lies below the target.
- **Active recall prompts:**
  1. State Satz 4.2.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.2.3 — 4.2. Der Zwischenwertsatz

- **Theorem name:** Satz 4.2.3 
- **Source:** PDF p70; section 4.2. Der Zwischenwertsatz
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir nehmen an, dass f injektiv ist, aber weder streng monoton wachsend noch stren g monoton fal- lend. Wenn f nicht streng monoton fallend ist, gibt es x1, x2 \in I mit x1 < x2 und f (x1) ≤ f (x2). Weil f injektiv ist, gilt dann auch rechts eine echte Ungleichung, also x1 < x2 und f (x1) − f (x2) < 0. Wenn f nicht streng monoton ANALYSIS I-III, 2011/2013 69 fallend ist, gibt es ebenso y1, y2 \in I mit y1 < y2 und f (y1)? f (y2) > 0. Betrachte die Funktion g : [0,1] → R mit g(t) := f ((1 − t)x1 + ty1) − f ((1 − t)x2 + ty2). Diese Funktion ist als Komposition stetiger Funktionen s tetig auf dem Intervall [0 ,1]. Weiter ist g(0) = f (x1) − f (x2) < 0, g(1) = f (y1) − f (y1) > 0. Also gibt es nach dem Zwischen- wertsatz ein t \in (0,1) mit g(t) = 0, also mit f ((1 − t)x1 + ty1) = f ((1 − t)y2 + ty2). Aber nach den Rechenregeln für Ungleichungen gilt (1 − t)x2 + ty1 < (1 − t)x2 + ty2. Das ist ein Widerspruch zur Injektivität von f . Zur Stetigkeit von f − 1: Sei y0 \in f (I) = J. Nehmen wir an, dass y0 im Innneren des Intervalls J liegt, d. h. es gibt c, d \in J mit y0 \in (c, d) \subset J. Seien a, b \in I mit f (a) = c, f (b) = d. Sei I0 das kompakte Intervall mit Endpunkten a, b. Dann gilt f (I0) = [c, d] und f | I0 : I0 → [c, d] is bijektiv und stetig. Der Satz 4.1.4 besagt, dass die Umkerfunktion ( f | I0 )− 1 = f − 1| [c,d] ist stetig. Daraus folgt, dass f − 1 stetig in y0 ist, da y0 \in (c, d). Falls y0 ein Endpunkt von J ist, argumentiert man analog. □ Der Zwichenwersatz erlaubt eine vollständige Beschreibun g der reellen Exponentialfunktion exp : R \to R (lie- fert nämlich die Bildmenge) und dies führt wiederum zur Defin ition des Logarithmus. Diese Definition des Logarithmus als Umkehrung des Exponentialfunktion findet s ich erstmals in Eulers Buch [8]. 4.2.4. Def…
```
- **Key idea:** This result packages a reusable fact from 4.2. Der Zwischenwertsatz; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, limits, intervals, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 4.2.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.3.2 — Satz vom Maximum und Minimum

- **Theorem name:** Folgerung 4.3.2 Satz vom Maximum und Minimum
- **Source:** PDF p72; section 4.3. Satz vom Maximum und Minimum
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** A continuous function on a closed bounded interval cannot escape and must reach its extremes.
- **Dependency list:** Continuity, Bolzano-Weierstrass/compact interval behavior.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Folgerung 4.3.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.4.3 — 4.4. Grenzwerte von Funktionen

- **Theorem name:** Satz 4.4.3 
- **Source:** PDF p75; section 4.4. Grenzwerte von Funktionen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Der Beweis erfolgt analog zum Beweis von Satz 4.1.5. Wir illustrieren den Satz in einigen speziellen Fällen. Für x0, a \in R erhalten wir das \varepsilon− δ–Kriterium für Grenz- werte. Sei x0 \in R Häufungspunkt von D \subset R, f : D → R und a \in R. Dann sind äquivalent: (i) limx→ x0 f (x) = a. (ii) Für alle \varepsilon > 0 gibt es ein δ > 0, so dass für alle x \in D \ {x0} gilt: | x − x0| < δ ⇒ | f (x) − a| < \varepsilon. In der Tat, Bedingung (ii) kann man auch wie folgt schreiben: \forall \varepsilon > 0 \existsδ > 0 \forall x \in D \ {x0}: x \in (x0 − δ, x0 + δ) ⇒ f (x) \in (a − \varepsilon, a + \varepsilon). Für x0 \in R, a = \infty : limx→ x0 f (x) = \infty \Longleftrightarrow Für alle C \in R gibt es ein δ > 0, so dass für alle x \in D \{x0} gilt: | x− x0| < δ ⇒ f (x) > C. Die enge Beziehung des Grenzwetz-Begrifffs zur Stetigkeit kann wie folgt formuliert werden:
```
- **Key idea:** This result packages a reusable fact from 4.4. Grenzwerte von Funktionen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, limits, intervals, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 4.4.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 4.4.6 — 4.4. Grenzwerte von Funktionen

- **Theorem name:** Satz 4.4.6 
- **Source:** PDF p76; section 4.4. Grenzwerte von Funktionen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Übung. Dies ist insbesondere bei stückweise definierten Funktione n nützlich.
```
- **Key idea:** This result packages a reusable fact from 4.4. Grenzwerte von Funktionen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, limits, intervals, and completeness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 4.4.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.1.2 — 5.1. Definition und erste Eigenschaften

- **Theorem name:** Satz 5.1.2 
- **Source:** PDF p80; section 5.1. Definition und erste Eigenschaften
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es sei f : D → R eine Funktion und x0 \in D. Satz 4.4.4 besagt, dass die Funktion f im Punkt x0 stetig ist, genau dann, wenn lim x→ x0 f (x) = f (x0). Wenn f im Punkt x0 differenzierbar ist, dann gilt limx→ x0 ( f (x) − f (x0)) = limx→ x0 ( f (x) − f (x0) x − x0 ·(x − x0) ) = limx→ x0 f (x) − f (x0) x − x0   = f ′(x0) ·limx→ x0 (x − x0)    = 0 weil beide Grenzwerte existieren = f ′(x0) ·0 = 0. □ Die Umkehrung ist falsch. Die Funktion f : R \to R, f (x) = | x| liefert ein Gegenbeispiel; sie ist stetig in 0, aber nicht differentierbar . Man kann aber sagen, dass f einseitig differenzierbar ist, siehe dazu die Notizen §5.6 . Es gibt Funktionen, die auf ganz R stetig, aber nirgends differenzierbar sind! Siehe [13, § 9. 11]. 5.2. Ableitungsregeln.
```
- **Key idea:** This result packages a reusable fact from 5.1. Definition und erste Eigenschaften; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.1.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.2.1 — Ableitungsregeln

- **Theorem name:** Satz 5.2.1 Ableitungsregeln
- **Source:** PDF p81; section 5.2. Ableitungsregeln
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es folgt leicht aus den Definitionen, dass die erste Eigensch aft gilt. Wir beweisen nun die Produkt- regel. Es ist ( f ·g)′(x) = limx→ x0 1 h ( f (x)g(x) − f (x0)g(x0)) Wir wollen jetzt in den Ausdruck f (x)g(x) − f (x)g(x) die Differenzen f (x) − f (x0) und g(x) − g(x0) einführen, welche in den Definitionen von f ′(x0) und g′(x0) auftauchen. Wir wenden jetzt genau den gleichen Trick wie im Beweis von Satz 2.2.2 an. = limx→ x0 1 h ( f (x)g(x)− f (x0)g(x) + f (x0)g(x) − f (x0)g(x0) ) = limx→ x0 1 h ( f (x)g(x) − f (x0)g(x) ) + limx→ x0 1 h ( f (x0)g(x) − f (x0)g(x0) ) = limx→ x0 1 x− x0 ( f (x) − f (x0) )    = f ′(x0) · limx→ x0 g(x)    = g(x),weil g stetig + f (x0) ·limx→ x0 1 x− x0 ( g(x) − g(x) )    = g′(x0) = f ′(x0)g(x0) + f (x0)g′(x0). Wir wenden uns nun dem Beweis der Quotientenregel zu. Diese w ird ganz ähnlich bewiesen wie die Produkt- regel. In der Tat, es ist limx→ x0 1 x − x0 ( f (x) g(x) − f (x0) g(x0) ) = limx→ x0 1 g(x)g(x0) f (x)g(x0) − f (x0)g(x) x − x0 = limx→ x0 1 g(x)g(x0) f (x)g(x0)− f (x0)g(x0) + f (x0)g(x0) − f (x0)g(x) x − x0 = limx→ x0 1 g(x)g(x0) ( f (x) − f (x) x − x0 g(x) − g(x) − g(x0) x − x0 f (x) ) = 1 g(x0)2 ( f ′(x0)g(x0) − g′(x0) f (x0)). □
```
- **Key idea:** This result packages a reusable fact from 5.2. Ableitungsregeln; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 5.2.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.2.3 — Lineare Approximation

- **Theorem name:** Satz 5.2.3 Lineare Approximation
- **Source:** PDF p82; section 5.2. Ableitungsregeln
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(i)⇒ (ii)) Setze \lambda := f ′(x0) und ρ(x) := f (x) − f (x0) − \lambda (x − x0). Dann ist ρ(x0) = 0, und limx→ x0 ρ(x) x − x0 = limx→ x0 ( f (x) − f (x0) x − x0 − \lambda ) = 0. (ii)⇒ (iii) Setze r(x) :=      \lambda + ρ(x) x − x0 , x ̸= x0, \lambda, x = x0. Dann gilt limx→ x0 r(x) = \lambda = r(x0), also ist r in x0 stetig. Ausserdem: f (x0) + r(x) (x − x0) = f (x0) + \lambda(x − x0) + ρ(x) = f (x). (iii)⇒ (i) limx→ x0 f (x) − f (x0) x − x0 = limx→ x0 r(x) = r(x0). also f ist differenzierbar in x0. □ Der Satz sagt insbesondere: • Unter allen linearen Funktionen approximiert T(x) = f (x0) + f ′(x0)(x − x0) die Funktion f nahe x0 am besten (falls f ′(x0) existiert). • Differenzierbarkeit von f mit Ableitung f ′(x0) ist äquivalent zu f (x0 + h) − f (x0) − f ′(x0)h h → 0, h → 0. • Die Gleichung in (ii) drückt quantitativ aus, dass der Graph von T tangential an den Graphen von f in ( x0, f (x0)) ist.
```
- **Key idea:** This result packages a reusable fact from 5.2. Ableitungsregeln; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.2.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 5.2.4 — Kettenregel

- **Theorem name:** Satz 5.2.4 Kettenregel
- **Source:** PDF p82; section 5.2. Ableitungsregeln
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Nach Satz 5.2.3 gibt es Funktionen r : I → R und s: J → R, die in x0 bzw .y0 = f (x0) stetig sind, mit r(x0) = f ′(x0), s(y0) = g′(y0), und f (x) = f (x0) + r(x) (x − x0), g(y) = g(y0) + s(y) (y − y0). Setze t(x) := s( f (x)) ·r(x) für x \in I. ANALYSIS I-III, 2011/2013 81 Dann ist t stetig in x0 (denn f ist stetig in x0 und s ist stetig in y0, also mit der Kompositionsregel Satz 4.1.3 für stetige Funktionen ist x → s( f (x)) stetig in x0). Wir ersetzen y = f (x) in der Formel für g und erhalten g( f (x)) = g( f (x0)) + s( f (x)) (f (x) − f (x0)) = g( f (x0)) + s( f (x)) r(x) (x − x0) = g( f (x0)) + t(x) (x − x0). Nach Satz 5.2.3 ist also g ◦ f in x0 differenzierbar , und (g ◦ f )′(x0) = t(x0) = s( f (x0)) r(x0) = g′( f (x0)) ·f ′(x0). Beispiele. (1) Sei f sei differenzierbar in x0. Dann ist auch e f differenzierbar in x0 und ( e f )′(x0) = e f (x0) f ′(x0), kurz (e f )′= e f f ′ wenn f differenzierbar ist. (2) Ist f differenzierbar und n \in N, so gilt ( f n)′= n f n− 1 f ′ (3) Sei a > 0 fest, f : R \to R+ , f (x) = ax := ex log a (Definition 4.2.5). Dann ist f = g ◦ h, wobei h : R \to R, h(x) = x log a, g : R \to R+ , g(y) = e y. Es gilt h′(x) = x′log a + x(log a)′ = log a, g′(y) = e y. Nach Kettenregel folgt (ax)′= ex log a ·(x log a)′= ax log a. (ax)′= ax log a, x \in R , a > 0 Insbesondere: lim x→ 0 ax − 1 x = log a. 20.01.26
```
- **Key idea:** Rates multiply through composition.
- **Dependency list:** Derivative definition and linear approximation.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 5.2.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.2.5 — Differenzierbarkeit der Umkehrfunktion

- **Theorem name:** Satz 5.2.5 Differenzierbarkeit der Umkehrfunktion
- **Source:** PDF p83; section 5.2. Ableitungsregeln
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Es folgt aus Satz 4.2.3, dass g : J → I stetig ist. Für y \in J schreibe x = f − 1(y), also y = f (x). Nach Satz 5.2.3 gibt es eine Funktion r : I → R, stetig in x0, mit f (x) = f (x0) + r(x) (x − x0) für x \in I. Da f streng monoton ist, gilt r(x) ̸= 0 für alle x ̸= x0, und r(x0) = f ′(x0) ̸= 0. Setze y0 := f (x0) und g := f − 1. Definiere s : g(I) → I, s(y) := 1 r(g(y)) . Da 1/r stetig in x0 ist, folgt dass s stetig in y0 ist. Es gilt y = y0 + r(g(y)) (g(y) − x0), also g(y) = x0 + y − y0 r(g(y)) = g(y0) + s(y) (y − y0). Nach Satz 5.2.3 ist g in y0 differenzierbar , und g′(y0) = s(y0) = 1 f ′(g(y0)) · □ Bemerkung. (1) Die anschauliche Bedeutung der Umkehrregel wird in Abbi ldung 10 skizziert. Wir erhalten den Graphen von f − 1, indem wir den Graphen von f an der x y-Diagonale spiegeln. Ganz analog erhalten wir die Tangente zum Graphen von f − 1 am Punkt ( f (x0), f − 1( f (x0)) = ( f (x0), x0), indem wir die Tangente zum Graphen von f am Punkt ( x0, f (x0)) an der x y-Diagonale spiegeln. Ganz allgemein gilt jedoch, dass wenn wir eine Gerade mit Steigung m an der x y-Diagonale spiegeln, erhalten wir eine Gerade mit Steigung 1 m . (2) Die Formel für ( f − 1)′ lässt sich auch aus der Kettenregel herleiten: Aus f − 1( f (x)) = x für alle x folgt durch Ableiten ( f − 1)′( f (x0) ) ·f ′(x0) = 1 und damit die Bedingung f ′(x0) ̸= 0 und die Formel. Doch beweist dies nur eine Hälfte des Satzes , da wir für die Anwendung der Kettenregel die Differenzierbarkeit von f − 1 voraussetzen mussten. ANALYSIS I-III, 2011/2013 82 Tangente zum Graphen der Funktion f am Punkt ( x0, f (x0)) mit Steigung f ′(x0) Tangente zum Graphen der Funktion f − 1 am Punkt ( f (x0), f − 1( f (x0)) mit Steigung 1 f ′(x0) Graph der Umkehrfunktion f − 1 Graph der Funktion f ( f (x0), x0) = ( f (x0), f − 1(…
```
- **Key idea:** This result packages a reusable fact from 5.2. Ableitungsregeln; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.2.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.3.3 — Notwendiges Extremwertkriterium; Fermat, um 1638

- **Theorem name:** Satz 5.3.3 Notwendiges Extremwertkriterium; Fermat, um 1638
- **Source:** PDF p84; section 5.3. Mittelwertsätze
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Angenommen, f hat in x0 ein lokales Minimum. (Der andere Fall kann analog gezeigt we rden.) Da x0 innerer Punkt von I ist, können wir also δ > 0 wählen, so dass ( x0 − δ, x0 + δ) \subset I und f (x) ≥ f (x0) für alle x \in (x0 − δ, x0 + δ) gilt. Dann folgt: (a) f (x) − f (x0) x − x0 ≥ 0, falls x0 < x < x0 + δ. (b) f (x) − f (x0) x − x0 ≤ 0, falls x0 − δ < x < x0. Da f ′(x0) = limx→ x0 f (x) − f (x0) x − x0 existiert, muss dieser Grenzwert gleich dem linksseitigen und gleich dem rechtsseitigen Grenzwert sein: f ′(x0) = limx→ x0 f (x) − f (x0) x − x0 = limx→ x0− f (x) − f (x0) x − x0 = limx→ x0+ f (x) − f (x0) x − x0 Aus (a) folgt: Der rechtsseitige Grenzwert ist ≥ 0, also f ′(x0) ≥ 0. Aus (b) folgt: Der linksseitige Grenzwert ist ≤ 0, also f ′(x0) ≤ 0. Insgesamt muss also f ′(x0) = 0 gelten. □ Bemerkung. (i) Geometrische Interpretation: Die Tangente an den Graph en in einem inneren Extremum ist parallel zur x-Achse. /Bullet/Circle /Bullet/Circle /Bullet/Circle zwei lokale Extrema Sattelpunkt (ii) Wenn x0 kein innerer Punkt ist, so ist die Aussage i.A. falsch; Beisp iel: f : [0,1] \to R, f (x) = x, x0 = 0; dann ist x0 ein Minimum, f differenzierbar in x0, aber f ′(x0) = 1. (iii) Die Umkehrung von Satz 5.3.3 ist falsch; Beispiel: f : R \to R, f (x) = x3. Dann ist x0 = 0 ein kritischer Punkt ( f ′(0) = 3 ·02 = 0), aber kein lokales Extremum, sondern einen Sattelpunkt. ANALYSIS I-III, 2011/2013 84 Beispiele. Als Anwendung des Satzes 5.3.3 betrachten wir das folgende B eispiel. Sei f : R → R, f (x) = (x2 − 1)2. Wir suchen die Extremstellen von f . Dafür suchen wir die kritischen Punkte. Sie sind die Nullst ellen von f ′(x), d. h. die Lösungen der Gleichung 4 x(x2 − 1) = 0, also die Stellen x1 = − 1, x2 = 0, x3 = 1. Wegen f (1) = f (− 1) = 0 und f (x) ≥ 0 für alle x \in R sin…
```
- **Key idea:** This result packages a reusable fact from 5.3. Mittelwertsätze; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 5.3.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.3.4 — Rolle, um 1691

- **Theorem name:** Satz 5.3.4 Rolle, um 1691
- **Source:** PDF p86; section 5.3. Mittelwertsätze
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Der Fall, dass f konstant ist, ist trivial. Wenn f nicht konstant ist, gibt es ein x0 \in (a, b) mit f (x0) ̸= f (a). Es gelte zunächst f (x0) > f (a). Nach dem Satz vom Maximum hat f ein Maximum \xi \in [a, b]. Dann muss \xi innerer Punkt von [ a, b] sein, denn f (\xi) ≥ f (x0) > f (a) = f (b), woraus \xi ̸= a und \xi ̸= b folgt. Somit folgt mit Satz 5.3.3: f ′(\xi) = 0. Falls f (x0) < f (a) ist, argumentiert man analog mit dem Minimum. □ /Bullet/Circle a /Bullet/Circle /Bullet/Circle b /Bullet/Circle/Bullet/Circlef (a) = f (b) /Bullet/Circle \xi1 (\xi1,f (\xi1)) /Bullet/Circle /Bullet/Circle /Bullet/Circle \xi2 (\xi2,f (\xi2)) /Bullet/Circle Geometrische Interpretation: Es gibt innere Punkte \xi\in (a, b), so dass die Tangente in ( \xi, f (\xi)) parallel zur x-Achse ist.
```
- **Key idea:** This result packages a reusable fact from 5.3. Mittelwertsätze; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.3.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.3.5 — Mittelwertsatz

- **Theorem name:** Satz 5.3.5 Mittelwertsatz; Lagrange, um 1797
- **Source:** PDF p86; section 5.3. Mittelwertsätze
- **Proof strategy in one sentence:** Subtract the secant line and apply Rolle's theorem.
- **Full proof rewritten clearly:**
  Subtract the secant line and apply Rolle's theorem.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir wollen von f eine lineare Funktion abziehen und dann Satz 5.3.4 von Rolle anwenden. Setze also h(x) = f (x) − mx mit m \in R. Für welches m gilt h(a) = h(b)? Wir wollen f (a) − ma = f (b) − mb, und daraus folgt m = f (b)− f (a) b− a . Setze h(x) = f (x) − f (b) − f (a) b − a x. h ist stetig auf [ a, b], differenzierbar auf ( a, b) und es ist h(a) = h(b). Damit erfüllt h die Bedingungen von Satz 5.3.4 von Rolle, also gibt es \xi\in (a, b) mit h′(\xi) = 0. Nun liefert 0 = h′(\xi) = f ′(\xi) − f (b) − f (a) b − a genau die gesuchte Formel. □ Bemerkung. Der Mittelwertsatz hat die folgende geometrische Interpre tation. Die Gleichung der Sekante durch ( a, f (a)), ( b, f (b)) ist y − f (a) = f (b)− f (a) b− a ·(x − a), und die Gleichung der Tangente an Graph( f ) in ( \xi, f (\xi)) ist y − f (\xi) = f ′(\xi)(x − \xi). Die beiden Geraden haben dieselbe Steigung f ′(\xi) = f (b)− f (a) b− a , sind also parallel. Also: Jede Sehnensteigung ist Tangentensteigung in einem g eeigneten Zwischenpunkt. ANALYSIS I-III, 2011/2013 85 /Bullet/Circle /Bullet/Circle /Bullet/Circle/Bullet/Circle /Bullet/Circle /Bullet/Circle (\xi2,f (\xi2)) (\xi1,f (\xi1)) /Bullet/Circle (a,f (a)) /Bullet/Circle (b,f (b)) a \xi1 \xi2 b Die Tangenten in den Punkten ( \xi1, f (\xi1)), (\xi2, f (\xi2)) sind parallel zur Sekante durch ( a, f (a)) und ( b, f (b)) (2) Wieso betrachtet man im Mittelwertsatz Funktionen, die nur auf ( a, b) differenzierbar sind? Der Grund ist, dass wir Funktionen wie f : [0,1] → R, f (x) = \sqrtx nicht ausschließen möchten ( f ist in 0 nicht differenzierbar). 5.4. Anwendungen des Mittelwertsatzes. Der Mittelwertsatz hat viele Anwendungen: Er ist die Brücke zwischen Ableitungsinformationen und Informationen über die Funktion selbst. Die wichtigsten sind: der Ein- deutigkeitssatz d…
```
- **Key idea:** Some instantaneous slope equals the average slope.
- **Dependency list:** Rolle's theorem, extrema theorem, differentiability.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Subtract the secant line and apply Rolle's theorem.
- **Active recall prompts:**
  1. State Satz 5.3.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.4.1 — Eindeutigkeitssatz der Differentialrechnung

- **Theorem name:** Satz 5.4.1 Eindeutigkeitssatz der Differentialrechnung
- **Source:** PDF p87; section 5.4. Anwendungen des Mittelwertsatzes
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir wissen bereits, dass konstante Funktionen überall die A bleitung Null haben. Es gelte nun f ′(x) = 0 für alle x \in ̊I = (a, b). Wir wollen zeigen, dass f konstant ist, d. h. dass f (x) = f (y) für alle x, y \in (a, b) gilt. Seien x, y \in (a, b). O. B. d. A. sei x < y. Der Mittelwertsatz gibt uns ein \xi \in (x, y) mit f ′(\xi) = f (y) − f (x) y − x . Wegen f ′(\xi) = 0 folgt f (x) = f (y). □ Bemerkung. Es ist hierbei wesentlich, dass I ein Intervall ist: Man betrachte z.B. die Funktion f : (− 1,0) \cup (0,1) \to R mit f (x) = 0 für x \in (− 1,0) und f (x) = 1 für x \in (0,1). Dann ist f ′(x) = 0 für alle x \in (− 1,0) \cup (0,1), aber f ist nicht konstant.
```
- **Key idea:** This result packages a reusable fact from 5.4. Anwendungen des Mittelwertsatzes; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.4.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.4.2 — Monotoniekriterium

- **Theorem name:** Satz 5.4.2 Monotoniekriterium
- **Source:** PDF p87; section 5.4. Anwendungen des Mittelwertsatzes
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(2) Wir beweisen zuerst die „ ⇒ “ Richtung. Es sei also f ′(x) ≥ 0 für alle inneren x in I. Seien x1 < x2 in I. Wenn wir den Mittelwertsatz auf die Einschränkung von f auf [x1, x2] anwenden, erhalten wir ein \xi \in (x1, x2), so dass f (x2) − f (x1) = f ′(\xi)(x2 − x1) ≥ 0, also f (x1) ≥ f (x2). Wir beweisen nun die „ ⇐ “ Richtung. Es sei also f monoton steigend. Dann gilt für alle inneren Punkte x in I, dass f ′(x) = lim h→ 0 f (x + h) − f (x) h   ≥ 0 für h > 0 und h < 0, weil f monoton steigend ≥ 0. □
```
- **Key idea:** This result packages a reusable fact from 5.4. Anwendungen des Mittelwertsatzes; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.4.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.4.4 — zweiten hinreichendes Extremwertkriterium

- **Theorem name:** Satz 5.4.4 zweiten hinreichendes Extremwertkriterium
- **Source:** PDF p89; section 5.4. Anwendungen des Mittelwertsatzes
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir betrachten nur den Fall, dass f ′′(x0) > 0. Der zweite Fall wird natürlich ganz analog bewiesen. Es folgt aus f ′′(x0) > 0, dass lim h→ 0 f ′(x0 + h) − f ′(x0) h = f ′′(x0) > 0. Es existiert also ein δ > 0, so dass f ′(x0 + h) − f ′(x0) h > 0 für alle h ̸= 0 \in (− δ, δ). Es folgt, dass f ′(x0 + h) > f ′(x0) = 0, für alle h \in (0, δ), und f ′(x0 + h) < f ′(x0) = 0, für alle h \in (− δ,0). Es folgt aus Satz 5.4.3 f ist auf dem Intervall [ x0, x0 + δ) streng monoton steigend, und f ist auf dem Intervall ( x0 − δ, x0] streng monoton fallend. Dies wiederum impliziert, dass x0 ein lokales Minimum ist. □ Unsere zweite Regel zur Bestimmung der inneren lokalen Extr ema lautet: 1 Bestimme die kritschen Punkte x \in ̊I. 2 Für jeden kritischen Punkt x0 berechne f ′′(x0) (falls f zweimal differenzierbar in x0 ist). Gilt f ′′(x0) > 0 ⇝ x0 lokales Minimum; Gilt f ′′(x0) > 0 ⇝ x0 lokales Maximum. ANALYSIS I-III, 2011/2013 88 3 Gilt f ′′(x0) = 0, dann liefert das Kriterium 5.4.4 keine Auskunft und es kan n passieren, dass x0 eine Extremumstelle oder einen Sattelpunkt ist. Man kann höhere Ableitungen zur Untersuchung heran- ziehen, siehe Satz 5.4.4. Beispiele. (1) Sei f : R → R, f (x) = (x2− 1)2 aus Beispiel 5.3. Sie ist zweimal differenzierbar mit f ′(x) = 4x(x2− 1), f ′′(x) = 12x2 − 4. Die kritischen Punkte sind x1 = − 1, x2 = 0, x3 = 1. Es gilt f ′′(− 1) = f ′′(1) = 8 > 0 und f ′′(0) = − 4 < 0. Somit sind − 1 und 1 Minimumstellen und 0 Maximumstelle. (2) Für f : R → R, f (x) = x3 gilt f ′(0) = f ′′(0) = 0 und x = 0 is ein Sattelpunkt. Für f : R → R, f (x) = x4 gilt f ′(0) = f ′′(0) = 0 und x = 0 ist eine Minimumstelle. 27.01.26 Eine Funktion f : I → C heißt stetig differenzierbar , falls f differenzierbar und f ′: I → C stetig ist. Vorsicht! Es gibt differenzierbare Funktionen,…
```
- **Key idea:** This result packages a reusable fact from 5.4. Anwendungen des Mittelwertsatzes; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 5.4.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.4.5 — Schrankensatz

- **Theorem name:** Satz 5.4.5 Schrankensatz
- **Source:** PDF p90; section 5.4. Anwendungen des Mittelwertsatzes
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Die Ableitung f ′ : [a, b] \to R ist stetig auf dem kompakten Intervall [ a, b]. Der Satz über Maximum besagt, dass f ′ beschänkt ist. Sei L := supx\in[a,b] | f ′(x)| \in R. Seien x, y \in [a, b]. Wir können oBdA annehmen, dass x < y. Nach dem Mittelwertsatz angewandt auf dem kompakten Inter vall [ x, y], existiert \xi \in (x, y) \subset [a, b], so dass f (x) − f (y) = f ′(\xi)(x − y). Daraus folgt | f (x) − f (y)| = | f ′(\xi)(x − y)| ≤ L| x − y| . □
```
- **Key idea:** This result packages a reusable fact from 5.4. Anwendungen des Mittelwertsatzes; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.4.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.4.6 — Differenzierbarkeitssatz

- **Theorem name:** Satz 5.4.6 Differenzierbarkeitssatz
- **Source:** PDF p90; section 5.4. Anwendungen des Mittelwertsatzes
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei ( xn) in [ a, b] mit xn → x0, xn ̸= x0. Nach dem Mittelwertsatz existiert \xin \in [a, b] zwischen xn, x mit f (xn) − f (x0) = f ′(\xin)(xn − x0). Da \xin \in [a, b] zwischen xn und x liegt, und xn → x0, so gilt auch \xin → x0. Somit f (xn) − f (x0) xn − x0 = f ′(\xin) \to α, n → \infty . Es folgt, dass limx→ x0 f (x) − f (x0) x − x0 = α, d.h. f ist differenzierbar in x0 und f ′(x0) = α. □ Als Beispiel betrachte die Funktion f : R \to R, (5.7) f (x) = { e− 1/x , x > 0 0 , x \le 0 Die Funktion f ist stetig auf R und differenzierbar auf R \setminus {0}, mit f ′(x) = { 1 x2 e− 1/x , x > 0 0 , x < 0 Wegen lim xր 0 f ′(x) = 0 = limxց 0 f ′(x) ist f auch in 0 differenzierbar , und es gilt f ′(0) = 0. Für den Beweis der Regel von l’Hospital benötigen wir die folgende Verallgeme inerung des Mittelwertsatzes.
```
- **Key idea:** This result packages a reusable fact from 5.4. Anwendungen des Mittelwertsatzes; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 5.4.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.4.7 — Verallgemeinerter Mittelwertsatz, Cauchy

- **Theorem name:** Satz 5.4.7 Verallgemeinerter Mittelwertsatz, Cauchy
- **Source:** PDF p90; section 5.4. Anwendungen des Mittelwertsatzes
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wie wir gerade gesehen haben, ist der Satz eine Verallgemein erung vom Mittelwertsatz 5.3.5, welchen wir mithilfe des Satz 5.3.4 von Rolle bewiesen hatten. Auch d iesen Satz können wir mit fast dem gleichen Trick auf den Satz von Rolle zurückführen. ANALYSIS I-III, 2011/2013 89 0 1 2 3-1-2-3 0 -1 1 ABBILDUNG 12. Graph der Funktion f (x) = { e− 1/x , x > 0 0 , x \le 0 . Wie im Satz 5.3.5 führen wir eine Hilfsfunktion, damit wir de n Satz 5.3.4 von Rolle anwenden. Wir setzen h(x) := ( f (b) − f (a))g(x) − (g(b) − g(a)) f (x). Dann h(a) = f (b)g(a) − f (a)g(b) = h(b). Nach dem Satz 5.3.4 existiert \xi\in (a, b) mit 0 = h′(\xi) = ( f (b) − f (a))g′(\xi) − (g(b) − g(a)) f ′(\xi). □ Wird zusätzlich g′(x) ̸= 0 für alle x \in (a, b) vorausgesetzt, so folgt g(a) ̸= g(b) und wir können den verallgemei- nerter Mittelwertsatz in Bruchform schreiben, f (b) − f (a) g(b) − g(a) = f ′(\xi) g′(\xi) ·
```
- **Key idea:** This result packages a reusable fact from 5.4. Anwendungen des Mittelwertsatzes; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 5.4.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 5.4.8 — Regel von l’Hospital

- **Theorem name:** Satz 5.4.8 Regel von l’Hospital
- **Source:** PDF p91; section 5.4. Anwendungen des Mittelwertsatzes
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Um die Ideen zu konkretisieren, betrachten wir I = (a, b) mit a, b \in R, a < b, und x0 = a. Wir betrach- ten zunächst den Fall, wenn a \in R. Wir definieren die Funktionen ̃f , ̃g : [a, b) → R, durch ̃f (x) = { f (x), x \in (a, b), 0, x = a. ̃g(x) = { g(x), x \in (a, b), 0, x = a. Die Funktionen ̃f , ̃g sind stetig auf [ a, b) und differenzierbar auf ( a, b). Für x \in (a, b) gilt nach dem Mittelwert- satz, dass es ein \xix \in (a, x) gibt, mit ̃g(x) − ̃g(a) = ̃g′(\xix)(x − a) = g′(\xix)(x − a). Da g′(y) ̸= 0 für alle y \in I, folgt, dass g(x) = ̃g(x) ̸= ̃g(0) = 0. Nach dem verallgemeinerten Mittelwertsatz existiert \xix \in (a, x) mit f (x) g(x) = ̃f (x) ̃g(x) = ̃f (x) − ̃f (a) ̃g(x) − ̃g(a) = ̃f ′(\xix) ̃g′(\xix) = f ′(\xix) g′(\xix) . Wenn x → a gilt \xix → a, also limx→ a f (x) g(x) = limx→ a f ′(\xix) g′(\xix) = lim y→ a f ′(y) g′(y) = l. ANALYSIS I-III, 2011/2013 90 Der Fall a = −\infty kann auf den Fall b = 0 durch die Substitution y = 1 x zurückgeführt werden. Dabei ist x → a = −\infty äquivalent zu y → 0, y < 0. □ Beispiele. (1) Sei s > 0. Dann gilt: lim xց 0 xs log x = lim xց 0 log x x− s = lim xց 0 x− 1 (− s)x− s− 1 (l’Hospital, Typ \infty \infty , g′(x) ̸= 0 für x > 0) = lim xց 0 xs (− s) = 0 . (2) lim x→ 0 1 − cos x 3 1 − cos x (i) = lim x→ 0 1 3 sin x 3 sin x (l’Hospital, Typ 0 0 , g′(x) ̸= 0 für x \in (− π, π) \setminus {0}) (ii ) = lim x→ 0 1 9 cos x 3 cos x (l’Hospital, Typ 0 0 , g′(x) ̸= 0 für x \in (− π 2 , π 2 )) = 1 9 1 = 1 9 . Wir haben hier die Regeln wiederholt angewendet, was natürl ich nur dann erlaubt ist, wenn jeweils die Vor- aussetzungen des Satzes von l’Hospital erfüllt sind. Wir ha ben dies zunächst nur teilweise überprüft. Was in der Begründung der Zwischenschritte (i) und (ii) fehlt, ist die Existenz des Grenzwertes des Ableitungsquo-…
```
- **Key idea:** This result packages a reusable fact from 5.4. Anwendungen des Mittelwertsatzes; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Function limits, continuity, and algebra of limits.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 5.4.8 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 6.4.2 — Hauptsatz der Differential- und Integralrechnung

- **Theorem name:** Satz 6.4.2 Hauptsatz der Differential- und Integralrechnung
- **Source:** PDF p103; section 6.4. Der Hauptsatz der Differential- und Integralrechnung
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** Accumulated change differentiates back to the original rate, and antiderivatives compute integrals.
- **Dependency list:** Integral definition, continuity/regulated functions, derivative rules.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 6.4.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 6.6.5 — Taylorformel

- **Theorem name:** Satz 6.6.5 Taylorformel
- **Source:** PDF p108; section 6.6. Höhere Ableitungen. Die Taylorformel
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** Near a point, derivatives determine a polynomial approximation with a measurable error.
- **Dependency list:** Higher derivatives, mean value ideas, integration/differentiation.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 6.6.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.1.14 — Höldersche Ungleichung

- **Theorem name:** Satz 7.1.14 Höldersche Ungleichung
- **Source:** PDF p118; section 7.1. Konvexität und wichtige Ungleichungen
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** Dual exponents control products by separate norms.
- **Dependency list:** Young inequality and $p$-norms.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 7.1.14 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 7.1.15 — Minkowski-Ungleichung

- **Theorem name:** Satz 7.1.15 Minkowski-Ungleichung
- **Source:** PDF p118; section 7.1. Konvexität und wichtige Ungleichungen
- **Proof strategy in one sentence:** Start from the defining inequality or a known inequality, then estimate term by term.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** The $p$-norm satisfies the triangle inequality.
- **Dependency list:** Holder inequality.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Start from the defining inequality or a known inequality, then estimate term by term.
- **Active recall prompts:**
  1. State Satz 7.1.15 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.2.5 — 7.2. Metrische und normierte Räume

- **Theorem name:** Satz 7.2.5 
- **Source:** PDF p120; section 7.2. Metrische und normierte Räume
- **Proof strategy in one sentence:** Start from the defining inequality or a known inequality, then estimate term by term.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Ist y = 0 so ist die Aussage (a) klar . Sei y ̸= 0 also \|y\| ̸= 0. Dann gilt \|x\|2 · \|y\|2 − |〈 x, y〉| 2 =   x − 〈x, y〉 \|y\|2 y    2 \ge 0 . Die Rechnung im Detail: Wir benutzen die Bilinearität und er halten für \lambda \in C:  x − \lambda y  2 = ⟨ x − \lambda y, x − \lambda y ⟩ = 〈 x, x〉 − ⟨ x, \lambda y ⟩ − ⟨ \lambda y, x ⟩ + ⟨ \lambda y, \lambda y ⟩ = 〈 x, x〉 − \lambda ⟨ x, y ⟩ − \lambda ⟨ y, x ⟩ + \lambda\lambda ⟨ y, y ⟩ = \| x\|2 − \lambda ⟨ x, y ⟩ − \lambda ⟨ x, y ⟩ + | \lambda| 2 y  2 = \| x\|2 − 2 Re \lambda ⟨ x, y ⟩ + | \lambda| 2 y  2 (7.4) Setzen wir \lambda = 〈x,y〉 \| y\|2 ❀ \lambda ⟨ x, y ⟩ = |〈 x,y〉| 2 \| y\|2 , | \lambda| 2 = |〈 x,y〉| 2 \| y\|4 ❀   x − 〈x, y〉 \|y\|2 y    2 = \| x\|2 − 2 |〈 x, y〉| 2 \|y\|2 + |〈 x, y〉| 2 \|y\|4  y  2 = \| x\|2 − |〈 x, y〉| 2 \|y\|2 ✓ Zu (b): Da 〈y, x〉 = 〈x, y〉 gilt 〈x, y〉 + 〈 y, x〉 = 2 Re〈x, y〉. \|x + y\|2 = 〈 x + y, x + y〉 = 〈 x, x〉 + 〈 x, y〉 + 〈 y, x〉 + 〈 y, y〉 = \| x\|2 + 2 Re〈x, y〉 + \| y\|2 (a) \le \|x\|2 + 2\|x\|\|y\| + \| y\|2 = (\|x\| + \| y\|)2 Somit gilt \|x + y\| \le \|x\| + \| y\|. □ ANALYSIS I-III, 2011/2013 119
```
- **Key idea:** This result packages a reusable fact from 7.2. Metrische und normierte Räume; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Start from the defining inequality or a known inequality, then estimate term by term.
- **Active recall prompts:**
  1. State Satz 7.2.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 7.2.7 — 7.2. Metrische und normierte Räume

- **Theorem name:** Satz 7.2.7 
- **Source:** PDF p121; section 7.2. Metrische und normierte Räume
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Die Behauptung folgt aus der Abschätzung (7.5) 0 \le | ai| \le \|a\|2 = √ | a1| 2 + . . .+ | an| 2 \le | a1| + . . .+ | an| , d. h. \|a\|\infty \le \|a\|2 \le \|a\|1 . Es gelte lim k→\infty x(k) = x. Sei \varepsilon> 0. Dann \existsk(\varepsilon)\forall k \ge k(\varepsilon) : \|x(k) − x\|2 < \varepsilon. Für jedes i \in {1, . . . ,n} gilt | x(k) i − xi| \le \|x(k) − x\|2 daher \forall k \ge k(\varepsilon) : | x(k) i − xi| < \varepsilon. Daraus folgt, dass lim k→\infty x(k) i = xi. Nehmen wir nun an, dass letzteres für alle i gilt. Dann \existsk(\varepsilon, i) \forall k \ge k(\varepsilon, i) : \|x(k) i − xi\|2 < \varepsilon/n. Somit gilt für k \ge k(\varepsilon) := maxi k(\varepsilon, i): \|x(k) − x\|2 \le | x(k) 1 − x1| + . . .+ | x(k) n − xn| < n ·(\varepsilon/n) = \varepsilon. Durch Benutzung von (7.5) beweist man analog die Aussage übe r Cauchy-Folgen. □ Konvergenz im ( Rn, d2) bedeutet koordinatenweise Konvergenz. Dieser Satz erlaubt es uns die Konvergenz von Folgen im Rn auf das Studium der Konvergenz von Folgen von reellen Zahlen zurückzuführen. Insbesondere können wi r die Konvergenz von Folgen im Rn mithilfe der Methoden aus der Analysis I studieren. Der Satz ist ganz ähnl ich dem aus der Analysis I, der besagt, dass eine Folge {zn}n\inN von komplexen Zahlen konvergiert, genau dann, wenn die Real teile und Imaginärteile von den Folgengliedern konvergieren.
```
- **Key idea:** This result packages a reusable fact from 7.2. Metrische und normierte Räume; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 7.2.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.2.11 — 7.2. Metrische und normierte Räume

- **Theorem name:** Satz 7.2.11 
- **Source:** PDF p122; section 7.2. Metrische und normierte Räume
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(x(k))k ist Cauchy-Folge in ( Rn, d2) \Longleftrightarrow \forall i (x(k) i )k ist Cauchy-Folge in R ⇐ ⇒ \forall i (x(k) i )k ist konvergent in R \Longleftrightarrow (x(k))k ist konvergent in ( Rn, d2) □
```
- **Key idea:** This result packages a reusable fact from 7.2. Metrische und normierte Räume; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.2.11 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 7.2.12 — 7.2. Metrische und normierte Räume

- **Theorem name:** Satz 7.2.12 
- **Source:** PDF p122; section 7.2. Metrische und normierte Räume
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sein ( f k)k eine Cauchy-Folge in ( B(D), dD ), d.h. \forall \varepsilon > 0 \existsk(\varepsilon) \forall k, l \ge k(\varepsilon) : \| f k − fl\|D < \varepsilon Für jedes x \in D gilt | f k(x) − fl(x)| \le \| f k − fl\|D also \forall \varepsilon > 0 \existsk(\varepsilon) \forall k, l \ge k(\varepsilon) \forall x \in D : | f k(x) − fl(x)| < \varepsilon daher ist ( f k(x))k eine Cauchy-Folge in C. Da C vollständig ist, existiert f (x) := limk→\infty f k(x). Wir haben also eine Funktion f : D → C konstruiert als Kandidat für den Grenzwert der Folge ( f k)k. Durch Limesübergang l → \infty in der Ungleichung | f k(x) − fl(x)| < \varepsilon erhalten wir \forall \varepsilon > 0 \existsk(\varepsilon) \forall k \ge k(\varepsilon) \forall x \in D : | f k(x) − f (x)| \le \varepsilon ⇐ ⇒ \forall \varepsilon > 0 \existsk(\varepsilon) \forall k \ge k(\varepsilon) : \| f k − f \|D \le \varepsilon Daraus folgt, dass f beschränkt ist und dass f k k→\infty \to f in (B(D), dD ). Ist ( f k)k eine Cauchy-Folge in ( C0([a, b]), d[a,b]), so wissen wir zusätlich, dass f stetig sein muss. □
```
- **Key idea:** This result packages a reusable fact from 7.2. Metrische und normierte Räume; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.2.12 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.2.14 — Bolzano-Weierstraß in Rn

- **Theorem name:** Satz 7.2.14 Bolzano-Weierstraß in Rn
- **Source:** PDF p122; section 7.2. Metrische und normierte Räume
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei ( x(k))k eine beschränkte Folge. Schreibe x(k) = (x(k) 1 , . . . ,x(k) n ). Dann ist ( x(k) i )k beschränkt für alle i \in {1, . . . ,n}. Nach Bolzano-Weierstraß in R hat ( x(k) 1 )k eine konvergente Teilfolge x(k′) 1 k′→\infty \to x1 Wiederum nach Bolzano-Weierstraß in R hat die Teilfolge ( x(k′) 2 )k′ eine konvergente Teilfolge, sagen wir x(k′′) 2 k′′→\infty \to x2 Beachte, dass immer noch x(k′′) 1 k′′→\infty \to x1 gilt. Wir fahren so bis zur n-ten Komponente fort und erhalten schliess- lich eine Teilfolge ( x( ̃k)) ̃k von ( x(k))k und Werte x1, . . . ,xn mit x( ̃k) i ̃k→\infty \to xi, i = 1, . . . ,n. Das bedeutet gerade x( ̃k) ̃k→\infty \to x := (x1, . . . ,xn) in ( Rn, d2) □ Wie funktioniert den Beweis für n = 2? (1) Wir wählen der ersten Komponentenfolge ( x(k) 1 )k wird eine konvergente Teilfolge aus: (x(1) 1 , x(2) 1 , . . . ,x(k) 1 , . . .) \supset (x(k1) 1 , x(k2) 1 , . . . ,x(kl) 1 , . . .) \to x1, l → \infty . (2) Wir betrachten die Teilfolge ( x(kl) 2 )l mit den Indizes ( kl)l innerhalb der zweiten Komponentenfolge und wir wählen eine konvergente Teilfolge (x(k1) 2 , x(k2) 2 , . . . ,x(kl) 2 , . . .) \supset (x (kl1 ) 2 , x (kl2 ) 2 , . . . ,x (klm ) 2 , . . .) \to x2, m → \infty . ANALYSIS I-III, 2011/2013 121 (3) Die Teilfolge mit der Indizes ( lm)m (x (kl1 ) 1 , x (kl2 ) 1 , . . . ,x (klm ) 1 , . . .) \subset (x(k1) 1 , x(k2) 1 , . . . ,x(kl) 1 , . . .) ist eine Teilfolge der konvergenten Teilfolge ( x(k1) 1 , x(k2) 1 , . . . ,x(kl) 1 , . . .) und konvergiert gegen x1. (4) Somit konvergieren die beiden Komponenten der Teilfolg e ( x(klm ))m und limm→\infty x(klm ) = (x1, x2). Zur Anschauung, werden in der folgende Figur die Teilfolgen mit Indizes k1, k2, . . . ,kl, . . . mit Blau markiert und die Teilfolgen mit Indizes kl1 , kl2 , . . . ,klm , . .…
```
- **Key idea:** This result packages a reusable fact from 7.2. Metrische und normierte Räume; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.2.14 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.2.20 — 7.2. Metrische und normierte Räume

- **Theorem name:** Satz 7.2.20 
- **Source:** PDF p124; section 7.2. Metrische und normierte Räume
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Die Reihe \sum\infty n= 0 xn ist absolut konvergent, da \|xn\| \le \|x\|n und \sum\infty n= 0 \|x\|n eine geometrische Reihe ist. Insbesondere xn n→\infty \to 0. Es gilt (e − x) \infty\sum n= 0 xn = (e − x) limm→\infty m\sum n= 0 xn = limm→\infty (e − x) m\sum n= 0 xn = limm→\infty ( m\sum n= 0 xn − m+ 1\sum n= 1 xn) = limm→\infty (e − xm+ 1) = e.
```
- **Key idea:** This result packages a reusable fact from 7.2. Metrische und normierte Räume; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.2.20 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.3.3 — 7.3. Topologie eines metrischen Raumes. Topologische Räume.

- **Theorem name:** Satz 7.3.3 
- **Source:** PDF p126; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(1) Die Teilmenge U := X ist offen, weil für jedes x \in U = X gilt B1(x) \subset X . Die leere Menge besitzt per Definition kein einziges Element, also gibt es bei der Offenh eit auch nichts zu überprüfen, d.h. die leere Menge ist offen. (2) Es sei Ui, i \in I eine Familie 8 von offenen Teilmengen. Wir zeigen, dass die Vereinigungsm enge \cup i\in I Ui ebenfalls offen ist. Es sei x \in \cup i\in IUi. Dann existiert insbesondere ein i0 \in I, so dass x \in Ui0 . Nach Voraussetzung existiert ein \varepsilon> 0, so dass B\varepsilon(x) \subset Ui0 . Dann gilt aber auch, dass B\varepsilon(x) \subset Ui0 \subset \bigcup i\in I Ui. Somit ist \cup i\in IUi offen. (3) Es seien U1, . . . ,Uk offene Teilmengen von X . Wir zeigen, dass die Schnittmenge U1 \cap U2 \cap · · · \capUk offen ist. Es sei x \in U1 \cap U2 \cap · · · \capUk. Nach Voraussetzung existiert für jedes i \in {1, . . . ,k} ein \varepsiloni > 0, so dass B\varepsiloni (x) \subset Ui. Wir setzen \varepsilon:= min{\varepsilon1, . . . ,\varepsilonk}. Dann gilt für jedes i \in {1, . . . ,k}, dass B\varepsilon(x) \subset B\varepsiloni (x) \subset Ui. Also folgt, dass Bmin(\varepsilon1,...,\varepsilonk )(x) \subset U1 \cap U2 \cap · · · \capUk. 8Das heißt Folgendes: I ist eine Menge (z.B. {1, . . . ,k} oder N, aber I kann auch z.B. überabzählbar sein), und jedem Element i \in I ist eine Menge Ui zugeordnet. Siehe auch: http://de.wikipedia.org/wiki/Familie_(Mathematik) ANALYSIS I-III, 2011/2013 125 Für den Beweis von (1’)-(3’) werden wir die de Morgansche Reg el verwenden: für beliebige Teilmengen A, B von einer Menge M gilt M \ (A \cup B) = (M \ A) \cap (M \ B) und M \ (A \cap B) = (M \ A) \cup (M \ B). Dies folgt sofort aus den Definition und elementarer Logik. M an kann dies auch mithilfe von Abbildung 15 verifizier…
```
- **Key idea:** This result packages a reusable fact from 7.3. Topologie eines metrischen Raumes. Topologische Räume.; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.3.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.3.5 — 7.3. Topologie eines metrischen Raumes. Topologische Räume.

- **Theorem name:** Satz 7.3.5 
- **Source:** PDF p127; section 7.3. Topologie eines metrischen Raumes. Topologische Räume.
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei x := limk→\infty xk \in X . Angenommen x \in X \ F, so existiert \varepsilon> 0 mit B\varepsilon(x) \subset X \ F, da X \ F offen ist. F x1 x2 · · · x B\varepsilon(x) Mit der Definition der Konvergenz gilt xk \in B\varepsilon(x) \subset X \setminus F für fast alle k. Widerspruch. □ Mittels Satz 7.3.5 kann man z. B. zeigen: • Die Menge { x \in Rn : Ax = b } ist abgeschlossen in Rn, wobei A \in Mm× n(R), b \in Rm. ANALYSIS I-III, 2011/2013 126 • Die Menge C0([a, b]) ist abgeschlossen in ( B([a, b]), d[a,b]).
```
- **Key idea:** This result packages a reusable fact from 7.3. Topologie eines metrischen Raumes. Topologische Räume.; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.3.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.4.3 — 7.4. Stetige Abbildungen

- **Theorem name:** Satz 7.4.3 
- **Source:** PDF p133; section 7.4. Stetige Abbildungen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir zeigen die Implikationen (1) ⇒ (2) und (2) ⇒ (1). (1) ⇒ (2): Sei f stetig in a und sei ( xn)n eine Folge in X mit lim n→\infty xn = a. Zu zeigen ist, dass lim n→\infty f (xn) = f (a). Sei \varepsilon> 0 gegeben. Da f in a stetig ist, gibt es ein δ > 0, so dass dX (x, a) < δ \Rightarrow dY ( f (x), f (a) ) < \varepsilon. ANALYSIS I-III, 2011/2013 132 Da xn → a, existiert ein n0 \in N, so dass für alle n ≥ n0 gilt: dX (xn, a) < δ. Folglich erhält man für alle n ≥ n0 dY ( f (xn), f (a) ) < \varepsilon. Damit ist nach Definition des Grenzwertes von Folgen limn→\infty f (xn) = f (a). (2) ⇒ (1): Wir zeigen die Kontraposition. Angenommen, f ist nicht stetig in a. Dann gibt es ein \varepsilon0 > 0, so dass zu jedem δ > 0 ein Punkt x \in X existiert mit dX (x, a) < δ und dY ( f (x), f (a) ) ≥ \varepsilon0. Insbesondere können wir für jedes n \in N ein xn \in X wählen mit dX (xn, a) < 1 n und dY ( f (xn), f (a) ) ≥ \varepsilon0. Aus dX (xn, a) < 1/n folgt limn→\infty xn = a. Nach Voraussetzung (2) müsste daher gelten lim n→\infty f (xn) = f (a). Dies ist jedoch unmöglich, denn für alle n \in N gilt dY ( f (xn), f (a) ) ≥ \varepsilon0. Also kann die Folge ( f (xn))n nicht gegen f (a) konvergieren. Dieser Widerspruch zeigt, dass f in a stetig sein muss. Somit sind (1) und (2) äquivalent. □
```
- **Key idea:** This result packages a reusable fact from 7.4. Stetige Abbildungen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 7.4.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.4.4 — 7.4. Stetige Abbildungen

- **Theorem name:** Satz 7.4.4 
- **Source:** PDF p134; section 7.4. Stetige Abbildungen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir verwenden das Folgenkriterium für Stetigkeit. (1) Sei ( xn)n eine Folge in X mit limn→\infty xn = a. Da f und g in a stetig sind, folgt aus dem Folgenkriterium limn→\infty f (xn) = f (a), limn→\infty g(xn) = g(a). Mit den Rechenregeln für konvergente Folgen in C erhalten wir limn→\infty ( f + g)(xn) = limn→\infty ( f (xn) + g(xn) ) = f (a) + g(a) = ( f + g)(a), also ist f + g in a stetig. Ferner gilt limn→\infty ( f ·g)(xn) = limn→\infty ( f (xn)g(xn) ) = f (a)g(a) = ( f ·g)(a), also ist f ·g in a stetig. Schliesslich folgt limn→\infty (\lambda f )(xn) = limn→\infty \lambda f (xn) = \lambda f (a) = (\lambda f )(a), also ist auch \lambda f in a stetig. (2) Angenommen, g(a) ̸= 0. Sei wiederum ( xn)n eine Folge in X mit lim n→\infty xn = a. Dann gilt limn→\infty g(xn) = g(a) ̸= 0. Daher existiert ein N \in N, so dass g(xn) ̸= 0 für alle n ≥ N. Für n ≥ N ist also der Quotient f (xn) g(xn) definiert. Mit der Quotientenregel für konvergente Folgen erhalten wir limn→\infty f (xn) g(xn) = limn→\infty f (xn) limn→\infty g(xn) = f (a) g(a) = ( f g ) (a). Nach dem Folgenkriterium ist somit f /g in a stetig. □ Daraus folgt insbesondere, dass alle Polynome P : Rn \to R, P \in R[x1, . . . ,xn], stetig sind. Dabei hat ein Polynom die Form P(x1, . . . ,xn) = \sum α= (α 1,...,α n) aα xα 1 1 · · ·xα n n , wobei nur endlich viele Koeffizienten aα \in R von Null verschieden sind. Beispiele sind P(x, y) = x2 + 3x y− 2y + 1, P(x, y, z) = x3 + y2 z − 5xz + 7, P(x1, . . . ,xn) = x2 1 + · · · +x2 n. Ebenso sind rationale Funktionen R = P Q , R : Rn \ {x \in Rn : Q(x) = 0} \to R, ANALYSIS I-III, 2011/2013 133 stetig. Beispiele sind R(x, y) = x2 + y2 1 + x2 + y2 , R(x, y) = x y x2 + y2 , (x, y) ̸= (0,0), sowie R(x, y, z) = x + y + z 1 + x2 + y2 + z2 ·
```
- **Key idea:** This result packages a reusable fact from 7.4. Stetige Abbildungen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 7.4.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.4.5 — 7.4. Stetige Abbildungen

- **Theorem name:** Satz 7.4.5 
- **Source:** PDF p135; section 7.4. Stetige Abbildungen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir verwenden das Folgenkriterium für Stetigkeit. Sei ( xn)n eine Folge in X mit lim n→\infty xn = a. Da f in a stetig ist, folgt aus dem Folgenkriterium limn→\infty f (xn) = f (a) = b. Da g in b stetig ist, können wir das Folgenkriterium erneut anwenden und erhalten limn→\infty g( f (xn)) = g(b) = g( f (a)). Somit gilt limn→\infty (g ◦ f )(xn) = (g ◦ f )(a). Da dies für jede Folge ( xn)n mit xn → a gilt, ist g ◦ f nach dem Folgenkriterium in a stetig. □ Wir könen den Satz auch mit Hilfe der \varepsilon− δ Definition beweisen. Beweis: Wähle eine \varepsilon-Kugel um g( f (a)) in Z. Wegen der Stetigkeit von g gibt es eine η-Kugel um f (a) in Y , deren Bild in der \varepsilon-Kugel liegt. Wegen der Stetigkeit von f gibt es eine δ-Kugel um a in X , deren Bild in der η-Kugel liegt. Daher landet die δ-Kugel unter g ◦ f in der \varepsilon-Kugel. □ X a Bδ(a) Y f (a) Bη( f (a)) Z g( f (a)) B\varepsilon(g( f (a))) f g f (Bδ(a)) g( f (Bδ(a))) f (Bδ(a)) \subset Bη( f (a)), g(Bη( f (a)) \subset B\varepsilon(g( f (a))) daher f (Bδ(a)) \subset B\varepsilon(g( f (a)))
```
- **Key idea:** This result packages a reusable fact from 7.4. Stetige Abbildungen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 7.4.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.4.6 — 7.4. Stetige Abbildungen

- **Theorem name:** Satz 7.4.6 
- **Source:** PDF p135; section 7.4. Stetige Abbildungen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(⇒ ) Sei f stetig und sei i \in {1, . . . ,m}. Da pr i : Rm → R stetig ist, so ist f i = pri ◦ f stetig, nach Satz 7.4.5. (⇐ ) Wir verwenden das Folgenkriterium. Dazu erinnern wir , das s die Konvergenz in Rm komponentenweise Konvergenz ist: y(k) = (y(k) 1 , . . . ,y(k) m ) → y = (y1, . . . ,ym), k → \infty , genau dann, wenn y(k) i → y(k) i , k → \infty i = 1, . . . ,m. Seien nun alle f i stetig. Wir zeigen die Stetigkeit von F. Sei ( xk)k eine Folge in X mit xk → a, k → \infty . Da f i stetig ist, gilt für jedes i = 1, . . . ,m, f i(xk) → f i(a), k → \infty . ANALYSIS I-III, 2011/2013 134 Somit konvergieren alle Komponenten von f (xk) gegen die entsprechenden Komponenten von f (a). Nach dem Konvergenzkriterium für Folgen in Rm folgt f (xk) = ( f1(xk), . . . ,f m(xk) ) \to ( f1(a), . . . ,f m(a) ) = f (a) k → \infty . Nach dem Folgenkriterium ist f stetig. □ Beispiele: (1) Die Abbildung f : R \to R2, f (t) = (cos t,sin t), ist stetig. Tatsächlich sind die Komponentenfunktionen f1(t) = cos t, f2(t) = sin t stetig. Nach dem Satz 7.4.6 über die komponentenweise Steti gkeit ist daher auch f = ( f1, f2) stetig. (2) Die Abbildung Φ : [0,\infty ) × R \to R2, Φ(r, θ) = (r cos θ, r sin θ), ist stetig. Die Projektionen ( r, θ) \mapstor, ( r, θ) \mapstoθ sind stetig. Da auch die Funktionen sin ,cos : R \to R stetig sind, folgt aus dem Satz 7.4.5 über die Stetigkeit von Komposition en, dass (r, θ) \mapstor cos θ, (r, θ) \mapstor sin θ stetig sind. Mit den Rechenregeln für stetige Funktionen er halten wir die Stetigkeit der Komponenten (r, θ) \mapstor cos θ, (r, θ) \mapstor sin θ. Nach dem Satz über 7.4.6 die komponentenweise Stetigkeit is t somit Φ(r, θ) = (r cos θ, r sin θ) stetig. (3) Die Funktion f : R2 \to R, f (x, y) =      x3 y x2 + y2 , falls ( x, y) ̸= (0,0) 0 , fall…
```
- **Key idea:** This result packages a reusable fact from 7.4. Stetige Abbildungen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 7.4.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 7.4.7 — Globale Charakterisierung der Stetigkeit

- **Theorem name:** Satz 7.4.7 Globale Charakterisierung der Stetigkeit
- **Source:** PDF p136; section 7.4. Stetige Abbildungen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir zeigen die Implikationen (1) ⇒ (2) ⇒ (3) ⇒ (1). (1) ⇒ (2): Sei U \subset Y offen. Wir zeigen, dass f − 1(U) offen ist. ANALYSIS I-III, 2011/2013 135 Sei a \in f − 1(U). Dann gilt f (a) \in U. Da U offen ist, ist U eine offene Umgebung von f (a). Wegen der Stetigkeit von f in a gibt es eine offene Umgebung V von a mit f (V ) \subset U. Daraus folgt V \subset f − 1(U). Somit besitzt jeder Punkt von f − 1(U) eine offene Umgebung, die ganz in f − 1(U) enthalten ist. Also ist f − 1(U) offen. (2) ⇒ (3): Sei F \subset Y abgeschlossen. Dann ist Y \ F offen. Nach (2) ist daher f − 1(Y \ F) offen in X . Da Urbilder mit Komplementbildung vertauschen, gilt f − 1(Y \ F) = X \ f − 1(F). Folglich ist X \ f − 1(F) offen, also f − 1(F) abgeschlossen. (3) ⇒ (1): Sei a \in X . Wir zeigen, dass f in a stetig ist. Sei U eine offene Umgebung von f (a). Dann ist F := Y \U abgeschlossen. Nach (3) ist f − 1(F) abgeschlossen, also ist X \ f − 1(F) offen. Wegen X \ f − 1(F) = f − 1(Y \ F) = f − 1(U) ist f − 1(U) eine offene Menge in X . Da f (a) \in U, gilt a \in f − 1(U). Somit ist f − 1(U) eine offene Umgebung von a. Ausserdem gilt f ( f − 1(U) ) \subset U. Nach der Definition der Stetigkeit ist f in a stetig. Da a \in X beliebig war , ist f stetig. □
```
- **Key idea:** This result packages a reusable fact from 7.4. Stetige Abbildungen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 7.4.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.4.10 — Parametrisierung der Kreislinie

- **Theorem name:** Satz 7.4.10 Parametrisierung der Kreislinie
- **Source:** PDF p137; section 7.4. Stetige Abbildungen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Für den Beweis der Stetigkeit von arg betrachte die offenen M engen in S1: V1 = S1 \cap {z : Im z > 0}, V2 = S1 \cap {z : Im z < 0}, V3 = S1 \cap {z : Re z < 0} und die stetigen Abbildungen f1 : V1 → R , f1(z) = arccos(Re z) , f2 : V2 → R , f2(z) = − arccos(Re z) , f3 : V3 → R , f3(z) = arcsin(Im z) . (Verkettungen der stetigen Abbildungen z \mapstoRe z und arccos, bzw . z \mapstoIm z und arcsin). Es ist S1 \ {− 1} = V1 \cup V2 \cup V3 und arg z =        f1(z) , z \in V1 , f2(z) , z \in V2 , f3(z) , z \in V3 . also die zwei Definitionen in (7.6) “verkleben” sich stetige rweise in z = 1. Formal, sei z0 \in S1 \ {− 1}. Dann gibt es k \in {1,2,3} mit z0 \in Vk. Da Vk offen ist, gilt lim z→ z0 z\in S1\{− 1} arg(z) = lim z→ z0 z\inVk f k(z) = f k(z0) = arg(z0) ANALYSIS I-III, 2011/2013 136 Andererseits gilt lim z→− 1 Im z< 0 arg z = lim x→− 1 (− arccos x) = − π , lim z→− 1 Im z>0 arg z = lim x→− 1 arccos x = π also hat arg ein Sprung von 2 π in z = − 1. □ Die Aussage (i) kann man so umformulieren: \forall (x, y) \in R2 , x2 + y2 = 1 \exists\varphi \in R : x = cos \varphi , y = sin \varphi cos \varphi 1 = cos\varphi 2 , sin \varphi 1 = sin \varphi 2 \Longleftrightarrow \varphi 1 − \varphi 2 \in 2πZ Wir können uns \varphi \mapstop(\varphi ) = ei\varphi als Beschreibung der Bewegung eines Punktes vorstellen, de r zum Zeitpunkt \varphi am Ort ei\varphi ist. Die Geschwindigkeit des Punktes ist p′(\varphi ) = ie i\varphi , ein Tangentialvektor an die beschriebene Kurve in p(\varphi ). Es gilt | p′(\varphi )| = | ie i\varphi | = 1 für alle \varphi . /Bullet/Circle /Bullet/Circle/Bullet/Circle /Bullet/Circle /Bullet/Circle /Bullet/Circle O(0,0) ei0= 1 ei π 2 = i eiπ =− 1 ei 3π 2 =− i ei\varphi
```
- **Key idea:** This result packages a reusable fact from 7.4. Stetige Abbildungen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 7.4.10 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 7.5.3 — 7.5. Kompaktheit

- **Theorem name:** Satz 7.5.3 
- **Source:** PDF p140; section 7.5. Kompaktheit
- **Proof strategy in one sentence:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir beweisen beide Aussagen indirekt. (i) Angenommen, K ist nicht abgeschlossen. Dann existiert eine konvergente F olge ( xn) in K, so dass x = limn→\infty xn nicht in K liegt. Folglich hat ( xn) keinen Häufungswertt in K, denn eine konvergente Folge besitzt nur einen Häufungswertt, nämlich ihren Grenzwert. ANALYSIS I-III, 2011/2013 139 K x1 x2 · · · x ̸\in K (ii) Angenommen, K ist unbeschränkt. Dann existiert a \in X und xn \in K \ Bn(a), n = 1,2, . . . . Existierte eine konvergente Teilfolge xnk − − − \to k→\infty b, so gäbe es ein k0, so dass d(xnk , b) < 1 für alle k ≥ k0. Mit der Dreiecksungleichung folgt dann d(xnk , a) ≤ d(xnk , b) + d(b, a) < 1 + d(a, b), also eine von k unabhängige Schranke. K a B1(a) x1 x2 x3 · · · xn \in K \ Bn(a) b B1(b) xnk → b d(a, b) Dies steht im Widerspruch zu d(xnk , a) ≥ nk − − − \to k→\infty \infty . □
```
- **Key idea:** This result packages a reusable fact from 7.5. Kompaktheit; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Active recall prompts:**
  1. State Satz 7.5.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.5.4 — Heine-Borel

- **Theorem name:** Satz 7.5.4 Heine-Borel
- **Source:** PDF p141; section 7.5. Kompaktheit
- **Proof strategy in one sentence:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir haben schon gezeigt, dass ( i) \Rightarrow (ii ). Zu ( ii ) \Rightarrow (i): Da K beschränkt ist, hat jede Folge in K eine konvergente Teilfolge in Rn. Da K abgeschlossen ist, liegt deren Grenzwert in K. Somit ist K kompakt. □ (1) Wir betrachten die n–dimensionale Sphäre Sn := {(x1, . . . ,xn+ 1) \in Rn+ 1 | x2 1 + · · · +x2 n+ 1 = 1}. Wir wollen zei- gen, dass Sn kompakt ist. Nach dem Satz von Heine–Borel genügt es zu zeige n, dass Sn beschränkt und abgeschlossen ist. Es folgt sofort aus der Definition, dass Sn beschränkt ist. Aus Beispiel 7.4.9 folgt, dass auch Sn abgeschlossen ist. 9 (2) Ganz analog kann man auch zeigen, dass die n-dimensionale Scheibe D n := {(x1, . . . ,xn) \in Rn | x2 1 +· · ·+x2 n ≤ 1} kompakt ist.
```
- **Key idea:** This result packages a reusable fact from 7.5. Kompaktheit; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Active recall prompts:**
  1. State Satz 7.5.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.5.5 — 7.5. Kompaktheit

- **Theorem name:** Satz 7.5.5 
- **Source:** PDF p141; section 7.5. Kompaktheit
- **Proof strategy in one sentence:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei ( yk) eine Folge in f (X ). Für jedes k wähle ein xk \in X mit f (xk) = yk. Da K kompakt ist, besitzt die Folge (xk) eine konvergente Teilfolge ( xkl) mit xkl − − − \to l→\infty x \in X . 9Man könnte natürlich auch versuchen ‘per Hand’ mithilfe der \varepsilon–Definition zu zeigen, dass Rn+ 1 \ Sn offen ist. Aber dies ist gelinde gesagt umständlich. In vielen Fällen kann m an die Offenheit bzw . Abgeschlossenheit einer Menge durch geschicktes anwenden von Satz 7.4.7 zeigen. ANALYSIS I-III, 2011/2013 140 Xx1 x2 x3 . . . xk xk1 xk2 xk3 xk4 x f f (X )y1 y2 y3 . . . yk yk1 yk2 yk3 yk4 f (x) Wegen der Stetigkeit von f folgt ykl = f (xkl) − − − \to l→\infty f (x) \in f (X ). Also besitzt jede Folge in f (X ) eine konvergente Teilfolge mit Grenzwert in f (X ). Daher ist f (X ) kompakt. □
```
- **Key idea:** This result packages a reusable fact from 7.5. Kompaktheit; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Active recall prompts:**
  1. State Satz 7.5.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.5.6 — Satz vom Maximum und Minimum

- **Theorem name:** Satz 7.5.6 vom Maximum und Minimum
- **Source:** PDF p142; section 7.5. Kompaktheit
- **Proof strategy in one sentence:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Da X kompakt und f stetig ist, folgt aus Satz 7.5.5, dass das Bild f (X ) \subset R kompakt ist. Aus Satz 7.5.3 folgt, dass f (X ) \subset R beschränkt und abgeschlossen ist. Da f (X ) beschränkt ist, existiert insbesondere s := inf( f (X )). Das Infimum inf( f (X )) ist der Grenzwert einer Folge von Punkten in f (X ). Da f (X ) abgeschlossen ist, liegt auch der Grenzwert in f (X ). Es existiert also ein \xi1 \in X , so dass f (\xi1) = inf( f (X )). Dann gilt aber für alle x \in X , dass f (\xi1) = inf( f (K)) ≤ f (x). Die Existenz von \xi2 zeigt man ganz analog. □ 7.6. Zusammenhang. Die Rolle der Intervalle in R wird in metrischen Räumen übernommen von den soge- nannten zusammenhängenden Mengen, die wir jetzt kennenler nen.
```
- **Key idea:** Compactness is the correct general reason extrema exist.
- **Dependency list:** Compactness and continuity.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Active recall prompts:**
  1. State Satz 7.5.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.6.2 — Zusammenhängende Teilmengen von R

- **Theorem name:** Satz 7.6.2 Zusammenhängende Teilmengen von R
- **Source:** PDF p144; section 7.6. Zusammenhang
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
\Rightarrow : A \subset R sei zusammenhängend. Setze a = inf A \in R, b = sup A \in R (wobei R = R \cup {±\infty }.) Dann ist A \subset (a, b) \cap {a, b}. Wir zeigen, dass ( a, b) \subset A. Daraus folgt, dass A ein Intervall mit Endpunkten a, b ist. Gilt (a, b) ̸\subset A, so gibt es c \in (a, b), c ̸\in A. Sei U = A \cap (−\infty , c), V = A \cap (c,\infty ). Dann sind U,V offen in A, U \cap V = \emptyset und A = U \cup V . ANALYSIS I-III, 2011/2013 143 a c b U = A \cap (−\infty , c) V = A \cap (c,\infty ) c \notin A Ausserdem gibt es a1 \in (a, c) \cap A, b1 \in (c, b) \cap A wegen a = inf A, b = sup A, also U ̸= \emptyset, V ̸= \emptyset. Dies ist ein Widerspruch. ⇐ = : Seien U,V offen in A, U \cap V = \emptysetund A = U \cup V . Sei x \in U, y \in V und OBdA x < y. Sei z = sup(U \cap [x, y]). x y z = sup(U \cap [x, y])U V Es gilt z ̸\in U: Sonst existiert \varepsilon > 0 mit [ z, z + \varepsilon) \subset U \cap [x, y] (beachte z < y) und das ist unmöglich wegen der Supremumseigenschaft von z. z u [z, z + \varepsilon) \subset U Andererseits ist V \cap [x, y] offen in [ x, y] also ihr Komplement U \cap [x, y] ist abgeschlossen in [ x, y]. Daraus folgt, dass z \in U \cap [x, y]. Widerspruch. □
```
- **Key idea:** On the real line, connectedness is exactly having no gaps.
- **Dependency list:** Connectedness, intervals, order topology.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.6.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.6.3 — 7.6. Zusammenhang

- **Theorem name:** Satz 7.6.3 
- **Source:** PDF p145; section 7.6. Zusammenhang
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Seien U,V offen in f (X ), disjunkt, mit f (X ) = U \cup V . Dann gilt X = f − 1(U)\cup f − 1(V ), f − 1(U)\cap f − 1(V ) = \emptyset. Da f stetig ist, sind f − 1(U), f − 1(V ) offen. Da X zusammenhängend ist, es muss f − 1(U) = \emptysetoder f − 1(V ) = \emptyset. Daraus folgt, dass U = \emptysetoder V = \emptyset. □ f − 1(U) f − 1(V ) X X = f − 1(U) \cup f − 1(V ) f U V f (X ) f (X ) = U \cup V
```
- **Key idea:** This result packages a reusable fact from 7.6. Zusammenhang; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 7.6.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.6.7 — 7.6. Zusammenhang

- **Theorem name:** Satz 7.6.7 
- **Source:** PDF p146; section 7.6. Zusammenhang
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Angenommen X wäre nicht zusammenhängend. Sei X = U \cup V eine Zerlegung in zwei nichtleeren, disjunkten offenen Mengen ist, wähle x \in U, y \in V und γ : [0,1] → X , stetig, mit γ(0) = x, γ(1) = y. Dann ist [0,1] = γ− 1(U) \cap γ− 1(V ) eine Zerlegung in zwei nichtleeren, disjunkten offenen Me ngen. Widerspruch. □ X U V x y γ 0 1 γ− 1(U) γ− 1(V ) [0,1] = γ− 1(U) \cup γ− 1(V )
```
- **Key idea:** This result packages a reusable fact from 7.6. Zusammenhang; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.6.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 7.6.9 — 7.6. Zusammenhang

- **Theorem name:** Satz 7.6.9 
- **Source:** PDF p147; section 7.6. Zusammenhang
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei x0 \in D fest. Definiere U = {x \in D : \exists Streckenzug S \subset D zwischen x0 und x}. Wir werden zeigen, dass U ist offen, abgeschlossen und nicht leer ist. Daraus folgt, d ass U = D, weil D zusammenhängend ist. Es gilt offensichtlich x0 \in U, also ist U nicht leer .U ist offen: Sei x \in U und sei Br(x) \subset D. Sei y \in Br(x). Falls S \subset D einen Streckenzug zwischen x0 und x ist, so ist S\cup [x, y] \subset D einen Streckenzug zwischen x0 und y. Somit gilt Br(x) \subset D also U ist offen. U ist abgeschlossen: Sei V = D \setminus U. Sei x \in V und sei Br(x) \subset D. Dann gilt Br(x) \subset U. Gäbe es einen Stre- ckenzug S in D von x0 zu z \in Br(x), so wäre S(x0, z) \cup [z, x] einen Streckenzug in D von x0 zu x. Somit ist V offen und folglich ist U abgeschlossen.
```
- **Key idea:** This result packages a reusable fact from 7.6. Zusammenhang; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Sequences, convergence, inequalities, and set/topology language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 7.6.9 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.1.3 — 8.1. Definition und einfache Regeln

- **Theorem name:** Satz 8.1.3 
- **Source:** PDF p152; section 8.1. Definition und einfache Regeln
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Zu (i): Mit T wie in der Definition gilt f (a + tv) = f (a) + tT (v) + \| tv\|r(a + tv) für v \in V , t \in R, mit | t| < r (wobei Br(a) \subset D). Dann gilt f (a + tv) − f (a) t − T(v) = | t| · \|v\| t r(a + tv), t ̸= 0,| t| < r,     f (a + tv) − f (a) t − T(v)     = \| v\|\|r(a + tv)\| → 0, t → 0,| t| < r, Zu (ii): Es gibt C ≥ 0, so dass für alle v \in V gilt \|T(v)\| ≤ C\|v\|. Dann gilt \| f (a + h) − f (a)\| =  T(h) + \| h\|r(h)   ≤ \| T(h)\| + \| h\| · \|r(h)\| ≤ (C + \| r(h)\|) \|h\|. Da \|r(h)\| → 0, h → 0 gilt auch f (x) → f (a), x → a. □ 8.1.4. Beispiele. (1) Eine konstante Abbildung f : D \to W ist differenzierbar in D, und d f (x) = 0 \in L(V ,W) für alle x \in D. (2) Eine lineare Abbildung T \in L(V ,W) ist differenzierbar und dT (x) = T \in L(V ,W) für alle x \in V . Daher ist dT eine konstante Abbildung mit Werten in L(V ,W); ihr Wert ist aber die i.A. nicht konstante Abbildung T. (3) Seien V1, . . . ,Vn,W endlichdimensionale normierte Vektorräume. Dann ist jede multilineare Abbildung T : V1 × . . .× Vn \to W stetig. Daraus folgt, dass T differenzierbar ist und dT (x1, . . . ,xn)[v1, . . . ,vn] = T(v1, x2, . . . ,xn) + T(x1, v2, x3, . . . ,xn) + . . .+ T(x1, . . . ,xn− 1, vn). Als Beispiel betrachten wir det : Mn× n(R) \to R. Für A \in Mn× n(R) schreiben wir A = (a1, . . . ,an) wobei a1, . . . ,an \in Rn die Spalten von A sind. Wir haben einen Isomorphismus Mn× n(R) \to Rn × . . .× Rn, A \mapsto(a1, . . . ,an) \in Rn × . . .× Rn. Damit ist die Abbildung det : Rn × . . .× Rn \to R eine multilineare Abbildung. Sei H \in Mn× n(R). Dann gilt d(det)( A) ·H = det(h1, a2, . . . ,an) + . . .+ det(a1, . . . ,an− 1, hn) = n\sum i, j= 1 hi j Ai j , wobei Ai j die Kofaktoren (algebraische Komplementen) von ai j in A sind. Wenn A# = (A ji )1\lei, j\len, d…
```
- **Key idea:** This result packages a reusable fact from 8.1. Definition und einfache Regeln; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Metric/normed spaces, one-variable differentiability, and linear algebra.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 8.1.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 8.1.5 — Reduktionsregel

- **Theorem name:** Satz 8.1.5 Reduktionsregel
- **Source:** PDF p152; section 8.1. Definition und einfache Regeln
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
′′⇒ ′′ Sei f (a + h) = f (a) + T(h) + ρ(h), mit lim h→ 0 ρ(h) \|h\| = 0. Dabei ist T : V → W1 × W2 linear also T = (T1, T2) mit Ti : V → Wi linear . Außerdemρ : D → W1 × W2 hat die Form ρ = (ρ1, ρ2) und ρ(h) \|h\| = (ρ1(h) \|h\| , ρ2(h) \|h\| ) ANALYSIS I-III, 2011/2013 151 also ρ1(h) \|h\| → 0, ρ2(h) \|h\| → 0, h → 0 ❀ f i(a + h) = f i(a) + Ti(h) + ρi(h), i = 1,2 ❀ f i differenzierbar in a und d f (a) = (d f1(a), d f2(a)) ′′⇐ ′′analog.
```
- **Key idea:** This result packages a reusable fact from 8.1. Definition und einfache Regeln; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Metric/normed spaces, one-variable differentiability, and linear algebra.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 8.1.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.1.8 — Kettenregel

- **Theorem name:** Satz 8.1.8 Kettenregel
- **Source:** PDF p153; section 8.1. Definition und einfache Regeln
- **Proof strategy in one sentence:** Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.
- **Full proof rewritten clearly:**
  Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Sei b = f (a). Nach Definition ist f (a + h) = f (a) + d f (a) ·h + r(h), r(h) = o(\|h\|) für h → 0, sowie g(b + k) = g(b) + d g(b) ·k + s(k), s(k) = o(\|k\|) für k → 0. Daraus folgt (g ◦ f )(a + h) = g( f (a + h)) = g ( f (a) = :b + d f (a) ·h + r(h)   = :k ) = g(b) + d g(b) [ d f (a) ·h + r(h) ) + s ( d f (a) ·h + r(h) ) = (g ◦ f )(a) + ( d g(b) ◦ d f (a) ) ·h + r2(h), (8.3) wobei r2(h) = d g(b)[r(h)] + s ( d f (a) ·h + r(h) ) . Es bleibt zu zeigen, dass r2(h) = o(\|h\|) für \|h\| → 0. Da d g(b) stetig ist, existiert C ≥ 0, so dass \|d g(b)·k\| ≤ C\|k\| für alle k \in W. Somit \|d g(b)[r(h)]\| ≤ C\|r(h)\|. Aus r(h) = o(\|h\|) folgt damit d g(b)[r(h)] = o(\|h\|). ANALYSIS I-III, 2011/2013 152 Ähnlich verfährt man mit dem zweiten Summanden von r2(h). Da d f (a) stetig ist, existiert C′ ≥ 0, so dass \|d f (a) ·h\| ≤ C′\|h\| für alle h \in V . Wegen lim h→ 0 \|r(h) \|h\| = 0 existiert ein \varepsilon > 0, so dass für \|h\| < \varepsilon gilt: \|r(h)\| ≤ \| h\|. Mit der Dreiecksungleichung folgt dann für \|h\| < \varepsilon:  d f (a) ·h + r(h)   ≤ C′′\|h\|, C′′= C′+ 1. Daraus ergibt sich schließlich mit s(k) = o(\|k\|) und k = d f (a) ·k + r(h) → 0 für h → 0, dass 1 \|h\| s ( d f (a) ·k + r(h) ) = 1 \|h\| s ( k ) = \|k\| \|h\| beschänkt 1 \|k\| s ( k ) → 0, h → 0. Somit gilt insgesamt r2(h) = o(\|h\|), für h → 0, und der Beweis ist abgeschlossen. □
```
- **Key idea:** Linear approximations compose.
- **Dependency list:** Differential as linear map.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.
- **Active recall prompts:**
  1. State Satz 8.1.8 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** OCR/math symbol normalization should be manually checked.

## Proof 8.1.9 — Leibniz-Regel

- **Theorem name:** Satz 8.1.9 Leibniz-Regel
- **Source:** PDF p154; section 8.1. Definition und einfache Regeln
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
\varphi ( f1, f2) ist die zusammengesetzte Abbildung D ( f1,f2) \to W1 × W2 \varphi \to Z. Nach der Kettenregel folgt: \varphi ( f1, f2) ist differenzierbar in a, und d\varphi ( f1, f2)(a) ·h = d\varphi ( f1(a), f2(a)) ·(d f1(a) ·h, d f2 (a) ·h) = \varphi (d f1(a) ·h, f2(a)) + \varphi ( f1(a), d f2(a) ·h) .
```
- **Key idea:** This result packages a reusable fact from 8.1. Definition und einfache Regeln; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Metric/normed spaces, one-variable differentiability, and linear algebra.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 8.1.9 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.2.10 — Hauptkriterium für Differenzierbarkeit

- **Theorem name:** Satz 8.2.10 Hauptkriterium für Differenzierbarkeit
- **Source:** PDF p157; section 8.2. Richtungsableitungen und partielle Ableitungen
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** Continuous partial derivatives are enough to assemble a true linear approximation.
- **Dependency list:** Partial derivatives, Jacobian, continuity.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 8.2.10 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.3.7 — Schrankensatz

- **Theorem name:** Satz 8.3.7 Schrankensatz
- **Source:** PDF p158; section 8.3. Mittelwertsatz und Schrankensatz
- **Proof strategy in one sentence:** Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** Derivative bounds control total change.
- **Dependency list:** Integral representation and operator norm.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction.
- **Active recall prompts:**
  1. State Satz 8.3.7 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.4.3 — Satz von Schwarz

- **Theorem name:** Satz 8.4.3 Satz von Schwarz
- **Source:** PDF p159; section 8.4. Höhere Ableitungen und der Satz von Schwarz
- **Proof strategy in one sentence:** Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
O.B.d.A. n = 2, a = (0,0), i = 1, j = 2. Dann gilt: ∂2(∂1 f )(0,0) = lim h→ 0 1 h [ (∂1 f )(0, h) − (∂1 f )(0,0) ] = lim h→ 0 1 h [ lim k→ 0 f (k, h) − f (0, h) k − lim k→ 0 f (k,0) − f (0,0) k ] = lim h→ 0 lim k→ 0 1 hk [ f (k, h) − f (0, h) − f (k,0) + f (0,0) ] Sei zunächst k und h fest. Nun verwenden wir den Mittelwertsatz für gk(y) := f (k, y) − f (0, y): f (k, h) − f (0, h) − f (k,0) + f (0,0) = gk(h) − gk(0) = hg ′ k(η) für ein η zwischen 0 und h. Aber g′ k(η) = ∂2 f (k, η) − ∂2 f (0, η). Setze r(x) = ∂2 f (x, η). Wir verwenden erneut den Mittelwertsatz: r(k) − r(0) = kr′(\xi) = k∂1(∂2 f )(\xi, η) für ein \xi zwischen 0 und k. Also: Für alle k, h gibt es \xi, η (mit \xi zwischen 0 und k, sowie η zwischen 0 und h) mit [ f (k, h) − f (0, h) − f (k,0) + f (0,0)] = hk∂1(∂2 f )(\xi, η) Da ∂1∂2 f stetig ist und \xi, η → 0 für k, h → 0 gilt, folgt: ∂2(∂1 f )(0,0) = lim h→ 0 lim k→ 0 ∂1(∂2 f )(\xi, η) = ∂1(∂2 f )(0,0). □ Die Aussage des Satzes von Schwarz trifft insbesondere für z weimal stetig differenzierbaren Funktionen zu (siehe Def. 8.4.5).
```
- **Key idea:** With enough regularity, the order of differentiating in two directions does not matter.
- **Dependency list:** Partial derivatives and continuity.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use epsilon-delta or sequential continuity and track the relevant neighborhoods.
- **Active recall prompts:**
  1. State Satz 8.4.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.5.3 — Taylorformel

- **Theorem name:** Satz 8.5.3 Taylorformel
- **Source:** PDF p161; section 8.5. Die Taylorformel
- **Proof strategy in one sentence:** Apply one-variable Taylor reasoning along the segment from the base point to the evaluation point.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** Multivariable functions have polynomial local models governed by higher differentials.
- **Dependency list:** Higher differentials and one-variable Taylor along line segments.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Apply one-variable Taylor reasoning along the segment from the base point to the evaluation point.
- **Active recall prompts:**
  1. State Satz 8.5.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.6.3 — Fermatsches Kriterium

- **Theorem name:** Satz 8.6.3 Fermatsches Kriterium für lokale Extrema
- **Source:** PDF p161; section 8.6. Lokale Extrema
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** At an interior optimum, every first-order direction has zero slope.
- **Dependency list:** Differentiability and one-dimensional extremum idea along lines.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 8.6.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.6.4 — Hinreichendes Kriterium für lokale Extrema

- **Theorem name:** Satz 8.6.4 Hinreichendes Kriterium für lokale Extrema
- **Source:** PDF p161; section 8.6. Lokale Extrema
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** The quadratic part determines local shape when it is decisive.
- **Dependency list:** Taylor formula and Hessian definiteness.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 8.6.4 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 8.9.3 — 8.9. Notizen: Komplexe Differenzierbarkeit

- **Theorem name:** Satz 8.9.3 
- **Source:** PDF p164; section 8.9. Notizen: Komplexe Differenzierbarkeit
- **Proof strategy in one sentence:** Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
(i) \Longleftrightarrow (ii) ist klar , da HomC(C,C) \subset HomR(C,C). Zu (ii) \Longleftrightarrow (iii): d f (z0) \in HomC(C,C) \Longleftrightarrow \exists \lambda \in C mit d f (z0)(z) = \lambda ·z \Longleftrightarrow \exists \lambda \in C mit d f (z0) ·1 = \lambda , d f (z0) ·i = i\lambda . d.h. das folgende Diagramm kommutiert: C z\mapsto\lambda·z − − − − \toC z\mapsto(x,y)   ↓   ↓z\mapsto(x,y) R2 − − − − \to d f (z0) R2 Aber ∂f ∂x (z0) = d f (z0) ·e1 und ∂f ∂x (z0) = d f (z0) ·e2, wobei e1 = (1,0) und e2 = (0,1). Durch den Isomorphismus R2 ∼ = C, ( x, y) \mapstox + i y werden e1 und e2 auf 1 und i abgebildet. Es folgt d f (z0) ·1 = ∂f ∂x (z0) , d f (z0) ·i = ∂f ∂y (z0) . Also d f (z0) \in HomC(C,C) \Longleftrightarrow (8.8). Wenn wir Realteil und Imaginärteil von (8.8) betrach ten, erhalten wir (8.9). □ Führen wir die folgenden partiellen differentiellen Opera toren ein: (8.11) ∂f ∂z = 1 2 (∂f ∂x − i ∂f ∂y ) , ∂f ∂z = 1 2 (∂f ∂x + i ∂f ∂y ) Damit gilt d f (z0) = ∂f ∂z (z0)dz + ∂f ∂z (z0)dz. Die Cauchy-Riemannschen Gleichungen (8.8) werden (8.12) ∂f ∂z (z0) = 0 . Ist f komplex-diferrenzierbar , so gilt nach (8.8), (8.11) (8.13) ∂f ∂z (z0) = ∂f ∂x (z0) = d f (z0) ·1 = f ′(z0). Wenn wir z und z als Variablen betrachten und eine Funktion f (x, y) = f (z + z 2 , z − z 2i ) nach z und z mittels Kettenregel ableiten, erhalten wir die Formel (8.1 1). Dies bedeutet, dass wir ∂f ∂z , ∂f ∂z durch formelles Differenzieren nach den Variablen z und z erhalten. Dies erleichtert viele Rechnungen. Z.B. ∂ ∂z zn = nz n− 1, ∂ ∂z zn = 0. ∂ ∂z | z| 2 = ∂ ∂z (zz) = z. ANALYSIS I-III, 2011/2013 164 9. U MKEHRSATZ UND SATZ ÜBER IMPLIZITE FUNKTIONEN 9.1. Banachscher Fixpunktsatz. Viele Gleichungen kann man in die Form f (x) = x bringen. Beispiel: Für gegebenes a > 0 ist x2 = a ist äqu…
```
- **Key idea:** This result packages a reusable fact from 8.9. Notizen: Komplexe Differenzierbarkeit; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Metric/normed spaces, one-variable differentiability, and linear algebra.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails.
- **Active recall prompts:**
  1. State Satz 8.9.3 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 9.1.2 — Banachscher Fixpunktsatz

- **Theorem name:** Satz 9.1.2 Banachscher Fixpunktsatz
- **Source:** PDF p166; section 9.1. Banachscher Fixpunktsatz
- **Proof strategy in one sentence:** Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.
- **Full proof rewritten clearly:**
  Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** Repeated shrinking forces all iterates into one unavoidable point.
- **Dependency list:** Complete metric spaces, Cauchy sequences, contractions.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.
- **Active recall prompts:**
  1. State Satz 9.1.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 9.2.5 — Umkehrsatz

- **Theorem name:** Satz 9.2.5 Umkehrsatz
- **Source:** PDF p168; section 9.2. Der Umkehrsatz
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** An invertible linearization makes the nonlinear map locally invertible.
- **Dependency list:** Differentials, Banach fixed point/estimates, inverse derivative rule.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 9.2.5 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 9.3.1 — Satz über implizite Funktionen

- **Theorem name:** Satz 9.3.1 Satz über implizite Funktionen
- **Source:** PDF p171; section 9.3. Der Satz über implizite Funktionen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.
- **Key idea:** A nondegenerate equation can locally be solved for the chosen variables.
- **Dependency list:** Inverse function theorem and block differentials.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 9.3.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 9.3.2 — 9.3. Der Satz über implizite Funktionen

- **Theorem name:** Folgerung 9.3.2 
- **Source:** PDF p171; section 9.3. Der Satz über implizite Funktionen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Für alle x \in U ′ gilt F(x) := f (x, g(x)) = z0, d.h. F ist konstant, also für alle h \in Rm: 0 = dF (x) ·h = d f ( (x, g(x)) ) ·(h, d g(x) ·h) = dx f (x, g(x)) ·h + d y f (x, g(x)) ·(d g(x) ·h) . Daraus folgt: d g(x0) ·h = − (d y f (x0, y0))− 1dx f (x0, y0) ·h. □
```
- **Key idea:** This result packages a reusable fact from 9.3. Der Satz über implizite Funktionen; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** Complete metric spaces, differential estimates, inverse/differential calculus.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Folgerung 9.3.2 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof 9.4.1 — Multiplikatorregel von Lagrange

- **Theorem name:** Satz 9.4.1 Multiplikatorregel von Lagrange
- **Source:** PDF p174; section 9.4. Extrema unter Nebenbedingungen
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Angenommen, die Vektoren {grad f (a),grad \varphi 1(a), . . . ,grad \varphi m(a)} wären linear unabhängig; insbe- sondere m + 1 \le n. Wir betrachten dann in den n + 1 Variablen ( x1, . . . ,xn, y) = (x, y) das Gleichungssystem f (x1, . . . ,xn)− y = 0, \varphi 1(x1, . . . ,xn) = 0,· · ·, \varphi m(x1, . . . ,xn) = 0 nahe (a, f (a)). Seine Jacobi-Matrix nach x = (x1, . . . ,xn) hat laut Annahme in x = a den Zeilenrang m + 1, also auch den Spaltenrang m + 1. Es kann somit nahe (a, f (a)) \in Rn+ 1 nach geeigneten m + 1 der Variablen x1, . . . ,xn aufgelöst werden. Daraus folgt, dass in jeder Umgebung von a sowohl y > f (a) wie auch y < f (a) möglich ist (unter Wahrung der Nebenbedingungen). Wi- derspruch! Rezept. Zur Bestimmung der Kandidaten für Extremstellen von f : U \to R unter den Nebenbedingungen \varphi = 0 mit \varphi : U \to Rm, wobei Rang J\varphi (x) = m für alle x mit \varphi (x) = 0 sei, bildet man die Lagrange-Funktion L : U × Rm \to R, L(x, \lambda) = f (x) + \summ j= 1 \lambda j \varphi j(x) und sucht die Lösungen des Systems grad L(x, \lambda) = 0, d.h. ∂L ∂xi (x, \lambda) = ∂f ∂xi + m\sum j= 1 \lambda j ∂\varphi j ∂xi = 0 für 1 \le i \le n und ∂L ∂\lambda j (x, \lambda) = \varphi j(x) = 0 für 1 \le j \le m . Das sind n + m Gleichungen für die n + m Variablen x1, . . . ,xn, \lambda1, . . . ,\lambdam. Nach dem Lösen kann man die \lambda j wieder vergessen.
```
- **Key idea:** At a constrained optimum, the objective gradient has no component tangent to the constraint surface.
- **Dependency list:** Implicit function theorem, gradients, extrema.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz 9.4.1 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof A.1.9 — Aussagenlogische Gesetze

- **Theorem name:** Satz A.1.9 Aussagenlogische Gesetze
- **Source:** PDF p179; section A.1. Aussagenlogik
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Betrachten wir z.B. die Abtrennungsregel. Wir können sie be weisen, indem wir die Wahrheitswert- tabelle erstellen. A B A ⇒ B A ∧ (A ⇒ B) (A ∧ (A ⇒ B)) ⇒ B w w w w w w f f f w f w w f w f f w f w Da in der Kolonne für die Formel (A.7) immer der Wahrheitswer t w steht, ist die Formel eine Tautologie. Eine andere Möglichkeit ist, die Formel mit Hilfe der aussagenlo gischen Gesetze zu einer Tautologie zu transfor- mieren. Es ist (A ∧ (A ⇒ B)) ⇒ B äq. ( A ∧ (¬ A ∨ B)) ⇒ B (nach (A.6)) (A ∧ (¬ A ∨ B)) ⇒ B äq. (( A ∧ ¬ A) ∨ (A ∧ B)) ⇒ B (nach (A.4)) ((A ∧ ¬ A) ∨ (A ∧ B)) ⇒ B äq. (⊥ ∨ (A ∧ B)) ⇒ B (nach (A.2)) (⊥ ∨ (A ∧ B)) ⇒ B äq. ( A ∧ B) ⇒ B (nach (A.1)) Weil ( A ∧ B) ⇒ B eine Tautologie (Abschwächungsregel) ist und (A.7) damit ä quivalent ist, ist auch (A.7) eine Tautologie. Wir erstellen die Wahrheitstabelle zum Kontrapositionsge setz: ANALYSIS I-III, 2011/2013 178 A B A ⇒ B ¬ B ¬ A ¬ B ⇒ ¬ A (A ⇒ B) \Longleftrightarrow (¬ B ⇒ ¬ A) w w w f f w w w f f w f f w f w w f w w w f f w w w w w Da in der Kolonne für die Formel (A.8) immer der Wahrheitswer t w steht, ist die Formel eine Tautologie. □ A.2. Prädikatenlogik.
```
- **Key idea:** This result packages a reusable fact from A.1. Aussagenlogik; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** None beyond ordinary mathematical language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz A.1.9 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof A.3.6 — A.3. Beweistechnik

- **Theorem name:** Satz A.3.6 
- **Source:** PDF p182; section A.3. Beweistechnik
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir beweisen den Satz durch Kontraposition. Wir bezeichnen A: „In einer Schule gibt es 733 Schüler .“ B: „Es gibt in einem Jahr mindestens 3 Schüler , die ihren Gebu rtstag am gleichen Tag feiern.“ Zu zeigen: A ⇒ B. Wir beweisen die logisch äquivalente Aussage ¬ B ⇒ ¬ A, d.h. wir nehmen an, ¬ B wäre wahr , und leiten daraus einen Widerspruch zu A her . ¬ B: „Es gibt höchstens 2 Schüler , die ihren Geburtstag am gleic hen Tag feiern.“ ⇒ „Es gibt höchstens 2 × 366 = 732 Schüler in der Schule.“ ⇒ „Es gibt nicht 733 Schüler in der Schule.“: ¬ A □ ANALYSIS I-III, 2011/2013 181
```
- **Key idea:** This result packages a reusable fact from A.3. Beweistechnik; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** None beyond ordinary mathematical language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz A.3.6 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof A.3.8 — A.3. Beweistechnik

- **Theorem name:** Satz A.3.8 
- **Source:** PDF p183; section A.3. Beweistechnik
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Wir beweisen den Satz durch Kontraposition. Um die Kontrapo sition der Aussage zu bilden, ist es hilfreich, die Implikation als logische Formel zu schreibe n: 3 ̸ | n ∨ 3 ̸ | m ⇒ 3 ̸ | (m + n) ∨ 3 ̸ | (m − n) . Unter Benutzung der de Morganschen Regel erhält man die zuge hörige Kontraposition: 3| (m + n) ∧ 3| (m − n)) ⇒ 3| m ∧ 3| n . Um diese Implikation für beliebige ganze Zahlen zu zeigen, g enügt es den Fall zu betrachten, in dem die linke Seite wahr ist. (Andernfalls ist die Implikation sowieso wa hr .) Gelte also m + n = 3k und m − n = 3k0 mit k, k0 \in Z. Addition der beiden Gleichungen ergibt: 2 m = 3(k + k0). Die rechte Seite davon muss also durch 2 teilbar sein. Da 2 und 3 teilerfremd sind, ist k + k0 durch 2 teilbar , also m = 3(k + k0)/2. Damit ist also m durch 3 teilbar . Subtraktion der Gleichungen ergibt 2n = 3(k− k0). Wie oben kann man schließen, dass n = 3(k− k0)/2, also ist auch n durch 3 teilbar . □ Der Beweis durch Widerspruch beruht auf dem Gesetz (A.9). Wenn ein Satz in der Form A ⇒ B vorliegt, gewinnen wir einen Beweis des Satzes, indem wir eine Implika tion A ∧ ¬ B ⇒ ⊥ beweisen, wobei ⊥ eine falsche Aussage ist. Wir nehmen also ¬ B mit als Voraussetzung auf und leiten mit Hilfe der Abschluss regeln daraus einen Widerspruch her , d.h. eine falsche Aussage, z.B. ( x \in M und x ̸\in M) oder ( a = b und a ̸= b).
```
- **Key idea:** This result packages a reusable fact from A.3. Beweistechnik; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** None beyond ordinary mathematical language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz A.3.8 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.

## Proof A.3.10 — A.3. Beweistechnik

- **Theorem name:** Satz A.3.10 
- **Source:** PDF p183; section A.3. Beweistechnik
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Die Konklusion ist B :“ \sqrt 2 ist irrational.“ Das Gegenteil ist ¬ B :“ \sqrt 2 ist rational.“ Die folgende Schluss- kette gilt: x = \sqrt 2 ist rational : \Longleftrightarrow \exists p, q \in Z, q ̸= 0 : x = p/q = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : x = p/q = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : 2 = x2 = p2/q2 = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : 2p2 = q2 = ⇒ \exists p, q \in Z, q ̸= 0 und (p, q) = 1 : 2| p und 2| q . (A.21) Die letzte Implikation zeigt man so: 2p2 = q2 \Rightarrow 2| q2 \Rightarrow 2| q \Rightarrow \exists k \in Z : q = 2k = ⇒ q2 = 4k2 \Rightarrow 4k2 = q2 = 2p2 \Rightarrow 2k2 = p2 \Rightarrow 2| p2 \Rightarrow 2| p = ⇒ 2| q und 2| p . Die letzte Behauptung von (A.21) ( \exists p, q \in Z, q ̸= 0 und ( p, q) = 1 : 2 | p und 2| q) ist offensichtlich falsch. Wir haben also gezeigt, dass ¬ B \Rightarrow ⊥ wahr ist. Das ist aber nur möglich, wenn ¬ B falsch ist (siehe Wahrheitswert- tabelle der Implikation), d.h. wenn B wahr ist. □ In der Praxis wird man die Voraussetzung, Behauptung usw . ni cht explizit angeben und bezeichnen. Ein nor- maler Beweis beginnt mit „Nehmen wir an, x = \sqrt 2 wäre rational“ und fährt fort, bis man die falsche Aussage „\exists p, q \in Z, q ̸= 0 und (p, q) = 1 : 2| p und 2| q“ hergeleitet hat. Dann schreibt man einfach „Widerspruch“ , und der Beweis ist vollbracht!
```
- **Key idea:** This result packages a reusable fact from A.3. Beweistechnik; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** None beyond ordinary mathematical language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz A.3.10 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** Very short extracted statement; verify against PDF.

## Proof A.3.13 — Euklid

- **Theorem name:** Satz A.3.13 Euklid
- **Source:** PDF p184; section A.4. Mengenlehre
- **Proof strategy in one sentence:** Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Full proof rewritten clearly:**
  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.

  **Script proof transcription (OCR-normalized; verify symbols):**
```text
Bezeichnen wir die Menge der Primzahlen von N mit P \subset N. Nehmen wir an, P wäre endlich, P = {p1, . . . ,pk}. Sei n := p1 . . .pk+ 1 \in N; da n > p j für alle j = 1, . . . ,k, ist n ̸\in P. Der Fundamentalsatz der Arithmetik besagt, dass es eine Primzahl p \in P mit p| n gibt. Weil p eine der Zahlen p1, . . . ,pk ist, folgt p| p1 . . .pk und dann p| n − p1 . . .pk = 1. Wenn aber p| 1 gilt, muss p = 1 sein. Widerspruch zur Definition der Primzahlen. Die Menge P muss also unendlich sein. □ Für weitere Beispiele und eine „Gebrauchsanleitung zur For mulierung mathematischer Gedanken mit vie- len praktischen Tipps“ siehe das Buch [3]. Eine Geschichte des Beweisbegriffes findet man auch in "‘The History and Conce pt of A.4. Mengenlehre. Die Mengenlehre dient heute weitgehend als Grundlage der Ma thematik, und viele fun- damentale Begriffe und Methoden lassen sich auf die Mengenl ehre zurückführen. Der Begründer der Mengentheorie ist Georg Cantor (1845–191 8). Er hat die Mengenvorstellung folgender- maßen ausgedrückt: „Unter einer „Menge“ verstehen wir jede Zusammenfassung M von bestimmten wohlunterschiedenen Objekten unserer Anschauung oder unseres Denkens (welche die „Eleme nte“ von M genannt werden) zu einem Ganzen“. Es handelt sich um eine „naive“ Definition. Was bedeutet „Zus ammenfassung“ oder „Objekt unserer An- schauung“ ? Diese Vorstellung führt zu Kontradiktionen, de n sogenannten Russellschen Antinomien. Um diese Antinomien auszuschließen, wurden mehrere Wege vorgeschlagen (Russell, Zermelo–Fraenkel, Gödel–Bernays). Zermelo (1871–1953) hat das erste brauchbare Axiomensyste m der Mengenlehre formuliert. Ohne in Details zu gehen, beschreiben wir kurz sein Vorgehen. Wir setzen vor aus, dass es zwei Typen von Objekten gibt, Ele- mente und Mengen. Diese Objekte kö…
```
- **Key idea:** This result packages a reusable fact from A.4. Mengenlehre; learn both its assumptions and where the conclusion can be applied.
- **Dependency list:** None beyond ordinary mathematical language.
- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.
- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result.
- **Active recall prompts:**
  1. State Satz A.3.13 with all assumptions.
  2. What is the first object introduced in the proof?
  3. Which earlier theorem or definition is the decisive step?
  4. Where does the proof use each hypothesis?
- **Uncertainty:** No major extraction warning detected.
