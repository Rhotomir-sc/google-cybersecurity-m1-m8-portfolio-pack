# Detections (Module 4)

## Detection 1 — Multiple failed logons
- Signal: repeated failed authentication attempts
- Why it matters: brute force attempts often start like this
- Evidence: filtered Security logs screenshot

## Detection 2 — Suspicious PowerShell execution
- Signal: PowerShell execution recorded (controlled simulation)
- Why it matters: PowerShell is frequently used for living-off-the-land techniques
- Evidence: process/log screenshot

## Detection 3 — New local admin user
- Signal: new user added to local administrators group
- Why it matters: privilege escalation / persistence indicator
- Evidence: user/group change screenshot + timeline note
