# SOC INCIDENT REPORT

## Alert Summary

Suspicious SSH activity detected involving multiple failed login attempts followed by a successful root login from external IP **185.143.223.15**. Post-compromise, persistent cron-based execution of a script in `/tmp` was observed.

---

## Investigation Process

- Analyzed authentication logs to identify brute-force patterns and successful login events
- Correlated SSH session activity with command execution (including shell access)
- Reviewed cron logs to detect persistence mechanisms
- Filtered benign system activity (APT processes, systemd events, internal user access)
- Reconstructed attacker behavior through timeline analysis

---

## Evidence Identified

- Multiple failed SSH login attempts targeting the root account from external IP **185.143.223.15**
- Successful root login from the same IP, confirming brute-force success
- Interactive shell execution (`/bin/bash`) post-authentication
- Suspicious cron job executing `/tmp/backup.sh` from a non-standard directory
- Cron execution persisted after attacker session termination, confirming persistence

---

## Attack Timeline

Brute-force attempts → Successful root login → Interactive shell access → Cron-based persistence → Continued execution post-session  
_(Detailed timeline documented separately)_

---

## Impact Assessment

- Unauthorized root-level access achieved from an external source
- Full system compromise confirmed
- No privilege escalation required (direct root access obtained)
- Persistence established via cron job executing script from `/tmp`
- Ongoing risk due to automated execution after attacker exit

**Severity: CRITICAL**

---

## Recommended Response

### Immediate Actions

- Isolate affected system from the network
- Terminate active sessions
- Remove malicious cron entries and `/tmp/backup.sh`

### Containment

- Block attacker IP **185.143.223.15**
- Reset all credentials, especially privileged accounts

### Recovery

- Rebuild system from a trusted backup (preferred) or perform full integrity validation
- Verify system files and configurations

### Post-Incident Hardening

- Disable direct root SSH login
- Enforce SSH key-based authentication
- Deploy brute-force protection (e.g., Fail2Ban)
- Centralize logging and enable continuous monitoring

---

## Conclusion

The system was fully compromised via an SSH brute-force attack targeting the root account. The attacker established persistence using a cron-based mechanism and terminated the session while maintaining ongoing execution capability through a malicious script.