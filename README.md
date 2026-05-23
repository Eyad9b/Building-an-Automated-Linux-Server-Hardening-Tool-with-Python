# Building-an-Automated-Linux-Server-Hardening-Tool-with-Python
The main goal of this project is to automate Linux server security hardening and auditing tasks

![Firewall Diagram][(https://raw.githubusercontent.com/username/repo/main/images/firewall.png](https://github.com/Eyad9b/Building-an-Automated-Linux-Server-Hardening-Tool-with-Python/blob/204b98b36abcfc508fed1774d917300b5ab0e50b/architecture%20diagram.png
))

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



