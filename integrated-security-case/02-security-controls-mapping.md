# 02 - Security Controls Mapping

## Objective

The goal of this stage is to map the main risks from the Northstar Solutions scenario to practical security controls.

The controls are grouped as:

```text
Preventive
Detective
Corrective
```

This helps show how different controls work together instead of relying on a single defensive measure.

---

# Control Mapping

| Risk | Preventive Controls | Detective Controls | Corrective Controls |
|---|---|---|---|
| Cloud account compromise | MFA, strong password policy, Conditional Access | Sign-in monitoring, failed-login alerts | Password reset, session revocation, account remediation |
| Customer database exposure | Least privilege, network restrictions, strong admin authentication | Database logging, access monitoring | Permission correction, credential reset, incident response |
| Phishing | Email filtering, awareness training, MFA | Email monitoring, suspicious sign-in alerts | Account recovery, malicious email removal, password reset |
| Web server compromise | Patching, hardening, firewall restrictions | Web logs, IDS/SIEM monitoring | Patch deployment, malware removal, restore from clean state |
| Remote administration exposure | Source-IP restrictions, least-privilege firewall rules | Remote-access logging, authentication alerts | Disable exposed service, remove unsafe rule, rotate credentials |

---

# Risk 1 - Cloud Account Compromise

## Preventive

```text
MFA
Strong password policy
Conditional Access
Least privilege
```

These controls reduce the likelihood of successful account takeover.

## Detective

```text
Failed sign-in monitoring
Unusual IP detection
Impossible-travel / location review
Interactive sign-in review
```

These controls help identify suspicious authentication activity.

## Corrective

```text
Reset credentials
Revoke active sessions
Disable compromised account
Review account permissions
```

These actions reduce impact after compromise is confirmed.

---

# Risk 2 - Customer Database Exposure

## Preventive

```text
Least-privilege database permissions
Network segmentation
Restricted administrative access
Strong authentication
```

## Detective

```text
Database audit logs
Access monitoring
Unusual query detection
Administrative activity review
```

## Corrective

```text
Remove excessive permissions
Reset affected credentials
Contain exposed systems
Review affected records
```

---

# Risk 3 - Phishing

## Preventive

```text
Email filtering
SPF / DKIM / DMARC
Security awareness
MFA
```

## Detective

```text
Suspicious sender review
URL analysis
Sign-in monitoring
Mailbox investigation
```

## Corrective

```text
Remove malicious email
Reset compromised credentials
Revoke sessions
Block malicious infrastructure
```

---

# Risk 4 - Web Server Compromise

## Preventive

```text
Patch management
Service hardening
Firewall restrictions
Least privilege
```

## Detective

```text
Web access logs
Error monitoring
IDS / SIEM alerts
Unexpected process review
```

## Corrective

```text
Remove malicious files
Patch exploited weakness
Restore trusted configuration
Validate system integrity
```

---

# Risk 5 - Remote Administration Exposure

## Preventive

```text
Restrict source addresses
Limit management ports
Require strong authentication
Disable unused services
```

## Detective

```text
Remote login monitoring
Firewall log review
Authentication alerts
Administrative session review
```

## Corrective

```text
Remove overly broad firewall rules
Disable unnecessary remote services
Rotate credentials
Review active sessions
```

---

# Defense-in-Depth Example

For cloud identity, one control is not enough.

```text
MFA
   +
Conditional Access
   +
Sign-in Monitoring
   +
Session Revocation
   +
Incident Response
```

This provides protection before, during, and after suspicious activity.

---

# Control Priority

The highest-priority controls for this environment are:

1. MFA and Conditional Access
2. Least-privilege access
3. Sign-in and log monitoring
4. Firewall source restrictions
5. Patch management
6. Incident-response procedures

These controls directly address the highest-risk areas identified in the previous assessment.

---

# Key Takeaway

Security controls are strongest when they work together.

A practical defensive model is:

```text
Prevent
   ↓
Detect
   ↓
Respond
   ↓
Recover
```

The next stage of the case will analyse technical evidence from authentication and web activity.
