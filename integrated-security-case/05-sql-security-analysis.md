# 05 - SQL Security Analysis

## Objective

The goal of this stage is to use SQL to investigate authentication activity and add asset context to the Northstar Solutions case.

The dataset is stored in:

```text
sample-data/security-case.sql
```

The analysis focuses on:

- failed authentication attempts
- source-IP concentration
- successful sign-ins after failures
- application access
- high-value assets

---

# Query 1 - Failed Sign-ins

```sql
SELECT username,
       source_ip,
       COUNT(*) AS failed_attempts
FROM signin_events
WHERE status = 'failed'
GROUP BY username, source_ip
ORDER BY failed_attempts DESC;
```

Expected result:

```text
emma.lee@northstar.example
198.51.100.23
6 failed attempts
```

This query reduces the authentication dataset to repeated failures grouped by user and source IP.

---

# Query 2 - Successful Activity From the Same Source

After identifying the suspicious source IP, I searched for successful sign-ins from the same address.

```sql
SELECT timestamp,
       username,
       source_ip,
       application,
       status
FROM signin_events
WHERE source_ip = '198.51.100.23'
AND status = 'success'
ORDER BY timestamp;
```

The results show successful access to:

```text
OfficeHome
Outlook Web
My Profile
```

for:

```text
emma.lee@northstar.example
```

---

# Query 3 - Complete Activity Timeline

```sql
SELECT timestamp,
       application,
       status,
       error_code
FROM signin_events
WHERE username = 'emma.lee@northstar.example'
AND source_ip = '198.51.100.23'
ORDER BY timestamp;
```

This reconstructs the suspicious sequence:

```text
6 failed sign-ins
        ↓
Successful OfficeHome sign-in
        ↓
Outlook Web access
        ↓
My Profile access
```

The value of this query is correlation rather than any single event.

---

# Query 4 - Authentication Error Review

```sql
SELECT error_code,
       COUNT(*) AS event_count
FROM signin_events
WHERE status = 'failed'
GROUP BY error_code;
```

The failed events use:

```text
50126
```

In this fictional dataset, this value represents invalid authentication attempts.

The error code provides additional context for the failure pattern.

---

# Query 5 - Compare External and Internal Activity

```sql
SELECT timestamp,
       username,
       source_ip,
       application,
       status
FROM signin_events
WHERE username = 'emma.lee@northstar.example'
ORDER BY timestamp;
```

This shows both:

```text
198.51.100.23
```

and:

```text
10.10.20.33
```

associated with the same user.

The different source addresses are useful context, but IP difference alone does not prove malicious activity.

---

# Query 6 - Review Critical Assets

```sql
SELECT asset_name,
       asset_type,
       owner,
       criticality
FROM assets
WHERE criticality IN ('Critical', 'High')
ORDER BY criticality;
```

This returns assets such as:

```text
Customer Database
Microsoft 365 Tenant
Linux Web Server
Corporate Email
Remote Administration
```

This helps connect technical alerts with business-relevant systems.

---

# Query 7 - Focus on Identity-Related Assets

```sql
SELECT asset_name,
       asset_type,
       owner,
       criticality
FROM assets
WHERE asset_type = 'Cloud Identity'
OR asset_type = 'Cloud Service';
```

The results include:

```text
Microsoft 365 Tenant
Corporate Email
```

These assets are directly relevant to the suspicious authentication activity.

---

# Investigation Correlation

The SQL analysis connects:

```text
Authentication failures
        +
Source IP
        +
Successful authentication
        +
Application access
        +
Asset criticality
```

This produces a stronger investigation picture than reviewing one table row at a time.

---

# Findings

## Finding 1

`emma.lee@northstar.example` received:

```text
6 failed authentication attempts
```

from:

```text
198.51.100.23
```

---

## Finding 2

The same source later generated successful access to:

```text
OfficeHome
Outlook Web
My Profile
```

---

## Finding 3

The affected cloud environment includes high-value assets such as:

```text
Microsoft 365 Tenant
Corporate Email
```

This increases the security relevance of the authentication activity.

---

# Assessment

The SQL results support escalation of the authentication sequence for further investigation.

The strongest evidence is:

```text
Repeated failed authentication
        ↓
Same identity
        ↓
Same source IP
        ↓
Successful authentication
        ↓
Additional cloud application access
```

The dataset supports a finding of:

```text
Suspicious authentication activity
with possible account compromise
```

Additional user verification, MFA information, session telemetry, and endpoint evidence would be required for a confirmed compromise verdict.

---

# Recommended Response

Recommended next steps include:

- verify activity with the account owner
- review MFA and Conditional Access evidence
- investigate sessions from `198.51.100.23`
- review mailbox activity
- check for account or permission changes
- revoke suspicious sessions if required
- reset credentials if compromise is confirmed
- preserve authentication evidence

---

# SQL Concepts Applied

This case used:

```text
SELECT
WHERE
AND
GROUP BY
COUNT
ORDER BY
IN
OR
```

These operations helped transform a small security dataset into investigation-focused results.

---

# Key Takeaway

SQL is useful because it allows an analyst to move from:

```text
Raw structured data
```

to:

```text
Correlated security findings
```

The query itself does not make the final security decision.

It provides evidence that supports analyst judgement.

---

## Next Step

The next stage will combine the authentication and web findings into a detection and incident-response assessment.
