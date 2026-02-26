# Windows Event Log Map (Module 3)

## Use-cases and evidence sources
1) Failed logons (brute force indicator)
- Source: Security logs
- Evidence: repeated failed attempts + account name + timestamp pattern

2) PowerShell execution (potential abuse signal)
- Source: Windows logs / process evidence (depending on config)
- Evidence: PowerShell activity + command context (benign simulation)

3) New local admin user (privilege change)
- Source: account/group management evidence + related logs
- Evidence: user created / added to admin group / later removed
