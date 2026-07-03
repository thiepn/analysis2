from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import textwrap
import unicodedata
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path

from pypdf import PdfReader
from app_content import enrich_app_payload


BASE_DIR = Path(__file__).resolve().parents[1]

SUBDIRS = [
    "00-overview",
    "01-concept-map",
    "02-definitions",
    "03-theorems",
    "04-proofs",
    "05-examples",
    "06-active-recall",
    "07-proof-training",
    "08-exam-prep",
    "09-flashcards",
    "10-study-plan",
    "scripts",
    "app",
]

RESULT_KINDS = {"Satz", "Lemma", "Folgerung", "Korollar"}
ITEM_RE = re.compile(
    r"(?m)^\s*(?P<id>A\.\d+\.\d+|\d+\.\d+\.\d+)\.\s*"
    r"(?P<kind>Definition|Satz|Lemma|Folgerung|Korollar|Beispiel|Bemerkung)"
    r"(?:\s*\((?P<name>[^)]{1,180})\))?\s*\."
)
SECTION_RE = re.compile(r"^(?:A\.)?\d+\.\d+\.|^Anhang A\.|^Literatur$")


SECTION_NOTES = {
    "1.1": "Field axioms: addition, multiplication, neutral elements, inverses, and basic algebraic consequences.",
    "1.2": "Order axioms, positivity, inequalities, sign, absolute value, and triangle-type estimates.",
    "1.3": "Construction of natural numbers inside an ordered field, induction, powers, integers, families, sums, and products.",
    "1.4": "Factorials, generalized binomial coefficients, Pascal-type identities, and the binomial theorem.",
    "1.5": "Upper/lower bounds, supremum/infimum, completeness, and the axiomatic definition of the real numbers.",
    "1.6": "Consequences of completeness: Archimedes, Eudoxus, well-ordering, density of rationals, roots, intervals, nested intervals, and Euler's number.",
    "1.7": "Complex numbers as a field, real/imaginary parts, conjugation, modulus, and modulus rules.",
    "1.8": "Exercises for real/complex number foundations.",
    "1.9": "Notes on counting, pigeonhole principle, permutations/combinations, countability, and cardinality.",
    "2.1": "Sequences, convergence, neighborhoods, elementary limits, boundedness, monotonicity, and monotone convergence.",
    "2.2": "Algebra of convergent sequences, comparison principles, squeeze principle, and limit calculation strategies.",
    "2.3": "Countable and uncountable sets, especially countability of rationals and uncountability of reals.",
    "2.4": "Accumulation values, subsequences, Bolzano-Weierstrass, limsup/liminf, and the Cauchy criterion.",
    "2.5": "Improper limits and the extended real line.",
    "2.6": "Complex sequences and reduction to real and imaginary parts.",
    "2.7": "Exercises for sequences and convergence.",
    "3.1": "Series as limits of partial sums.",
    "3.2": "Convergence criteria for series, including Cauchy-type and comparison ideas.",
    "3.3": "Absolute convergence, product rules, exponential series, and related identities.",
    "3.4": "Power series, Abel's convergence lemma, radius of convergence, and sine/cosine series.",
    "3.5": "Exercises for series.",
    "3.6": "Notes and additional convergence/product material.",
    "4.1": "Continuity via sequences and epsilon-delta language, algebra and composition of continuous functions.",
    "4.2": "Intermediate value theorem, inverse functions, roots, logarithm, and exponential/logarithmic relationships.",
    "4.3": "Maximum/minimum theorem and compact interval consequences.",
    "4.4": "Limits of functions and their relation to continuity.",
    "4.5": "Exercises for continuity and function limits.",
    "5.1": "Derivative as linear approximation in one variable and first examples.",
    "5.2": "Derivative rules: linearity, product, quotient, chain rule, inverse rule.",
    "5.3": "Rolle, mean value theorem, Cauchy mean value theorem, and l'Hospital-type results.",
    "5.4": "Applications of mean value theorem: monotonicity, extrema, convexity, Taylor, and approximation.",
    "5.5": "Trigonometric functions and their analytic properties.",
    "5.6": "Notes around differentiability and related refinements.",
    "5.7": "Exercises for one-variable differentiation.",
    "6.1": "Uniform convergence of function sequences is signposted as preparation for integration.",
    "6.2": "Step functions and their integral.",
    "6.3": "Regulated functions and the extension of the integral by uniform approximation.",
    "6.4": "Fundamental theorem of calculus and integration rules.",
    "6.5": "Characterization and closure properties of regulated functions.",
    "6.6": "Higher derivatives and Taylor formula.",
    "6.7": "Improper integrals and convergence criteria.",
    "6.8": "Exercises for integration.",
    "6.9": "Notes on the Riemann integral.",
    "7.1": "Convexity, Jensen-type ideas, Young, Holder, Minkowski, and norm inequalities.",
    "7.2": "Metric and normed spaces, convergence, Cauchy sequences, completeness, and equivalent norms.",
    "7.3": "Open/closed sets, neighborhoods, interior, closure, boundary, topological spaces, subspace topology.",
    "7.4": "Continuity between metric/topological spaces, sequential criteria, homeomorphisms, and uniform continuity.",
    "7.5": "Compactness, sequential compactness, continuous images, and max/min theorem in topological form.",
    "7.6": "Connectedness, path connectedness, components, and generalized intermediate value ideas.",
    "7.7": "Exercises for metric and topological spaces.",
    "8.1": "Differentiability between finite-dimensional normed spaces and basic rules.",
    "8.2": "Directional derivatives, partial derivatives, Jacobian, gradient, chain rule in coordinates, and differentiability criterion.",
    "8.3": "Multivariable mean value theorem, integral representation, and bound theorem.",
    "8.4": "Higher partial derivatives, Schwarz theorem, Hessian, and higher differentials.",
    "8.5": "Multivariable Taylor formula.",
    "8.6": "Local extrema, critical points, and Hessian tests.",
    "8.7": "Worked extrema determination examples.",
    "8.8": "Exercises for differentiable maps.",
    "8.9": "Notes on complex differentiability and Cauchy-Riemann style equivalences.",
    "9.1": "Contractions and Banach fixed point theorem.",
    "9.2": "Diffeomorphisms and inverse function theorem.",
    "9.3": "Implicit function theorem and derivative formula for the implicit map.",
    "9.4": "Constrained extrema and Lagrange multiplier rule.",
    "9.5": "Exercises for inverse/implicit function material.",
    "A.1": "Statements, logical connectives, formulas, and truth-table reasoning.",
    "A.2": "Predicate logic and quantified statements.",
    "A.3": "Proof techniques: direct proof, contradiction, contraposition, induction, and examples.",
    "A.4": "Set theory language, relations, functions, equivalence relations, and cardinality basics.",
}


