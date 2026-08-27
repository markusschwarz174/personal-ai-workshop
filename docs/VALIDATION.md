# Validation That Matches the Question

Validation is not synonymous with testing code. A useful workshop asks what could be wrong at this moment.

## Four different questions

### 1. EXPERT_REVIEW — ideas and diagnoses

An independent reviewer examines the same problem without first adopting the original author's framing. Only after writing an independent view should both views be compared.

Use it when a plausible first idea could lead the human into unnecessary work.

### 2. SIMULATION_TEST — plans

Walk through the plan against the real inputs without changing them. Look for missing steps, false assumptions, unavailable tools, and downstream breakage.

### 3. DIFF_CHECK — implementation fidelity

Compare the approved change, the previous state, and the resulting state. Prefer deterministic tools over an LLM opinion.

### 4. FINAL_TEST — real-world effect

Run or inspect the changed system or artifact against the original goal. A correct diff can still produce the wrong outcome.

## Independence

Independence can be strengthened in three ways:

1. a fresh context with the same model;
2. a different model or reviewer;
3. a deterministic tool that does not rely on model judgment.

Packages should state which form they require rather than claiming all validation is equivalent.

