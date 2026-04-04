# 🛡️ Cybersecurity Portfolio — Nithishkumar

## 👨‍💻 Who I Am

I am an aspiring **SOC Analyst (L1)** focused on **log analysis, incident investigation, and network security validation**.

I build **hands-on lab environments** to simulate real-world attack scenarios and analyze them from a defender’s perspective — focusing on how attackers behave, how systems respond, and how compromises can be detected.

This portfolio reflects my ability to **investigate, reconstruct, and explain security incidents clearly using real artifacts**.

---

## ⚡ What Makes This Portfolio Different

Instead of only learning theory, I focus on:

- Simulating **real attack scenarios**
- Working with **raw logs (no SIEM shortcuts)**
- Reconstructing **full attacker timelines**
- Validating **network security controls through testing**

---

## 🧱 Portfolio Structure

---

### 🌐 Network Security Labs

**Focus:** Segmentation, routing, ACL enforcement, and traffic validation

#### Network Segmentation & ACL Validation Lab

- Designed multi-router segmented network using subnetting
- Implemented **static routing and DHCP configuration**
- Applied **extended ACLs to restrict ICMP traffic**
- Verified enforcement using:
    - `ping`
    - `traceroute`
    - `show access-lists`

**Key Insight:**  
Validated how segmentation policies actively control communication between network segments.

---

#### Network Security & Traffic Analysis Lab

- Implemented **VLAN segmentation (HR / IT)**
- Configured **Router-on-a-Stick (Inter-VLAN routing)**
- Applied **ACL-based traffic restrictions**
- Enabled:
    - Port Security
    - DHCP Snooping
    - Syslog logging
- Analyzed packet behavior using:
    - ARP
    - DHCP (DORA)
    - DNS
    - ICMP

**Key Insight:**  
Understood how packet-level behavior reflects network configuration and security enforcement.

---

### 🛡️ SOC Investigations (Linux)

**Focus:** Log analysis, attack detection, and incident reconstruction

---

#### Project 1 — Linux SOC Incident Investigation

- Analyzed `auth.log` for suspicious login activity
- Detected **privilege escalation via sudo**
- Identified **cron-based persistence (/tmp execution)**
- Observed **log tampering indicators**
- Investigated access to `/etc/shadow`

**Outcome:**  
Reconstructed attacker behavior and identified multiple compromise indicators.

---

#### Project 2 — Linux Log Compromise Reconstruction

- Detected **SSH brute force attack**
- Identified **direct root compromise**
- Correlated logs across events
- Reconstructed full attack timeline
- Produced structured SOC report

**Outcome:**  
Simulated real SOC investigation with noisy logs and confirmed system compromise.

---

#### Project 3 — SOC Final Boss Simulation

- Investigated mixed log dataset with noise
- Filtered false positives
- Confirmed attacker access and persistence
- Delivered:
    - Attack timeline
    - Compromise assessment
    - Full incident report

**Outcome:**  
Demonstrated end-to-end SOC investigation capability under realistic conditions.

---

### 🔧 Security Tooling

#### Python Authentication Analysis Tool (CLI)

- Built CLI tool to simulate authentication attempts
- Processed credential datasets
- Simulated:
    - Brute-force patterns
    - Account lockout behavior
- Logged and analyzed authentication outcomes

**Security Insight:**

- Identified how repeated failures appear in logs
- Observed detection patterns used in monitoring systems

---

## 🎯 Skills Demonstrated

### Networking

- Network segmentation & subnetting
- Static routing & inter-VLAN routing
- ACL configuration and validation
- DHCP, DNS fundamentals

### SOC & Blue Team

- Log analysis (`auth.log`, syslog)
- Incident investigation & timeline reconstruction
- Privilege escalation detection
- Persistence detection (cron jobs)
- Log tampering identification

### Security Analysis

- Attack pattern recognition
- IOC identification
- False positive filtering
- Evidence-based reporting

### Scripting

- Python CLI development
- File handling and dataset processing
- Authentication workflow simulation

---

## 🧠 How to Navigate

Each project includes:

- Logs / artifacts
- Investigation reports
- Validation screenshots
- Demo videos (where applicable)

Start with **project READMEs or demo videos** for quick understanding.

---

## ⚠️ Disclaimer

All projects were performed in **controlled lab environments** for educational and security research purposes only.

---

## 🔗 Connect

LinkedIn:  
[https://www.linkedin.com/in/nithish-kumar-cyber](https://www.linkedin.com/in/nithish-kumar-cyber)