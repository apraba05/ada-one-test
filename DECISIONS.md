# Ada Knowledge QA — Architectural Decisions and Tradeoffs

Companion to [DESIGN.md](DESIGN.md). That document describes *what* was built. This one argues
*why*, and what each choice cost.

## How to read this

Every decision is examined through two lenses, because they genuinely disagree in places and
the disagreement is the interesting part:

- **CEO lens** — what this does to trust, cost, speed of evaluation, dependency risk and
  optionality. What it signals about the product to whoever is watching.
- **Staff Engineer lens** — correctness, failure modes, coupling, operational burden,
  reversibility, and whether we can *prove* the thing works.

Where the two lenses conflict, the resolution is stated explicitly rather than papered over.
Each decision ends with the condition that should make us revisit it — a decision without a
revisit trigger is a belief, not a decision.

---

## D1 — Refuse rather than hedge

**The decision everything else follows from.** When confidence is insufficient, return a flat
refusal. No "based on the available information, it appears that…", no partial answers, no
confidence percentages for the user to interpret.

**Forcing question:** what is the worst thing this tool can do?

**Options considered:** (a) always answer, with a confidence score attached; (b) hedge with
qualifying language when unsure; (c) hard refuse below a bar.

**CEO lens.** The user is evaluating Ada. A fabricated answer doesn't cost a support ticket —
it costs belief in the product being evaluated, and it's the kind of failure that gets repeated
to other people. A refusal costs one follow-up question. The asymmetry isn't close. Hedging is
the worst of both: it still delivers the wrong information, but with deniability, and it teaches
users to skim past the qualifier. Options (a) and (b) both quietly transfer the burden of
judgement onto the person least equipped to carry it.

**Staff lens.** A confidence score exposed to users is a decision we've declined to make,
dressed as transparency. Someone must pick the bar; better it's us, once, visibly, and testable —
than every user, implicitly, differently. A binary output is also the only version that is
*assertable*: "refuses when it should" is a test case, "hedges appropriately" is not.

**What it costs.** The tool will sometimes refuse a question it could have partly answered.
We accept that; §D4 is the machinery for making the boundary defensible rather than arbitrary.

**Revisit when:** users report frequent refusals on genuinely covered material — that's a
retrieval or coverage problem masquerading as a policy problem, and the fix belongs upstream.

---

## D2 — Two independent gates, not one confidence number

Retrieval similarity ≥ 0.35 **and** an LLM judge's groundedness ≥ 0.60 **and**
`answers_question`. All must pass.

**Forcing question:** can a single number express "we should show this"?

**CEO lens.** These check different risks, so collapsing them hides one. Retrieval asks *do we
have material on this topic*; the judge asks *did the model actually stay inside that material*.
A tool can be well-supplied and still fabricate, or be honest about thin sources and still be
useless. One number averages those into something that means nothing in particular.

**Staff lens.** They fail independently, which is the entire argument for having both. And the
ordering is load-bearing: the cheap check runs first, so off-topic and adversarial input is
rejected in ~0.1s having spent zero LLM tokens. Safety and cost fall out of the same mechanism —
we didn't build a separate abuse path.

**What it costs.** Two thresholds to calibrate instead of one, and a compound condition that
needs the margin reporting in §D9 to stay honest.

**Revisit when:** the gates stop failing independently. If one never fires, it's decoration.
Today both do.

---

## D3 — The judge is a separate LLM call, not self-assessment

A second, independently framed call sees the question, the generated answer and the sources, and
audits the answer. It never sees itself as the author.

**Options considered:** ask the generator to rate its own output; use token logprobs as a
confidence proxy; a separate judge call.

**CEO lens.** This is the one place I'd spend the extra call. Self-reported confidence comes from
the same process that produced the error — asking a model to check its own work is asking the
witness to be the auditor. The cost is real (two calls per question, roughly double the per-query
LLM spend) and it buys the only thing the product actually sells.

