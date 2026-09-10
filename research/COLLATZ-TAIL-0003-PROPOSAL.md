# COLLATZ-TAIL-0003: landmark coordinates are run-length Collatz conjugacy

Research report, 2026-09-10. Source task: [Issue #32](https://github.com/pashamango/minutta-rp-pr-cycle-lab/issues/32).

Base: immutable `collatz-tail-0002`, commit `c4b63a01864524246f72697c6f496c19c953d858`, in `pashamango/collatz-landmark-coordinate`. This report supplies proofs beyond that handoff's finite verification. It does not prove the Collatz conjecture.

## Verdict and claim ledger

| Claim | Classification | Verdict |
|---|---|---|
| Maximal landmark congruence equals v₂(3n+1) for positive odd n | REFORMULATION | PROVED, §1 |
| Coordinate successor is 3q+c_k | REFORMULATION | PROVED when k is maximal; otherwise it is only a partially divided successor |
| Finite reconstruction with terminal remainder | KNOWN / REFORMULATION | PROVED, §2 |
| Infinite reconstruction for actual infinite odd trajectories in Z₂ | KNOWN / REFORMULATION | PROVED, §2 |
| Every infinite sequence of positive finite run lengths gives a unique starting point | KNOWN / REFORMULATION | PROVED in the domain D below, not in positive integers |
| Formula is Bernstein's inverse conjugacy | KNOWN | Exact identification, §3; not a new global theorem |
| Exact J-run prefix fixes a class modulo 2^(s_J+1) | REFORMULATION | PROVED; the extra odd-terminal bit matters |
| Arbitrary run lengths reconstruct a positive integer | FALSIFIED | Constant 1 gives −1; constant 3 gives 1/5 |
| Remainder can simply be discarded over the reals | FALSIFIED | n=1, K=(2,2,…) gives remainder (4/3)^J |
| The same finite maximal-k theorem covers every odd 2-adic | FALSIFIED | At −1/3 every congruence holds, with no finite maximum |
| Landmarks are a dynamical attractor | FALSIFIED in the ordinary fixed-point-attractor sense | T(−1/3)=0; accelerated map is undefined there |
| Base 4 supplies an intrinsic entropy/compression reduction | FALSIFIED as a universal claim | Lossless regrouping and exact cylinder counts preserve information |
| Base 4 supplies a smaller full transducer or faster algorithm | CANDIDATE-NOVEL, UNRESOLVED | No such improvement established; a limited matcher simplification is real |
| Base 4 supplies a new invariant or proof route | CANDIDATE-NOVEL, UNRESOLVED | None found; natural monotonicity candidates fail |
| Educational and independent-implementation utility | REFORMULATION | Concrete present utility, not mathematical novelty |

Overall added-content verdict: **NEGATIVE for demonstrated new mathematical content; UNRESOLVED for future engineered advantages.** This does not purport to prove that every possible use or formulation is known.

## 1. One-step theorem and its exact scope

Write Z₂ for the 2-adic integers, v₂(0)=+∞, and |x|₂=2^(−v₂(x)). Define

    L_k = (4^ceil(k/2) − 1)/3,      k≥1,
    c_k = 1 (k even), 2 (k odd).

**Theorem A [REFORMULATION].** For every positive odd integer n,

    max{k≥1 : n ≡ L_k (mod 2^k)} = v₂(3n+1) =: k(n),
    U(n) := (3n+1)/2^k(n) = 3q+c_k(n),
    q = (n−L_k(n))/2^k(n).

**Proof.** The numerator defining L_k is divisible by 3. Directly,

    3L_k+1 = 2^(2 ceil(k/2)) = 2^k c_k.

Multiplication by 3 is invertible modulo 2^k. Consequently, for every k,

    n ≡ L_k (mod 2^k)
    iff 3n+1 ≡ 3L_k+1 ≡ 0 (mod 2^k)
    iff k ≤ v₂(3n+1).

For positive odd n, 3n+1 is nonzero and even, so the matching set is precisely the nonempty finite initial interval {1,…,v₂(3n+1)}. Substituting n=L_k+2^k q gives

    3n+1 = 2^k(3q+c_k).

At maximal k the factor in parentheses is odd, hence is exactly U(n). This proves both assertions without enumeration. ∎

**Necessary qualification.** If k is merely a matching index, the algebraic identity remains true but its quotient need not be odd. For n=1, k=1 matches, L_1=1, q=0, and 3q+c_1=2, whereas U(1)=1 with k=2. Thus an unqualified claim that *any* matching k produces the accelerated successor is false.

The argument extends to odd ordinary negative integers, using the valuation of the absolute numerator; 3n+1 cannot vanish at an integer. The handoff implementation intentionally accepts only positive odd integers. In Z₂ it extends to odd x≠−1/3, with q∈Z₂. At x=−1/3 all matches hold and no finite accelerated successor is defined. This is a domain exception, not a counterexample to Theorem A as stated.

### 1.1 Balls, shells, and base-4 digits [REFORMULATION]

Let

    C_k = −1/3 + 2^k Z₂,
    E_k = C_k \ C_(k+1).

C_k is a clopen 2-adic cylinder/ball. E_k is the exact-valuation shell. The matches are LSB-first 2-adic prefix agreements; they are trailing-bit agreements in ordinary MSB-first notation. C_(k+1)⊂C_k, their intersection is {−1/3}, and v₂(3x+1)=v₂(x+1/3).

The geometric series gives

    −1/3 = Σ_(r≥0) 4^r = (…1111)_4 = (…010101)_2,
    L_(2r−1) = L_(2r) = 1+4+…+4^(r−1).

Thus L_k is a convenient truncated representative of −1/3 modulo 2^k. Nothing in this equality changes the dynamics. At maximal k, oddness of 3q+c_k forces q even for even k and q odd for odd k. For positive n, q≥0: indeed 0<L_k<2^k and a negative integral q would make n negative.

An exact shell maps onto all odd 2-adics under U. For any odd y,

    x = (2^k y−1)/3

has exact valuation k and U(x)=y. Hence closeness to −1/3 does not constrain the next state to be close to that center. Even the positive fixed point U(1)=1 stays at constant distance |1+1/3|₂=1/4. The center is not an accelerated fixed point; T(−1/3)=0 for the shortcut map defined in §3. Static convergence of L_k to the center is not dynamical attraction.

## 2. Global reconstruction, convergence, and the inverse domain

Let k_i≥1 be finite integers, s_0=0, and s_j=Σ_(i<j)k_i. Suppose a sequence n_i satisfies

    n_i = (2^k_i n_(i+1)−1)/3.

**Finite identity [KNOWN / REFORMULATION].** For every J≥0,

    n_0 = −Σ_(j=0)^(J−1) 2^s_j / 3^(j+1) + R_J,
    R_J = 2^s_J n_J / 3^J.                         (F)

The empty sum convention makes J=0 valid. For the induction step, substitute the recurrence for n_J in R_J. It produces the new summand −2^s_J/3^(J+1) and new remainder 2^(s_J+k_J)n_(J+1)/3^(J+1). This is (F) at J+1. No trajectory estimates are used. ∎

**Infinite identity [KNOWN / REFORMULATION].** If all n_i are odd elements of Z₂ and the recurrence holds, then

    n_0 = −Σ_(j≥0) 2^s_j / 3^(j+1).              (I)

The terms have valuation s_j≥j, so the series converges in the complete field Q₂ and has sum in Z₂. Since 3 is a unit and n_J is odd,

    v₂(R_J)=s_J →∞.

Thus R_J→0, proving (I). The truncation error has *exactly* valuation s_J, not merely at least s_J. No boundedness in the ordinary absolute value and no Collatz-convergence assumption are needed. Every positive odd integer has an infinite odd trajectory, including continued repetition of 1 after first reaching it, so the hypotheses apply to all such integers.

More generally, for a recurrence in Q₂ the series converges exactly when s_j→+∞ (its terms must tend to zero); identification with n_0 additionally requires s_J+v₂(n_J)→+∞, with the usual convention at zero. Uniform integral n_J are sufficient when s_J→∞. Convergence of the series alone is not a terminal-boundary condition. For example k_i=1, n_i=3^i/2^i−1 satisfies the recurrence and has n_0=0, while the series sums to −1 and R_J=1−(2/3)^J→1 in Q₂. These n_i leave Z₂, so they do not contradict (I).

If zero run lengths are allowed, s_j need not tend to infinity; K=(0,0,…) has summands of valuation zero and does not converge in Q₂. Such words are outside odd-to-odd Collatz coding.

### 2.1 Every infinite positive run word has a unique 2-adic realization

**Theorem B [KNOWN / REFORMULATION].** Let N₊={1,2,…}. For every K∈N₊^N, define each tail value

    x_i = −Σ_(r≥0) 2^(k_i+…+k_(i+r−1)) / 3^(r+1),

where the exponent for r=0 is zero. Each series converges and x_i is odd: the first term is −1/3≡1 modulo 2 and all remaining terms are even. Splitting off the first term gives

    3x_i+1 = 2^k_i x_(i+1).

Because x_(i+1) is odd, the valuation is exactly k_i. These are actual accelerated iterates and none is the exceptional point −1/3. Conversely (I) proves uniqueness of any realization. Therefore K is in bijection with

    D = {x∈1+2Z₂ : the accelerated orbit exists for every finite step}.

Equivalently D consists of odd x whose shortcut parity sequence contains infinitely many 1s. The omitted odd points have finitely many 1s and eventually reach zero under T; at their last odd visit they equal −1/3. Thus D is not all odd Z₂. Its complement within the odd part is countable: finite binary supports form a countable set, and the parity inverse in §3 is bijective.

The coding sends U to deletion of the first run: U(F(K))=F(shift K). It is a homeomorphism for the product topology on N₊^N and the subspace topology on D: a finite prefix determines the ball computed next, and each finite exact-valuation itinerary is locally constant. It is a first-return coding, not a conjugacy identifying one accelerated step with one *binary* shift.

### 2.2 What a finite run prefix determines [REFORMULATION]

Put A_J=−Σ_(j<J)2^s_j/3^(j+1). Prescribing J exact run lengths allows any odd terminal y, and backward substitution yields

    x = A_J + (2^s_J/3^J)y.

Backward intermediate states are odd and have the prescribed exact valuations. Thus the exact prefix is precisely

    x ∈ A_J + 2^s_J/3^J + 2^(s_J+1) Z₂.          (C)

It fixes s_J+1 input bits. Merely requiring x≡A_J modulo 2^s_J omits the odd-terminal bit and can admit a longer last run. For example K=(1) requires x≡3 modulo 4; x≡1 modulo 2 alone also admits x=1, whose run is 2. Every cylinder (C) contains infinitely many positive integers, so no finite run prefix by itself excludes positive-integer realizations. An infinite word need not have one.

### 2.3 Counterexamples to stronger interpretations

For constant K=(a,a,…), the convergent 2-adic geometric series gives

    x = −(1/3)/(1−2^a/3) = 1/(2^a−3).

It is an odd rational fixed point of U, with exact exponent a. Thus a=1 gives −1, a=2 gives 1, a=3 gives 1/5, and a=4 gives 1/13. Positivity and ordinary integrality are separate requirements. These examples falsify any inference that the coding parametrizes positive integers by all infinite positive run words.

For a periodic word (k_0,…,k_(p−1)), let S=s_p and

    B = Σ_(j<p) 3^(p−j−1) 2^s_j.

Solving (F) with n_p=n_0 gives

    n_0 = B/(2^S−3^p).                            (P)

The denominator is nonzero and odd; B is odd. Tail construction proves the resulting rational orbit has those exact runs (its minimal period may divide p). Positivity requires 2^S>3^p, and integrality requires the denominator to divide B. This is a useful standard arithmetic filter, not a new cycle theorem. An eventually periodic word similarly gives a rational value by a finite prefix followed by (P). No converse asserting eventual periodicity for every rational starting point is proved here.

Over the reals (I) is generally false. For n=1 with K=(2,2,…), R_J=(4/3)^J and the negative partial sums tend to −∞, although the 2-adic sum is 1. For K=(1,1,…), the real sum happens to converge to −1; that does not license interchange of the two topologies.

## 3. Exact Bernstein–Lagarias dictionary

The primary comparison is [Bernstein–Lagarias 1996, §1, equations (1.1)–(1.6)](https://websites.umich.edu/~lagarias/doc/bernstein.pdf). It defines the shortcut map T, shift S, parity inverse Φ⁻¹, and inverse series Φ. Its (1.6) uses indexing beginning at 1; our sum begins at 0. It credits the series to Bernstein 1994 and the parity construction to earlier work. Consequently the global formula here is exactly a known inverse-conjugacy series after replacing 1-bit positions by cumulative runs; no extra landmark term appears.

To remove convention ambiguity, this report uses

    T(x) = x/2 if even; (3x+1)/2 if odd,
    σ(z) = (z−(z mod 2))/2,
    Q(x) = Σ_(t≥0) (T^t(x) mod 2) 2^t,
    Φ = Q^(-1).

The unshortened convention “odd step is 3x+1” is not T; with that convention the positions change. All equalities below use this displayed T.

| Object | Exact correspondence |
|---|---|
| Parity coordinate | Q(x); Bernstein–Lagarias (1.5), denoted Φ⁻¹ there |
| 1-bit positions | Q(x)=Σ_j 2^d_j, with d_j strictly increasing |
| Odd starting point | d_0=0 |
| Accelerated state | n_j=T^s_j(n_0) |
| Run k_j | One odd shortcut step followed by k_j−1 even steps |
| Parity block | 1 followed by k_j−1 zeros, in time order / LSB-first |
| Position identity | d_j=s_j, exactly, not s_j+j |
| Global series | Φ(Σ_j2^d_j)=−Σ_j2^d_j/3^(j+1) |
| Binary dynamics | Q∘T=σ∘Q; T=Φ∘σ∘Q |
| Accelerated dynamics | Q(U(x))=σ^{k(x)}(Q(x)), where k(x)=v₂(3x+1) |
| Run dynamics | K(U(x))=shift(K(x)) on D |
| Landmark congruence | x∈C_k iff first return to odd takes at least k shortcut steps, excluding the infinite-return exception |
| Exact shell | x∈E_k iff first return takes exactly k steps |
| Non-odd initial point | d_0>0 records initial even steps; infinite K alone then omits that initial offset |
| Finite binary support | Finite inverse sum; eventual T-orbit zero, outside D when starting odd |

In the accelerated-dynamics row σ^{k(x)} means the iterate σ raised to the integer k(x), not evaluation of σ on k. Written without typography ambiguity: `Q(U(x)) = iterate(σ, k(x), Q(x))`.

**Independent verification of the dictionary [REFORMULATION].** Starting at odd n_j, write 3n_j+1=2^k_j n_(j+1). After the odd T step the value is 2^(k_j−1)n_(j+1); after k_j−1 more halvings it first becomes odd again. Hence the next 1 position advances by k_j, proving d_j=s_j inductively. Substitution in the inverse series yields (I) verbatim.

For completeness, the series inverse and conjugacy can also be checked without assuming them. For any binary z with increasing 1 positions, define Φ(z) by that series, with empty sum zero. It preserves parity. If z is even, Φ(z)=2Φ(z/2). If z is odd,

    Φ(z)=−1/3 + (2/3)Φ((z−1)/2).

Therefore TΦ=Φσ. Iteration and parity preservation show QΦ(z)=z. Conversely, any prescribed N-bit parity word determines x modulo 2^N uniquely: invert the N affine T branches, each having slope 2 or 2/3, so the composed inverse has slope 2^N divided by an odd number. All terminal Z₂ values therefore produce one input residue, with the desired branch parities. Compatible residues over all N give a unique x, proving ΦQ(x)=x. This also proves that Q and Φ preserve the 2-adic distance by preserving the first differing bit position. ∎

An easy source of confusion is that the same rational −1/3 occurs in two different spaces: Φ(1)=−1/3 (state whose parity word is a lone 1), whereas Q(1)=−1/3 (parity word 101010… for the state 1). The coordinate space and the state space are isomorphic copies of Z₂, not identical interpretations of each numeral.

The coefficients α_j=−3^(−j), j≥1, are 2-adic landmarks indexed by inverse powers of 3. They are not a “3-adic chain.” Their indexing in (I) is α_(j+1); they are not the integer truncations L_k.

## 4. What base 4 adds, and what it does not

### 4.1 Finite-state comparison

**Established limited simplification [REFORMULATION].** A matcher for the infinite LSB-first binary word 101010… needs two live phase states, expecting 1 and 0 respectively, plus a failure sink if recognition is required. They cannot be identified: the same next bit has opposite accept/fail behavior in the two phases. Grouping pairs gives the base-4 word 111…, needing one live matching state plus a sink. This is a real notation-level simplification, bought by a four-symbol rather than two-symbol alphabet and a two-bit consumption step.

It is not a demonstrated smaller transducer for the full accelerated successor. A nonmatching base-4 digit still requires distinguishing which of its two bits first mismatched, to recover odd versus even k. Emitting an unbounded integer k also needs a counter or a variable-length output convention; a mere recognizer does not compute it.

For a fair elementary arithmetic baseline, an LSB-first transducer for multiplication by 3 plus 1 in base b has initial carry c=1 and rule

    output digit = (3a+c) mod b,
    next carry = floor((3a+c)/b).

For both b=2 and b=4 the reachable carry states are exactly {0,1,2}. All are closed under the rule and reachable from c=1. They are distinguishable by future output: in base 4 their immediate outputs at a=0 differ; in base 2 c=1 differs immediately, while c=0 and c=2 differ on the following zero after their first zero output. This compares the arithmetic core, not a proved minimal composite accelerated machine. Base 4 has twice as many transitions per carry state. Stripping zeros and output alignment add further control.

**Verdict:** no smaller complete machine established. Minimality across every model, signed digit system, or asynchronous transducer remains unproved. Related automata already exist: Stérin–Woods construct a quasi-cellular Collatz automaton involving bases 2 and 3 [R3]. That is relevant prior art, not a proof of equivalence to this particular matcher.

### 4.2 Compression and entropy

**[REFORMULATION]** Replacing k bits `10…0` with an integer k is ordinary run-length coding. Counting integer symbols without charging for their bit lengths is misleading. An Elias gamma code for k has length 2 floor(log₂ k)+1: at k=2 it uses 3 bits instead of 2; at k=4 it uses 5 instead of 4; at k=64 it uses 13 instead of 64. Savings are data-dependent and equally available from binary parity words. Two bits regrouped into a base-4 digit still carry two bits of information.

There is also an exact ensemble statement derived here from (C). Normalize Haar measure on odd Z₂ to total mass 1. A prefix K of total length S has probability 2^(−S); hence its run probabilities factor as Π_i2^(−k_i). The runs are independent geometric variables in this measure, with

    P(k=a)=2^(−a), E[k]=2,
    H(k)=−Σ_(a≥1)2^(−a)log₂(2^(−a))=2 bits/run.

The original unary parity block has precisely that expected length. A uniquely decodable lossless code cannot strictly shorten *every* block; the original lengths already satisfy Σ_a2^(−a)=1. More elementarily, at each finite binary precision the parity map permutes all residues, so an injective re-encoding cannot give all words shorter distinct binary descriptions. “Zero modular entropy” is therefore false if it means disappearance of this information. A deterministic map having zero conditional uncertainty once the input is specified is a different, trivial statement.

This is a Haar-ensemble result, **not** a proof that every fixed positive-integer orbit has independent runs or negative average real drift. Positive integers form a countable Haar-null subset; almost-everywhere statements cannot resolve the Collatz conjecture.

### 4.3 Invariants and monotonicity

**[FALSIFIED for the following explicit candidates]** Ordinary state size, k, and L_k do not decrease monotonically. Along 3→5→1→1, k is 1,4,2,2 and the corresponding L_k is 1,5,1,1. Thus both directions of monotonicity fail for k and L_k, while ordinary size first increases. Distance to the center similarly decreases then increases, because it equals 2^(−k).

There is a stronger limitation for invariants depending only on k on D: every adjacent pair (a,b) occurs, since every positive infinite word is realizable. Thus if f(k(U(x)))=f(k(x)) for every x∈D, f(a)=f(b) for all a,b, so f is constant. Even requiring a nonincrease for every orbit forces f(b)≤f(a) for every pair, hence constancy. The same argument applies to positive integers for adjacent runs, since every finite prefix has positive representatives by (C). This does not rule out invariants depending on the full state or more elaborate data.

### 4.4 Does it expose an unavailable proof obligation?

**[REFORMULATION]** The positive-integer Collatz conjecture becomes:

    for every positive odd n, K(n) is eventually (2,2,2,…).

The reverse implication holds because the all-2 tail uniquely reconstructs 1; the forward implication holds because U(1)=1. This is clear notation, but exactly the parity-tail criterion transported through §3. Formula (P) isolates cycle integrality; again it already follows from ordinary affine iteration. The reconstruction theorem supplies no real growth bound, no exclusion of all nontrivial positive cycles, and no treatment of all possible divergent positive orbits. None of those missing ingredients is recovered by regrouping bits.

### 4.5 Computation and cryptography

**Present utility [REFORMULATION]:** the handoff supplies a separate implementation of the same transition, useful for cross-checking carry, stripping, and indexing errors. AST separation is source-level independence; the evaluators remain algebraically identical. The landmark loop makes k+1 congruence attempts and repeatedly constructs powers, while the direct implementation computes 3n+1 and a lowest-set-bit valuation. This is a structural operation comparison, not a benchmark or universal complexity lower bound. No timing or hardware-energy advantage was measured.

**[FALSIFIED as a security rationale]** The known finite parity permutation is efficiently invertible without a key: compute the N-term modular inverse series. It preserves input residue classes and the first differing bit position. Therefore mere use of this permutation supplies neither one-wayness nor conventional avalanche diffusion across low bits. The accelerated map alone also loses branch information (for instance U(1)=U(5)=1). Calling either representation a cipher, a hash, or “Feistel-like” does not establish a construction or security property. No cryptographic scheme is proposed or audited here; combinations with independent secret-key primitives would require a separate specification and proof.

## 5. Experiments and reproducibility

All experiments use Python 3.12.0 standard-library exact integers and Fraction arithmetic. Source: `research/verify_tail_0003.py`; observed output: `research/COLLATZ-TAIL-0003-EXPERIMENTS.json`. No randomness, floating-point convergence inference, third-party dependency, or large brute-force conjecture search was used in the new script.

Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
PYTHONPATH=. python3 research/verify_tail_0003.py
```

| Experiment actually run | Observed result | What it checks |
|---|---|---|
| Existing handoff suite | 3 tests passed | 1,000 small and 1,000 seeded 64-bit one-step comparisons, landmark identities, source separation |
| 100 positive odd starts below 200, 32 odd steps each | 3,200 checks passed | Finite identity, exact remainder valuation, both evaluators, shortcut parity blocks |
| Every binary parity word of length 1 through 12 | 8,190 words passed | Modular inverse, forward parity reproduction, bijection at each precision |
| Words of lengths 1–4 over {1,2,3,4}, three positive lifts per cylinder | 340 cylinders passed | Exact s_J+1-bit prefix formula and realized runs |
| Same 340 words repeated periodically | 340 rational cycles passed | Periodic reconstruction and exact valuations, including nonintegral cases |
| Reachable arithmetic carries for bases 2 and 4 | Both {0,1,2} | Bounded arithmetic-core state comparison |
| Gamma versus raw lengths at 1,2,3,4,8,16,64 | Both expansions and savings | Refutes a uniform compression story for this code |

The symbolic arguments above establish the infinite assertions; these finite tests detect indexing mistakes and implementation regressions. They are not independent formal proof verification. The new script deliberately includes the odd terminal bit and permits rational periodic examples to prevent positive-integer assumptions from passing unnoticed.

## 6. Literature record, scope, and unresolved questions

Sources accessed on 2026-09-10. Primary formulas were read in the full Bernstein–Lagarias author-hosted PDF, especially its first two pages; no conjecture-proof claim from informal search results is used. Bernstein's 1994 bibliographic record and indexed abstract were also checked. The direct `cr.yp.to` PDF fetch failed in the browser tool; the Lagarias-hosted full 1996 paper supplied the necessary exact formulas, so literature access was not a blocker.

- **R1.** Daniel J. Bernstein, *A non-iterative 2-adic statement of the 3N+1 conjecture*, Proceedings of the AMS **121** (1994), 405–408. [DOI](https://doi.org/10.2307/2160415); [author PDF](https://cr.yp.to/papers/231.pdf); [institutional bibliographic record](https://research.tue.nl/en/publications/a-non-iterative-2-adic-statement-of-the-3n1-conjecture/). The indexed abstract explicitly gives the series with coefficients −1/3, −1/9, −1/27 and increasing 1-bit positions. Full 1994 text was not successfully fetched in this run; exact formula attribution is independently present in R2.
- **R2.** Daniel J. Bernstein and Jeffrey C. Lagarias, *The 3x+1 conjugacy map*, Canadian Journal of Mathematics **48** (1996), 1154–1169. [DOI](https://doi.org/10.4153/CJM-1996-060-x); [full author-hosted PDF inspected](https://websites.umich.edu/~lagarias/doc/bernstein.pdf). §1, equations (1.1)–(1.6), is the decisive comparison. The paper explicitly discusses rationality/periodicity separately from the conjugacy; this report makes no converse rationality claim.
- **R3.** Tristan Stérin and Damien Woods, *The Collatz process embeds a base conversion algorithm*, [arXiv:2007.06979v4](https://arxiv.org/abs/2007.06979v4), 2022 revision of a 2020 submission. The author abstract describes a quasi-cellular automaton, simultaneous binary/ternary evolution, and a base-3-to-base-2 conversion interpretation. Abstract-level comparison only; no minimal-state theorem from this work is asserted.

Searches included “Bernstein Lagarias 3x+1 conjugacy map”, “Collatz parity vector inverse Bernstein formula”, “Collatz base 4 finite state transducer landmark 1 5 21”, and “Collatz run length encoding parity vector accelerated map entropy geometric distribution”. These targeted searches suffice to identify the global formula's prior publication, but are not an exhaustive priority search for every base-4 implementation. No claim of novelty follows from failure to find an identical phrase.

**Strongest remaining mathematical question:** characterize which infinite K reconstruct positive ordinary integers in a way strong enough to prove an eventual all-2 tail. The series alone is a coordinate restatement; solving this in full would solve the positive Collatz problem. A more bounded arithmetic project is to use (P) with a specified restricted word family and prove new integrality exclusions, comparing against existing cycle bounds before claiming novelty.

**Strongest bounded CANDIDATE-NOVEL engineering question:** under a specified streaming model, bit-cost measure, output format, and target hardware, does a base-4 exact-shell/successor implementation improve total states, delay, or energy over an optimized binary implementation after alphabet and alignment costs? Require a complete machine, correctness proof, minimized baseline, and reproducible measurements. This report establishes no such advantage.

## 6A. Opportunity / extra-mile broker result: what can be decoded from K?

This is the adjacent question suggested by the phrase “need not reconstruct positive integer.” It has a sharper answer than the original report's domain warning.

**Theorem C [KNOWN / REFORMULATION].** Let F map an infinite positive run word K to the 2-adic value in Theorem B. A finite prefix of K never certifies that F(K) is an ordinary positive integer. In fact, every prefix cylinder contains infinitely many positive odd integers and infinitely many nonintegral 2-adic values.

**Proof.** A prefix of total length S fixes the input to one odd residue class modulo 2^(S+1), by (C). Every positive representative of that class has the same exact prefix, and there are infinitely many such representatives. For nonintegral realizations, the same cylinder contains continuum-many tail words, hence continuum-many 2-adic values by injectivity of F, whereas ordinary integers are countable. Thus no finite observed K prefix decides integer membership. ∎

The result is stronger than “the reconstruction may be negative.” It says that an exact decoder needs an additional promise, such as an a priori bound 0<n<B, a finite binary description of n, or a terminal certificate. Under a known bound B, one can compute enough K bits to recover the unique residue in [1,B] (at most ceil(log₂B)+1 bits beyond the relevant prefix) and verify the finite run prefix directly. Without such a bound, the natural procedure “keep extending the prefix until the residue stabilizes as a small integer” is only a semidecision procedure: a later bit may still change the residue.

There is no contradiction with uniqueness in Z₂. The infinite address determines exactly one 2-adic point; the obstruction is deciding whether that point belongs to the countable subset N⊂Z₂ from an unbounded stream. In a general computable-input model this membership problem has no uniform finite-time algorithm: a binary stream can encode an arbitrary undecidable set, while “is eventually all zero” (the ordinary-integer condition in the state’s binary expansion) is not decidable from finite observations. A precise complexity theorem requires fixing the representation of infinite K and the allowed oracle model; the unconditional statement established here is the finite-prefix impossibility and the bounded-promise algorithm.

This also reframes the practical value of K. It is an exact *address/certificate stream* for a 2-adic state, not a standalone compression format for an ordinary integer. With a bound or a supplied terminal certificate, it becomes an effective decoder; without one, it is an exact representation with a noncomputable-in-general range-membership question. This is the strongest useful adjacent result found in the broker pass.

## 7. Five speculative applications or monetization ideas

These are speculation, not mathematical results or validated market opportunities.

- A paid interactive lesson showing how real and 2-adic convergence differ using the same Collatz series.
- An open-source exact-arithmetic certificate checker with paid integration support for research workflows.
- A classroom parity/run-length/base-4 visualizer sold as a teaching module or workshop.
- A benchmark package comparing verified binary and radix-4 streaming implementations for education and hardware experiments.
- A reproducibility service that turns experimental number-theory claims into proof obligations, counterexample suites, and auditable reports.
- A bounded-address decoder API that accepts K together with an explicit integer bound and returns a verifiable ordinary-integer candidate (speculative product idea, not a mathematical result).

## 8. Delivery and boundaries

Dedicated branch: `agent/wolfram/COLLATZ-TAIL-0003`. The local repository is `/Users/pavelcherkashin/Research/collatz-tail-0003`; this full report is at `research/COLLATZ-TAIL-0003-PROPOSAL.md`. A standalone local copy is saved at `/Users/pavelcherkashin/Research/COLLATZ-TAIL-0003-PROPOSAL.md`. New code and evidence are confined to `research/`; the stable implementation, tag, and existing history are preserved.

Publication is to one PR from this branch to main; no merge is authorized. The final user-facing delivery records the actual commit and independently verified PR URL, avoiding a self-referential report commit hash. No mailbox envelope or outcome path was supplied in this direct user session, and no mailbox state, receipts, host configuration, credentials, or secrets were changed.

    one-step symbolic theorem: PROVED
    global reconstruction theorem: PROVED under the stated hypotheses
    Bernstein-Lagarias dictionary: COMPLETE
    base-4 added-content test: NEGATIVE for demonstrated new content;
                              UNRESOLVED for future engineering advantages
    proposal file: PASS
    auto-merge: NO
