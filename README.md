# Personal AI Workshop

**One entry. Many packages. Experience that stays.**

Personal AI Workshop is a small, human-led method for building reusable AI work packages for everyday work. You do not need to know which agent, prompt, model, or tool to choose before you begin. You enter through one conversational intake, clarify the task, and choose a fitting package together.

This repository is written for curious non-programmers as well as technical users. It is not an enterprise orchestration framework and it does not require an agent platform.

## The idea in one minute

```text
your problem
    ↓
single entry: clarify intent and missing information
    ↓
recommend a package and its entry role
    ↓
human approval
    ↓
package-specific work and validation
    ↓
return to the human
    ↓
keep only reusable experience
```

A package may be tiny or elaborate. It can contain Markdown instructions, roles, JSON contracts, scripts, templates, examples, and several kinds of validators. Packages share a minimal contract, not a mandatory internal shape.

## Start here

1. Read [WORKSHOP.md](WORKSHOP.md).
2. Use [adviser/ADVISER.md](adviser/ADVISER.md) as the single entry.
3. Browse [package-core/PACKAGE_TEMPLATE](package-core/PACKAGE_TEMPLATE).
4. Try one of the packages in [examples](examples).
5. Validate the repository with `python scripts/validate_workshop.py`.

## What makes a package different from a skill?

A skill teaches an agent a reusable capability. A package governs a complete piece of work: its entry, roles, passes, human decisions, outputs, handovers, and appropriate validation. A package may contain or invoke several skills.

## Repository map

```text
adviser/        single entry and routing
package-core/   minimal common package contract and templates
post-box/       explicit handovers between roles
experience/     reviewed lessons worth keeping
examples/       two deliberately different packages
docs/           validation model and visual scene briefs
scripts/        deterministic repository checks
tests/          tests for the validator
```

## Human authority

The ADVISER recommends. Packages work. Validators inspect. The human decides.

No package silently activates another package. Every package returns its result to the human-facing conversation.

## License

Documentation, methods, prompts, examples, and visual materials are licensed under [CC BY 4.0](LICENSE-CONTENT). Executable code and tests are licensed under the [MIT License](LICENSE-CODE). See [LICENSING.md](LICENSING.md).

