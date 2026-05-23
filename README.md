# Building-an-Automated-Linux-Server-Hardening-Tool-with-Python
The main goal of this project is to automate Linux server security hardening and auditing tasks

Features
SSH hardening- The tool automatically secures SSH by:
Disabling root login
Enforcing key-based authentication
Limiting login attempts

Firewall automation- It configures system firewall rules using UFW: 
Allows only essential ports (SSH, HTTP, HTTPS)
Blocks all unnecessary incoming traffic by default

Brute-force protection- Integrates Fail2Ban (intrusion prevention framework for Linux) to detect and block repeated unauthorized login attempts

Auditing- The system can:
List open ports
Show running services
Analyze failed login attempts from system logs

Security Report Generator- One of the most important features is the ability to generate a full system report including:
Open network ports
Authentication logs
Active services

