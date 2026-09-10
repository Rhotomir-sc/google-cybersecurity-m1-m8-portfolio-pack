# Module 5 - Assets, Threats, and Vulnerabilities

| Information | Details |
|---|---|
| Course | Assets, Threats, and Vulnerabilities |
| Program | Google Cybersecurity Professional Certificate |
| Focus | Asset Security, Threats, Vulnerabilities & Risk Assessment |
| Status | Completed |

---

## Overview

This module focused on understanding what organisations need to protect, what can threaten those assets, where weaknesses may exist, and how security teams can reduce exposure.

I learned to think about security using a simple relationship:

```text
Asset
+
Threat
+
Vulnerability
=
Security Risk
```

The module also reinforced:

- asset classification
- attack surface
- threat actors
- social engineering
- vulnerabilities
- security controls
- risk prioritisation
- defense-in-depth

---

# Asset Security

An asset is anything that has value to an organisation.

Examples include:

```text
Data
User identities
Endpoints
Servers
Applications
Cloud services
Network infrastructure
```

Not all assets have the same importance.

A customer database containing sensitive information usually requires stronger protection than a low-impact public resource.

---

## Asset Classification

Asset classification helps determine how strongly something should be protected.

Important factors include:

- sensitivity
- business importance
- confidentiality requirements
- operational impact
- legal or regulatory requirements

A security team should understand the value of the asset before deciding which controls are appropriate.

---

# Threats

A threat is something that may cause harm to an asset.

Examples include:

- phishing
- malware
- credential theft
- ransomware
- insider misuse
- unauthorized remote access
- exploitation of exposed services

Threats can come from both external and internal sources.

---

# Vulnerabilities

A vulnerability is a weakness that may be exploited by a threat.

Examples include:

```text
Weak passwords
Missing MFA
Unpatched software
Overly broad permissions
Open administrative ports
Misconfigured firewall rules
Insufficient monitoring
```

A vulnerability does not automatically mean a system has already been compromised.

It represents an opportunity for exploitation.

---

# Threat, Vulnerability, and Risk Relationship

One example:

```text
Asset:
Employee cloud account

Threat:
Credential theft

Vulnerability:
No MFA

Risk:
Account takeover

Impact:
Unauthorized access to company resources

Control:
MFA + Sign-in Monitoring
```

This helped me understand why security findings should be evaluated in context.

---

# Attack Surface

The attack surface includes all possible paths that could be used to interact with or attack a system.

Examples include:

- internet-facing services
- user accounts
- email
- cloud applications
- endpoints
- remote access services
- open ports
- APIs

Reducing unnecessary exposure helps reduce risk.

---

## Attack Surface Reduction

Examples include:

```text
Disable unused services
Close unnecessary ports
Remove inactive accounts
Restrict remote access
Apply least privilege
Use network segmentation
Patch vulnerable software
```

---

# Defense-in-Depth

One control should not be expected to stop every attack.

A stronger security model uses several layers.

Example for protecting user accounts:

```text
Strong password policy
        +
MFA
        +
Phishing awareness
        +
Authentication monitoring
        +
Incident response
```

If one control fails, another layer may still detect or limit the attack.

---

# Portfolio Artifact - Asset Risk Assessment

I created a fictional asset risk assessment to apply the concepts from this module.

[View Asset Risk Assessment](asset-risk-assessment.md)

The assessment includes:

- asset inventory
- asset importance
- threats
- vulnerabilities
- possible impact
- recommended controls
- risk prioritisation
- attack-surface observations
- defense-in-depth recommendations

The scenario covers assets such as:

```text
Customer Database
Employee Accounts
Corporate Email
Employee Laptops
File Server
Remote Access Service
```

---

# Risk Prioritisation

Security teams cannot treat every risk with the same priority.

I considered:

```text
Likelihood
+
Impact
```

to determine which risks required more attention.

Examples from the assessment included:

| Risk | Likelihood | Impact | Priority |
|---|---|---|---|
| Employee account compromise | High | High | Critical |
| Phishing attack | High | High | Critical |
| Customer database exposure | Medium | High | High |
| Unauthorized remote access | Medium | High | High |
| Ransomware on file server | Medium | High | High |
| Endpoint malware | Medium | Medium | Medium |

---

# Related TryHackMe Practice

Several completed TryHackMe labs reinforce the concepts from this module.

### Threat Intelligence & IOC Analysis

[08 - Threat Intelligence & IOC Analysis](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/08-threat-intelligence-ioc-analysis)

This reinforced:

- malware indicators
- threat intelligence
- IOC enrichment
- ATT&CK mapping

### Cloud Identity Basics

[10 - Cloud Identity Basics](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/10-cloud-identity-basics)

This reinforced:

- identity threats
- authentication failures
- account compromise
- sign-in monitoring

### Firewall Rule Audit

[11 - Firewall Rule Audit](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/11-firewall-rule-audit)

This reinforced:

- attack surface
- remote-access exposure
- firewall misconfiguration
- least-privilege network controls

### Phishing Detection

[12 - Phishing Detection](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/12-phishing-detection)

This reinforced:

- social engineering
- phishing threats
- malicious links
- sender-domain analysis

A complete mapping is available here:

[Related TryHackMe Labs](../related-tryhackme-labs.md)

---

# What I Practiced

During this module, I practiced:

- identifying important assets
- understanding asset classification
- distinguishing threats from vulnerabilities
- analysing attack surface
- identifying security weaknesses
- evaluating likelihood and impact
- prioritising security risks
- recommending security controls
- applying defense-in-depth
- connecting technical findings with business impact
- documenting a structured asset risk assessment

---

# Key Takeaways

## 1. Security starts with understanding the asset

Before applying controls, I need to know:

```text
What am I protecting?
Why is it important?
What happens if it is compromised?
```

---

## 2. A vulnerability is not the same as an incident

A vulnerability is a weakness.

An incident occurs when security is actually affected.

This distinction is important when documenting findings.

---

## 3. Attack surface should be reduced where possible

Every unnecessary account, port, service, or permission can increase exposure.

Reducing unused access can lower risk.

---

## 4. Risk requires context

A technical weakness becomes more meaningful when combined with:

```text
Asset value
Threat
Likelihood
Impact
```

---

## 5. Defense-in-depth reduces dependence on one control

Security should not rely on one password, one firewall rule, or one detection system.

Layered controls provide stronger protection.

---

# Result

This module helped me connect assets, threats, vulnerabilities, and controls into a structured security assessment.

I created an asset risk assessment covering identities, endpoints, data, email, servers, and remote-access services.

The most important lesson was that security findings become more useful when they are connected to the asset being protected, the realistic threat, the possible impact, and the controls that can reduce the risk.

---

## Next Step

Module 6 focuses on detection, alert investigation, incident response, and documenting security incidents.
