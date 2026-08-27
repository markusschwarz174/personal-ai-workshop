# Package Core

## Definition

A package is a governed bundle for one class of work. It may contain Markdown, JSON, scripts, templates, examples, and roles. Packages share a minimal contract, not a mandatory internal workflow.

## Required contract

Every package declares:

1. purpose and non-purpose;
2. routing conditions;
3. entry role and required inputs;
4. passes with entry, action, exit, and owner;
5. human decisions;
6. applicable validation;
7. return path;
8. storage and cleanup rules.

## Invariants

- The working role does not perform the final validation of its own material work.
- A package does not silently activate another package.
- A human approval authorizes only the decision that was actually presented.
- A plan is not completion; completion requires an observable output or finding.
- Evidence names the real tool, source, comparison, or test used.
- Simpler work may use fewer passes and validators.

## Validation families

| Validation | Question | Typical moment |
|---|---|---|
| EXPERT_REVIEW | Is the idea or diagnosis sound enough to continue? | Before commitment to a solution |
| SIMULATION_TEST | Would the plan work against the real inputs? | Before mutation |
| DIFF_CHECK | Does the result match exactly what was approved? | After mutation |
| FINAL_TEST | Does the real outcome achieve the original goal? | After mechanical correctness |

Not every package needs all four. The package states which error classes are real.

