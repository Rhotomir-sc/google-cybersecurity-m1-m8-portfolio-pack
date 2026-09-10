# Linux Lab Commands

This file documents practical Linux commands I used while working through security-focused exercises.

The goal is to show how I applied Linux commands during hands-on practice rather than repeat a general command reference.

---

## Lab 1 - User Management

### Create a User

```bash
sudo useradd researcher9
```

This created a new local user account.

### Assign a Primary Group

```bash
sudo usermod -g research_team researcher9
```

This changed the user's primary group to:

```text
research_team
```

### Verify the Account

```bash
id researcher9
```

I used `id` to confirm the user's UID, GID, and group membership.

---

## Lab 2 - File Permissions

### Review Permissions

```bash
ls -la
```

I used this command to review:

```text
Owner
Group
Other
```

permissions before making changes.

### Remove Write Permission from Others

```bash
chmod o-w project_k.txt
```

This removed the `write` permission from the `Other` permission group.

The goal was to reduce unnecessary access and apply least privilege.

### Additional Permission Practice

```bash
chmod g-r report.txt
```

This removed read permission from the group.

---

## Lab 3 - Log Analysis

I used Linux command-line utilities to analyse an Apache access log.

The log file was:

```text
apache.log
```

### Review Log Structure

```bash
head -n 10 apache.log | awk '{print $1, $4, $6, $7, $9}'
```

This helped me focus on useful fields such as:

```text
Source IP
Timestamp
HTTP method
Requested resource
Status code
```

---

## Review HTTP Errors

```bash
awk '$9 >= 400 {print $1, $4, $6, $7, $9}' apache.log | head -n 12
```

This filtered requests with HTTP status codes of `400` or higher.

I used this to quickly review failed or unusual web requests.

---

## Identify Frequent Source IPs

```bash
cut -d ' ' -f 1 apache.log | sort | uniq -c | sort -nr | head -n 10
```

This command:

```text
Extracted source IPs
→ Sorted them
→ Counted repetitions
→ Ranked the most frequent sources
```

A frequently occurring IP is not automatically malicious, but it can be useful for further investigation.

---

## Review Requests to a Specific Endpoint

```bash
grep "/admin.php" apache.log | awk '{print $1, $4, $6, $7, $9}'
```

This filtered requests targeting:

```text
/admin.php
```

I used this to focus on activity involving a potentially sensitive administrative endpoint.

---

# Command Combination Example

One of the most useful lessons was combining multiple commands into a pipeline.

Example:

```bash
cut -d ' ' -f 1 apache.log | sort | uniq -c | sort -nr
```

This simple pipeline turns raw log data into a ranked list of source IP activity.

The workflow is:

```text
Raw log
  ↓
Extract useful field
  ↓
Sort
  ↓
Count
  ↓
Rank
```

---

# Security Concepts Reinforced

These exercises reinforced several security concepts:

- least privilege
- user and group management
- permission review
- access control
- log filtering
- pattern identification
- basic incident investigation
- evidence-based analysis

---

# Related TryHackMe Practice

The Linux exercises connect directly with the following completed labs:

- [01 - Linux User Management](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/01-linux-user-management)
- [02 - Linux Permissions and Least Privilege](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/02-linux-permissions-and-least-privilege)
- [05 - Log Analysis Basics](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/05-log-analysis-basics)

---

# Key Takeaway

The most useful part of Linux for security work is not memorising individual commands.

It is learning how to combine commands to:

```text
Inspect
Filter
Correlate
Verify
Document
```

system and security activity.
