## ATTACK TIMELINE

| Timestamp       | Event                                      | Suspicion Level | Explanation |
|----------------|-------------------------------------------|-----------------|------------|
| Jun 10 10:01:22 | Failed root login from 185.143.223.15     | Medium          | Initial brute-force attempt from external IP |
| Jun 10 10:01:25 | Failed root login from 185.143.223.15     | Medium          | Continued rapid authentication attempts |
| Jun 10 10:01:29 | Failed root login from 185.143.223.15     | Medium          | Repeated failures confirm credential guessing pattern |
| Jun 10 10:02:10 | Successful root login from 185.143.223.15 | **Critical**    | Brute-force attack succeeded → unauthorized root access |
| Jun 10 10:02:12 | SSH session opened for root               | High            | Attacker gained interactive access |
| Jun 10 10:05:03 | Execution of `/bin/bash`                  | High            | Interactive shell spawned by attacker |
| Jun 10 10:06:40 | Cron execution of `/tmp/backup.sh`        | **Critical**    | Suspicious script in non-standard directory indicates persistence |
| Jun 10 10:08:10 | SSH session closed for root               | Medium          | Attacker terminated session after establishing persistence |
| Jun 10 10:15:33 | Cron execution of `/tmp/backup.sh`        | **Critical**    | Persistence mechanism active post-session |
| Jun 10 10:35:11 | Cron execution of `/tmp/backup.sh`        | **Critical**    | Repeated execution confirms automated persistence |