**Staff lens.** Logprobs measure fluency, not factuality; a confidently-worded fabrication scores
well. Self-assessment shares the failure mode we're guarding against. A separate call with a
different framing gets independent judgement — not truly independent, since it's usually the same
weights, but the framing and inputs differ enough to catch a class of errors the generator
won't. Output is schema-enforced (Anthropic `messages.parse()` with a Pydantic model, Ollama's
JSON-schema `format`), so there's no prose parsing to break.

**Where the lenses tension.** A CEO looking at unit economics sees 2× LLM cost for something the
user never directly sees. The resolution: the judge *is* the feature. Remove it and this becomes
an ordinary RAG bot with a nice card layout.

**What it costs.** ~3.7s of the ~6s response, and double the per-query token spend. Notably the
judge is the *more* expensive call despite emitting fewer tokens — its prompt carries the answer
plus all four chunks.

**Revisit when:** a cheaper reliable signal exists (a small trained verifier, or a provider-native
groundedness API). The interface is already the seam.

---

## D4 — `answers_question` is separate from groundedness

The judge returns two signals. A grounded non-answer scores high on groundedness and still gets
refused.

**This came from a real bug, and it's the most instructive decision here.** "How much does Ada
cost per month?" originally shipped as a green *grounded answer*. The model had honestly written
"there is no information about pricing in the sources" — which is perfectly grounded, scoring
1.0 — so it cleared a groundedness gate and rendered as a confident answer.

**CEO lens.** The user asked a question and got a green checkmark above a paragraph explaining
nothing. That's worse than a refusal, because the visual language promised an answer. This is
precisely the failure mode D1 exists to prevent, and it had slipped through the mechanism built
to catch it.

**Staff lens.** The root cause was conceptual, not numeric: we had conflated *supported by the
sources* with *answers the question*. They are orthogonal — an answer can be either, both or
neither. The fix adds a signal rather than moving a threshold, and that distinction matters:
tuning `JUDGE_THRESHOLD` would have "fixed" this case by breaking legitimate ones, and it would
have been a number chosen to make one test pass. **The thresholds never moved.** When a threshold
change fixes a conceptual bug, you've usually hidden it.

**What it costs.** A boolean with no margin. §D9 shows this is now the *only* thing protecting
the most dangerous bucket — a real single point of failure, visible because we measure it.

**Revisit when:** we find cases where "partially answers" is the honest verdict and a boolean
can't express it.

---

## D5 — Chunk to the model's window, not to the spec

The brief suggested 300–500 token chunks. We use ~210 with 40-token overlap.

**Forcing question:** what happens at 300–500 with this specific embedding model?

`all-MiniLM-L6-v2` caps at 256 word-pieces and **silently truncates** beyond it — no warning, no
error. Re-measured on this corpus with the shipped chunker pointed at the low end of that range
(300 tokens): **274 chunks, of which 159 — 58% — exceed 256 and would be silently truncated.**
At a 400-token target it is 85%. That text exists in the corpus and could never be retrieved.

**CEO lens.** A quarter of the knowledge base would have been invisible, and the failure would
have looked like the model being unhelpful rather than the pipeline dropping data. Worse, it
would have made the *gate* look wrong — refusing things the docs actually cover — and we'd have
spent the debugging effort in the wrong place entirely.

**Staff lens.** Deviating from a written spec needs a stronger reason than preference; "the
number is incompatible with the component we're required to use" is that reason. The verification
matters as much as the change: **375 chunks, max 250 tokens, zero truncated.** Oversized blocks
(wide tables, long lists) go through progressive decomposition — paragraph → newlines →
sentences → hard token window — so the guarantee holds for arbitrary input, not just the corpus
we happen to have.

**What it costs.** More chunks, slightly more fragmented context per retrieval.

**Revisit when:** the embedding model changes. This number is a property of the model, not a
preference — which is why it's part of the cache fingerprint.

---

## D6 — In-memory numpy, no vector database

375 chunks × 384 dimensions, held in memory, persisted as a fingerprinted pickle.

**CEO lens.** A database here would be infrastructure we run, monitor and pay for, to get results
identical to a matmul over 562 KiB. It's the kind of choice that looks rigorous in a diagram and
costs real time in practice. The interesting engineering in this project is the gate; spending
the complexity budget on storage would be spending it in the wrong place.

