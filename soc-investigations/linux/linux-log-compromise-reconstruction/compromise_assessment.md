## Compromise Assessment

**Was the system compromised:**  
Yes

**Initial access method:**  
SSH brute-force attack resulting in successful login to the root account

**Attacker IP:**  
185.143.223.15 (external)

**Privilege escalation observed:**  
No — attacker gained direct root access without requiring escalation

**Persistence mechanism:**  
Suspicious cron job executing `/tmp/backup.sh` at regular intervals, continuing after session termination

**Evidence summary:**  
Multiple failed SSH login attempts targeting the root account were observed, followed by a successful authentication from an external IP address (185.143.223.15). The attacker established a root session and executed commands, including spawning an interactive shell. A cron job executing a script from the `/tmp` directory was identified both during and after the session, indicating an automated persistence mechanism.