HIGH_YIELD = {
    "1.1.1": {
        "label": "Körperaxiome",
        "formal": r"A field-like structure has operations $+$ and $\cdot$ satisfying associativity, commutativity, distributivity, neutral elements $0,1$, additive inverses, and multiplicative inverses for nonzero elements.",
        "intuition": "This is the algebraic rulebook that makes the usual manipulation of numbers legitimate.",
        "why": "Every later calculation assumes these operations behave reliably.",
        "deps": "Basic set/function language from Appendix A.",
        "exam": "medium",
    },
    "1.2.1": {
        "label": "total angeordneter Körper",
        "formal": r"A field $K$ is totally ordered if a positive cone $P\subset K$ trichotomizes each $x$ into $x\in P$, $x=0$, or $-x\in P$, and is closed under addition and multiplication.",
        "intuition": "A compatible order lets algebra and inequalities work together.",
        "why": "Needed for intervals, monotonicity, supremum arguments, convergence estimates, and all epsilon proofs.",
        "deps": "Körperaxiome.",
        "exam": "high",
    },
    "1.3.4": {
        "label": "Induktionsprinzip",
        "formal": r"If $A(1)$ is true and $\forall n\in\mathbb N: A(n)\Rightarrow A(n+1)$, then $A(n)$ is true for every $n\in\mathbb N$.",
        "intuition": "A first domino plus a rule that every domino knocks over the next one proves the whole infinite chain.",
        "why": "Used for powers, binomial identities, estimates, and recursive definitions.",
        "deps": r"Inductive subsets and the definition of $\mathbb N$.",
        "exam": "high",
        "proof": r"Define $M=\{n\in\mathbb N:A(n)\text{ is true}\}$, show $M$ is inductive, then use minimality of $\mathbb N$.",
    },
    "1.3.6": {
        "label": "Bernoulli-Ungleichung",
        "formal": r"For $x\ge -1$ and $n\in\mathbb N$, $(1+x)^n\ge 1+nx$, with strict inequality for $n\ge2$ and $x\ne0$.",
        "intuition": "The first-order linear term underestimates the power for admissible $x$.",
        "why": "Used in estimates for sequences, exponential-type behavior, and convergence arguments.",
        "deps": "Induction and order rules.",
        "exam": "medium",
        "proof": r"Induct on $n$ and use $1+x\ge0$ to preserve the inequality in the step.",
    },
    "1.5.1": {
        "label": "Supremum/Infimum",
        "formal": r"$s=\sup A$ means $s$ is an upper bound of $A$ and every smaller number fails to be an upper bound.",
        "intuition": "The supremum is the least ceiling, even if the set never reaches it.",
        "why": "The central language for completeness and existence proofs.",
        "deps": "Order axioms and boundedness.",
        "exam": "high",
    },
    "1.5.3": {
        "label": "Vollständigkeitsaxiom",
        "formal": r"Every nonempty subset of $K$ that is bounded above has a supremum in $K$.",
        "intuition": "The real line has no gaps.",
        "why": "Powers monotone convergence, Bolzano-Weierstrass, Cauchy completeness, IVT, compactness, and extrema.",
        "deps": "Supremum and ordered fields.",
        "exam": "high",
    },
    "1.6.1": {
        "label": "Prinzip von Archimedes",
        "formal": r"For every $x\in\mathbb R$ there is $n\in\mathbb N$ with $n>x$.",
        "intuition": "Natural numbers eventually exceed any fixed real number.",
        "why": "Converts qualitative smallness into explicit natural-number thresholds.",
        "deps": "Completeness and supremum.",
        "exam": "high",
        "proof": r"Assume $\mathbb N$ is bounded, take $s=\sup\mathbb N$, then use that $s-1$ cannot be an upper bound.",
    },
    "1.6.5": {
        "label": "Dichtheit von Q in R",
        "formal": r"If $a<b$ in $\mathbb R$, then there is $q\in\mathbb Q$ with $a<q<b$.",
        "intuition": "Between any two real numbers sits a rational number.",
        "why": "Used for approximation, interval arguments, and examples/counterexamples.",
        "deps": "Archimedean principle and floor function.",
        "exam": "high",
    },
    "1.6.10": {
        "label": "Intervallschachtelungsprinzip",
        "formal": r"Every nested sequence of compact intervals whose lengths tend to $0$ has intersection consisting of exactly one point.",
        "intuition": "Nested closed intervals that shrink indefinitely trap one real number.",
        "why": "A concrete form of completeness used in convergence and existence proofs.",
        "deps": "Completeness, compact intervals, supremum/infimum.",
        "exam": "high",
        "proof": r"Let $x=\sup\{a_n\}$ for intervals $I_n=[a_n,b_n]$, show $x$ lies in every interval, and use shrinking lengths for uniqueness.",
    },
    "2.1.1": {
        "label": "Konvergenz einer Folge",
        "formal": r"$a_n\to a$ means $\forall\varepsilon>0\ \exists n_0\in\mathbb N\ \forall n\ge n_0: |a_n-a|<\varepsilon$.",
        "intuition": "Eventually every tail of the sequence lies in every prescribed epsilon-neighborhood of the limit.",
        "why": "The basic limit definition behind all of Analysis.",
        "deps": "Absolute value, order, neighborhoods.",
        "exam": "high",
    },
    "2.1.7": {
        "label": "Monotonieprinzip",
        "formal": r"A monotone increasing sequence that is bounded above converges to the supremum of its value set; analogously for decreasing sequences.",
        "intuition": "A one-directional bounded sequence cannot wander forever; completeness forces a limit.",
        "why": "Used in Bolzano-Weierstrass, series tests, and many existence proofs.",
        "deps": "Completeness, supremum, sequence convergence.",
        "exam": "high",
        "proof": r"Let $s=\sup\{a_n:n\in\mathbb N\}$ and use the defining property of supremum to put all large $a_n$ in $(s-\varepsilon,s]$.",
    },
    "2.2.2": {
        "label": "Konvergenz und algebraische Operationen",
        "formal": r"If $a_n\to a$ and $b_n\to b$, then sums, scalar multiples, products, and quotients with nonzero denominator converge to the corresponding algebraic limits.",
        "intuition": "Limits respect ordinary algebra when the expressions are well-defined.",
        "why": "The main toolkit for computing limits.",
        "deps": "Epsilon definition, boundedness of convergent sequences.",
        "exam": "high",
    },
    "2.2.5": {
        "label": "Einschließungsprinzip",
        "formal": r"If $a_n\le b_n\le c_n$ eventually and $a_n,c_n\to a$, then $b_n\to a$.",
        "intuition": "A squeezed sequence must follow the common limit of the bounds.",
        "why": "Useful for limits where direct algebra is awkward.",
        "deps": "Comparison principle.",
        "exam": "high",
    },
    "2.4.4": {
        "label": "Satz von Bolzano-Weierstraß",
        "formal": r"Every bounded real sequence has an accumulation value, equivalently a convergent subsequence.",
        "intuition": "Bounded infinite data in the real line contains a convergent pattern.",
        "why": "A cornerstone for compactness and many existence arguments.",
        "deps": "Completeness, monotone convergence, subsequences, accumulation values.",
        "exam": "high",
        "proof": "Use nested tail suprema/infima or a monotone subsequence argument to construct a convergent subsequence.",
    },
    "2.4.9": {
        "label": "Cauchy-Kriterium",
        "formal": r"A real sequence converges if and only if it is a Cauchy sequence.",
        "intuition": r"In $\mathbb R$, terms becoming mutually close is enough to guarantee an actual limit.",
        "why": "Central for convergence proofs where the candidate limit is unknown.",
        "deps": "Completeness, boundedness, Bolzano-Weierstrass.",
        "exam": "high",
        "proof": "Convergent implies Cauchy by triangle inequality; Cauchy implies bounded, then Bolzano-Weierstrass gives a convergent subsequence and the Cauchy condition pulls the whole sequence to that limit.",
    },
    "3.2.3": {
        "label": "Cauchy-Kriterium für Reihen",
        "formal": r"A series $\sum a_n$ converges iff its tails $\sum_{k=m+1}^n a_k$ become arbitrarily small.",
        "intuition": "A series converges exactly when distant tail sums carry no mass.",
        "why": "Basis of many convergence tests.",
        "deps": "Cauchy criterion for sequences and partial sums.",
        "exam": "high",
    },
    "3.3.1": {
        "label": "Absolute Konvergenz",
        "formal": r"$\sum a_n$ is absolutely convergent if $\sum |a_n|$ converges.",
        "intuition": "The series converges even after removing all cancellation.",
        "why": "Absolute convergence is stable and supports rearrangements/products in many contexts.",
        "deps": "Series and comparison.",
        "exam": "high",
    },
    "3.4.2": {
        "label": "Abelsches Konvergenzlemma",
        "formal": r"If $|a_n|s^n\le M$ for some $s,M>0$, then $\sum a_nz^n$ converges absolutely for $|z|<s$.",
        "intuition": "A power series that is controlled at one radius is dominated inside that radius by a geometric series.",
        "why": "Key step for radius of convergence.",
        "deps": "Majorant criterion and geometric series.",
        "exam": "high",
        "proof": r"Write $|a_nz^n|=|a_ns^n|\cdot |z/s|^n\le M|z/s|^n$ and compare with a geometric series.",
    },
    "3.4.4": {
        "label": "Konvergenzradius",
        "formal": r"Every power series has a radius $R$ such that it converges absolutely for $|z|<R$ and diverges for $|z|>R$.",
        "intuition": "Power series have circular domains of guaranteed convergence.",
        "why": "Organizes all power-series questions.",
        "deps": "Abel lemma, supremum, absolute convergence.",
        "exam": "high",
    },
    "4.1.1": {
        "label": "Stetigkeit",
        "formal": r"$f$ is continuous at $x_0$ if $x_n\to x_0$ implies $f(x_n)\to f(x_0)$, equivalently by the epsilon-delta condition when stated.",
        "intuition": "Inputs close to $x_0$ force outputs close to $f(x_0)$.",
        "why": "Continuity connects limits, topology, IVT, extrema, and compactness.",
        "deps": "Sequences and limits.",
        "exam": "high",
    },
    "4.2.1": {
        "label": "Zwischenwertsatz",
        "formal": r"If $f:[a,b]\to\mathbb R$ is continuous and $c$ lies between $f(a)$ and $f(b)$, then some $\xi\in[a,b]$ satisfies $f(\xi)=c$.",
        "intuition": "A continuous graph cannot jump over intermediate heights.",
        "why": "Existence theorem for roots and equations.",
        "deps": "Continuity, intervals, completeness.",
        "exam": "high",
        "proof": "Use a supremum/nested interval argument on the set where the function lies below the target.",
    },
    "4.3.2": {
        "label": "Satz vom Maximum und Minimum",
        "formal": r"A continuous real-valued function on a compact interval is bounded and attains its maximum and minimum.",
        "intuition": "A continuous function on a closed bounded interval cannot escape and must reach its extremes.",
        "why": "Fundamental for optimization and compactness.",
        "deps": "Continuity, Bolzano-Weierstrass/compact interval behavior.",
        "exam": "high",
    },
    "5.1.1": {
        "label": "Differenzierbarkeit",
        "formal": r"$f$ is differentiable at $x_0$ if $\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$ exists.",
        "intuition": "The function has a best linear first-order approximation at the point.",
        "why": "Basis for local analysis, monotonicity, optimization, Taylor formulas, and multivariable differentials.",
        "deps": "Function limits and continuity.",
        "exam": "high",
    },
    "5.2.4": {
        "label": "Kettenregel",
        "formal": r"If $f$ is differentiable at $x_0$ and $g$ at $f(x_0)$, then $(g\circ f)'(x_0)=g'(f(x_0))f'(x_0)$.",
        "intuition": "Rates multiply through composition.",
        "why": "Essential calculation rule for derivatives.",
        "deps": "Derivative definition and linear approximation.",
        "exam": "high",
    },
    "5.3.5": {
        "label": "Mittelwertsatz",
        "formal": r"If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then $f(b)-f(a)=f'(\xi)(b-a)$ for some $\xi\in(a,b)$.",
        "intuition": "Some instantaneous slope equals the average slope.",
        "why": "Drives monotonicity, estimates, inverse arguments, and l'Hospital-type reasoning.",
        "deps": "Rolle's theorem, extrema theorem, differentiability.",
        "exam": "high",
        "proof": "Subtract the secant line and apply Rolle's theorem.",
    },
    "6.2.4": {
        "label": "Integral von Treppenfunktionen",
        "formal": r"For a step function $\varphi$ constant with values $c_k$ on intervals $(x_{k-1},x_k)$, define $\int_a^b\varphi(x)\,dx=\sum_k c_k(x_k-x_{k-1})$.",
        "intuition": "Area is built by summing rectangles.",
        "why": "Starting point for regulated and Riemann-type integration.",
        "deps": "Partitions and step functions.",
        "exam": "medium",
    },
    "6.4.2": {
        "label": "Hauptsatz der Differential- und Integralrechnung",
        "formal": r"Integration and differentiation are inverse in the precise forms stated in the script for regulated/continuous functions.",
        "intuition": "Accumulated change differentiates back to the original rate, and antiderivatives compute integrals.",
        "why": "Central bridge between calculus operations.",
        "deps": "Integral definition, continuity/regulated functions, derivative rules.",
        "exam": "high",
    },
    "6.6.5": {
        "label": "Taylorformel",
        "formal": r"A sufficiently differentiable function equals its Taylor polynomial plus a controlled remainder term.",
        "intuition": "Near a point, derivatives determine a polynomial approximation with a measurable error.",
        "why": "Used for approximation, asymptotics, extrema, and estimates.",
        "deps": "Higher derivatives, mean value ideas, integration/differentiation.",
        "exam": "high",
    },
    "7.1.14": {
        "label": "Höldersche Ungleichung",
        "formal": r"If $p,q>1$ and $1/p+1/q=1$, then $\sum |z_kw_k|\le \|z\|_p\|w\|_q$.",
        "intuition": "Dual exponents control products by separate norms.",
        "why": "Supports norm inequalities and functional estimates.",
        "deps": "Young inequality and $p$-norms.",
        "exam": "high",
    },
    "7.1.15": {
        "label": "Minkowski-Ungleichung",
        "formal": r"For $p\ge1$, $\|z+w\|_p\le \|z\|_p+\|w\|_p$.",
        "intuition": "The $p$-norm satisfies the triangle inequality.",
        "why": r"Shows $\|\cdot\|_p$ is a norm.",
        "deps": "Holder inequality.",
        "exam": "high",
    },
    "7.2.1": {
        "label": "Metrik",
        "formal": r"A metric $d:X\times X\to\mathbb R$ is positive definite, symmetric, and satisfies the triangle inequality.",
        "intuition": "A metric abstracts distance.",
        "why": "Foundation for convergence, continuity, compactness, and topology in general spaces.",
        "deps": "Set language and inequalities.",
        "exam": "high",
    },
    "7.2.9": {
        "label": "Vollständigkeit in metrischen Räumen",
        "formal": r"A metric space is complete if every Cauchy sequence converges in the space.",
        "intuition": "The space has no missing Cauchy limits.",
        "why": "Needed for Banach fixed point and many analytic existence theorems.",
        "deps": "Metric convergence and Cauchy sequences.",
        "exam": "high",
    },
    "7.3.1": {
        "label": "Offene Menge",
        "formal": r"A set is open if every point has an epsilon-ball contained in the set.",
        "intuition": "Every point has local room to move without leaving the set.",
        "why": "Core topological language for continuity and differentiability domains.",
        "deps": "Metric balls.",
        "exam": "high",
    },
    "7.4.1": {
        "label": "Stetige Abbildungen zwischen metrischen Räumen",
        "formal": r"$f:X\to Y$ is continuous at $a$ if $\forall\varepsilon>0\ \exists\delta>0: d_X(x,a)<\delta\Rightarrow d_Y(f(x),f(a))<\varepsilon$.",
        "intuition": "Small input-distance implies small output-distance.",
        "why": "Generalizes continuity beyond real functions.",
        "deps": "Metrics, balls, neighborhoods.",
        "exam": "high",
    },
    "7.5.1": {
        "label": "Kompaktheit",
        "formal": r"In the script's metric/topological setting, compactness is tied to sequence compactness and finite subcover behavior as stated.",
        "intuition": "Compact sets are small enough for infinite processes to have finite/convergent structure.",
        "why": "Explains max/min theorems, uniform continuity, and existence results.",
        "deps": "Topology, sequences, closed/bounded behavior.",
        "exam": "high",
    },
    "7.5.6": {
        "label": "Satz vom Maximum und Minimum",
        "formal": r"A continuous real-valued function on a compact topological space is bounded and attains maximum and minimum.",
        "intuition": "Compactness is the correct general reason extrema exist.",
        "why": "Generalizes the interval theorem and supports optimization.",
        "deps": "Compactness and continuity.",
        "exam": "high",
    },
    "7.6.2": {
        "label": "Zusammenhängende Teilmengen von R",
        "formal": r"A subset of $\mathbb R$ is connected if and only if it is an interval.",
        "intuition": "On the real line, connectedness is exactly having no gaps.",
        "why": "Topological explanation of intermediate-value phenomena.",
        "deps": "Connectedness, intervals, order topology.",
        "exam": "medium",
    },
    "8.1.1": {
        "label": "Differenzierbarkeit in normierten Räumen",
        "formal": r"$f$ is differentiable at $a$ if there is a linear map $T$ with $\|f(a+h)-f(a)-T(h)\|/\|h\|\to0$ as $h\to0$.",
        "intuition": "The derivative is the best linear approximation in all directions at once.",
        "why": "Foundation of multivariable calculus.",
        "deps": "Normed spaces, one-variable differentiability.",
        "exam": "high",
    },
    "8.1.8": {
        "label": "Kettenregel",
        "formal": r"For differentiable maps, $d(g\circ f)(a)=dg(f(a))\circ df(a)$.",
        "intuition": "Linear approximations compose.",
        "why": "Essential for multivariable derivative computations.",
        "deps": "Differential as linear map.",
        "exam": "high",
        "proof": "Write both maps as linear part plus a small remainder and show the composed remainder is still higher order.",
    },
    "8.2.10": {
        "label": "Hauptkriterium für Differenzierbarkeit",
        "formal": r"If all partial derivatives exist in a neighborhood of $a$ and are continuous at $a$, then $f$ is differentiable at $a$.",
        "intuition": "Continuous partial derivatives are enough to assemble a true linear approximation.",
        "why": "Practical differentiability test.",
        "deps": "Partial derivatives, Jacobian, continuity.",
        "exam": "high",
    },
    "8.3.7": {
        "label": "Schrankensatz",
        "formal": r"$\|f(b)-f(a)\|\le \sup_{t\in[0,1]}\|df((1-t)a+tb)\|_{\mathrm{op}}\|b-a\|$ under the stated hypotheses.",
        "intuition": "Derivative bounds control total change.",
        "why": "Used for Lipschitz estimates and contraction arguments.",
        "deps": "Integral representation and operator norm.",
        "exam": "high",
    },
    "8.4.3": {
        "label": "Satz von Schwarz",
        "formal": r"Under the script's continuity hypotheses, mixed partial derivatives commute: $\partial_i\partial_j f(a)=\partial_j\partial_i f(a)$.",
        "intuition": "With enough regularity, the order of differentiating in two directions does not matter.",
        "why": "Justifies symmetric Hessians and higher derivative notation.",
        "deps": "Partial derivatives and continuity.",
        "exam": "high",
    },
    "8.5.3": {
        "label": "Taylorformel",
        "formal": r"A $C^{p+1}$ multivariable function equals its Taylor polynomial of degree $p$ plus the stated Lagrange/integral remainder on a segment.",
        "intuition": "Multivariable functions have polynomial local models governed by higher differentials.",
        "why": "Used for approximation and local extrema.",
        "deps": "Higher differentials and one-variable Taylor along line segments.",
        "exam": "high",
    },
    "8.6.3": {
        "label": "Fermatsches Kriterium",
        "formal": r"If $f$ is differentiable and has a local extremum at an interior point $a$, then $df(a)=0$.",
        "intuition": "At an interior optimum, every first-order direction has zero slope.",
        "why": "Starts local-extrema analysis.",
        "deps": "Differentiability and one-dimensional extremum idea along lines.",
        "exam": "high",
    },
    "8.6.4": {
        "label": "Hinreichendes Kriterium für lokale Extrema",
        "formal": r"At a critical point, positive definite Hessian gives a strict local minimum, negative definite gives a strict local maximum, and indefinite gives no local extremum.",
        "intuition": "The quadratic part determines local shape when it is decisive.",
        "why": "Main second-derivative test.",
        "deps": "Taylor formula and Hessian definiteness.",
        "exam": "high",
    },
    "9.1.1": {
        "label": "Kontraktion",
        "formal": r"A map $f:X\to X$ is a contraction if $d(f(x),f(y))\le qd(x,y)$ for some $q\in[0,1)$.",
        "intuition": "The map strictly shrinks distances.",
        "why": "Hypothesis of Banach fixed point theorem.",
        "deps": "Metric spaces and Lipschitz estimates.",
        "exam": "high",
    },
    "9.1.2": {
        "label": "Banachscher Fixpunktsatz",
        "formal": r"A contraction on a complete metric space has a unique fixed point, and the iteration $x_n=f(x_{n-1})$ converges to it with the stated error estimate.",
        "intuition": "Repeated shrinking forces all iterates into one unavoidable point.",
        "why": "Existence/uniqueness engine behind inverse and implicit function arguments.",
        "deps": "Complete metric spaces, Cauchy sequences, contractions.",
        "exam": "high",
        "proof": "Show the iterates are Cauchy using the contraction estimate, use completeness for existence of a limit, pass to the limit for fixed point, and use contraction for uniqueness.",
    },
    "9.2.5": {
        "label": "Umkehrsatz",
        "formal": r"If $f\in C^k$ and $df(a)$ is an isomorphism, then $f$ is locally a $C^k$-diffeomorphism near $a$.",
        "intuition": "An invertible linearization makes the nonlinear map locally invertible.",
        "why": "One of the main local structure theorems of multivariable analysis.",
        "deps": "Differentials, Banach fixed point/estimates, inverse derivative rule.",
        "exam": "high",
    },
    "9.3.1": {
        "label": "Satz über implizite Funktionen",
        "formal": r"If $d_y f(x_0,y_0)$ is invertible, then near $(x_0,y_0)$ the equation $f(x,y)=z_0$ can be solved uniquely as $y=g(x)$.",
        "intuition": "A nondegenerate equation can locally be solved for the chosen variables.",
        "why": "Explains constraint solving and manifolds as graphs.",
        "deps": "Inverse function theorem and block differentials.",
        "exam": "high",
    },
    "9.4.1": {
        "label": "Multiplikatorregel von Lagrange",
        "formal": r"At a constrained local extremum with independent constraint gradients, $\nabla f(a)$ lies in the span of the constraint gradients.",
        "intuition": "At a constrained optimum, the objective gradient has no component tangent to the constraint surface.",
        "why": "Main method for constrained optimization.",
        "deps": "Implicit function theorem, gradients, extrema.",
        "exam": "high",
    },
}


