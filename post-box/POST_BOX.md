# Post-box

A post-box is an explicit, addressed handover between roles. It prevents a result from existing only in chat memory.

## Message lifecycle

```text
PENDING → ACKNOWLEDGED → COMPLETED
```

- `PENDING`: the recipient has not yet accepted the handover;
- `ACKNOWLEDGED`: the recipient checked the required inputs;
- `COMPLETED`: the requested action finished with evidence.

A failed input check leaves the message pending and records the concrete blocker.

## Boundaries

- A post-box does not decide whether work is good.
- A handover does not authorize unrelated work.
- A post-box is short-lived operational communication, not long-term memory.
- The ADVISER may report pending messages at session entry.