**Staff lens.** Search is one dot product over a 375×384 matrix — **0.013ms**, utterly dominated by
embedding the query, not by the search. Adding pgvector or Qdrant buys index structures that
matter at 10⁶ vectors and cost latency at 10². What we *did* build is the part that's expensive
to retrofit: `Index.search` is a clean seam, and the cache is keyed by a **SHA-256 of the model
name, chunking parameters and every KB file's contents**, so a stale index is impossible by
construction. That fingerprint is worth more than a database — it eliminates the classic silent
bug where you tune chunking and unknowingly evaluate against old vectors.

**What it costs.** No incremental updates, no persistence beyond a local file, single process.

**Revisit when:** the corpus outgrows memory, needs incremental updates, or must be shared across
processes. None are true at 15 documents — and note that all three are *operational* triggers, not
speed ones. Measured linear-scan scaling on this machine:

| Vectors | Scan time | Memory |
|---|---|---|
| 375 (today) | 0.05 ms | 0.5 MiB |
| 10,000 | 0.21 ms | 15 MiB |
| 100,000 | 3.46 ms | 147 MiB |
| 1,000,000 | 32.1 ms | 1.4 GiB |

A brute-force scan is still faster than one LLM token at a million vectors. Approximate-nearest-
neighbour indexes buy latency we do not need; a database earns its place by owning durability and
incremental writes, which is a different argument and the one we would actually make.

---

## D7 — Provider abstraction, keyless by default

Two backends behind one interface. Auto-selects Claude when `ANTHROPIC_API_KEY` exists, else a
local Ollama model. `LLM_PROVIDER` forces either.

**CEO lens.** The tool runs with no API key, no procurement and no per-query cost, and upgrades to
Claude the moment a key appears — **with no code change**. That's optionality for free: no vendor
lock-in, no budget conversation blocking a demo, and a credible answer to "what if we want a
different model later."

**Staff lens.** Normally I'd resist this — provider abstractions are usually speculative
generality that ossifies around one vendor's semantics. It earns its place here for a specific
reason: it makes model strength a **single controlled variable**. "How much does judge quality
depend on the model?" becomes one command against a fixed eval set. That experimental capability
is what justified D8, and it's why the abstraction is only two methods wide — `generate` and
`generate_json` — rather than a general-purpose LLM framework.

**What it costs.** Two code paths for structured output, and the honest caveat that a small local
judge is weaker at exactly this job.

**Revisit when:** a third backend is needed — at which point check whether the two-method surface
still fits before widening it.

---

## D8 — Default to a 3B model, validated rather than assumed

Switched the default from `llama3.1:8b` to `llama3.2:3b`: ~2× faster, and `eval.py` still passes
8/8.

**Where the lenses openly conflict.** The CEO wants the demo fast — 12 seconds of silence in front
of an audience is the difference between "impressive" and "a bit rough." The Staff Engineer
objects that a smaller model is a weaker judge, and the judge is the product.

**How it was resolved, and this is the point:** not by argument, but by running the eval suite on
both. 8/8 on each, in 43 seconds. The switch is defensible because the gate's behaviour is
*measured* as unchanged, not asserted. Without the harness from §D9 this would have been a
gut-feel tradeoff between speed and safety; with it, it was a 43-second experiment.

**The caveat we kept.** The 3B's judge scores are visibly less discriminating — a flat 0.90 across
bucket A where the 8B spreads 0.80–1.00. Same classifications, less headroom. So `OLLAMA_MODEL`
remains one environment variable away, documented, and the recommendation for fidelity work is
still Claude.

**What it costs.** A less discriminating judge in the default configuration, accepted knowingly
and written down.

**Revisit when:** margins narrow, or the judge comparison against Claude (still unrun) shows the
small model diverging on cases the suite doesn't cover.

---

## D9 — An executable eval suite, and then margins

Eight labelled questions as data, run through the full pipeline, **non-zero exit on any
misclassification**. Later extended to report each case's distance to the threshold that decided
it.

**CEO lens.** This is time spent not building features, and it's the highest-leverage time in the
project. It converted "we believe the gate works" into "the gate is checked in 43 seconds," which
is what makes every subsequent change cheap instead of scary. It paid for itself immediately: D8
was a 2× speed win that would otherwise have been unshippable on principle.

