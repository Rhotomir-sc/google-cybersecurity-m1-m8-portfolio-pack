# 06 - Detection & Incident Response

## Objective

The goal of this stage is to combine the authentication and web-server findings into a structured detection and incident-response assessment.

The two suspicious activity patterns are analysed separately because the available evidence does not prove that they were performed by the same actor.

---

# Detection Summary

The investigation produced three main security findings.

## Finding 1 - Suspicious Cloud Authentication

User:

```text
emma.lee@northstar.example
```

Source:

```text
198.51.100.23
```

Observed pattern:

```text
6 failed sign-ins
        ↓
Successful OfficeHome sign-in
        ↓
Outlook Web access
        ↓
My Profile access
```

Assessment:

```text
Possible account compromise
```

This activity should be escalated because repeated failures were followed by successful authentication from the same source.

---

## Finding 2 - Web Enumeration

Source:

```text
203.0.113.50
```

Requested resources included:

```text
/admin.php
/admin/login
/wp-admin
/phpmyadmin
/.env
/backup.zip
```

The requests occurred within a short time window.

Assessment:

```text
Likely automated web enumeration / scanning
```

The log does not show successful access to these sensitive resources.

---

## Finding 3 - Suspicious Login Pattern Against Web Application

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

Assessment:

```text
Suspicious authentication sequence
```

An HTTP `200` response does not independently confirm successful authentication, so application authentication logs would be required before classifying this as an account compromise.

---

# Evidence Correlation

The strongest cloud identity evidence is:

```text
Same user
+
Same source IP
+
Repeated failures
+
Successful authentication
+
Post-login application access
```

The strongest web enumeration evidence is:

```text
Same source IP
+
Multiple sensitive paths
+
Short time interval
+
Repeated 401 / 404 responses
```

These patterns provide enough evidence for investigation and defensive response.

However:

```text
198.51.100.23
203.0.113.50
198.51.100.44
```

are different source addresses.

I therefore do not claim that the cloud authentication activity and web activity belong to the same attacker.

---

# Severity Assessment

| Finding | Likelihood | Potential Impact | Priority |
|---|---|---|---|
| Possible cloud account compromise | High | High | Critical |
| Sensitive endpoint enumeration | High | Medium | High |
| Suspicious web login activity | Medium | High | High |

The cloud identity event receives the highest priority because successful access to business applications was observed after repeated authentication failures.

---

# Incident Response - Cloud Identity

## Detection

Suspicious authentication activity was identified for:

```text
emma.lee@northstar.example
```

from:

```text
198.51.100.23
```

---

## Analysis

Relevant evidence includes:

- six failed sign-ins
- one successful OfficeHome sign-in
- subsequent Outlook Web access
- subsequent My Profile access
- same user and same source IP
- interactive authentication activity

The available evidence supports escalation for possible account compromise.

---

## Containment

If the activity is confirmed as unauthorised, immediate containment should include:

```text
Revoke active sessions
Disable or restrict the account if required
Block or investigate the suspicious source
Prevent further unauthorised access
```

User verification should happen as quickly as possible.

---

## Eradication

Possible eradication actions include:

- reset the account password
- remove unauthorised authentication methods
- review MFA registrations
- remove suspicious mailbox rules
- remove unauthorised applications or sessions
- review account permission changes

---

## Recovery

Recovery should include:

- restore legitimate user access
- require secure authentication
- confirm MFA configuration
- review recent account activity
- monitor for repeated suspicious sign-ins
- verify that no unauthorised changes remain

---

# Incident Response - Web Activity

## Detection

Web access logs showed rapid requests to common administrative and sensitive resources.

Another source generated repeated login requests followed by an HTTP `200` response.

---

## Analysis

The web investigation should continue with:

- application authentication logs
- user-agent information
- web application logs
- WAF / reverse proxy logs if available
- endpoint telemetry
- server file-integrity information

The current access log alone does not show successful exploitation.

---

## Containment

Possible defensive actions include:

- rate-limit abusive requests
- temporarily block clearly abusive sources
- restrict administrative interfaces
- verify that sensitive resources are not publicly accessible

Blocking decisions should consider business context and false-positive risk.

---

## Eradication

If compromise is discovered:

- remove malicious files
- patch exploited vulnerabilities
- rotate affected credentials
- correct unsafe permissions
- remove unauthorised accounts or persistence
- restore trusted configuration

---

## Recovery

After remediation:

- verify web application functionality
- confirm sensitive paths are protected
- monitor for repeated scanning
- review authentication activity
- validate system integrity

---

# Detection Opportunities

## Authentication Detection

A useful detection rule could look for:

```text
Multiple failed sign-ins
        ↓
Same user + same source
        ↓
Successful authentication within a short period
```

This pattern may help identify password guessing followed by successful access.

---

## Web Enumeration Detection

A useful web detection could look for:

```text
Single source IP
        ↓
Multiple sensitive paths
        ↓
Short time window
        ↓
Repeated 401 / 404 responses
```

Example sensitive paths:

```text
/admin
/wp-admin
/phpmyadmin
/.env
/backup
```

---

# Incident Indicators

| Type | Indicator |
|---|---|
| User | `emma.lee@northstar.example` |
| Authentication Source | `198.51.100.23` |
| Web Enumeration Source | `203.0.113.50` |
| Web Login Source | `198.51.100.44` |
| Cloud Application | `OfficeHome` |
| Cloud Application | `Outlook Web` |
| Sensitive Path | `/.env` |
| Sensitive Path | `/phpmyadmin` |
| Sensitive Path | `/backup.zip` |

The IP addresses are documentation-only ranges used for this fictional scenario.

---

# Response Priority

My response order would be:

```text
1. Validate possible cloud account compromise
        ↓
2. Contain unauthorised cloud sessions if confirmed
        ↓
3. Review account and mailbox changes
        ↓
4. Investigate web enumeration
        ↓
5. Validate web authentication activity
        ↓
6. Harden exposed services
        ↓
7. Continue monitoring
```

---

# Evidence vs Assumptions

Throughout the case, I keep direct evidence separate from conclusions.

### Supported by evidence

```text
Six failed cloud sign-ins occurred.
The same source later authenticated successfully.
Outlook Web and My Profile were accessed.
Sensitive web paths were requested.
Two web login requests returned 401 and one returned 200.
```

### Not yet proven

```text
The cloud account was definitely compromised.
The HTTP 200 response proves a successful web login.
The web server was exploited.
All suspicious activity came from one attacker.
```

Additional evidence would be required for those conclusions.

---

# Key Takeaway

Detection becomes stronger when individual events are correlated, but correlation must remain evidence-based.

The correct workflow is:

```text
Detect
   ↓
Validate
   ↓
Correlate
   ↓
Assess severity
   ↓
Contain
   ↓
Eradicate
   ↓
Recover
   ↓
Monitor
```

---

## Next Step

The next stage will automate part of the investigation with Python by analysing the authentication dataset and identifying repeated failed sign-ins followed by successful access.