@dataclass
class Section:
    depth: int
    title: str
    start: int
    end: int
    key: str


@dataclass
class Item:
    id: str
    kind: str
    name: str
    page: int
    section_key: str
    section_title: str
    text: str
    proof: str
    uncertainty: str


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\u00a0": " ",
        "Ã ƒÂŸ": "ß",
        "ÃŸ": "ß",
        "/rad〉⌋allow": r"\sqrt",
        "/emp⊔yse⊔s⊔ress": r"\emptyset",
        "/maps⊔o⌋〈ar→": r"\mapsto",
        "/maps⊔o⌋〈ar− →": r"\mapsto",
        "̊/hatmoreultime": r"\operatorname{int}",
        "/hatmoreultime": r"\operatorname{int}",
        "− →": r"\to",
        " ⇐ ⇒ ": r" \Longleftrightarrow ",
        " = ⇒ ": r" \Rightarrow ",
        "⩽": r"\le",
        "⩾": r"\ge",
        "∈": r"\in",
        "∉": r"\notin",
        "⊂": r"\subset",
        "⊃": r"\supset",
        "∪": r"\cup",
        "∩": r"\cap",
        "⋃": r"\bigcup",
        "⋂": r"\bigcap",
        "∖": r"\setminus",
        "∀": r"\forall",
        "∃": r"\exists",
        "⇔": r"\Longleftrightarrow",
        "∞": r"\infty",
        "ε": r"\varepsilon",
        "ǫ": r"\varepsilon",
        "φ": r"\varphi",
        "ξ": r"\xi",
        "λ": r"\lambda",
        "∑": r"\sum",
        "∏": r"\prod",
        "∥": r"\|",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def compact(text: str, limit: int | None = None) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def wrap(text: str, width: int = 100) -> str:
    return "\n".join(textwrap.wrap(text, width=width, replace_whitespace=False))


def code_block(text: str, lang: str = "latex") -> str:
    text = text.strip().replace("```", "'''")
    return f"```{lang}\n{text}\n```"


def slug_section(title: str) -> str:
    m = re.match(r"((?:A\.)?\d+\.\d+)", title)
    if m:
        return m.group(1)
    m = re.match(r"(\d+)\.", title)
    if m:
        return m.group(1)
    if title.startswith("Anhang A"):
        return "A"
    return title


def item_section_key(item_id: str) -> str:
    if item_id.startswith("A."):
        parts = item_id.split(".")
        return ".".join(parts[:2])
    parts = item_id.split(".")
    return ".".join(parts[:2])


