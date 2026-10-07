# Security

## Current controls

- no secrets are stored in source
- irreversible requests are denied by default
- tools are explicit callables rather than arbitrary code execution
- failures are contained at the orchestration boundary
- telemetry records execution outcomes

## Not yet implemented

This prototype does not provide production authentication, authorization infrastructure, sandboxing, network egress control, or persistent audit storage.

Those omissions are intentional and should not be interpreted as production guarantees.
