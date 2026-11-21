# Validation of hidden-task card development

Completed November 21, 2026. This is a document/inventory validation, not task certification or an independent red-team report. No ML experiments, GPU jobs, human-outcome collection, live cheat sessions or panel rollouts were run. All empirical acceptance gates remain unmeasured.

## Inventory and format

Read-only Python inspection of the final card files observed **32/32 required IDs**, exactly D01 through D32, with no extra card IDs. All have nonempty sections for the problem, recipe plateau/risk, deterministic grader, hidden-score design, strongest attack and ESTIMATED reward, saturation against the user-specified 10T/12h target, cheapest decisive check with ESTIMATED GPU-h, both-round GDM/accepted-shape comparison, distinctness and verdict. Generator, stage × artifact and modality metadata are present throughout.

The common format was derived from creative cards C001, C031, C085 and C127 and the creative PROMPT.md. Audit recovery is recorded as the generator; no nonexistent creative seed ancestry is claimed. Card prose was written individually in separate authored patches. The only scripts used here inspected existing files; no batch/template card-generation script was used.

Observed card length is **441–513 whitespace-delimited words**, totaling **14,880 words**, including headings, metadata and links. This is the intended one-page prose scale; no fixed-layout PDF pagination was tested.

Observed verdicts are **5 promising, 19 conditional, 8 cut**. The index contains **32 ranked entries with 32 unique IDs**, covering precisely the card inventory. Rankings and verdicts are explicitly provisional design judgments. D31 is a full card with an explicit asset-blocked cut, not an omitted sketch.

## Fields and scientific honesty

Each card defines the native outcome rather than rewarding a convenient training surrogate: actual student/agent learning, exact application state, valid evaluator outcomes or explicitly bounded selection utility. Cases with unresolved proxy validity are not treated as passed. For example D23 is cut, and D31's proposed grader is explicitly conditional on absent data.

Every attack section contains **ESTIMATED reward: F_D(U_attack)** and names the assumptions under which the recipe could approach reference/control utility. These are symbolic forecasts, not measured payouts. The acceptance bar's attack-table instructions specifically permit symbolic reward when physical anchors are unknown and forbid invented numeric payouts without assumptions. No b/c anchors exist for these cards, so no decimal attack rewards or fabricated results are supplied. The index defines the common mapping, calibration provenance and stronger attainable-control requirement. Each pilot GPU-h number is explicitly ESTIMATED; conceptual or asset screens estimate no GPU use while leaving CPU/preparation costs to be priced.

The saturation field in every card names a concrete stronger-researcher shortcut and a task-specific residual or reason to cut. The index supplies the binding absolute, best-of-4, pass@4, projected stronger-tier/compute and attainable-ceiling-relative gates from v2. No low score, secret seed, larger dataset, unavailable asset or theoretical perfect ceiling is presented as evidence of resistance. All retained candidates still require full recipe floors, native reserve, causal edge evidence, Exp-E6/B8, uncertainty resolution and the S studies.

The both-round sections cover task-specific lessons rather than asserting compliance: R1 trainer caps/noise/complete keys/real outcomes, and R2 artifact smuggling, portable ownership/lifecycle, protected dev gold, timing fidelity, independent positive controls and complete logs where relevant. The index carries the remaining release obligations, including independent design review and live attacks. This deliverable is a card set, not the full per-task certification audit required by E6.

## Parent mappings and distinctness

The validator extracted each D sketch's `WRONG into` parent from the independent audit and compared it with the corresponding card's wrong-parent clause. **All 32 mappings matched.** Every card also names a concrete other task from the permitted catalogs and explains the intervention/observation/artifact difference. D01's neighbor was corrected during review from its own source to Claude Suite 3.4. Nearest-neighbor choices are reasoned design judgments, not measured cross-solution equivalence.

## Sources, local links and URLs

The card link inventory contains **83 Markdown citations**, including **4 distinct external URLs**; all remaining card citation paths resolved locally after stripping line-number suffixes. The local primary suites support intervention contracts and recipe-risk hypotheses, not invented empirical plateau claims. External sources were checked with web search/open; their titles and primary-source URLs are cited directly in the relevant cards:

| Card | Checked primary source | Scope used |
|---|---|---|
| D03 | [Policy invariance under reward transformations: Theory and application to reward shaping](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa09/readings/NgHaradaRussell-shaping-ICML1999.pdf) | Potential-based shaping is an existing baseline; no new empirical plateau is attributed to it. |
| D09 | [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) | Soft-target transfer is a known recipe, without claiming safe-channel efficacy. |
| D22 | [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686) | Learning on policy-induced states motivates the DAgger control. |
| D26 | [Gradient Surgery for Multi-Task Learning](https://arxiv.org/abs/2001.06782) | Direct handling of conflicting gradients is an existing method, not the proposed future-acquisition novelty. |

All external destinations opened successfully. Checks establish source identity and the limited recipe claims used, not a comprehensive current-literature review. No external paper's quantitative efficacy or a source suite's unverified social-media result is imported as evidence. Other cards intentionally describe plateau mechanisms as unmeasured hypotheses or say no plateau is established; they do not invent citations to support them.

## Boilerplate check

Observed **zero duplicated prose paragraphs** across cards. A second diagnostic stripped Markdown destinations while preserving citation labels and IDs, excluded required headings/metadata, and compared contiguous body-word sequences. With an **ESTIMATED audit heuristic of 20-word windows**, it observed **zero shared spans** across different cards. Required field headings and comparable scientific concepts naturally recur. This check supports absence of shared paragraphs; it cannot prove originality or substantive distinctness by itself. Manual review checked each card's artifact boundary, exact outcome, complete baseline, decisive check and parent contrast.

The initial broader scan tokenized URL paths and removed numeric IDs, creating apparent matches from repeated catalog paths. Those were citation syntax, not shared prose; the corrected check above preserves IDs and removes destinations. A first field checker also required bold markup before the neighbor label; semantic-label checking confirmed that all labels were already present. Neither diagnostic artifact was treated as a content failure.

## Exclusion, scope and checkpointing

No card proposes souping, model merging, weight averaging or combining donor parameters. D08 transfers examples into clean recipients; D09/D22 use ordinary teacher/student learning, not parameter combination. A case-insensitive lexical scan for the excluded-method roots found only D14's ordinary deduplication phrase “future merge”; manual context review confirmed it refers to possible future task-family deduplication. No excluded method is an intervention, baseline or suggested next step.

Every successful card-creation patch also updated progress.json to include that card before the next card was authored. The final completed list matches D01–D32. Final status is complete after inventory, ranking and validation checks. Existing PROMPT.md and codex_run.log were left untouched by authored edits. All authored writes are confined to `/workspace/hidden_task_cards_v4/`; no shared documents were written and nothing was sent to GDM. GPU use was absent.

The final outcome is **complete as a design-writing task, uncertified as a task portfolio**. Cheap checks are proposals only; no funding, launch, deployment or outbound approval is implied.