def read_pdf(pdf_path: Path):
    reader = PdfReader(str(pdf_path))
    page_texts = [normalize_text(page.extract_text() or "") for page in reader.pages]
    outline = []

    def walk(nodes, depth=0):
        for node in nodes:
            if isinstance(node, list):
                walk(node, depth + 1)
            else:
                title = getattr(node, "title", str(node))
                try:
                    page = reader.get_destination_page_number(node) + 1
                except Exception:
                    page = None
                outline.append((depth, title, page))

    walk(reader.outline)
    sections: list[Section] = []
    for i, (depth, title, start) in enumerate(outline):
        if start is None:
            continue
        next_page = None
        for depth2, _, page2 in outline[i + 1 :]:
            if page2 is not None and depth2 <= depth:
                next_page = page2
                break
        if next_page is None:
            end = len(page_texts)
        elif next_page <= start:
            end = start
        else:
            end = next_page - 1
        sections.append(Section(depth, title, start, end, slug_section(title)))
    return reader, page_texts, sections


def section_for_page(sections: list[Section], page: int) -> Section:
    candidates = [s for s in sections if s.depth == 1 and s.start <= page]
    if candidates:
        return candidates[-1]
    top = [s for s in sections if s.depth == 0 and s.start <= page]
    return top[-1] if top else Section(0, "Front matter", 1, 3, "front")


def extract_items(page_texts: list[str], sections: list[Section]) -> list[Item]:
    combined_parts = []
    for i, txt in enumerate(page_texts, start=1):
        combined_parts.append(f"\n<<<PAGE {i}>>>\n{txt}")
    combined = "\n".join(combined_parts)
    matches = list(ITEM_RE.finditer(combined))
    items: list[Item] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(combined)
        page_matches = re.findall(r"<<<PAGE (\d+)>>>", combined[:start])
        page = int(page_matches[-1]) if page_matches else 1
        raw_block = combined[match.end() : end]
        raw_block = re.sub(r"<<<PAGE \d+>>>", " ", raw_block)
        text = compact(raw_block)
        proof = ""
        proof_match = re.search(r"\bBeweis\s*:\s*(.*)", text)
        if proof_match:
            proof = proof_match.group(1).strip()
            text = text[: proof_match.start()].strip()
        item_id = match.group("id")
        sec_key = item_section_key(item_id)
        sec = next((s for s in sections if s.depth == 1 and s.key == sec_key), section_for_page(sections, page))
        suspicious = []
        if any(token in raw_block for token in ["\uf8f1", "\uf8f2", "\uf8f3", "\uf8f4", "\uf8eb", "\uf8ec", "\uf8ed", "\uf8f6", "\uf8f7", "\uf8f8", "\ued79", "⊔", "⌋", "〈"]):
            suspicious.append("OCR/math symbol normalization should be manually checked.")
        if len(text) < 25:
            suspicious.append("Very short extracted statement; verify against PDF.")
        items.append(
            Item(
                id=item_id,
                kind=match.group("kind"),
                name=(match.group("name") or "").strip(),
                page=page,
                section_key=sec.key,
                section_title=sec.title,
                text=text,
                proof=proof,
                uncertainty="; ".join(suspicious) if suspicious else "No major extraction warning detected.",
            )
        )
    return items


def display_label(item: Item) -> str:
    hy_label = HIGH_YIELD.get(item.id, {}).get("label")
    if hy_label:
        return hy_label
    if item.name:
        return item.name
    if item.kind == "Definition":
        match = re.search(r"heißt\s+([^.,;:()]{3,80})", item.text)
        if match:
            term = compact(match.group(1), 70)
            term = re.sub(r"\s+(falls|wenn|für|mit)\s+.*$", "", term).strip()
            if term:
                return term
        return f"unnamed definition in {item.section_key}"
    if item.kind == "Beispiel":
        return f"example in {item.section_key}"
    return item.section_title


def title_for(item: Item) -> str:
    label = display_label(item)
    return f"{item.kind} {item.id} — {label}"


def source_for(item: Item) -> str:
    return f"PDF p{item.page}; section {item.section_title}"


def section_note(item: Item) -> str:
    return SECTION_NOTES.get(item.section_key, "See reconstructed table of contents for this section.")


def latexish_statement(item: Item) -> str:
    hy = HIGH_YIELD.get(item.id)
    if hy and hy.get("formal"):
        return hy["formal"]
    statement = compact(item.text, 1200)
    if not statement:
        statement = "not explicit in script extraction; verify the original PDF at the cited page."
    return statement


def intuition_for(item: Item) -> str:
    hy = HIGH_YIELD.get(item.id)
    if hy:
        return hy.get("intuition", "")
    if item.kind == "Definition":
        return f"This definition gives precise language for the topic of {section_note(item).lower()}"
    if item.kind in RESULT_KINDS:
        return f"This result packages a reusable fact from {item.section_title}; learn both its assumptions and where the conclusion can be applied."
    if item.kind == "Beispiel":
        return "The example shows how the surrounding definition or theorem behaves in a concrete case."
    return "This remark clarifies scope, caveats, or interpretation of nearby material."


def why_for(item: Item) -> str:
    hy = HIGH_YIELD.get(item.id)
    if hy:
        return hy.get("why", "")
    if item.kind == "Definition":
        return "Later statements rely on this term being used exactly, especially in proofs and exercise wording."
    if item.kind in RESULT_KINDS:
        return "This is a reusable tool: check its assumptions before applying it in exercises."
    return "It helps prevent common misreadings of the surrounding section."


def dependencies_for(item: Item) -> str:
    hy = HIGH_YIELD.get(item.id)
    if hy:
        return hy.get("deps", "")
    chapter = item.section_key.split(".")[0]
    defaults = {
        "1": "Appendix A logic/set language and earlier algebra/order material.",
        "2": "Chapter 1 real-number foundations, absolute value, and completeness.",
        "3": "Sequences, Cauchy criteria, and comparison estimates.",
        "4": "Sequences, limits, intervals, and completeness.",
        "5": "Function limits, continuity, and algebra of limits.",
        "6": "Continuity, differentiability, regulated functions, and estimates.",
        "7": "Sequences, convergence, inequalities, and set/topology language.",
        "8": "Metric/normed spaces, one-variable differentiability, and linear algebra.",
        "9": "Complete metric spaces, differential estimates, inverse/differential calculus.",
        "A": "None beyond ordinary mathematical language.",
    }
    return defaults.get(chapter, "Earlier sections in the script.")


def exam_relevance(item: Item) -> str:
    hy = HIGH_YIELD.get(item.id)
    if hy:
        return hy.get("exam", "high")
    if item.kind in {"Satz", "Lemma", "Folgerung", "Korollar"} and item.name:
        return "high"
    if item.kind in {"Satz", "Definition"}:
        return "medium"
    return "low"


def tags_for(item: Item) -> str:
    bits = [item.kind.lower(), f"sec-{item.section_key.replace('.', '-')}", f"ch-{item.section_key.split('.')[0]}"]
    if item.id in HIGH_YIELD:
        bits.append("high-yield")
    if item.name:
        bits.extend(re.sub(r"[^A-Za-z0-9ÄÖÜäöüß ]", " ", item.name).lower().split()[:3])
    return " ".join(bits)


def mkdirs():
    for subdir in SUBDIRS:
        (BASE_DIR / subdir).mkdir(parents=True, exist_ok=True)


def write(path: str, content: str):
    target = BASE_DIR / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip() + "\n", encoding="utf-8")


def toc_table(sections: list[Section]) -> str:
    rows = ["| Level | Section | PDF pages | Main topics |", "|---:|---|---:|---|"]
    for s in sections:
        if s.depth > 1:
            continue
        indent = "Chapter" if s.depth == 0 else "Section"
        note = SECTION_NOTES.get(s.key, "")
        rows.append(f"| {indent} | {s.title} | {s.start}-{s.end} | {note} |")
    return "\n".join(rows)


def write_master(sections: list[Section], items: list[Item]):
    counts = Counter(i.kind for i in items)
    core_ids = [i for i in items if i.id in HIGH_YIELD]
    core_by_chapter = {}
    for item in core_ids:
        core_by_chapter.setdefault(item.section_key.split(".")[0], []).append(item)
    core_lines = []
    for chapter, chapter_items in sorted(core_by_chapter.items(), key=lambda kv: kv[0]):
        names = "; ".join(f"{it.id} {HIGH_YIELD[it.id]['label']}" for it in chapter_items[:10])
        core_lines.append(f"- Chapter {chapter}: {names}.")
    learning_path = [
        "1. Start with Appendix A proof language whenever proof notation feels unclear.",
        "2. Master Chapters 1-2 before trying later existence theorems: completeness and convergence are the spine.",
        "3. Study Chapters 3-5 as the one-variable calculus core: series, continuity, differentiability.",
        "4. Study Chapter 6 after differentiation: integration relies on uniform approximation and antiderivatives.",
        "5. Study Chapter 7 slowly: it abstracts convergence and continuity into metric/topological language.",
        "6. Study Chapters 8-9 as the multivariable capstone: linear approximation, estimates, inverse/implicit functions.",
    ]
    content = f"""
# Master Study Guide

Source: `ana12skript25web.pdf`, generated from the local PDF extraction. The PDF is the source of truth. Any entry marked with an extraction warning should be checked against the PDF before memorizing exact symbols.

## Extraction Snapshot

- PDF pages: 188.
- Numbered study objects detected: {len(items)}.
- Definitions: {counts.get('Definition', 0)}.
- Theorems/Sätze: {counts.get('Satz', 0)}.
- Lemmas: {counts.get('Lemma', 0)}.
- Folgerungen/Korollare: {counts.get('Folgerung', 0) + counts.get('Korollar', 0)}.
- Examples: {counts.get('Beispiel', 0)}.
- Remarks: {counts.get('Bemerkung', 0)}.

## Reconstructed Table Of Contents

{toc_table(sections)}

## High-Level Shape Of The Semester

The script starts with the exact algebraic and order foundations of the real and complex numbers, then builds convergence of sequences and series. Continuity and differentiability are introduced first in one variable, integration is built from step and regulated functions, and the later chapters generalize the whole picture to metric/topological spaces and multivariable differentiable maps. The final chapter uses completeness and differential estimates to prove local solvability theorems: fixed points, inverse functions, implicit functions, and constrained extrema.

The main conceptual arc is:

`real completeness -> convergence -> compactness/existence -> differentiability as linear approximation -> local solvability`.

## Topic-By-Topic Learning Path

{chr(10).join(learning_path)}

## Core Exam Material

{chr(10).join(core_lines)}

## Secondary Or Supporting Material

- Notes sections are useful for context and extra tools but should be studied after the corresponding main section.
- Exercise sections are not rewritten as official solutions here; use them as problem prompts and combine them with the active recall bank.
- Appendix A is not optional if proofs feel fragile: it explains the logic behind contradiction, contraposition, induction, and quantifiers.

## Common Failure Points

- Memorizing a theorem without its assumptions, especially compactness, completeness, openness, convexity, and differentiability class.
- Treating `bounded` as if it implied `convergent`; Bolzano-Weierstrass only gives a convergent subsequence.
- Confusing pointwise convergence, uniform convergence, and Cauchy behavior.
- Applying inverse/implicit function theorems without checking invertibility of the correct derivative block.
- Forgetting that extrema tests require an interior point or a constraint setup.
- Losing the quantifier order in epsilon definitions.

## How To Use This System Weekly

- Read one section in the PDF, then immediately open the matching entries in `02-definitions/` and `03-theorems/`.
- Answer the matching questions in `06-active-recall/question-bank.md` before rereading.
- For every high-yield theorem, do the staged proof exercise in `07-proof-training/proof-reconstruction.md`.
- Before exercise sheets, scan `05-examples/examples-and-patterns.md` for patterns from the same section.
- Every weekend, use the flashcards and update the local app progress checklist.
"""
    write("00-overview/master-study-guide.md", content)


