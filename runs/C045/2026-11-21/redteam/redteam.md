# C045: Pretraining with stateful external memory under update churn — independent adversarial review

**Verdict: FIX.** Learned dependencies on mutable memory can produce a genuine training problem, but the proposal must distinguish avoidable stale references, legal parametric learning and irrecoverably deleted information. Robustness to memory absence, versioned references and pre-eviction rehearsal form a stronger lawful floor than the stated age-aware controller.

Source file: `/workspace/task_ideation_v4_creative/cards/C045.md`.

There is no named memory-store implementation, read/write-policy source file or replacement-wave manifest in the card. Those are described processes, not inspected artifacts. All rewards and costs here are ESTIMATED planning judgements. This session did not execute a policy, generate training events or access hidden memory content.

## Independent attack table

| Attack | Concrete adversary steps | Current/vulnerable reward | Does current defense block it? | Required fix or decisive control | Post-fix reward | Residual risk |
|---|---|---|---|---|---|---|
| Train away fragile retrieval dependence | Randomly mask, replace or stale legal training-memory results; jointly optimize normal retrieval and memory-absent prediction so the backbone tolerates churn. | ESTIMATED 0.65–0.87 | No: changing the read/write training policy is the intervention. | Matched-work retrieval-corruption and memory-dropout floor, including no-memory training. | ESTIMATED 0.61–0.85 | A robust parametric backbone can eliminate most benefit from dependency-aware memory. |
| Version every learned reference | Address content by generation/version, validate retrieval ancestry, invalidate dependent cached features on replacement, and recompute from surviving legal evidence. | ESTIMATED 0.64–0.88 | Replacement is specified, but reference identity semantics are not. | Correct versioned starter plus content-addressed read and dependency-invalidation baseline; charge its graph and recomputation. | ESTIMATED 0.55–0.82 | The apparent scientific effect may be an ordinary dangling-reference bug. |
| Consolidate likely evictions through training | Use current memory while legal to rehearse high-value facts and relationships into fixed model parameters; retain compressed sufficient summaries for rare relations. | ESTIMATED 0.62–0.86 | Hidden copies are prohibited, but normal learned parameter information cannot simply be outlawed. | Explicit fixed-capacity weight-learning contract; pre-eviction rehearsal, parametric-only and compact-summary alternatives at the same work budget. | ESTIMATED 0.56–0.83 | Banning all internalized information would contradict pretraining itself. |
| Filesystem/mount/proc/IPC/frozen-asset access | Reopen evicted backing files, recover page-cache or shared-memory handles, read the future replacement queue, or mutate the frozen initialization. | ESTIMATED 0.94–1.00 | Persistent-copy accounting is required, without namespace or deletion semantics. | Trusted store owns eviction, isolates future waves and closes all handles; immutable base and live proc/mount/IPC probes. | ESTIMATED 0.00 | Mapped pages or a read RPC can retain old bytes after logical deletion. |
| Interface or encoded-state smuggling | Store full evicted entries in policy literals, numeric metadata, optimizer-side arrays, retrieval indexes or an unmetered model-side KV cache. | ESTIMATED 0.89–1.00 | The card explicitly recognizes model-cache copies, but the complete inventory is absent. | Aggregate canonical accounting for all external/cache/index bytes; trusted gradient-only model writes and bounded payload decoding. | ESTIMATED 0.00 | Separate a legal learned compressed representation from a concealed byte store. |
| Spoofed verdict/skipped execution/benign-bank fingerprint | Return cached low next-event losses, skip replacement, claim refresh occurred or recognize evaluator-positive memory snapshots by hash. | ESTIMATED 1.00 | Deterministic grading does not itself establish replacement or prediction execution. | Parent applies waves and computes loss from captured logits; independent equivalent positives, wrong-event and no-refresh controls. | ESTIMATED 0.00 | A candidate-provided deserializer could quietly restore pre-eviction state. |
| Timing/check-decoupling/branch laundering | Read entries after they should be displaced, do refresh training before the cost clock, check one memory snapshot and evaluate another. | ESTIMATED 0.90–1.00 | Reads/writes/refresh are charged in prose; snapshot chronology is unspecified. | Atomic wave/update/read ledger, synchronized capture and exact checkpoint/store binding; charge failed branches and reap detached workers. | ESTIMATED 0.00 | Asynchronous prefetch needs a clear commit-before-eviction rule. |
| Dev-hidden leakage/cue inference | Predict displaced support or future queries from slot IDs, replacement-message lengths, generator templates or event serialization rather than learned relationships. | ESTIMATED 0.72–0.97 | Shared churn distributions do not rule out semantic or metadata leakage. | Cross slot encodings with dependency truth; independent event/dependency families and metadata-only loss predictor. | ESTIMATED 0.18–0.47 | The public event grammar may permit a small lawful relational solver. |
| Adaptive aggregate oracle | Probe eviction/read-policy variants that isolate slots or relation classes, use loss differences to infer which hidden memories future queries require. | ESTIMATED 0.67–0.91 | No query budget, output precision or final-bank separation is committed. | Root-global protected-dev allowance and fresh final dependencies; full-cap adaptive controller in the legal floor. | ESTIMATED 0.45–0.76 | Low-dimensional retention policies can generalize after little feedback. |
| Slice abandonment/denominator optimization | Ignore events whose support was displaced, improve common retained facts, drop failed predictions or count refresh time outside the reward denominator. | ESTIMATED 0.65–0.94 | The source asks for displaced-support performance without weighting or failure rules. | Fixed offered tokens, native retained/displaced/composed strata, explicit cost function and smooth local deficits. | ESTIMATED 0.27–0.60 | Aggregate next-event loss may still reward memory avoidance. |
| Strongest lawful combined recipe | Combine version-correct retrieval, corruption/missing-memory training, selective pre-eviction rehearsal, compact dependency summaries and adaptive refresh/read allocation; compare with parametric-only learning. | ESTIMATED 0.68 (ESTIMATED 0.44–0.89) | No: all operations can respect a finite external-memory and training budget. | Execute this complete compatible stack on observable learned dependencies and actual displaced-support queries. | ESTIMATED 0.68 (ESTIMATED 0.44–0.89) | Security fixes cannot lower the reward of legal internalization and robust training. |

