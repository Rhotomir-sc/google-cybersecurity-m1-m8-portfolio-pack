# Linux Security Cheatsheet

This cheatsheet contains Linux commands that I found useful while learning system administration and cybersecurity fundamentals.

The goal is not to list every Linux command, but to keep a short reference for commands I can use during security labs and investigations.

---

## Navigation

```bash
pwd
```

Shows the current working directory.

```bash
ls
ls -la
```

Lists files and directories.

`-la` also shows hidden files and detailed permissions.

```bash
cd /path/to/directory
cd ..
cd ~
```

Changes the current directory.

---

## File and Directory Management

```bash
touch file.txt
```

Creates an empty file.

```bash
mkdir security-lab
```

Creates a directory.

```bash
cp source.txt copy.txt
```

Copies a file.

```bash
mv old.txt new.txt
```

Moves or renames a file.

```bash
rm file.txt
rm -r directory/
```

Removes files or directories.

I use destructive commands carefully and verify the target path before running them.

---

## Reading Files

```bash
cat file.txt
```

Displays the complete file.

```bash
head file.txt
tail file.txt
```

Shows the beginning or end of a file.

```bash
less file.txt
```

Allows easier navigation through larger files.

---

## Searching

```bash
grep "failed" auth.log
```

Searches for matching text.

```bash
grep -i "error" logfile.txt
```

Performs a case-insensitive search.

```bash
find /var/log -name "*.log"
```

Searches for files by name.

---

## Users and Groups

```bash
whoami
```

Displays the current user.

```bash
id
```

Shows the current user's UID, GID, and group memberships.

```bash
id username
```

Reviews another user's account and groups.

```bash
sudo useradd username
```

Creates a user.

```bash
sudo usermod -aG groupname username
```

Adds a user to a supplementary group.

```bash
getent group groupname
```

Displays group membership information.

---

## File Permissions

```bash
ls -l
```

Shows file ownership and permissions.

Example:

```text
-rw-r-----
```

Permission groups are:

```text
Owner
Group
Other
```

Permission values:

```text
r = read
w = write
x = execute
```

---

## chmod

```bash
chmod o-w file.txt
```

Removes write permission from others.

```bash
chmod g-r file.txt
```

Removes group read permission.

```bash
chmod 640 file.txt
```

Sets:

```text
Owner: read + write
Group: read
Other: no access
```

---

## Ownership

```bash
chown user file.txt
```

Changes the owner.

```bash
chown user:group file.txt
```

Changes both owner and group.

```bash
chgrp group file.txt
```

Changes only the group.

---

## Processes

```bash
ps
ps aux
```

Lists running processes.

```bash
top
```

Shows running processes and system resource usage.

```bash
kill PID
```

Sends a termination signal to a process.

Process activity should be reviewed before terminating anything during an investigation.

---

## Network Information

```bash
ip addr
```

Shows interface and IP address information.

```bash
ip route
```

Shows the routing table.

```bash
ss -tuln
```

Lists listening TCP and UDP sockets.

```bash
ss -tunap
```

Displays network connections with process information when permissions allow.

---

## Logs

Common Linux log location:

```text
/var/log/
```

Useful commands:

```bash
ls -la /var/log
```

```bash
tail /var/log/auth.log
```

```bash
grep "Failed" /var/log/auth.log
```

Logs can help identify authentication failures, system activity, service problems, and security events.

---

## Pipes and Redirection

```bash
command1 | command2
```

Sends the output of one command into another command.

Example:

```bash
cat access.log | grep "404"
```

Output redirection:

```bash
command > output.txt
```

Overwrites a file.

```bash
command >> output.txt
```

Appends to a file.

---

## Sorting and Counting

```bash
sort file.txt
```

Sorts lines.

```bash
uniq
```

Removes adjacent duplicate lines.

```bash
uniq -c
```

Counts repeated lines.

Example:

```bash
cut -d ' ' -f 1 access.log | sort | uniq -c | sort -nr
```

This can be used to identify frequently occurring IP addresses in a web log.

---

## Useful Security Workflow

A simple Linux investigation flow I use is:

```text
Identify the file or process
        ↓
Check ownership and permissions
        ↓
Review related logs
        ↓
Search for suspicious patterns
        ↓
Review network activity
        ↓
Document the finding
```

---

## Key Takeaway

Linux commands become more useful when they are combined.

For security analysis, commands such as:

```text
grep
cut
sort
uniq
find
ss
```

can turn raw system data into useful investigation evidence.