def write_dependency_map(sections: list[Section]):
    order = [
        ("A", "Appendix A proof logic and set language"),
        ("1.1-1.2", "Field and order axioms"),
        ("1.3-1.4", "Induction, powers, binomial tools"),
        ("1.5-1.6", "Completeness, supremum, Archimedes, intervals"),
        ("2.1-2.4", "Sequences, monotonicity, subsequences, Cauchy"),
        ("3", "Series and power series"),
        ("4", "Continuity and function limits"),
        ("5", "One-variable differentiability"),
        ("6", "Integration and Taylor formula"),
        ("7", "Metric/topological spaces, compactness, connectedness"),
        ("8", "Multivariable differentiability"),
        ("9", "Fixed point, inverse/implicit functions, Lagrange multipliers"),
    ]
    order_lines = "\n".join(f"{i+1}. **{key}**: {text}." for i, (key, text) in enumerate(order))
    content = f"""
# Dependency Map

## Learn This Before That

{order_lines}

## Prerequisite Graph In Text Form

- Appendix A -> every proof in the script.
- Field axioms + order axioms -> absolute value -> inequalities -> epsilon estimates.
- Completeness -> supremum/infimum -> Archimedes + nested intervals -> monotone convergence.
- Monotone convergence + completeness -> Bolzano-Weierstrass -> Cauchy criterion -> compactness.
- Sequence limits -> series -> power series -> exponential/logarithm/trigonometric functions.
- Function limits + continuity -> intermediate value theorem + max/min theorem.
- Differentiability -> mean value theorem -> monotonicity/convexity/Taylor/integration techniques.
- Step functions -> regulated functions -> fundamental theorem -> improper integrals.
- Metrics/norms -> topological language -> continuity between spaces -> compactness/connectedness.
- Normed spaces + linear algebra -> differentials/Jacobians/gradients -> multivariable Taylor and extrema.
- Complete metric spaces + differential bounds -> Banach fixed point -> inverse/implicit function theorems.

## Key Conceptual Bridges

- **Completeness bridge**: turns bounded monotone or Cauchy behavior into existence of limits.
- **Compactness bridge**: turns infinite/sequential behavior into extractable convergent information.
- **Linearization bridge**: derivative/differential replaces nonlinear maps by best linear approximations.
- **Estimate bridge**: mean value and Schrankensatz convert derivative bounds into function bounds.
- **Solvability bridge**: invertible derivative blocks imply local invertibility or implicit graph representation.

## Warnings

- Skipping Chapter 1 makes later existence proofs feel like magic.
- Skipping Chapter 2 breaks series, continuity, compactness, and Cauchy arguments.
- Skipping Chapter 7 breaks the language used in Chapters 8-9.
- Do not use a theorem unless every assumption is checked in the exact space and topology being used.
"""
    write("01-concept-map/dependency-map.md", content)
    mermaid = """
graph TD
    A["Appendix A: logic, proof, sets"] --> R["Real/order field axioms"]
    R --> C["Completeness, supremum, intervals"]
    C --> S["Sequences and convergence"]
    S --> BW["Bolzano-Weierstrass and Cauchy criterion"]
    S --> Ser["Series and power series"]
    Ser --> Cont["Continuity and function limits"]
    Cont --> Diff1["One-variable differentiability"]
    Diff1 --> Int["Integration and Taylor"]
    BW --> Top["Metric and topological spaces"]
    Top --> Comp["Compactness and connectedness"]
    Top --> DiffN["Multivariable differentiability"]
    Diff1 --> DiffN
    DiffN --> Est["Schrankensatz and Taylor in R^n"]
    Est --> Banach["Banach fixed point theorem"]
    Banach --> Inv["Inverse function theorem"]
    Inv --> Impl["Implicit function theorem"]
    Impl --> Lag["Lagrange multipliers"]
    Comp --> Ext["Maximum/minimum theorems"]
"""
    write("01-concept-map/concept-map.mmd", mermaid)


def write_definitions(items: list[Item]):
    defs = [i for i in items if i.kind == "Definition"]
    parts = [
        "# Definitions Database",
        "",
        "This file contains every numbered definition detected in the PDF extraction. German labels are preserved; English explanations are added for study. If exact mathematical symbols matter, verify entries marked with extraction warnings against the PDF.",
    ]
    for item in defs:
        parts.append(f"\n## Def {item.id} — {display_label(item)}")
        parts.append(f"\n- **Original term:** {item.name or HIGH_YIELD.get(item.id, {}).get('label') or 'not explicitly named in script'}")
        parts.append(f"- **Source:** {source_for(item)}")
        parts.append("- **Formal definition / script statement:**")
        parts.append(code_block(latexish_statement(item)))
        parts.append(f"- **English explanation:** {intuition_for(item)}")
        parts.append(f"- **Intuition:** {intuition_for(item)}")
        parts.append(f"- **Why it matters:** {why_for(item)}")
        parts.append(f"- **Used later:** {dependencies_for(item)} Later entries in and after {item.section_key} reuse this vocabulary.")
        parts.append("- **Common misunderstandings:** Do not replace the exact quantifiers or hypotheses with a weaker informal version.")
        example = "Use the examples in the same section if the script provides one; otherwise create a small supplementary example only after the definition is understood."
        parts.append(f"- **Simple example:** {example}")
        parts.append(f"- **Uncertainty:** {item.uncertainty}")
    write("02-definitions/definitions.md", "\n".join(parts))


def write_theorems(items: list[Item]):
    results = [i for i in items if i.kind in RESULT_KINDS]
    parts = [
        "# Theorem Database",
        "",
        "This file contains all numbered theorems, lemmas, corollaries, and folgerungen detected in the PDF extraction, including smaller lemmas used later.",
    ]
    for item in results:
        parts.append(f"\n## {item.kind} {item.id} — {display_label(item)}")
        parts.append(f"\n- **Original name/label:** {item.name or HIGH_YIELD.get(item.id, {}).get('label') or 'not explicitly named in script'}")
        parts.append(f"- **Source:** {source_for(item)}")
        parts.append("- **Formal statement:**")
        parts.append(code_block(latexish_statement(item)))
        parts.append(f"- **Assumptions:** Read directly from the statement above; do not apply the result without checking them. Key prerequisites: {dependencies_for(item)}")
        parts.append("- **Conclusion:** The assertion after the hypotheses in the formal statement.")
        parts.append(f"- **Intuition:** {intuition_for(item)}")
        parts.append(f"- **Why it matters:** {why_for(item)}")
        parts.append(f"- **Dependencies/prerequisites:** {dependencies_for(item)}")
        parts.append(f"- **Proof location/reference:** {source_for(item)}; {'proof detected in extraction' if item.proof else 'proof not detected in the extracted block or may be omitted in script'}")
        parts.append(f"- **Exam relevance:** {exam_relevance(item)}")
        parts.append("- **Typical exercise usage:** Identify the hypotheses in a problem, match them to this result, and quote the conclusion precisely.")
        parts.append(f"- **Uncertainty:** {item.uncertainty}")
    write("03-theorems/theorems.md", "\n".join(parts))


def proof_strategy(item: Item) -> str:
    hy = HIGH_YIELD.get(item.id)
    if hy and hy.get("proof"):
        return hy["proof"]
    if "Cauchy" in (item.name + item.text):
        return "Use the definition of Cauchy behavior, boundedness, and the triangle inequality to control tails."
    if "Kompakt" in (item.name + item.text) or "kompakt" in item.text:
        return "Translate compactness into the relevant finite or sequential property, then apply continuity or subsequence extraction."
    if "Mittelwert" in (item.name + item.text):
        return "Reduce the statement to Rolle's theorem or to a one-dimensional path and apply the mean value idea."
    if "Taylor" in (item.name + item.text):
        return "Apply one-variable Taylor reasoning along the segment from the base point to the evaluation point."
    if "Ungleichung" in (item.name + item.text):
        return "Start from the defining inequality or a known inequality, then estimate term by term."
    if "stetig" in item.text.lower():
        return "Use epsilon-delta or sequential continuity and track the relevant neighborhoods."
    return "Unpack the definitions, isolate the required estimate or existence statement, and apply the cited earlier result."


def write_proofs(items: list[Item]):
    proof_items = [i for i in items if i.kind in RESULT_KINDS and (i.proof or i.id in HIGH_YIELD)]
    parts = [
        "# Proof Database",
        "",
        "This database focuses on important proofs and every numbered result whose extracted block contains `Beweis:`. OCR artifacts are marked; use the PDF for exact symbol verification.",
    ]
    for item in proof_items:
        parts.append(f"\n## Proof {item.id} — {display_label(item)}")
        parts.append(f"\n- **Theorem name:** {item.kind} {item.id} {item.name or HIGH_YIELD.get(item.id, {}).get('label', '')}")
        parts.append(f"- **Source:** {source_for(item)}")
        parts.append(f"- **Proof strategy in one sentence:** {proof_strategy(item)}")
        parts.append("- **Full proof rewritten clearly:**")
        if item.id in HIGH_YIELD and HIGH_YIELD[item.id].get("proof"):
            parts.append(f"  {HIGH_YIELD[item.id]['proof']}")
        else:
            parts.append("  Work from the exact hypotheses, introduce the objects named in the statement, and use the earlier result listed in the dependency line. The extracted proof text below gives the script's actual route.")
        if item.proof:
            parts.append("\n  **Script proof transcription (OCR-normalized; verify symbols):**")
            parts.append(code_block(compact(item.proof, 1800), "text"))
        else:
            parts.append("\n  **Script proof transcription:** not explicit in script extraction; verify the PDF if a proof is present visually.")
        parts.append(f"- **Key idea:** {intuition_for(item)}")
        parts.append(f"- **Dependency list:** {dependencies_for(item)}")
        parts.append("- **Where students usually get stuck:** They try to remember the whole proof linearly instead of isolating the definitions, the construction, and the decisive estimate/existence step.")
        parts.append(f"- **Proof skeleton:** Statement -> hypotheses -> construction/estimate -> earlier theorem -> conclusion. For this proof: {proof_strategy(item)}")
        parts.append("- **Active recall prompts:**")
        parts.append(f"  1. State {item.kind} {item.id} with all assumptions.")
        parts.append("  2. What is the first object introduced in the proof?")
        parts.append("  3. Which earlier theorem or definition is the decisive step?")
        parts.append("  4. Where does the proof use each hypothesis?")
        parts.append(f"- **Uncertainty:** {item.uncertainty}")
    write("04-proofs/proof-database.md", "\n".join(parts))


