# D12 — Assign credit between a planner and its local executor

**Generator:** recovered hierarchical-learning intervention. **Stage × artifact:** objective × model weights. **Modality:** plans and tool trajectories.

## Problem

An inherited hierarchical agent selects reusable plans through a planner adapter and carries them out through a separate executor adapter with bounded local context. A failed episode may reflect a bad subgoal or a good subgoal executed badly. Submit role-specific learning and credit rules under fixed dispatch, following [Suite 7.12](/workspace/task_suites_claude.md:8800); flattening away the separate parameter interface would change the task.

## Why known recipes plateau

Planner imitation, executor behavioral cloning, generic hierarchical RL and prefix-based continuation credit are full baselines. Their proposed limitation is that improving either role changes the counterfactual competence against which the other should be judged. No experiment establishes that this coupling defeats a strong demonstration teacher or joint training.

## Deterministic grader

Trusted dispatch binds each decision and update to its role/version. Train both adapters with equal actual token and environment budgets, then execute the resulting hierarchy on exact terminal tasks. U macro-averages success across new subtask compositions and inherited skills. Plan plausibility, subgoal completion and rolewise loss are diagnostics; final outcomes determine F_D12.

## Hidden-score design

Privately authored workflows reuse local skills in different dependency orders. A declared composition shift needs protected dev compositions with matched horizon, role context and action semantics. Neither adapter may access hidden goal predicates, and executor memory cannot silently become a privileged global planner.

## Strongest attack + rough ESTIMATED reward

**ESTIMATED reward: F_D12(U_joint_imitation).** Assuming a legal planner can generate sufficiently varied demonstrations, joint planner/executor imitation plus ordinary hierarchical fine-tuning may recover reference behavior. Charge demonstration generation and continuation search; do not forbid them to preserve the preferred credit method.

## Saturation note vs 10T / 12h

The researcher can generate counterfactual role swaps and search plan libraries. Reserve must survive those controls through real moving-competence interactions, demonstrated by credit×role-learning ablations. All index hard gates apply; architecture separation alone is not saturation resistance.

## Cheapest decisive check

**ESTIMATED: 20 GPU-h** including planner/executor training and terminal tests. Cross fixed versus improving executor competence with ordinary versus counterfactual planner credit, alongside complete joint imitation. Kill if demonstrations or standard hierarchy erase the residual.

## GDM Round 2 compliance and shape

The learning loop resembles pretraining_latest, with agentic_search-style tool execution. R1 requires full-pipeline variance; R2 requires role/version receipts, per-seed timeouts and structural control of both adapter-training channels so a credit callback cannot inject arbitrary weights.

## DISTINCTNESS NOTE

**Wrong parent: v3 02B. Nearest other: [T04](/workspace/task_catalog_v3_full/packets/T04.md).** A single delayed-credit tool policy does not preserve separate roles. T04 studies protocol transfer, while D12 studies coupled responsibility and learning between parameter-separated planner/executor components.

## Verdict

**conditional** — A distinct architecture/credit experiment, pending proof that complete imitation and ordinary hierarchical RL leave native learning reserve.