**Staff lens.** Two details separate this from theatre. First, **the harness was verified to
fail** — a forced mislabel produces the FAIL row, diagnostics and exit code 1. A regression gate
nobody has seen go red is decoration. Second, **8/8 says nothing about robustness**, so margins
report the signed distance to the deciding threshold and flag anything within 0.10.

That second addition immediately said something uncomfortable and true:

```
THIN MARGINS (< 0.1) — closest to reclassifying:
  +0.08  (B) How much does Ada cost per month?  [decided by: answers_question]
```

**Both Bucket B questions clear the retrieval floor** (0.43 and 0.52 against 0.35). The retrieval
gate is *not* protecting the most dangerous bucket — `answers_question` is doing it alone, with
0.08 to spare. We only know that because we measured margins instead of counting passes, and it
directly changes the roadmap: any change that lifts retrieval scores reclassifies a pricing
question into a confident answer.

**What it costs.** ~43 seconds per run, and 8 questions is a small sample — it catches
regressions, it does not establish accuracy.

**Revisit when:** immediately. Expanding into the untested 0.24–0.43 band is the top roadmap item.

---

## D10 — No streaming, deliberately

**CEO lens.** Streaming is what every comparable product does and it's the obvious answer to "make
it feel faster." Not shipping it looks like a gap, and I'd want a strong reason.

**Staff lens.** The reason is structural: **Gate 2 runs after generation.** Streaming tokens means
displaying an answer the judge may be about to reject. The single promise this product makes is
that nothing ungrounded reaches the screen, and streaming breaks it in the most visible way
possible — text appears, then vanishes or is contradicted. Buffering the stream and revealing it
only after judging gains nothing, since the user sees text at the same moment either way.

**Resolution.** Attack the real number instead of masking it: latency work took a question from
~20s to ~6s (§D11), and the UI shows genuine pipeline stages with a live timer rather than an
opaque spinner. Honest progress, no false promises.

**Revisit when:** the architecture changes such that grounding can be verified *during*
generation — constrained decoding, or span-level attribution as tokens are produced. Then
streaming becomes compatible rather than merely tempting.

---

## D11 — Measure before optimising

The complaint was "too slow." The instinct was to cache, parallelise, or shrink the prompt.

**Measured first:** local generation runs at **29.6 tok/s**; retrieval is ~7ms; warm-to-warm model
overhead is 1.7s. Conclusion: response time is **almost entirely tokens generated**. Retrieval was
never worth touching, and the two LLM calls can't be parallelised because the judge needs the
answer.

That redirected the work to three things that actually mattered: a smaller model (D8), capping
answer length (~190 words → ~43), and warming both models at startup. That last one came from a
measurement I'd have missed by guessing — **a cold process pays 5.8s on its first search** because
the SentenceTransformer is lazy-loaded, so the first question was paying for *both* model loads.

| | Before | After |
|---|---|---|
| First question after boot | ~19–20s | **~6s** |
| Eval suite | 86.3s | **42.6s** |

**CEO lens.** The first-question number is the one that matters, because it's the one an audience
watches. Optimising average latency while the first question takes 20 seconds would have been
technically productive and commercially useless.

**Staff lens.** Every one of my pre-measurement instincts was aimed at something worth
milliseconds. The 5.8s lazy-load in particular was invisible in normal operation and dominant in
the exact scenario that mattered.

---

## D12 — Transparency as a product surface

The confidence trace, the evidence panel, and the thresholds themselves are rendered in the UI.

**CEO lens.** In a tool whose value proposition is trustworthiness, showing the work *is* the
feature. "It refused" is a claim; "it refused, here are both scores against their thresholds, here
is the judge's reasoning, and here are the passages it read" is evidence. It also makes the
thresholds a conversation rather than a mystery, which is what you want when the audience is
technical.

**Staff lens.** Thresholds are rendered from the API response, not hardcoded in the frontend, so
**the UI cannot drift from the policy it displays** — a class of bug that's otherwise inevitable
the first time someone tunes a constant. The evidence panel appears under refusals too, which is
the harder and more useful case: it lets someone confirm a refusal was correct rather than take
it on faith.