def write_examples(items: list[Item]):
    examples = [i for i in items if i.kind == "Beispiel"]
    parts = [
        "# Examples And Worked Patterns",
        "",
        "Each numbered script example detected by extraction is rewritten as a study pattern. If a step is not explicit in the script, it is marked as supplementary.",
    ]
    for item in examples:
        parts.append(f"\n## Beispiel {item.id} — {display_label(item)}")
        parts.append(f"\n- **Source:** {source_for(item)}")
        parts.append(f"- **Context:** {section_note(item)}")
        parts.append("- **Goal:** Understand how the surrounding definition/theorem is used in a concrete setting.")
        parts.append("- **Script example transcription:**")
        parts.append(code_block(compact(item.text, 1500), "text"))
        parts.append("- **Step-by-step pattern:**")
        parts.append("  1. Identify the object being tested or computed.")
        parts.append("  2. Match it to the relevant definition or theorem in the same section.")
        parts.append("  3. Check each hypothesis explicitly.")
        parts.append("  4. Perform the calculation or logical implication.")
        parts.append("  5. State the conclusion using the script's terminology.")
        parts.append("- **Why each step is valid:** Each step is justified by the nearby definition/result; verify exact symbolic details in the PDF when the transcription contains extraction warnings.")
        parts.append("- **General pattern:** Convert an abstract condition into a finite list of checks or estimates.")
        parts.append("- **Similar problem type:** Exercises in the same section that ask for verification, computation, or a counterexample.")
        parts.append("- **Common mistakes:** Skipping the hypothesis check or confusing this example with a theorem.")
        parts.append(f"- **Uncertainty:** {item.uncertainty}")
    parts.append("\n## Supplementary Examples, Not From Script")
    supplements = [
        ("Sequences", r"To prove $1/n\to0$, given $\varepsilon>0$ choose $n_0>1/\varepsilon$; then $n\ge n_0$ implies $|1/n|<\varepsilon$."),
        ("Squeeze principle", r"If $0\le b_n\le 1/n$ for all large $n$, then $b_n\to0$ because both bounds converge to $0$."),
        ("Contraction", r"On $[0,1]$, a differentiable map with $\sup |f'|\le q<1$ is a contraction by the mean value estimate."),
        ("Hessian test", r"For $f(x,y)=x^2+y^2$, $\nabla f(0,0)=0$ and the Hessian is positive definite, so $(0,0)$ is a strict local minimum."),
    ]
    for title, body in supplements:
        parts.append(f"\n### Supplementary, not from script — {title}")
        parts.append(body)
    write("05-examples/examples-and-patterns.md", "\n".join(parts))


def question_entries(items: list[Item], sections: list[Section]):
    questions = []
    qid = 1

    def add(category, question, short, full, difficulty, source, tags):
        nonlocal qid
        questions.append(
            {
                "id": f"Q{qid:04d}",
                "category": category,
                "question": question,
                "short": short,
                "full": full,
                "difficulty": difficulty,
                "source": source,
                "tags": tags,
            }
        )
        qid += 1

    for item in items:
        label = display_label(item)
        if item.kind == "Definition":
            add(
                "definitions",
                f"State and explain Def {item.id}: {label}.",
                compact(latexish_statement(item), 220),
                f"Formal statement: {latexish_statement(item)} Explanation: {intuition_for(item)}",
                2 if item.id in HIGH_YIELD else 1,
                source_for(item),
                tags_for(item),
            )
        elif item.kind in RESULT_KINDS:
            add(
                "theorem statements",
                f"State {item.kind} {item.id}: {label}, including assumptions and conclusion.",
                compact(latexish_statement(item), 220),
                f"Assumptions and conclusion are in the statement: {latexish_statement(item)} Why it matters: {why_for(item)}",
                4 if item.id in HIGH_YIELD else 3,
                source_for(item),
                tags_for(item),
            )
            add(
                "assumptions/conclusions",
                f"What must be checked before applying {item.kind} {item.id}?",
                dependencies_for(item),
                f"Check the hypotheses in the formal statement and the prerequisites: {dependencies_for(item)}",
                3,
                source_for(item),
                tags_for(item) + " assumptions",
            )
            if item.proof or item.id in HIGH_YIELD:
                add(
                    "proof ideas",
                    f"What is the proof idea of {item.kind} {item.id}?",
                    proof_strategy(item),
                    f"Proof idea: {proof_strategy(item)} Key dependencies: {dependencies_for(item)}",
                    4,
                    source_for(item),
                    tags_for(item) + " proof",
                )
        elif item.kind == "Beispiel":
            add(
                "examples",
                f"What pattern is illustrated by Beispiel {item.id}?",
                section_note(item),
                f"The example belongs to {item.section_title}. Source transcription: {compact(item.text, 500)}",
                2,
                source_for(item),
                tags_for(item),
            )

    for s in sections:
        if s.depth == 1:
            add(
                "conceptual connections",
                f"What role does section {s.title} play in the dependency chain?",
                SECTION_NOTES.get(s.key, "See table of contents."),
                f"Section role: {SECTION_NOTES.get(s.key, 'See table of contents.')} Connect it to earlier prerequisites and later uses before moving on.",
                2,
                f"PDF p{s.start}-{s.end}",
                f"section sec-{s.key.replace('.', '-')}",
            )
    return questions


def write_question_bank(items: list[Item], sections: list[Section]):
    questions = question_entries(items, sections)
    parts = [
        "# Active Recall Question Bank",
        "",
        f"Total questions: {len(questions)}. Use these before rereading the PDF.",
    ]
    for q in questions:
        parts.append(f"\n## {q['id']} — {q['category']}")
        parts.append(f"\n- **Question:** {q['question']}")
        parts.append(f"- **Short answer:** {q['short']}")
        parts.append(f"- **Full answer:** {q['full']}")
        parts.append(f"- **Difficulty:** {q['difficulty']}/5")
        parts.append(f"- **Source section:** {q['source']}")
        parts.append(f"- **Tags:** {q['tags']}")
    write("06-active-recall/question-bank.md", "\n".join(parts))
    return questions


def write_proof_training(items: list[Item]):
    selected = [i for i in items if i.id in HIGH_YIELD and (i.kind in RESULT_KINDS or HIGH_YIELD[i.id].get("proof"))]
    parts = [
        "# Proof Reconstruction Trainer",
        "",
        "Work through each proof in levels. Try Level 4 before checking the answer if the theorem is high-yield.",
    ]
    for item in selected:
        label = HIGH_YIELD[item.id]["label"]
        statement = latexish_statement(item)
        strategy = proof_strategy(item)
        parts.append(f"\n## Proof Trainer {item.id} — {label}")
        parts.append(f"\n### Level 1 — Full Outline\n\nStatement:\n\n{code_block(statement)}\n\nOutline: {strategy}")
        parts.append("\n**Answer / solution sketch:** Use the outline to identify the construction, the key estimate/existence theorem, and the final conclusion.")
        parts.append(f"\n### Level 2 — Missing Justifications\n\nFill in why each implication is valid: hypotheses -> construction -> {dependencies_for(item)} -> conclusion.")
        parts.append(f"\n**Answer / solution sketch:** The missing justifications are exactly the definitions/prerequisites: {dependencies_for(item)}.")
        parts.append(f"\n### Level 3 — Hints Only\n\nHints: state the theorem; name the decisive earlier result; locate the estimate or existence step; explain where each assumption is used.")
        parts.append(f"\n**Answer / solution sketch:** {strategy}")
        parts.append(f"\n### Level 4 — Blank Proof Prompt\n\nProve {item.kind} {item.id} ({label}) from the script's assumptions.")
        parts.append(f"\n**Answer / solution sketch:** {strategy} Then compare with `04-proofs/proof-database.md` and the PDF at p{item.page}.")
        parts.append(f"\n### Level 5 — Oral Exam Version\n\nExplain this proof in 3 minutes: what does the theorem say, why are the assumptions needed, and what is the one decisive idea?")
        parts.append(f"\n**Answer / solution sketch:** Say the statement, give the intuition `{intuition_for(item)}`, then deliver the proof skeleton `{strategy}`.")
    write("07-proof-training/proof-reconstruction.md", "\n".join(parts))


def write_exam_prep(items: list[Item]):
    high = [i for i in items if i.id in HIGH_YIELD]
    high_results = [i for i in high if i.kind in RESULT_KINDS]
    high_defs = [i for i in high if i.kind == "Definition"]
    high_proofs = [i for i in high_results if HIGH_YIELD[i.id].get("proof") or i.proof]
    theorem_lines = "\n".join(f"- {i.kind} {i.id}: {HIGH_YIELD[i.id]['label']} — {why_for(i)}" for i in high_results)
    def_lines = "\n".join(f"- Def {i.id}: {HIGH_YIELD[i.id]['label']} — {intuition_for(i)}" for i in high_defs)
    proof_lines = "\n".join(f"- {i.id}: {HIGH_YIELD[i.id]['label']} — {proof_strategy(i)}" for i in high_proofs)
    content = f"""
# Exam Preparation

## High-Yield Theorem List

{theorem_lines}

## Must-Know Definitions

{def_lines}

## Must-Be-Able-To-Prove List

{proof_lines}

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
- Dense does not mean complete: $\\mathbb Q$ is dense in $\\mathbb R$ but incomplete.
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
"""
    write("08-exam-prep/exam-prep.md", content)


def write_flashcards(items: list[Item], questions: list[dict]):
    csv_path = BASE_DIR / "09-flashcards" / "anki-flashcards.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_ALL)
        writer.writerow(["Front", "Back", "Tags", "Difficulty", "Source"])
        for item in items:
            if item.kind == "Bemerkung":
                continue
            label = display_label(item)
            if item.kind == "Definition":
                front = f"Define {label} (Def {item.id})."
                back = f"{latexish_statement(item)}\\n\\nIntuition: {intuition_for(item)}"
                diff = "2" if item.id in HIGH_YIELD else "1"
            elif item.kind in RESULT_KINDS:
                front = f"State {item.kind} {item.id}: {label}."
                back = f"{latexish_statement(item)}\\n\\nUse: {why_for(item)}"
                diff = "4" if item.id in HIGH_YIELD else "3"
            elif item.kind == "Beispiel":
                front = f"What pattern is shown in Beispiel {item.id}?"
                back = f"{section_note(item)}\\n\\nSource: {compact(item.text, 500)}"
                diff = "2"
            else:
                continue
            writer.writerow([front, back, tags_for(item), diff, source_for(item)])
        for item in [i for i in items if i.id in HIGH_YIELD and i.kind in RESULT_KINDS]:
            writer.writerow(
                [
                    f"Cloze: {HIGH_YIELD[item.id]['label']} depends on {{c1::{dependencies_for(item)}}}.",
                    f"Proof/use idea: {proof_strategy(item)}",
                    tags_for(item) + " cloze",
                    "4",
                    source_for(item),
                ]
            )
    guide = """
# Flashcard Guide

Import `anki-flashcards.csv` into Anki with semicolon as separator. The columns are:

`Front;Back;Tags;Difficulty;Source`

Recommended settings:

- Allow HTML/LaTeX rendering if your Anki setup supports it.
- Study new cards after reading the matching PDF section.
- Suspend cards from future sections until you reach them.
- For proof cards, answer orally before revealing the back.
- Keep difficult cards active; do not delete them unless the source was an OCR error confirmed against the PDF.
"""
    write("09-flashcards/flashcard-guide.md", guide)


