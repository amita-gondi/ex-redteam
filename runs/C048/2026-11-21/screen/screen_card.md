# C048 — Pretrain under a changing lossless data codec — saturation screen
## 1. What the grader actually rewards
The outcome is complete time-to-loss-target, or private terminal loss at timeout, while source receipts verify that decompression did not silently alter intended exposure. A codec speedup matters only through the actual training pipeline and permitted distribution. ESTIMATED R≈0 is the frozen competent loader floor and ESTIMATED R≈1 a stronger attainable training pipeline; the censored stock loader is provisionally ESTIMATED R=0.00, reference ESTIMATED R=0.60. The attack forecast describes a better-tuned replacement exceeding fixed calibration on new codec mixtures; if full asynchronous fair delivery already consumes the attainable gap, re-normalizing cannot turn that absence of reserve into hardness.
## 2. Strongest lawful combined attack
Replace completion-order sampling with a precommitted sample sequence, asynchronous shard workers and bounded reorder/prefetch queues. [PyTorch's loader documentation](https://docs.pytorch.org/docs/stable/data.html) explicitly warns that out-of-order delivery can skew imbalanced data. [NVIDIA DALI](https://docs.nvidia.com/deeplearning/dali/user-guide/docs/pipeline.html) documents asynchronous CPU/GPU overlap and queue-depth controls. These are established solutions to the two mechanisms named by the card, although its specific text codec still needs an integration layer.

Add per-source sampling debt, entropy-aware decompression scheduling and cache admission under actual RAM/storage limits. [MosaicML Streaming](https://docs.mosaicml.com/projects/streaming/en/stable/api_reference/generated/streaming.StreamingDataset.html) provides concrete predownload, cache-limit and balanced-stream controls. Tune worker counts, queue depth, codec block size and storage layout jointly. If source order is fixed, prioritize imminent expensive blocks; if only mixture proportions are fixed, use debt-corrected fair scheduling without silently dropping slow examples. Both interpretations admit a competent whole-loader replacement.

ESTIMATED single-run R=0.88, range ESTIMATED 0.66–0.97; ESTIMATED best-of-4=0.93; ESTIMATED pass@4 at R≥0.60=0.99; ESTIMATED projected upper-95% bound=0.99. Most provisional reward comes from eliminating avoidable GPU starvation and restoring intended source exposure; ordinary tuning captures much of the remaining overlap opportunity. Residual loss is irreducible decompression work, limited buffering and long-tail dependencies between codec blocks. Those constrain all pipelines and cannot establish a distant scientific ceiling without a demonstrated better same-resource control.
## 3. Other routes
An ordered multiprocess loader with enough lookahead reaches ESTIMATED R=0.76, range ESTIMATED 0.50–0.92. It can repair bias and hide substantial latency even without a sophisticated learned scheduler.

Autotuning worker affinity, compressed block size, prefetch depth and queue memory yields ESTIMATED R=0.82, range ESTIMATED 0.57–0.95. A cheap throughput screen can prune poor configurations before a small set receives full loss-target runs. Predecompressing a bounded hot working set is a lawful shortcut when preparation time and disk bytes are charged, ESTIMATED R=0.62, range ESTIMATED 0.35–0.86. It cannot be excluded just because it avoids online codec complexity.
## 4. What would lower lawful saturation
Begin with a complete asynchronous fair loader, then show a learning-stage-dependent sampling/decompression interaction that changes the best buffer investment after codec transitions. Keep source semantics fixed where required and demonstrate that a legal adaptive policy beats ordered lookahead plus debt correction in native training utility. ESTIMATED composite R might fall to 0.54–0.67. ESTIMATED cost is three systems-research weeks and ESTIMATED 128 H100 GPU-h of end-to-end calibration. A new codec name or a larger queueing tail alone leaves the standard overlap recipe intact.
## 5. Decisive-check GPU-h re-estimate
Old figure: ESTIMATED 8 GPU-h. New ESTIMATED 96 H100 GPU-h assumes an ESTIMATED 0.3B learner so CPU/storage bottlenecks remain visible, ESTIMATED four loader arms, ESTIMATED three source/codec seeds and ESTIMATED six H100-hours per full target-loss attempt: ESTIMATED 4×3×6=72. Warm/cold-cache replication costs ESTIMATED 16 GPU-h and independent final-loss checking ESTIMATED 8 GPU-h. Storage and CPU topology must match development. The old value covers a throughput demonstration, not whether restored exposure and faster delivery jointly improve the learned endpoint.
## 6. Duplicate check
05B: MODERATE, after reading its fixed-update-graph and durable-state contract; this card changes the upstream delivered training stream and time-to-quality. 01A: WEAK, from its read corpus-exposure contract, because here exposure variation is an unwanted loader effect rather than the principal learned data-policy intervention. No STRONG match is established, despite substantial systems overlap.
## 7. Verdict
CUT. ESTIMATED best-of-four exceeds its line by 0.33 and single-run by 0.18. Mature overlap, ordering and fair-delivery methods closely cover the stated failure and are cheaply searchable.
## 8. Measurement status
Rollouts UNMEASURED (planned: complete compressed-data training with source receipts). Grader noise UNMEASURED (planned: repeated cold-cache and learner runs). Score ladder UNMEASURED (planned: stock loader, ordered overlap, tuned fair pipeline and attainable adaptive control).
## Screen record
id: C048
verdict: CUT
binding_line: bo4>0.60
attack_single_est: 0.88
attack_single_range: 0.66-0.97
bo4_est: 0.93
pass4_est: 0.99
ub95_est: 0.99
gpuh_old: 8
gpuh_new_est: 96
duplicate_of: 05B MODERATE; 01A WEAK
kill_reason: asynchronous ordered loading and fair exposure repair main failure
souping_flag: no