**A related sub-decision worth its own line.** Coverage hints ("the KB doesn't have pricing, but
it does cover Content ingestion and Knowledge setup") appear **only on judge-gate refusals**. On
retrieval-gate refusals nothing cleared the relevance floor, so naming the nearest documents would
imply a relationship the scores explicitly deny. Being helpful there would mean being slightly
dishonest, which is the one thing this product can't afford.

---

## Smaller decisions, same reasoning

| Decision | Why |
|---|---|
| Fetch `.md`, never scrape HTML | Ada's docs serve clean markdown; no parser to maintain, no selector rot |
| Ingest fails closed below 10 docs | A silently under-populated KB produces refusals that look like gate failures |
| Single decision point (`answer_query`) | CLI, API and UI are thin adapters — no interface can apply different policy, and the eval suite tests the path the UI uses |
| Generation without extended thinking | Extraction from four short passages isn't a reasoning task; the judge is the correctness net |
| Answers capped at ~120 words | A CEO wants the answer, not an essay — and tokens are latency |
| Structured output for the judge | Schema-enforced by both providers; no prose parsing to break |
| Refusal styled distinctly, not as an error | A refusal is a correct outcome, not a failure |
| Single-turn only | Keeps the gate's contract unambiguous: one question, one verdict |
| Committed on `main`, staged commits | Solo greenfield repo; each stage independently reviewable |

---

## Decisions deliberately deferred

Not "we didn't get to these" — each has a trigger:

| Deferred | Trigger to build it |
|---|---|
| Hybrid search (BM25 + vector) | Exact-term queries (product names, API fields) start failing. **Must keep cosine as the gate signal** even if fusion drives ordering, or 0.35 changes meaning |
| Cross-encoder reranking | Retrieval ordering demonstrably hurts answer quality |
| Persistent vector store | Corpus outgrows memory or needs incremental updates |
| Retry/backoff | The local backend becomes flaky in practice; the Anthropic SDK already handles 429/5xx |
| Multi-turn | Users actually ask follow-ups; gate applies per turn |
| CI | A second person touches the repo. `eval.py` already exits non-zero — it needs a runner and a key, nothing more |

---

## Decisions I'd challenge in review

Where I think the argument is weakest, stated before someone else finds it:

1. **0.35 is defensible but not measured.** It's calibrated to observed bands (off-topic
   0.15–0.25, relevant 0.66–0.88) — but nothing in the eval set sits near it, so the true boundary
   is unknown. A threshold sweep should replace the judgement call.
2. **`answers_question` is a single point of failure for Bucket B**, with 0.08 of margin, and it's
   a boolean from a small model. That's thinner than I'd like for the most dangerous bucket.
3. **The eval set is too easy.** Clean separation between buckets flatters the gate. The
   half-covered cases — where the docs touch a topic without answering it — are where real systems
   fail, and they're absent.
4. **The Claude-versus-local judge comparison is documented but unrun.** The tooling exists; the
   evidence doesn't. It stays a stated risk until someone runs it with a key.
5. **Eight questions cannot establish accuracy.** They catch regressions. Those are different
   claims and I've tried not to conflate them anywhere.

---

## Reversibility map

The question I ask before defending any of the above: *what does it cost to undo?*

| Decision | Cost to reverse |
|---|---|
| Thresholds, top-k, token caps | Trivial — constants, then re-run the suite |
| Model / provider | Trivial — one env var, behind a two-method interface |
| Vector store | Contained — `Index.search` is the seam |
| Chunking strategy | Cheap — the fingerprint forces a rebuild automatically |
| Adding hybrid search | Moderate — changes the gate's input; needs eval before and after |
| Streaming | **Expensive** — requires the gate to move inside generation |
| Refusal-first posture (D1) | **Prohibitive** — it's the product |

The pattern is deliberate: everything numeric or vendor-specific is cheap to change, and the
expensive-to-reverse decisions are the two that define what the product *is*. That's where the
complexity budget went, and everywhere else was kept boring on purpose.
