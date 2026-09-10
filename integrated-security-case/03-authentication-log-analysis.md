# 03 - Authentication Log Analysis

## Objective

The goal of this stage is to review the authentication dataset and identify suspicious sign-in patterns.

The dataset is stored in:

```text
sample-data/signin-events.csv
```

The main investigation questions are:

- Which user experienced repeated authentication failures?
- Which source IP generated those failures?
- Did the same source later authenticate successfully?
- Which applications were accessed afterward?
- Is there enough evidence to escalate the activity?

---

# Dataset Review

The dataset contains authentication activity for several users.

Most users show normal successful sign-ins from internal addresses.

One account stands out:

```text
emma.lee@northstar.example
```

The suspicious source IP is:

```text
198.51.100.23
```

This address is used only as fictional documentation data for the portfolio scenario.

---

# Finding 1 - Repeated Failed Authentication

The account:

```text
emma.lee@northstar.example
```

received six consecutive failed login attempts from:

```text
198.51.100.23
```

The failed events used:

```text
Application: OfficeHome
Status: failed
Error Code: 50126
Interactive: true
```

The sequence occurred within approximately one minute.

---

## Authentication Pattern

```text
08:14:02 → Failed
08:14:11 → Failed
08:14:20 → Failed
08:14:32 → Failed
08:14:47 → Failed
08:15:03 → Failed
```

All six attempts targeted the same user from the same source IP.

This pattern is consistent with repeated credential guessing and requires further investigation.

A failed-login sequence alone does not prove account compromise.

---

# Finding 2 - Successful Authentication

At:

```text
08:15:19
```

the same account successfully authenticated from the same source:

```text
User:
emma.lee@northstar.example

Source IP:
198.51.100.23

Application:
OfficeHome

Status:
success

Interactive:
true
```

This happened only seconds after the failed authentication sequence.

---

# Finding 3 - Post-Authentication Access

After the successful OfficeHome sign-in, additional successful activity from the same source was recorded.

### 08:16:02

```text
Application: Outlook Web
Status: success
```

### 08:17:41

```text
Application: My Profile
Status: success
```

The complete suspicious sequence was:

```text
6 failed OfficeHome sign-ins
          ↓
Successful OfficeHome sign-in
          ↓
Outlook Web access
          ↓
My Profile access
```

---

# Comparison With Normal Activity

Other users in the dataset authenticated successfully from internal addresses such as:

```text
10.10.20.15
10.10.20.21
```

Later, `emma.lee@northstar.example` also authenticated successfully from:

```text
10.10.20.33
```

This provides useful context because the earlier suspicious sequence originated from a different source.

However, the dataset alone does not include enough network or identity context to determine whether the external source was a legitimate remote location.

---

# Correlation

The strongest finding comes from correlating:

```text
Same user
+
Same source IP
+
Repeated authentication failures
+
Successful authentication
+
Post-login application access
```

rather than treating each event separately.

---

# Investigation Timeline

| Time | User | Source IP | Application | Result |
|---|---|---|---|---|
| 08:14:02–08:15:03 | `emma.lee@northstar.example` | `198.51.100.23` | OfficeHome | 6 failures |
| 08:15:19 | `emma.lee@northstar.example` | `198.51.100.23` | OfficeHome | Success |
| 08:16:02 | `emma.lee@northstar.example` | `198.51.100.23` | Outlook Web | Success |
| 08:17:41 | `emma.lee@northstar.example` | `198.51.100.23` | My Profile | Success |
| 08:42:05 | `emma.lee@northstar.example` | `10.10.20.33` | OfficeHome | Success |

---

# Assessment

The sequence should be escalated for further investigation.

The strongest indicators are:

- six failed attempts against one identity
- all failures originated from the same source
- a successful login followed immediately afterward
- additional cloud applications were accessed from the same source

I would classify this as:

```text
Suspicious authentication activity
with possible account compromise
```

I would not classify it as confirmed compromise without additional identity, endpoint, or user-verification evidence.

---

# Recommended Response

Immediate next steps should include:

- verify the sign-in with the user
- review MFA and Conditional Access information
- inspect additional sign-in activity from the source IP
- review mailbox and account activity
- revoke suspicious sessions if compromise is confirmed
- reset credentials if required
- review permissions and account changes
- preserve relevant authentication logs

---

# Detection Logic

A basic detection concept for this pattern could be:

```text
Multiple failed logins
        ↓
Same user + same source
        ↓
Successful login shortly afterward
        ↓
Generate investigation alert
```

This type of correlation can reduce noise compared with alerting on every individual failed login.

---

# Key Takeaway

The important finding was not simply:

```text
Failed login
```

or:

```text
Successful login
```

It was the correlated sequence:

```text
Repeated failures
+
Same source
+
Successful authentication
+
Post-login activity
```

Correlation provided the context needed to justify escalation.

---

## Next Step

The next stage will analyse suspicious web-server activity and identify unusual request patterns using Linux-style log analysis.
