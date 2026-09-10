# 04 - Web & Linux Log Analysis

## Objective

The goal of this stage is to analyse the web server access log and identify unusual HTTP activity.

The dataset is stored in:

```text
sample-data/access.log
```

The main investigation questions are:

- Which source IPs generate unusual activity?
- Are sensitive or administrative paths being requested?
- Are there repeated authentication failures?
- Is there a successful request following those failures?
- Which events deserve escalation?

---

# Initial Log Review

I first reviewed the structure of the Apache-style access log.

A typical entry contains:

```text
Source IP
Timestamp
HTTP Method
Requested Resource
HTTP Status Code
Response Size
```

Example:

```text
203.0.113.50 - - [10/Sep/2026:09:10:02 +0000] "GET /admin.php HTTP/1.1" 404 312
```

---

# Finding 1 - Sensitive Endpoint Enumeration

I searched for requests to potentially sensitive paths.

Example Linux command:

```bash
grep -E "/admin|/wp-admin|/phpmyadmin|/\.env|/backup" sample-data/access.log
```

The source:

```text
203.0.113.50
```

requested several sensitive or administrative resources:

```text
/admin.php
/admin/login
/wp-admin
/phpmyadmin
/.env
/backup.zip
```

Most of these requests returned:

```text
404
```

while:

```text
/admin/login
```

returned:

```text
401
```

---

## Interpretation

The sequence is consistent with automated enumeration or scanning for common administrative and sensitive web resources.

The requests occurred within a short time window:

```text
09:10:02
→ 09:10:21
```

The activity should be investigated further, but the access log alone does not prove that the source successfully compromised the server.

---

# Finding 2 - Repeated Login Failures

I filtered requests to the login endpoint:

```bash
grep 'POST /login' sample-data/access.log
```

The source:

```text
198.51.100.44
```

generated:

```text
09:15:06 → POST /login → 401
09:15:12 → POST /login → 401
09:15:19 → POST /login → 200
```

This pattern shows two failed authentication-related requests followed by an HTTP `200` response.

---

## Interpretation

The sequence is suspicious because the same source produced:

```text
Repeated failed login attempts
        ↓
Same endpoint
        ↓
Same source IP
        ↓
HTTP 200 response
```

However, an HTTP `200` response alone does not automatically prove successful authentication.

The application response content or authentication logs would be required to confirm whether the login actually succeeded.

---

# Finding 3 - Source Activity Count

I counted how often each source IP appeared in the log:

```bash
cut -d ' ' -f 1 sample-data/access.log | sort | uniq -c | sort -nr
```

The result showed that:

```text
203.0.113.50
```

was one of the most active external sources.

Frequency alone is not malicious evidence, but when combined with the requested resources, the activity becomes more relevant.

---

# Finding 4 - HTTP Error Review

I reviewed HTTP responses with status codes of `400` or higher.

Example:

```bash
awk '$9 >= 400 {print $1, $4, $6, $7, $9}' sample-data/access.log
```

The output highlighted:

- repeated `404` requests to common sensitive paths
- `401` responses against login and administrative resources

This helped reduce the dataset to events that were more useful for investigation.

---

# Investigation Timeline

| Time | Source IP | Request | Status |
|---|---|---|---|
| 09:10:02 | `203.0.113.50` | `GET /admin.php` | 404 |
| 09:10:05 | `203.0.113.50` | `GET /admin/login` | 401 |
| 09:10:09 | `203.0.113.50` | `GET /wp-admin` | 404 |
| 09:10:13 | `203.0.113.50` | `GET /phpmyadmin` | 404 |
| 09:10:17 | `203.0.113.50` | `GET /.env` | 404 |
| 09:10:21 | `203.0.113.50` | `GET /backup.zip` | 404 |
| 09:15:06 | `198.51.100.44` | `POST /login` | 401 |
| 09:15:12 | `198.51.100.44` | `POST /login` | 401 |
| 09:15:19 | `198.51.100.44` | `POST /login` | 200 |

---

# Indicators

| Type | Value |
|---|---|
| Source IP | `203.0.113.50` |
| Source IP | `198.51.100.44` |
| Sensitive Path | `/admin.php` |
| Sensitive Path | `/admin/login` |
| Sensitive Path | `/wp-admin` |
| Sensitive Path | `/phpmyadmin` |
| Sensitive Path | `/.env` |
| Sensitive Path | `/backup.zip` |

The IP addresses are documentation-only example addresses used in the fictional scenario.

---

# Assessment

The most suspicious web activity is:

```text
203.0.113.50
→ rapid requests to multiple sensitive endpoints
```

and:

```text
198.51.100.44
→ repeated POST /login failures
→ followed by HTTP 200
```

The first pattern is consistent with web enumeration.

The second pattern should be correlated with application or authentication logs before concluding that credentials were successfully used.

---

# Recommended Response

Possible next steps include:

- review application authentication logs
- inspect requests from both source IPs
- check user-agent information if available
- review web application logs
- correlate timestamps with endpoint telemetry
- confirm whether `/login` HTTP 200 represents authentication success
- block or rate-limit abusive sources if appropriate
- verify that sensitive files and admin interfaces are not exposed

---

# Linux Commands Used

```bash
grep -E "/admin|/wp-admin|/phpmyadmin|/\.env|/backup" sample-data/access.log
```

```bash
grep 'POST /login' sample-data/access.log
```

```bash
cut -d ' ' -f 1 sample-data/access.log | sort | uniq -c | sort -nr
```

```bash
awk '$9 >= 400 {print $1, $4, $6, $7, $9}' sample-data/access.log
```

These commands helped reduce the raw access log into smaller groups of investigation-relevant events.

---

# Key Takeaway

The most important part of web log analysis is not simply finding unusual URLs.

Useful conclusions come from combining:

```text
Source IP
+
Time
+
HTTP Method
+
Requested Path
+
Status Code
+
Repeated Behaviour
```

The next stage will use SQL-style analysis to correlate structured security data from the case.
