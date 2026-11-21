# C076 — Adapter checkpoints whose reported training gains survive reload — saturation screen
## 1. What the grader actually rewards
Only task utility delivered by a cleanly reloaded trained adapter counts, with training, export, reload time and save-time memory all charged. Successful in-memory evaluation followed by an incomplete file is therefore a failed deliverable. R≈0 is the competent complete-export floor, including an unchanged working exporter, and R≈1 the attainable post-reload utility/time control; all score and compute forecasts below are ESTIMATED, and no source failure or training effect has been measured here.

An efficient faithful exporter has a nominal ESTIMATED R=0.60 reference placement, unsupported until the incident and an export-cost frontier are reproduced.

## 2. Strongest lawful combined attack
First treat the upstream incident as a documentary lead, not an established mechanism; its body and pinned-revision reproduction remain unverified in this desk review. Independently enumerate trainable adapter tensors, required non-adapter trainables, configuration, tokenizer/processor dependencies and immutable base identity. Serialize that declared state through a mature exporter with explicit name/shape validation, stage bounded tensor chunks on CPU, and publish a manifest only after complete durable writes.

[PEFT's checkpoint format](https://github.com/huggingface/peft/blob/main/docs/source/developer_guides/checkpoint.md) documents adapter weights and configuration, while its [troubleshooting guide](https://huggingface.co/docs/peft/developer_guides/troubleshooting) gives concrete reasons loaded behavior can differ, including missing running state and inactive adapters. Use those checks in a genuinely new process with the exact base and processor pins, comparing outputs and private task utility before and after reload. Compare adapter-enabled and disabled execution to ensure the trained artifact has a causal effect. No parameter-combination or consolidation route is part of this attack.

ESTIMATED single-run R=0.95, range 0.85–0.99; ESTIMATED best-of-4=0.98; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% score=1.00. These estimates are conditional on an actual export defect and a nontrivial trained adapter, not a claim that the incident was reproduced. The residual is architecture-specific state enumeration and peak memory while staging. Both are conventional serialization concerns. If independent export restores all learned behavior at negligible total cost, the task has essentially no research range after that complete method is placed in the floor.

## 3. Other routes
A standard complete adapter save/load path with pinned base configuration is the strongest single recipe: ESTIMATED R=0.90, range 0.74–0.98. It must include any legitimately trained non-adapter modules and processor state rather than assuming every useful change lives in low-rank tensors.

Autotune CPU staging chunk size, sharding, save concurrency and tensor layout under fresh-process parity checks. ESTIMATED R=0.93, range 0.81–0.99. This is a small systems search, not model research. Skipping saving, submitting untrained default weights or demonstrating only pre-export quality are not counted as lawful successes because the stated grader explicitly requires useful post-reload behavior.

## 4. What would lower lawful saturation
A possible replacement task would require an actual deployment frontier involving changing adapter architectures, constrained host/device memory and useful training time, with mature independent exporters already in the floor. Publish required state semantics and hold out structurally different export dependencies. ESTIMATED attack might remain 0.67–0.85 even then, so CUT is the prudent screen result. ESTIMATED authoring effort is 5–8 person-days and ESTIMATED 72 H100-h for a narrow train/export/reload pilot. An unreproducible issue should be rejected before training, rather than converted into invented experimental history.

## 5. Decisive-check GPU-h re-estimate
Old allowance: ESTIMATED 10 GPU-h. New ESTIMATED 72 H100-GPU-h assumes an ESTIMATED 3B VLM with trainable adapters, ESTIMATED 3 export arms×3 seeds×6 device-hours for actual adapter training and export=54. Clean reload, private inference and save-memory profiling add ESTIMATED 18, giving ESTIMATED 72. The adapter parameter count is architecture-dependent and must be profiled rather than assumed to determine full VLM training cost. The old figure is plausible for one short cycle and could already falsify the lead; the revised amount buys repeated learned-behavior checks, not saturation certification.

## 6. Duplicate check
05B: MODERATE after reading its source; durable learned state, cold restore and complete execution cost overlap, but this artifact is adapter export into an independent VLM rather than exact distributed optimizer continuation. T21: WEAK from its compression packet because it delivers inference-capable learned state under memory limits, while adapter serialization changes neither weight representation quality nor capability-recovery training. No STRONG duplicate is needed to reject a near-constructive export repair.

## 7. Verdict
CUT. ESTIMATED single-run reward exceeds the binding threshold by 0.25 and ESTIMATED best-of-4 exceeds its threshold by 0.38. More fundamentally, the specific incident is not reproduced and ordinary independent serialization appears capable of delivering the complete intended outcome if it exists.

## 8. Measurement status
Rollouts UNMEASURED (planned: only after pinned incident verification, independent export-repair attempts); grader noise UNMEASURED (planned: repeated fixed-adapter clean reload and private inference); score ladder UNMEASURED (planned: incomplete-export negative, mature complete exporter, bounded staging, architecture-aware export and attainable delivery control).

## Screen record
id: C076
verdict: CUT
binding_line: single>0.70
attack_single_est: 0.95
attack_single_range: 0.85-0.99
bo4_est: 0.98
pass4_est: 0.99
ub95_est: 1.00
gpuh_old: 10
gpuh_new_est: 72
duplicate_of: 05B MODERATE; T21 WEAK
kill_reason: mature complete adapter export nearly constructs the intended solution
souping_flag: no
