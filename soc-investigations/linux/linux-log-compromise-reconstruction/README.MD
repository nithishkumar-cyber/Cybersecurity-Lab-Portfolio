# Linux Log Compromise Reconstruction Lab (SOC Simulation)

## 📌 Overview

This project simulates a real-world SOC L1 investigation involving noisy Linux logs, brute force attacks, and persistence mechanisms.

The objective was to reconstruct a complete attacker timeline and determine whether a system compromise occurred.

---

## 🎯 Objectives

* Detect brute force SSH attacks
* Identify successful unauthorized access
* Analyze privilege context
* Detect persistence mechanisms (cron-based)
* Reconstruct attacker timeline
* Produce a professional SOC incident report

---

## 🛠 Tools Used

* grep
* awk
* less
* cat

(No SIEM tools used — manual analysis only)

---

## 🔍 Key Findings

* External attacker (185.143.223.15) performed SSH brute force
* Successfully gained root access
* Executed shell commands
* Established persistence using `/tmp/backup.sh` via cron
* Persistence continued after attacker session ended

---

## 🧠 Skills Demonstrated

* Log analysis (auth.log, syslog)
* Multi-log correlation
* False positive elimination
* Attack chain reconstruction
* Incident reporting

---

## 📁 Provided Log Evidence

The following log dataset was used to reconstruct the attacker timeline:

* `artifacts/provided_logs.log` — contains simulated Linux authentication and cron events

> ⚠️ Note: This is a lab-provided, fully sanitized dataset. All investigation and screenshots are derived from this file.

---

## 📄 Full Incident Report

A complete timeline-based investigation report is available here:

[View Incident Report](./soc_incident_report.md)

---

## 📄 Deliverables

* `attack_timeline.md`
* `compromise_assessment.md`
* `soc_incident_report.md`
* `artifacts/provided_logs.log`

---

## 🚨 Key Insight

The attacker did not escalate privileges — they directly compromised the root account, making detection more critical and dangerous.

---

## 📈 Outcome

This project simulates real SOC investigation conditions and demonstrates readiness for SOC L1 analyst roles.