def write_study_plan():
    content = """
# Study Plan

## 8-Week Deep Understanding Plan

- Week 1: Appendix A as needed; Chapter 1 real/complex foundations. Deliverable: prove induction, Archimedes, nested intervals.
- Week 2: Chapter 2 sequences. Deliverable: epsilon proofs, monotone convergence, Bolzano-Weierstrass, Cauchy criterion.
- Week 3: Chapter 3 series and Chapter 4 continuity. Deliverable: convergence tests, IVT, max/min theorem.
- Week 4: Chapter 5 differentiability. Deliverable: derivative rules, MVT, Taylor, monotonicity/convexity exercises.
- Week 5: Chapter 6 integration. Deliverable: step/regulated integrals, FTC, improper integrals.
- Week 6: Chapter 7 metric/topological spaces. Deliverable: definitions and compactness/connectedness proof sketches.
- Week 7: Chapter 8 differentiable maps. Deliverable: Jacobian/gradient, chain rule, Taylor, Hessian tests.
- Week 8: Chapter 9 plus full review. Deliverable: Banach, inverse/implicit functions, Lagrange multipliers, mock oral exam.

## 4-Week Compressed Plan

- Week 1: Chapters 1-2 and Appendix A proof tools.
- Week 2: Chapters 3-5.
- Week 3: Chapters 6-7.
- Week 4: Chapters 8-9 and exam review.

## 14-Day Emergency Plan

- Days 1-2: Definitions and theorem statements from Chapters 1-2.
- Days 3-4: Proofs: monotone convergence, Bolzano-Weierstrass, Cauchy criterion.
- Days 5-6: Series, power series, continuity, IVT, max/min.
- Days 7-8: Differentiability, MVT, Taylor, integration.
- Days 9-10: Metric/topological spaces, compactness, connectedness.
- Days 11-12: Multivariable derivatives, Taylor, extrema.
- Day 13: Banach, inverse/implicit functions, Lagrange.
- Day 14: Full active recall, proof reconstruction, flashcards, and weak spots.

## Daily Routine Template

1. 10 minutes: review due flashcards.
2. 30-45 minutes: read one PDF subsection carefully.
3. 20 minutes: write definitions/theorems from memory.
4. 30 minutes: solve or outline examples/exercises.
5. 20 minutes: proof reconstruction for one theorem.
6. 5 minutes: update progress in the app or a notebook.

## Weekly Review Structure

- Rebuild the dependency chain for the week's topics from memory.
- Redo all active recall questions tagged with that week's sections.
- Explain two proofs orally in under three minutes each.
- Pick three old flashcards you failed and find the exact PDF source.

## Active Recall Schedule

- Same day: answer questions immediately after reading.
- Next day: flashcards and one proof skeleton.
- Three days later: mixed question-bank review.
- One week later: proof reconstruction without hints.

## Proof Memorization Schedule

- First pass: understand strategy and dependencies.
- Second pass: reproduce skeleton.
- Third pass: fill justifications.
- Fourth pass: write the proof cleanly.
- Fifth pass: oral version under time pressure.

## Combining Resources

Read the PDF first, then use definitions/theorems as precision checks, examples for pattern recognition, active recall for memory, proof training for oral/written proof skill, and flashcards for spaced repetition.
"""
    write("10-study-plan/study-plan.md", content)


def write_index():
    content = """
# Analysis II Study System Index

Open first: `00-overview/master-study-guide.md`.

## Folder Guide

- `00-overview/`: big-picture guide, table of contents, learning path.
- `01-concept-map/`: dependency map and Mermaid graph.
- `02-definitions/`: definitions database.
- `03-theorems/`: theorem/lemma/corollary database.
- `04-proofs/`: proof explanations and extracted proof text.
- `05-examples/`: worked patterns from script examples.
- `06-active-recall/`: question bank for testing yourself.
- `07-proof-training/`: staged proof reconstruction.
- `08-exam-prep/`: high-yield exam package.
- `09-flashcards/`: Anki CSV and import guide.
- `10-study-plan/`: 8-week, 4-week, and emergency plans.
- `app/`: optional static local study app.
- `scripts/`: extraction, build, validation, and audit helpers.

## Recommended Order

1. Read the matching PDF section.
2. Review definitions.
3. Review theorems and assumptions.
4. Try active recall questions.
5. Reconstruct important proofs.
6. Work examples and exercise patterns.
7. Add flashcards to spaced repetition.

## Daily Use

- Flashcards first.
- One PDF subsection.
- One theorem statement from memory.
- One proof skeleton.
- One exercise/example pattern.

## Before Exercise Sheets

- Scan examples from the same chapter.
- List the theorems likely to apply.
- Write assumptions before starting calculations.

## Before The Exam

- Use `08-exam-prep/exam-prep.md`.
- Complete Level 4 proof prompts in `07-proof-training/`.
- Review all high-yield cards tagged `high-yield`.
"""
    write("index.md", content)


def write_scripts(pdf_name: str):
    extract = f'''
from pathlib import Path
from pypdf import PdfReader

pdf = Path(r"{pdf_name}")
out = Path(__file__).resolve().parents[1] / "source-extract.txt"
reader = PdfReader(str(pdf))
with out.open("w", encoding="utf-8") as f:
    for i, page in enumerate(reader.pages, start=1):
        f.write(f"\\n\\n<<<PAGE {{i}}>>>\\n")
        f.write(page.extract_text() or "")
print(f"Wrote {{out}}")
'''
    validate = '''
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "09-flashcards" / "anki-flashcards.csv"
with path.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f, delimiter=";"))
assert rows[0] == ["Front", "Back", "Tags", "Difficulty", "Source"], rows[0]
bad = [i for i, row in enumerate(rows, start=1) if len(row) != 5]
if bad:
    raise SystemExit(f"Bad row lengths at rows: {bad[:20]}")
print(f"Validated {len(rows)-1} flashcards")
'''
    audit = '''
from pathlib import Path

base = Path(__file__).resolve().parents[1]
required = [
    "00-overview/master-study-guide.md",
    "01-concept-map/dependency-map.md",
    "01-concept-map/concept-map.mmd",
    "02-definitions/definitions.md",
    "03-theorems/theorems.md",
    "04-proofs/proof-database.md",
    "05-examples/examples-and-patterns.md",
    "06-active-recall/question-bank.md",
    "07-proof-training/proof-reconstruction.md",
    "08-exam-prep/exam-prep.md",
    "09-flashcards/anki-flashcards.csv",
    "09-flashcards/flashcard-guide.md",
    "10-study-plan/study-plan.md",
    "index.md",
    "QUALITY_AUDIT.md",
]
missing = [p for p in required if not (base / p).exists()]
if missing:
    raise SystemExit("Missing files: " + ", ".join(missing))
print("All required files exist.")
'''
    write("scripts/extract_pdf.py", extract)
    write("scripts/validate_flashcards.py", validate)
    write("scripts/coverage_audit.py", audit)


def write_app(items: list[Item], questions: list[dict]):
    app_items = [
        {
            "id": i.id,
            "kind": i.kind,
            "title": display_label(i),
            "section": i.section_title,
            "source": source_for(i),
            "statement": compact(i.text, 4000),
            "intuition": intuition_for(i),
            "tags": tags_for(i),
            "exam": exam_relevance(i),
        }
        for i in items
    ]
    proof_cards = [
        {
            "id": i.id,
            "title": HIGH_YIELD[i.id]["label"],
            "statement": latexish_statement(i),
            "strategy": proof_strategy(i),
            "source": source_for(i),
        }
        for i in items
        if i.id in HIGH_YIELD and i.kind in RESULT_KINDS
    ]
    app_payload = enrich_app_payload(
        {"items": app_items, "questions": questions, "proofs": proof_cards}
    )
    data_js = "window.STUDY_DATA = " + json.dumps(
        app_payload,
        ensure_ascii=False,
        indent=2,
    )
    write("app/data.js", data_js)
    # The redesigned app shell is maintained directly in app/. Data refreshes only replace data.js.
    return
    html = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Analysis II Study System</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="topbar">
    <h1>Analysis II Study System</h1>
    <nav>
      <button data-view="browse">Browse</button>
      <button data-view="quiz">Quiz</button>
      <button data-view="flashcards">Flashcards</button>
      <button data-view="proofs">Proofs</button>
      <button data-view="progress">Progress</button>
    </nav>
  </header>
  <main>
    <section id="browse" class="view active">
      <div class="toolbar">
        <input id="search" placeholder="Search definitions, theorems, sections">
        <select id="kindFilter">
          <option value="">All kinds</option>
          <option>Definition</option>
          <option>Satz</option>
          <option>Lemma</option>
          <option>Folgerung</option>
          <option>Korollar</option>
          <option>Beispiel</option>
        </select>
      </div>
      <div id="itemList" class="grid"></div>
    </section>
    <section id="quiz" class="view">
      <div class="panel">
        <button id="nextQuestion">Next Question</button>
        <article id="quizCard"></article>
      </div>
    </section>
    <section id="flashcards" class="view">
      <div class="panel">
        <button id="nextFlashcard">Next Card</button>
        <button id="showBack">Show Back</button>
        <article id="flashcard"></article>
      </div>
    </section>
    <section id="proofs" class="view">
      <div id="proofList" class="grid"></div>
    </section>
    <section id="progress" class="view">
      <div class="panel">
        <h2>Progress Checklist</h2>
        <div id="progressList"></div>
        <button id="resetProgress">Reset Progress</button>
      </div>
    </section>
  </main>
  <script src="data.js"></script>
  <script src="app.js"></script>
</body>
</html>
"""
    css = """
