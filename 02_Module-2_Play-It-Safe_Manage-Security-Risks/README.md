# Module 2 - Play It Safe: Manage Security Risks

| Information | Details |
|---|---|
| Course | Play It Safe: Manage Security Risks |
| Program | Google Cybersecurity Professional Certificate |
| Focus | Risk Management, Security Controls & GRC |
| Status | Completed |

---

## Overview

This module focused on how organisations identify, evaluate, and reduce cybersecurity risk.

I learned that security decisions should not be based only on technical weaknesses. Risk analysis also needs to consider the value of the asset, the likelihood of an event, the possible business impact, and the controls already in place.

The main topics I focused on were:

- security risks
- vulnerabilities and threats
- security controls
- risk prioritisation
- security frameworks
- governance and compliance concepts
- security audits
- documenting security decisions

---

## Risk Management Approach

A simple workflow I used throughout this module was:

```text
Identify the asset
       ↓
Identify threats and vulnerabilities
       ↓
Estimate likelihood and impact
       ↓
Prioritise the risk
       ↓
Select appropriate controls
       ↓
Review residual risk
```

This helped me connect technical security findings with business impact.

---

# Portfolio Artifacts

## Risk Register

I created a structured risk register to document common organisational security risks.

[View Risk Register](risk-register.md)

The register includes examples such as:

- weak passwords
- excessive privileges
- delayed patching
- phishing
- sensitive data exposure

For each risk, I considered:

```text
Risk
→ Possible impact
→ Likelihood
→ Priority
→ Mitigation
```

The goal was to move beyond simply identifying a problem and also document how the risk could be reduced.

---

## Security Controls Mapping

I also created a control-mapping document:

[View Controls Mapping](controls-mapping.md)

The controls were grouped by their security purpose.

### Preventive Controls

Designed to stop or reduce the likelihood of an incident.

Examples:

- strong authentication
- least privilege
- firewall restrictions
- patch management
- security awareness

### Detective Controls

Designed to identify suspicious or unwanted activity.

Examples:

- log monitoring
- SIEM alerts
- IDS/IPS
- authentication monitoring
- security audits

### Corrective Controls

Designed to reduce impact and restore systems after an incident.

Examples:

- account remediation
- malware removal
- configuration recovery
- patch deployment
- incident response procedures

---

# Risk and Control Relationship

One of the most useful concepts from this module was understanding that risks and controls should be directly connected.

For example:

```text
Weak passwords
      ↓
Credential compromise
      ↓
MFA + password policy
```

```text
Excessive privileges
      ↓
Privilege misuse
      ↓
Least privilege + access reviews
```

```text
Unpatched systems
      ↓
Known vulnerability exploitation
      ↓
Patch management
```

```text
Phishing
      ↓
Credential theft / malware
      ↓
Email security + user awareness + MFA
```

This made risk management more practical because every security finding should lead to a reasonable mitigation strategy.

---

# Security Controls

I learned that no single security control can eliminate every risk.

A stronger defensive approach uses multiple layers.

```text
Prevent
   +
Detect
   +
Respond
```

For example, phishing risk can be reduced through:

```text
Email filtering
+
User awareness
+
MFA
+
Authentication monitoring
+
Incident response
```

This layered approach is also visible throughout the hands-on labs in my TryHackMe portfolio.

---

# Governance, Risk, and Compliance

This module also helped me understand the role of GRC in cybersecurity.

Technical security teams do not work independently from organisational requirements.

Security decisions may also depend on:

- company policies
- regulations
- business requirements
- acceptable risk
- internal standards
- audit findings

I learned that cybersecurity controls should support both technical protection and organisational objectives.

---

# Security Audits

A security audit can help identify gaps between:

```text
Expected security state
```

and:

```text
Current security state
```

Examples of audit findings could include:

- firewall profiles disabled
- excessive user privileges
- weak authentication requirements
- missing patches
- unnecessary services
- incomplete logging

The important part is not only identifying the gap but documenting its risk and recommended remediation.

---

# Related TryHackMe Practice

Several hands-on labs from my TryHackMe portfolio reinforce the risk and control concepts from this module.

### Firewall Rule Audit

[11 - Firewall Rule Audit](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/11-firewall-rule-audit)

I reviewed firewall profiles and identified an overly permissive WinRM rule.

This reinforced:

- control assessment
- network access restrictions
- least privilege
- security hardening

### Phishing Detection

[12 - Phishing Detection](https://github.com/Rhotomir-sc/tryhackme-portfolio-pack/tree/main/portfolio-labs/12-phishing-detection)

I analysed a suspicious email and identified brand impersonation, sender-domain mismatch, and suspicious link infrastructure.

This reinforced:

- phishing risk
- social engineering
- email security controls
- layered defence

A complete mapping between the Google modules and my TryHackMe labs is available here:

[Related TryHackMe Labs](../related-tryhackme-labs.md)

---

# What I Practiced

During this module, I practiced:

- identifying cybersecurity risks
- distinguishing threats, vulnerabilities, and risks
- estimating likelihood and impact
- prioritising risks
- creating a risk register
- mapping risks to security controls
- distinguishing preventive, detective, and corrective controls
- applying least-privilege concepts
- thinking about residual risk
- understanding security audits
- connecting technical findings with business impact
- documenting security recommendations

---

# Key Takeaways

## 1. Not every vulnerability has the same risk

A weakness becomes more important when it affects a valuable asset and has a realistic path to exploitation.

---

## 2. Controls should address specific risks

Security controls should not be applied randomly.

The control should reduce either:

```text
Likelihood
```

or:

```text
Impact
```

of an identified risk.

---

## 3. Layered security is stronger

Preventive controls alone are not enough.

Organisations also need:

```text
Detection
+
Response
+
Recovery
```

capabilities.

---

## 4. Security is also a business problem

A technical finding matters because of what it can do to:

- systems
- data
- users
- operations
- reputation
- business continuity

---

# Result

This module helped me move from basic cybersecurity concepts to a more structured risk-management mindset.

I created a risk register and mapped different risks to preventive, detective, and corrective security controls.

The most important lesson was that good security work requires more than identifying vulnerabilities.

It also requires understanding:

```text
What can happen
How likely it is
What the impact would be
Which controls can reduce the risk
```

---

## Next Step

Module 3 focuses on networks and network security, including network baselines, traffic analysis, protocols, and defensive network controls.
