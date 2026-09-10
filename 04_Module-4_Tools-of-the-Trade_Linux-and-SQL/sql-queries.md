# SQL Security Queries

This file documents SQL queries I practiced while learning how security analysts can filter and investigate structured data.

The goal was to use SQL for security questions such as:

- identifying failed login attempts
- narrowing activity by date and time
- reviewing unusual geographic activity
- combining multiple conditions
- retrieving user and device information

---

## Basic Query Structure

A basic SQL query follows this structure:

```sql
SELECT column_name
FROM table_name;
```

To return all columns:

```sql
SELECT *
FROM table_name;
```

---

# Login Analysis

## Review All Login Attempts

```sql
SELECT *
FROM log_in_attempts;
```

This provides the complete authentication dataset before applying filters.

---

## Failed Login Attempts

```sql
SELECT *
FROM log_in_attempts
WHERE success = 0;
```

This filters authentication attempts that were not successful.

From a security perspective, failed logins can help identify:

- mistyped passwords
- brute-force attempts
- password spraying
- attempts against disabled or invalid accounts

A failed login by itself is not enough to classify activity as malicious.

---

## Failed Attempts After Business Hours

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00'
AND success = 0;
```

This combines:

```text
Time condition
+
Authentication result
```

to focus on failed attempts occurring after normal working hours.

---

## Filter by Date

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09';
```

Date filtering is useful when an investigation has a known incident window.

---

## Activity After a Specific Date

```sql
SELECT *
FROM log_in_attempts
WHERE login_date > '2022-05-09';
```

This reduces the dataset to events that occurred after a known point in time.

---

# Geographic Filtering

## Review Logins From a Country

```sql
SELECT *
FROM log_in_attempts
WHERE country LIKE 'MEX%';
```

Using `LIKE` allows partial text matching.

`MEX%` can match values beginning with the same country identifier.

---

## Exclude Expected Geographic Activity

```sql
SELECT *
FROM log_in_attempts
WHERE country NOT LIKE 'MEX%';
```

This can help focus an investigation on authentication activity outside an expected location.

Geographic information alone should not be used to declare an event malicious.

---

# Using AND

`AND` requires both conditions to be true.

Example:

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
AND success = 0;
```

This returns only failed login attempts from the selected date.

---

# Using OR

`OR` allows either condition to match.

Example:

```sql
SELECT *
FROM employees
WHERE department = 'Finance'
OR department = 'Sales';
```

This can be useful when an investigation affects several business groups.

---

# Using NOT

`NOT` excludes matching results.

Example:

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

This could help separate IT accounts from non-IT users during an access review.

---

# Multiple Conditions

Security investigations often require several filters at once.

Example:

```sql
SELECT *
FROM log_in_attempts
WHERE success = 0
AND login_time > '18:00:00'
AND country NOT LIKE 'MEX%';
```

This narrows the results to:

```text
Failed login
+
After-hours activity
+
Outside the selected location
```

The query does not prove that the activity is malicious.

It produces a smaller set of events for further analysis.

---

# Employee Investigation

## Review Employees in a Department

```sql
SELECT *
FROM employees
WHERE department = 'Information Technology';
```

This can help identify users belonging to a specific team during access reviews or incident investigations.

---

## Search by Office

```sql
SELECT *
FROM employees
WHERE office LIKE 'East%';
```

This demonstrates how pattern matching can be used to filter users based on organisational information.

---

# SQL Joins

Security data may be spread across multiple tables.

A `JOIN` can connect related information.

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

This type of query can help connect:

```text
User
+
Department
+
Assigned device
+
Operating system
```

during an investigation.

---

## Why Joins Matter

An authentication alert may initially provide only a username.

Other datasets may contain:

```text
Employee information
Device information
Department
Location
Asset ownership
```

Combining these sources can provide better investigation context.

---

# Security Investigation Workflow

A simple SQL-based investigation can follow this process:

```text
Start with large dataset
        ↓
Filter relevant records
        ↓
Add time / user / location conditions
        ↓
Correlate related tables
        ↓
Review reduced dataset
        ↓
Document findings
```

SQL helps reduce large datasets into smaller groups of events that are easier to investigate.

---

# What I Practiced

During the SQL exercises, I practiced:

- `SELECT`
- `FROM`
- `WHERE`
- `AND`
- `OR`
- `NOT`
- `LIKE`
- wildcard `%`
- date filtering
- time filtering
- authentication filtering
- sorting investigation data
- combining multiple conditions
- joining related tables

---

# Security Use Cases

SQL can support tasks such as:

```text
Failed-login analysis
Account investigation
Access reviews
Asset correlation
Incident scoping
Log filtering
User and device correlation
```

The value of SQL is not only retrieving data.

It allows an analyst to ask increasingly specific questions about a security dataset.

---

# Key Takeaway

SQL provides a structured way to move from:

```text
Large amount of security data
```

to:

```text
Small set of relevant events
```

that can be investigated further.

The query result is evidence for analysis, but the filter itself does not automatically prove malicious activity.
