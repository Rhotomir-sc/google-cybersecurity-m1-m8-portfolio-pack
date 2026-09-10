# Asset Risk Assessment

This document is a small security risk assessment created to practice the asset, threat, vulnerability, and control concepts from Module 5.

The scenario is fictional and is used only for portfolio practice.

---

## Scenario

A small company uses:

- employee laptops
- Microsoft 365 accounts
- a customer database
- an internal file server
- remote access services
- corporate email

The goal is to identify important assets, possible threats, vulnerabilities, and suitable controls.

---

# Asset Inventory

| Asset | Type | Importance | Security Concern |
|---|---|---:|---|
| Customer Database | Data | High | Sensitive customer information |
| Employee Accounts | Identity | High | Account compromise |
| Corporate Email | Service | High | Phishing and credential theft |
| Employee Laptops | Endpoint | Medium | Malware and data loss |
| File Server | System | High | Unauthorized access and ransomware |
| Remote Access Service | Network Service | High | External exposure |

---

# Asset Classification

## High-Value Assets

The most important assets in this scenario are:

```text
Customer Database
Employee Identities
File Server
Corporate Email
Remote Access Service
```

A compromise of these assets could affect:

- confidentiality
- integrity
- availability
- business operations
- customer trust

---

# Threat and Vulnerability Analysis

## 1. Customer Database

### Threat

Unauthorized access or data theft.

### Vulnerabilities

Possible weaknesses include:

- excessive database permissions
- weak credentials
- exposed database services
- missing monitoring

### Possible Impact

```text
Sensitive data exposure
Privacy impact
Business reputation damage
```

### Recommended Controls

- least-privilege database access
- MFA for administrative accounts
- logging and monitoring
- network segmentation
- regular access reviews

---

## 2. Employee Accounts

### Threat

Credential theft or account takeover.

### Vulnerabilities

- weak passwords
- password reuse
- missing MFA
- phishing

### Possible Impact

An attacker could gain access to:

```text
Email
Cloud applications
Internal files
Other company systems
```

### Recommended Controls

- MFA
- strong authentication policies
- sign-in monitoring
- user awareness training
- account lockout and risk-based detection

---

## 3. Corporate Email

### Threat

Phishing and social engineering.

### Vulnerabilities

- users trusting display names
- malicious links
- weak email filtering
- lack of user awareness

### Possible Impact

```text
Credential theft
Malware infection
Account compromise
Business email compromise
```

### Recommended Controls

- email filtering
- SPF, DKIM, and DMARC
- security awareness
- URL inspection
- MFA

---

## 4. Employee Laptops

### Threat

Malware execution or endpoint compromise.

### Vulnerabilities

- outdated software
- excessive local privileges
- malicious downloads
- weak endpoint monitoring

### Recommended Controls

- patch management
- endpoint protection
- least privilege
- application control
- security logging

---

## 5. File Server

### Threat

Unauthorized access or ransomware.

### Vulnerabilities

- overly broad permissions
- exposed network services
- weak administrative access
- missing backups

### Recommended Controls

- least-privilege permissions
- network segmentation
- secure backups
- monitoring
- restricted administrative access

---

## 6. Remote Access Service

### Threat

Unauthorized remote access.

### Vulnerabilities

- open management ports
- broad firewall rules
- weak authentication
- unrestricted source addresses

### Recommended Controls

- restrict source IP ranges
- require MFA
- disable unused remote services
- monitor authentication logs
- apply least-privilege firewall rules

---

# Risk Prioritisation

| Risk | Likelihood | Impact | Priority |
|---|---|---|---|
| Employee account compromise | High | High | Critical |
| Customer database exposure | Medium | High | High |
| Phishing attack | High | High | Critical |
| Ransomware on file server | Medium | High | High |
| Malware on employee endpoint | Medium | Medium | Medium |
| Unauthorized remote access | Medium | High | High |

---

# Example Risk Chain

One example of how different security concepts connect:

```text
Asset
Employee Account
      ↓
Threat
Credential Theft
      ↓
Vulnerability
No MFA
      ↓
Risk
Account Compromise
      ↓
Impact
Access to cloud resources
      ↓
Control
MFA + Sign-in Monitoring
```

---

# Attack Surface Observations

The attack surface in this scenario includes:

```text
Internet-facing remote services
Email
User accounts
Employee endpoints
Cloud applications
Internal servers
```

Reducing unnecessary exposure can lower risk.

Examples include:

- closing unused ports
- removing unnecessary accounts
- restricting firewall rules
- disabling unused services
- reducing user privileges

---

# Defense-in-Depth

No single control is enough.

For example, protecting employee accounts may require:

```text
Strong passwords
      +
MFA
      +
Phishing awareness
      +
Sign-in monitoring
      +
Incident response
```

This layered approach reduces the chance that one failed control leads directly to a full compromise.

---

# Related TryHackMe Practice

The concepts in this assessment connect with several hands-on labs from my TryHackMe portfolio.

- [08 - Threat Intelligence & IOC Analysis](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/08-threat-intelligence-ioc-analysis)
- [10 - Cloud Identity Basics](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/10-cloud-identity-basics)
- [11 - Firewall Rule Audit](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/11-firewall-rule-audit)
- [12 - Phishing Detection](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/12-phishing-detection)

---

# What I Practiced

This assessment helped me practice:

- identifying important assets
- classifying asset importance
- identifying threats
- identifying vulnerabilities
- evaluating likelihood and impact
- prioritising risks
- recommending security controls
- applying defense-in-depth
- reducing attack surface
- connecting technical risks with business impact

---

# Key Takeaway

A vulnerability alone does not explain the full security risk.

A better assessment considers:

```text
Asset
+
Threat
+
Vulnerability
+
Likelihood
+
Impact
+
Controls
```

together.
