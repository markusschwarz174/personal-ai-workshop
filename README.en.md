# Personal AI Workshop

[Deutsch](README.md) · **English**

**One entry. Many packages. Experience that stays.**

[Open the interactive Agent Council](https://markusschwarz174.github.io/personal-ai-workshop/)

## “Why doesn’t GPT understand me?”

That is a question I often ask myself when I want to build something in a new chat. I have everything mapped out in my head and describe it in the prompt. Even so, I can never be certain how the session will develop. It feels as though GPT and I speak different languages.

When I think about this problem, I picture two gears that need to mesh: the synchronization of HUMAN and machine.

This idea leads to the `STARTER_AGENT`, briefly called `AUSRICHTER`. Before the actual work begins, it is meant to clarify a few things: What is the assignment? How will we recognize success? What is included—and what is not? Which sources apply? When do we stop? And when is the result good enough? The intended output is a master prompt that aligns HUMAN and machine.

I never pilot this design and eventually move it into the archive. But the work is not wasted. The idea that collaboration needs a WELCOMING and one clear point of contact remains. The gears turn into a hotel lobby, and several names eventually lead to the `ADVISOR`—my SINGLE POINT OF CONTACT.

Over time, this becomes my personal council of specialized agents. After my approval, the ADVISOR recommends the appropriate specialist, manages the handovers, and keeps the route to the goal in view. With GPT’s visualization capabilities, the council can now appear together and with individual faces.

[Read the full origin story in German](docs/ENTSTEHUNGSGESCHICHTE.md)

## Technical description by AI

> **Transparency notice:** The following technical description was created by AI after analyzing the historical MISSION CONTROL and the current agent system. The personal introduction and origin story were written by Markus Schwarz.

### What the Agent Council is

The Agent Council is a human-led interface for working with AI. It is designed to answer a simple question: **Who should help with a particular kind of task—and in which capacity?**

The entry point is the `ADVISOR`. It clarifies the request, keeps the goal and open state together, and recommends the smallest suitable engagement. A specialist agent then takes over for one clearly bounded work segment. The human confirms important transitions and retains decision authority.

The word *agent* is used here in a deliberately practical sense. It describes a recognizable counterpart with an assignment, an attitude, and boundaries. The council does not claim that seven autonomous programs are working simultaneously, nor does the visualization present a persistent system state.

### From a project-specific control room to a general Agent Council

The documented predecessor was MISSION CONTROL. It emerged inside a single workspace as an imaginary table: the human describes the intention, an advisory entry point clarifies the assignment and scope, suitable roles are recommended, and results return for human decision. Synchronization, routing, handovers, separated work and review steps, and learning from real routing cases were already explored there.

The current Agent Council does not simply retain every former role. It separates reusable functions from their original project context and reorganizes them. Numerous project-specific agents, helpers, and passes were consolidated into seven counterparts that are easier to understand across projects. Specialization is represented mainly through **modes** and **competences**, so a new character is not required for every activity.

### The seven agents

| Agent | Modes | Task in plain language |
|---|---|---|
| `ADVISOR` | `SYNCHRONIZER`, `ROUTER` | Clarifies the request, maintains orientation, and recommends the appropriate engagement. |
| `ASSISTANT` | `RESPONDER`, `EXECUTOR` | Answers simple questions or completes clearly bounded tasks directly. |
| `TUTOR` | `LERNARCHITEKT`, `LERNBEGLEITER`, `WEB_RESEARCHER` | Plans and supports learning and obtains traceable information for it. |
| `SPARRING` | `CHALLENGER`, `SOCRATIC` | Tests assumptions, develops counterpositions, and sharpens thinking through questions. |
| `ARCHITECT` | `EXPLORER`, `PROPOSER`, `PLANNER`, `IMPLEMENTOR`, `DEVELOPER`, `AI_ENGINEER`, `DEBUGGER` | Investigates, designs, plans, builds, improves, and repairs technical systems and AI solutions. |
| `GUARDIAN` | `OBSERVER`, `REVIEWER`, `VALIDATOR`, `AUDITOR` | Observes, reviews, validates, and audits work against named criteria and evidence. `TEAM_RED` is **Planned · not active**. |
| `TEXT_EDITOR` | `WRITER`, `READER`, `TRANSLATOR`, `VISUALIZER` | Creates, reviews, translates, and designs texts and smaller websites. |

Exactly **one mode** is active per work segment. A mode change is made visible. This keeps it clear whether an agent is exploring, planning, implementing, reviewing, or merely advising.

### Typical workflow

```text
the human’s idea or problem
            ↓
ADVISOR clarifies goal, context, and boundaries
            ↓
recommendation of agent and mode
            ↓
human confirmation
            ↓
clearly bounded assignment
            ↓
specialist work by the responsible agent
            ↓
separate review by GUARDIAN when needed
            ↓
result returns to ADVISOR and the human
```

Before material work begins, the engagement is recorded in a shared assignment frame. It covers, in particular, the task, expected result, scope, inputs, permitted actions, success criteria, delivery, and completion and abort conditions. Not every small question requires the full workflow: a simple answer should remain simple.

### Technical structure

The Agent Council is documentation-based and designed to be provider-neutral in principle. Its technical structure consists of several separated layers:

- **Presentation:** An interactive council makes agents and modes visible. It supports orientation and is not a live monitor of autonomous processes.
- **Identities:** Seven stable agents form the human-readable counterparts.
- **Modes:** Modes describe the function an agent is currently performing.
- **Competences:** Capabilities can be used across agents while retaining clearly assigned professional ownership.
- **Assignment frame:** A shared contract pattern binds the goal, scope, permitted work, success, and handover.
- **Routing:** A matrix describes permitted mappings and transitions between agents, modes, and reviews.
- **Validation:** Work and review functions remain separate. Validation against criteria is different from a general review or an observation.
- **Governance:** A private rule and protection layer exists. This repository acknowledges it as a foundation but does not publish it.

The underlying working system uses Markdown for readable agent profiles, YAML for the library and mappings, JSON Schema for structural checks, and HTML for the interactive presentation. The public documentation describes the concept; full agent contracts, system prompts, internal authority rules, and private governance remain outside this repository.

### Distinctive design choices

None of the following ideas is presented as a worldwide invention. What is distinctive is their concrete combination in a personal work system developed over an extended period.

1. **One human entry point without hidden takeover.** The ADVISOR remains approachable but hands specialist work over visibly. It is neither an all-knowing master agent nor an autonomous management layer.
2. **Few identities with several clearly bounded modes.** The council does not add another character for every new activity. Specialization first takes place inside a stable identity.
3. **Synchronization as an ongoing task.** The goal, decisions, open state, and next step are kept aligned throughout the collaboration, not only at the beginning.
4. **Protection against topic drift.** A new request is compared with the current assignment frame. A separate new topic is not silently absorbed into the existing task.
5. **Building and reviewing remain distinguishable.** A producer does not automatically describe its own checks as independent validation. Different review methods and references form a network; it is not a majority vote among agents.
6. **Visualization without autonomy theatre.** Faces and a shared table make responsibilities easier to remember. At the same time, the technical description makes clear that the interface is a selection surface, not evidence of parallel activity.
7. **Protection of the human voice.** The TEXT_EDITOR explicitly preserves strong passages and the author’s voice during condensation, revision, and design.
8. **Visible incompleteness.** Planned capabilities are not presented as active. `TEAM_RED` therefore remains explicitly marked **Planned · not active**.

### Relationship to Version 1

The first version of this repository focuses mainly on reusable **work packages**. A package brings together a complete working path with roles, steps, decisions, results, handovers, and validation.

The Version 2 Agent Council does not necessarily replace this model. It begins earlier: the human starts with the ADVISOR, selects a suitable agent, and can continue either with a simple direct task or with a larger work package. Agents mainly answer **“Who supports or handles this segment?”** Packages mainly answer **“How does this larger piece of work run from beginning to end?”**

The current public repository still contains the package-based prototype of the first version. The Agent Council is being added as a second, parallel stage of development. Historical and private working materials are not being published in full.

### Limitations

- The Agent Council does not guarantee correct results.
- A clear assignment does not replace professional capability or external sources.
- An agent name alone does not create technical independence.
- The visualization does not store a persistent working state.
- The human remains responsible for goals, approvals, and material decisions.

### Existing package prototype

1. Read [WORKSHOP.md](WORKSHOP.md).
2. Use [adviser/ADVISER.md](adviser/ADVISER.md) as the entry point for the first version.
3. Browse [package-core/PACKAGE_TEMPLATE](package-core/PACKAGE_TEMPLATE).
4. Try one of the packages in [examples](examples).
5. Validate the repository with `python scripts/validate_workshop.py`.

### License

Documentation, methods, prompts, examples, and visual materials are licensed under [CC BY 4.0](LICENSE-CONTENT). Executable code and tests are licensed under the [MIT License](LICENSE-CODE). See [LICENSING.md](LICENSING.md).
