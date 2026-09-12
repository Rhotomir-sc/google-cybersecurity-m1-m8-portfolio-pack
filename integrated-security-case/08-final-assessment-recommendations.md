# 08 - Final Assessment & Recommendations

## Executive Summary

This integrated security case combined risk assessment, control mapping, authentication analysis, Linux log analysis, SQL investigation, incident response, and Python automation.

The investigation identified three main areas of concern:

1. suspicious cloud authentication activity
2. web enumeration against sensitive paths
3. repeated web login attempts followed by an HTTP 200 response

The cloud authentication activity received the highest priority because repeated failed sign-ins were followed by successful access to multiple cloud applications from the same source.

The available evidence supports escalation for possible account compromise, but it does not prove that all suspicious activity belongs to the same attacker or that every event resulted in successful compromise.

---

# Final Findings

## Finding 1 - Possible Cloud Account Compromise

User:

```text
emma.lee@northstar.example
```

Source:

```text
198.51.100.23
```

Observed sequence:

```text
6 failed sign-ins
        ↓
Successful OfficeHome sign-in
        ↓
Outlook Web access
        ↓
My Profile access
```

### Final Assessment

```text
Priority: Critical
Classification: Suspicious authentication activity
Status: Possible account compromise
```

The activity should be investigated immediately.

---

## Finding 2 - Web Enumeration

Source:

```text
203.0.113.50
```

Observed requests included:

```text
/admin.php
/admin/login
/wp-admin
/phpmyadmin
/.env
/backup.zip
```

### Final Assessment

```text
Priority: High
Classification: Likely web enumeration / scanning
```

The access log does not show successful exploitation of these resources.

---

## Finding 3 - Suspicious Web Login Activity

Source:

```text
198.51.100.44
```

Observed sequence:

```text
POST /login → 401
POST /login → 401
POST /login → 200
```

### Final Assessment

```text
Priority: High
Classification: Suspicious authentication sequence
```

The HTTP `200` response alone does not confirm successful authentication.

Application authentication logs are required for validation.

---

# Risk Summary

| Area | Risk | Priority |
|---|---|---|
| Cloud Identity | Possible account compromise | Critical |
| Corporate Email | Unauthorised mailbox access | Critical |
| Web Server | Sensitive endpoint enumeration | High |
| Web Authentication | Possible credential guessing | High |
| Remote Administration | Excessive exposure | High |
| Customer Data | Exposure after account/system compromise | Critical |

---

# Immediate Response Priorities

## 1. Protect the Cloud Identity

For the affected user:

```text
emma.lee@northstar.example
```

recommended actions include:

- verify activity with the user
- revoke suspicious sessions if unauthorised activity is confirmed
- reset credentials where necessary
- review MFA registrations
- review Conditional Access results
- inspect mailbox rules
- inspect account and permission changes
- monitor subsequent sign-ins

---

## 2. Investigate Web Activity

For the suspicious web sources:

```text
203.0.113.50
198.51.100.44
```

recommended actions include:

- review application authentication logs
- review user-agent information
- correlate timestamps with other telemetry
- inspect WAF or reverse-proxy logs if available
- verify whether sensitive resources are exposed
- apply rate limiting where appropriate
- block clearly abusive sources if justified

---

## 3. Reduce Attack Surface

Recommended hardening actions include:

- remove unused services
- restrict administrative interfaces
- limit remote-management source addresses
- apply least privilege
- patch internet-facing services
- protect sensitive files and directories
- review firewall rules regularly

---

# Long-Term Security Recommendations

## Identity Security

```text
MFA
+
Conditional Access
+
Strong authentication policy
+
Sign-in monitoring
+
Session controls
```

Identity should receive high priority because cloud accounts can provide access to multiple business services.

---

## Network and Web Security

Recommended controls:

- firewall restrictions
- network segmentation
- secure administrative access
- web application monitoring
- rate limiting
- WAF controls where appropriate
- regular vulnerability management

---

## Endpoint Security

Recommended controls:

- endpoint monitoring
- malware protection
- patch management
- least privilege
- logging
- persistence monitoring

---

## Logging and Detection

Security-relevant logs should be centralised where possible.

Important sources include:

```text
Authentication logs
Web access logs
Endpoint logs
Firewall logs
Cloud activity logs
Administrative activity
```

Detection should focus on correlated behaviour rather than isolated events.

---

# Detection Improvements

## Cloud Authentication

Create detections for:

```text
Repeated failed authentication
        ↓
Same user + same source
        ↓
Successful authentication shortly afterward
```

---

## Web Enumeration

Create detections for:

```text
Single source
        ↓
Multiple sensitive endpoints
        ↓
Short time window
        ↓
Repeated 401 / 404 responses
```

---

## Remote Administration

Alert on:

- new remote-management rules
- overly broad source ranges
- unusual administrative logins
- unexpected management-service exposure

---

# Automation Opportunities

The Python authentication analyzer demonstrated how repetitive investigation tasks can be reduced.

Future automation could include:

- failed-login aggregation
- IOC extraction
- source-IP frequency analysis
- suspicious URL extraction
- authentication timeline creation
- simple alert prioritisation

Automation should support analyst investigation rather than replace analyst judgement.

---

# Evidence vs Conclusions

## Directly Supported by the Case Data

```text
Six failed cloud sign-ins occurred.

The same source later produced successful cloud authentication.

The same source accessed OfficeHome, Outlook Web, and My Profile.

Multiple sensitive web paths were requested from one source.

Two web login attempts returned 401.

A later web login request returned 200.
```

## Not Proven by the Current Evidence

```text
The cloud account was definitely compromised.

The web application login definitely succeeded.

The web server was exploited.

The customer database was accessed.

All suspicious activity came from the same attacker.
```

This distinction prevents overclaiming and keeps the investigation evidence-based.

---

# Integrated Investigation Workflow

The complete case followed this process:

```text
Asset Identification
        ↓
Risk Assessment
        ↓
Security Controls
        ↓
Authentication Analysis
        ↓
Linux Web Log Analysis
        ↓
SQL Investigation
        ↓
Detection & Incident Response
        ↓
Python Automation
        ↓
Final Assessment
```

---

# Skills Demonstrated

This case demonstrates practical application of:

```text
Risk assessment
Security controls
Identity security
Linux
Log analysis
SQL
Network / web security
Detection engineering concepts
Incident response
Python automation
Technical documentation
Evidence-based analysis
```

---

# Final Result

The most important finding in the case is the possible cloud identity compromise.

The investigation shows how several security disciplines can work together:

```text
Risk
+
Technical Evidence
+
Detection
+
Response
+
Automation
```

The case also demonstrates an important security principle:

> A suspicious event should be escalated based on evidence and correlation, without claiming more than the available data supports.

---

## Portfolio Note

This is a fictional security scenario created to integrate skills developed across the Google Cybersecurity Certificate portfolio.

It does not represent a real organisation or real production incident.
