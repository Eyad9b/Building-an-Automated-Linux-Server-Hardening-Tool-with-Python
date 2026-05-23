# Building-an-Automated-Linux-Server-Hardening-Tool-with-Python

<img src="architecture diagram.png">


The main goal of this project is to automate Linux server security hardening and auditing tasks
# 🔒 Security Tool Features

## SSH Hardening
- Disables root login  
- Enforces key‑based authentication  
- Limits login attempts  

## Firewall Automation
- Configures firewall rules using **UFW**  
- Allows only essential ports (SSH, HTTP, HTTPS)  
- Blocks all unnecessary incoming traffic by default  

## Brute‑Force Protection
- Integrates **Fail2Ban** intrusion prevention  
- Detects and blocks repeated unauthorized login attempts  

## Auditing
- Lists open ports  
- Shows running services  
- Analyzes failed login attempts from system logs  

## Security Report Generator
Generates a full system report including:
- Open network ports  
- Authentication logs  
- Active services  