## Published recipe shortcut — web checked

- [Memorizing Transformers](https://arxiv.org/abs/2203.08913) describes nearest-neighbor access to stored internal representations, establishing a concrete mutable external-memory baseline family rather than static prose retrieval alone.
- [Improving Language Models by Retrieving from Trillions of Tokens](https://proceedings.mlr.press/v162/borgeaud22a.html) supplies retrieval-conditioned autoregressive training. It does not establish resilience to endogenous replacement and must not be cited as solving this task.
- [RAFT: Adapting Language Model to Domain Specific RAG](https://arxiv.org/abs/2403.10131) trains models to ignore irrelevant retrieved documents, supporting a retrieval-robustness comparator. Missing-memory dropout and pre-eviction rehearsal are explicit adversary engineering additions, not attributed RAFT results.

The Memorizing Transformers and RAFT abstracts were opened, and the RETRO primary proceedings page was found through search this session. Verification reached mechanism descriptions, not writable-memory APIs or a faithful combined implementation. I estimate the compatible recipe at ESTIMATED 0.68, with ESTIMATED range 0.44–0.89. Factual retrieval results from these sources provide no numeric calibration for private next-event loss.

## Saturation against the hypothetical 10T researcher / 12h

The adversary can deliberately avoid creating brittle dependencies. Content-addressed reads and version checks prevent silent reuse of overwritten slots; corruption-aware training can make the learner robust to the failures that remain. Before eviction, standard replay can internalize recurring relationships into the fixed parameter budget. These options act on the same training-created dependencies that the card presents as the hard mechanism. The real residual would be deciding which useful dependencies to create and consolidate when both external storage and gradient work are scarce, with future use only partially predictable from legal evidence.

My single-run maximum scenario is ESTIMATED 0.85, compared with the binding >0.70 kill. Oracle best-of-4 mean is ESTIMATED 0.77 versus >0.60, and pass@4 is ESTIMATED 0.86 versus >0.50 at R>=0.60. Stronger-researcher/expanded-compute projected upper-95% is ESTIMATED 0.95 versus the source >=0.75 line. All are likely breaches for the current broad formulation. The projected endpoint is an ESTIMATED planning bound only; no statistical fit, observed target-tier result or confidence-calibrated extrapolation exists.

S1 cannot pass without an executable same-budget reference and a stronger legal control showing further native next-event improvement. A private evaluator that retains deleted information cannot serve as that control. S7 is OPEN until the independently achievable ceiling is bracketed. If fresh queries require arbitrary high-entropy facts whose only copies were forcibly removed and never internalized, residual loss may be irreducible; that is not a discoverable method gap. A decoder given extra retrieval or model state is a diagnostic, not an attainable lower ceiling bound.

Rollout scores and observed pass@k remain UNMEASURED; proposed collection spans independent event/dependency families and independently restarted full-budget read/write-policy searches. Observed run count is UNMEASURED. Grader noise is UNMEASURED; planned regrades distinguish deterministic scalar loss on frozen logits, stochastic memory writes and full-pipeline training variability. Retain failed attempts and compare actual protected-dev selection with retrospective oracle best-of-k. Researcher reasoning, parallel experiments, serial time and subject-update work must be swept separately. Assume the target researcher actually builds strong notes and robust checks; current-model errors do not defend this environment.

## Revised estimate versus the source card

The card gives source ESTIMATED 0.40 to age-aware replacement, refresh and rehearsal. My ESTIMATED 0.68 composite additionally changes how the learner depends on memory: version-safe addressing, robustness to irrelevant or missing results, and deliberate parametric consolidation before removal. A replacement invalidating many learned paths is not by itself evidence that these strategies fail; it is precisely the fault pattern the baseline should expose during legal training. The remaining uncertainty is whether small useful dependency summaries and fixed weights can carry enough information at the actual budgets.

There is also a scientific ambiguity in “private entry-replacement waves.” If replacement only evicts a representation of a still-true event, consolidation helps. If it changes the event's truth, rote consolidation can harm and explicit version/context semantics become essential. If it assigns a fresh hidden truth without any legal observation, nobody can recover it. Those cases must not be blended into a single apparently difficult score. The FIX recommendation depends on choosing the first or an observable version of the second case and specifying a feasible causal reference.

## Boilerplate and missing build content

I estimate source content as ESTIMATED 0.72–0.87 specific and ESTIMATED 0.13–0.28 generic; it is not mostly boilerplate. It still omits the memory schema, read/write action language, model initialization, fixed parameter capacity, permissible learned summaries, update order, replacement semantics, event distribution, total exposure/work law, loss mask and native-to-reward mapping. No reference demonstrates which dependencies it creates or how their later loss is repaired.

Build content must include an inventory of every persistent state category and its mutation authority. Ordinary trained parameters are fixed-capacity scientific state; a second shadow array containing evicted bytes is an external store. The boundary cannot be “whatever looks like remembering” after an attack succeeds. Charge memory metadata, retrieval indexes and recurrent/KV caches by canonical reconstructed size, and describe whether write policies can choose what gets replaced or only react to exogenous waves. The cost of tokenization, repeated retrieval and refresh updates needs a common unit or explicit hard limits before comparing policies.

## Duplicate check

The nearest W02 file named by the source was not in the permitted reference list and was not opened; its claimed difference remains unverified. Among reviewed items, C010 also considers retention after later information changes, but it stores robot evidence for revised labels rather than learning against a mutable read/write memory. C024 compresses a scientific ledger for a reset frozen researcher, whereas C045 jointly trains the model and memory policy. T08's checked FIX packet shares continual retention but fixes replay and changes tool obligations. Those comparisons do not establish a duplicate; they also do not prove catalog-wide novelty.

## Verdict, required fixes and cheapest decisive check

FIX with the following required work:

1. Define whether replacement evicts evidence, alters truth or both, and provide legal observations that make the target next event identifiable after each wave. Remove privileged-reference and impossible-information cases.
2. Start with version-correct references; add full missing/corrupted-memory training, consolidation/rehearsal and parametric-only controls under matched total work. Retain only a native residual involving learned dependency allocation.
3. Commit the fixed model capacity, all external/cache bytes, exact event/token denominators, costs and slice utility. Produce a reproducible reference and stronger same-contract control before normalization.
4. Enforce memory ownership and snapshot chronology in a portable isolated trainer. Regression tests must try old file handles, hidden stores, policy payloads, skipped replacement, forged loss, late reads and branch swaps; require independently constructed equivalent positive learners. Include protected representative dev, global query caps, trusted libraries, matched warmup, per-seed timeouts, pruned ancestors, decontamination and archive-level result reconciliation.

The cheapest decisive audit uses CPU reasoning at ESTIMATED 0 H100-hours: follow a small dependency graph through replacement and check whether all intended target conditionals are functions of legal remaining history and allowed learned state. In parallel as a design calculation, compare versioned invalidation with the intended “dependency repair”; if they are identical, reject the research claim before training. A contingent compact learner study is ESTIMATED 24 H100-hours for corruption-aware rehearsal, parametric-only, age-refresh and reference trajectories through shared-dependency waves. It exceeds the card's source ESTIMATED 18 GPU-h because the added whole-training alternatives are necessary, but remains provisional until actual model/throughput is specified. Neither audit nor study was executed; the CPU gate can falsify identifiability, not certify saturation.

## Verdict record

id: C045
source_group: creative_v4
verdict: FIX
strongest_attack: ESTIMATED 0.68 (ESTIMATED 0.44–0.89)
combined_recipe_attack: ESTIMATED 0.68 (ESTIMATED 0.44–0.89)
best_of_4: ESTIMATED 0.77
pass_at_4: ESTIMATED 0.86
single_run_max: ESTIMATED 0.85
upper95_projected: ESTIMATED 0.95
kill_line_breached: single,bo4,pass4,upper95
decisive_gpu_h: ESTIMATED 0
required_fixes: replacement truth semantics; version-correct starter; robust-retrieval and consolidation floors; complete memory ledger; identifiable post-wave events
main_kill_reason: robust training and legal consolidation bypass fragile memory
duplicate_of: none
souping_flag: none
urls_cited: ESTIMATED 3
