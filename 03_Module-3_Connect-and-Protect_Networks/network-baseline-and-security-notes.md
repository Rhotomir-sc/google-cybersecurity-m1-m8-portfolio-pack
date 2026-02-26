# Network Baseline & Security Notes (Module 3)

## Purpose
Create a simple network baseline and document common network security indicators for investigations.

## Baseline (my environment)
- Host: Windows (local machine)
- What I captured:
  - IP configuration (IP/DNS/Gateway)
  - Active connections snapshot
  - Open/listening ports snapshot

## Key concepts (quick notes)
- **DNS:** unexpected domains, suspicious lookups
- **HTTP/HTTPS:** unusual user-agents, repeated requests, strange destinations
- **RDP/SMB:** exposed services or unusual access attempts
- **Ports:** “expected vs unexpected” ports for the environment

## Investigation mindset (SOC-style)
- Start with a baseline (what is normal)
- Compare anomalies (new connections/ports)
- Correlate with endpoint evidence (if needed)

## Evidence (folder)
- See: `./evidence/`
