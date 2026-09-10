# Module 4 - Tools of the Trade: Linux and SQL

| Information | Details |
|---|---|
| Course | Tools of the Trade: Linux and SQL |
| Program | Google Cybersecurity Professional Certificate |
| Focus | Linux Administration, Command Line & SQL Analysis |
| Status | Completed |

---

## Overview

This module focused on two tools that are widely used in cybersecurity work:

- Linux
- SQL

I practiced using Linux commands for system administration, permissions, user management, log analysis, and basic network investigation.

I also practiced using SQL to filter structured data and answer security-related questions such as failed authentication, user activity, and asset relationships.

The main goal was to become more comfortable working directly with system and security data instead of relying only on graphical tools.

---

# Linux

## Why Linux Matters in Security

Linux is common in:

- servers
- cloud environments
- security appliances
- containers
- penetration testing systems
- SOC and DFIR tooling

Understanding Linux helps with both administration and investigation.

---

## Linux Security Cheatsheet

I created a short command reference for the Linux commands I use most often during security practice.

[View Linux Security Cheatsheet](linux-cheatsheet.md)

It includes commands related to:

- navigation
- files and directories
- users and groups
- permissions
- processes
- networking
- logs
- searching and filtering
- pipes and redirection

The goal was not to create a complete Linux manual, but a practical reference I can reuse during labs.

---

## Practical Linux Commands

I also documented commands I used during hands-on security exercises.

[View Linux Lab Commands](linux-lab-commands.md)

The practical work included:

### User Management

```bash
sudo useradd researcher9
sudo usermod -g research_team researcher9
id researcher9
```

These commands were used to create a user, assign a group, and verify account membership.

### Permission Management

```bash
chmod o-w project_k.txt
chmod g-r report.txt
```

These exercises reinforced least-privilege concepts and Linux file permissions.

### Log Analysis

I combined commands such as:

```text
grep
awk
cut
sort
uniq
head
```

to analyse Apache access logs.

Example:

```bash
cut -d ' ' -f 1 apache.log | sort | uniq -c | sort -nr | head -n 10
```

This converted raw log data into a ranked list of frequently observed source IPs.

---

# SQL

## Why SQL Matters in Security

Security data is often stored in structured databases.

SQL can help analysts investigate:

- authentication records
- users
- devices
- asset ownership
- timestamps
- geographic information
- access activity

Instead of manually reviewing every row, SQL allows an analyst to reduce the dataset to relevant events.

---

## SQL Security Queries

I documented the SQL queries I practiced here:

[View SQL Security Queries](sql-queries.md)

The exercises included:

- `SELECT`
- `WHERE`
- `AND`
- `OR`
- `NOT`
- `LIKE`
- wildcard matching
- date filtering
- time filtering
- failed-login filtering
- joins

---

## Authentication Analysis

One example was filtering failed login attempts:

```sql
SELECT *
FROM log_in_attempts
WHERE success = 0;
```

I also combined multiple conditions:

```sql
SELECT *
FROM log_in_attempts
WHERE success = 0
AND login_time > '18:00:00'
AND country NOT LIKE 'MEX%';
```

This type of query can reduce a large authentication dataset to a smaller set of events for further investigation.

The result still requires context and does not automatically prove malicious activity.

---

## Correlating Data With JOIN

I practiced combining information from different tables.

Example:

```sql
SELECT employees.username,
       employees.department,
       machines.device_id,
       machines.operating_system
FROM employees
INNER JOIN machines
ON employees.device_id = machines.device_id;
```

This can help connect:

```text
User
+
Department
+
Device
+
Operating System
```

during an investigation.

---

# Practical Workflow

The Linux and SQL sections reinforced a similar analysis workflow.

```text
Collect data
    ↓
Filter
    ↓
Reduce noise
    ↓
Identify relevant activity
    ↓
Correlate
    ↓
Document findings
```

Linux command-line tools are useful for text-based system and log data, while SQL is useful for structured database records.

---

# Portfolio Artifacts

This module contains three practical artifacts:

```text
linux-cheatsheet.md
linux-lab-commands.md
sql-queries.md
```

Each file serves a different purpose:

| Artifact | Purpose |
|---|---|
| `linux-cheatsheet.md` | Reusable Linux security command reference |
| `linux-lab-commands.md` | Commands applied during hands-on exercises |
| `sql-queries.md` | Security-focused SQL filtering and correlation examples |

---

# Related TryHackMe Practice

The Linux portion of this module connects directly with several completed TryHackMe labs.

### Linux User Management

[01 - Linux User Management](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/01-linux-user-management)

This reinforced:

- user creation
- group management
- identity verification

### Linux Permissions and Least Privilege

[02 - Linux Permissions and Least Privilege](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/02-linux-permissions-and-least-privilege)

This reinforced:

- Linux permissions
- access control
- least privilege

### Log Analysis Basics

[05 - Log Analysis Basics](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/05-log-analysis-basics)

This reinforced:

- command-line log analysis
- field extraction
- pattern filtering
- HTTP log review

A complete module mapping is available here:

[Related TryHackMe Labs](../related-tryhackme-labs.md)

---

# What I Practiced

During this module, I practiced:

- navigating Linux systems
- managing users and groups
- reviewing file permissions
- changing permissions with `chmod`
- reviewing processes
- reviewing network configuration
- analysing logs from the command line
- combining Linux utilities with pipes
- filtering structured data with SQL
- combining multiple SQL conditions
- filtering login attempts
- querying users and devices
- joining related tables
- reducing large datasets into investigation-relevant results

---

# Key Takeaways

## 1. Command-line tools become stronger when combined

A single command may provide limited information.

Combining tools such as:

```text
cut
sort
uniq
grep
awk
```

can turn raw text into useful security evidence.

---

## 2. Least privilege applies at the operating-system level

Linux permissions and group membership directly affect which users can access or modify resources.

Small permission changes can significantly reduce unnecessary access.

---

## 3. SQL helps reduce investigation noise

Security datasets can contain many records.

SQL makes it possible to progressively narrow those records using:

```text
User
Time
Date
Location
Authentication result
Asset
```

---

## 4. Query results still require analysis

A failed login, unusual country, or frequently observed IP is not automatically malicious.

The query identifies activity worth investigating.

The analyst still needs context and supporting evidence.

---

# Result

This module helped me become more comfortable working directly with security data through Linux and SQL.

I practiced user and permission management, command-line log analysis, structured authentication filtering, and data correlation.

The most important lesson was that both Linux and SQL are effective because they allow large amounts of system data to be reduced into smaller, more useful investigation results.

---

## Next Step

Module 5 focuses on assets, threats, vulnerabilities, security exposure, and risk assessment.