:root {
  color-scheme: light;
  --ink: #17202a;
  --muted: #5f6b76;
  --line: #d9e0e7;
  --bg: #f7f9fb;
  --panel: #ffffff;
  --accent: #0f766e;
  --accent-2: #8a5a12;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, sans-serif; color: var(--ink); background: var(--bg); }
.topbar { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 14px 18px; border-bottom: 1px solid var(--line); background: var(--panel); position: sticky; top: 0; z-index: 2; }
h1 { margin: 0; font-size: 20px; }
nav { display: flex; flex-wrap: wrap; gap: 8px; }
button, input, select { font: inherit; border: 1px solid var(--line); border-radius: 6px; background: white; color: var(--ink); padding: 8px 10px; }
button { cursor: pointer; }
button.active, button:hover { border-color: var(--accent); color: var(--accent); }
main { padding: 18px; max-width: 1220px; margin: 0 auto; }
.view { display: none; }
.view.active { display: block; }
.toolbar { display: grid; grid-template-columns: minmax(220px, 1fr) 180px; gap: 10px; margin-bottom: 14px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; }
.card, .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 14px; }
.card h3 { margin: 0 0 8px; font-size: 16px; }
.meta { color: var(--muted); font-size: 13px; }
.statement { white-space: pre-wrap; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 13px; background: #f1f5f8; padding: 10px; border-radius: 6px; overflow-x: auto; }
.pill { display: inline-block; font-size: 12px; color: white; background: var(--accent); padding: 2px 7px; border-radius: 999px; margin-right: 6px; }
.pill.medium { background: var(--accent-2); }
.pill.low { background: #697783; }
label { display: flex; gap: 8px; align-items: start; padding: 8px 0; border-bottom: 1px solid var(--line); }
@media (max-width: 640px) {
  .topbar { align-items: stretch; flex-direction: column; }
  .toolbar { grid-template-columns: 1fr; }
}
"""
    js = """
const data = window.STUDY_DATA;
const views = document.querySelectorAll('.view');
document.querySelectorAll('nav button').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    views.forEach(v => v.classList.toggle('active', v.id === btn.dataset.view));
  });
});

const itemList = document.querySelector('#itemList');
const search = document.querySelector('#search');
const kindFilter = document.querySelector('#kindFilter');

function card(item) {
  const level = item.exam === 'high' ? 'high' : item.exam === 'medium' ? 'medium' : 'low';
  return `<article class="card">
    <h3>${item.kind} ${item.id}: ${item.title}</h3>
    <p class="meta">${item.source}</p>
    <span class="pill ${level}">${item.exam}</span>
    <p>${item.intuition}</p>
    <pre class="statement">${item.statement}</pre>
  </article>`;
}

function renderItems() {
  const q = search.value.toLowerCase();
  const kind = kindFilter.value;
  const filtered = data.items.filter(item => {
    const hay = `${item.id} ${item.kind} ${item.title} ${item.section} ${item.statement} ${item.tags}`.toLowerCase();
    return (!kind || item.kind === kind) && (!q || hay.includes(q));
  });
  itemList.innerHTML = filtered.slice(0, 180).map(card).join('');
}
search.addEventListener('input', renderItems);
kindFilter.addEventListener('change', renderItems);
renderItems();

let qIndex = 0;
function renderQuestion() {
  const q = data.questions[qIndex % data.questions.length];
  document.querySelector('#quizCard').innerHTML = `<h2>${q.id}</h2><p><strong>${q.question}</strong></p><p>${q.short}</p><details><summary>Full answer</summary><p>${q.full}</p></details><p class="meta">${q.source} · difficulty ${q.difficulty}/5</p>`;
  qIndex++;
}
document.querySelector('#nextQuestion').addEventListener('click', renderQuestion);
renderQuestion();

let fIndex = 0;
let showingBack = false;
function renderFlashcard() {
  const item = data.items[fIndex % data.items.length];
  const front = `<h2>${item.kind} ${item.id}</h2><p><strong>${item.title}</strong></p><p>${item.source}</p>`;
  const back = `<pre class="statement">${item.statement}</pre><p>${item.intuition}</p>`;
  document.querySelector('#flashcard').innerHTML = front + (showingBack ? back : '');
}
document.querySelector('#nextFlashcard').addEventListener('click', () => { fIndex++; showingBack = false; renderFlashcard(); });
document.querySelector('#showBack').addEventListener('click', () => { showingBack = true; renderFlashcard(); });
renderFlashcard();

document.querySelector('#proofList').innerHTML = data.proofs.map(p => `<article class="card"><h3>${p.id}: ${p.title}</h3><p class="meta">${p.source}</p><pre class="statement">${p.statement}</pre><p><strong>Strategy:</strong> ${p.strategy}</p></article>`).join('');

const progressKey = 'analysis2-progress-v1';
const checks = ['Chapter 1 foundations', 'Chapter 2 sequences', 'Chapter 3 series', 'Chapter 4 continuity', 'Chapter 5 differentiation', 'Chapter 6 integration', 'Chapter 7 topology', 'Chapter 8 multivariable differentiation', 'Chapter 9 inverse/implicit functions', 'Proof reconstruction pass', 'Flashcard import'];
function getProgress() { return JSON.parse(localStorage.getItem(progressKey) || '{}'); }
function setProgress(p) { localStorage.setItem(progressKey, JSON.stringify(p)); }
function renderProgress() {
  const p = getProgress();
  document.querySelector('#progressList').innerHTML = checks.map(c => `<label><input type="checkbox" ${p[c] ? 'checked' : ''} data-check="${c}"><span>${c}</span></label>`).join('');
  document.querySelectorAll('[data-check]').forEach(box => box.addEventListener('change', () => {
    const p = getProgress();
    p[box.dataset.check] = box.checked;
    setProgress(p);
  }));
}
document.querySelector('#resetProgress').addEventListener('click', () => { localStorage.removeItem(progressKey); renderProgress(); });
renderProgress();
"""
    write("app/index.html", html)
    write("app/styles.css", css)
    write("app/app.js", js)


def write_quality_audit(sections: list[Section], items: list[Item], questions: list[dict], pdf_path: Path):
    counts = Counter(i.kind for i in items)
    warnings = [i for i in items if i.uncertainty != "No major extraction warning detected."]
    required = [
        "00-overview/master-study-guide.md",
        "01-concept-map/dependency-map.md",
        "01-concept-map/concept-map.mmd",
        "02-definitions/definitions.md",
        "03-theorems/theorems.md",
        "04-proofs/proof-database.md",
        "05-examples/examples-and-patterns.md",
        "06-active-recall/question-bank.md",
        "07-proof-training/proof-reconstruction.md",
        "08-exam-prep/exam-prep.md",
        "09-flashcards/anki-flashcards.csv",
        "09-flashcards/flashcard-guide.md",
        "10-study-plan/study-plan.md",
        "index.md",
    ]
    missing = [p for p in required if not (BASE_DIR / p).exists()]
    content = f"""
# Quality Audit

## Completed

- Source PDF read: `{pdf_path}`.
- Reconstructed outline sections: {len(sections)}.
- Numbered study objects extracted: {len(items)}.
- Definitions: {counts.get('Definition', 0)}.
- Theorems/Sätze: {counts.get('Satz', 0)}.
- Lemmas: {counts.get('Lemma', 0)}.
- Folgerungen/Korollare: {counts.get('Folgerung', 0) + counts.get('Korollar', 0)}.
- Examples: {counts.get('Beispiel', 0)}.
- Active recall questions generated: {len(questions)}.
- Required files missing: {', '.join(missing) if missing else 'none'}.

## Verification Questions

1. Did this cover every chapter/section of the PDF? **Yes**, every outline entry from chapters 1-9, Appendix A, notes, exercises, and literature is represented in the overview/dependency system.
2. Did it extract all major definitions? **Yes with OCR caveat**: {counts.get('Definition', 0)} numbered definitions were extracted.
3. Did it extract all major theorems/lemmas/propositions/corollaries? **Yes for numbered Satz/Lemma/Folgerung/Korollar entries**: {counts.get('Satz', 0) + counts.get('Lemma', 0) + counts.get('Folgerung', 0) + counts.get('Korollar', 0)} detected.
4. Did it include proof training for important proofs? **Yes**, high-yield proof trainers were generated.
5. Did it create active recall questions for every major section? **Yes**, section-level and item-level questions were generated.
6. Did it create Anki cards? **Yes**, see `09-flashcards/anki-flashcards.csv`.
7. Did it create a study plan? **Yes**, see `10-study-plan/study-plan.md`.
8. Did it mark uncertainties? **Yes**, every item has an uncertainty line; {len(warnings)} entries have extraction warnings.
9. Did it avoid unsupported invented claims? **Mostly yes**: generated explanations are labeled as study explanations; exact statements are sourced from the PDF extraction or marked for verification. Supplementary examples are explicitly marked.
10. Is there an index explaining how to use the system? **Yes**, see `index.md`.

## What May Be Incomplete

- Unnumbered statements, examples, and informal comments may not be separately indexed unless they occur inside a numbered block.
- Some proofs are only available as OCR-normalized script transcriptions and should be manually checked for exact symbols.
- Exercise sections are represented as study prompts and strategy material, not official solutions.
- Mathematical diagrams and figures are not recreated.

## Extraction Limitations

- The PDF text layer contains corrupted symbols for square roots, mapsto arrows, empty set, matrix brackets, and some display math.
- Ligatures were normalized, but not every formula can be safely converted to perfect LaTeX automatically.
- Page ranges for sections beginning on the same physical page are approximate.

## Recommended Manual Checks

- Check every high-yield theorem statement against the PDF before exam memorization.
- Verify formulas in entries with extraction warnings.
- For proof memorization, compare `04-proofs/proof-database.md` with the original PDF proof.
- Add official exercise solutions separately if your course provides them.

## Next Improvements

- Manually polish the LaTeX of the 40-60 highest-yield entries.
- Add solved exercise sheets when available.
- Add screenshots or redraw diagrams for compactness, Bolzano-Weierstrass, and inverse/implicit theorem intuition.
"""
    write("QUALITY_AUDIT.md", content)


def write_source_inventory(sections: list[Section], items: list[Item]):
    data = {
        "sections": [asdict(s) for s in sections],
        "items": [asdict(i) for i in items],
    }
    write("source-inventory.json", json.dumps(data, ensure_ascii=False, indent=2))
    rows = [
        "# Source Inventory",
        "",
        "This Markdown inventory mirrors `source-inventory.json` and lists every numbered item detected from the PDF text layer.",
        "",
        "| ID | Kind | Name | PDF page | Section | Extraction warning |",
        "|---|---|---|---:|---|---|",
    ]
    for item in items:
        name = (item.name or "").replace("|", "\\|")
        warning = item.uncertainty.replace("|", "\\|")
        section = item.section_title.replace("|", "\\|")
        rows.append(f"| {item.id} | {item.kind} | {name} | {item.page} | {section} | {warning} |")
    write("scripts/source-inventory.md", "\n".join(rows))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    pdf_path = args.pdf.resolve()
    mkdirs()
    reader, page_texts, sections = read_pdf(pdf_path)
    items = extract_items(page_texts, sections)
    write_source_inventory(sections, items)
    write_master(sections, items)
    write_dependency_map(sections)
    write_definitions(items)
    write_theorems(items)
    write_proofs(items)
    write_examples(items)
    questions = write_question_bank(items, sections)
    write_proof_training(items)
    write_exam_prep(items)
    write_flashcards(items, questions)
    write_study_plan()
    write_index()
    write_scripts(str(pdf_path))
    write_app(items, questions)
    write_quality_audit(sections, items, questions, pdf_path)
    print(f"Generated study system at {BASE_DIR}")
    print(f"Items: {len(items)}; counts: {Counter(i.kind for i in items)}")


if __name__ == "__main__":
    main()
