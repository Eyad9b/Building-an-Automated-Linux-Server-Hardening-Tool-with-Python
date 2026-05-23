import subprocess

# Configure firewall rules
def configure_firewall():

    print("[+] Configuring firewall...")

    # Allow SSH
    subprocess.run(["sudo", "ufw", "allow", "22"])

    # Allow HTTP
    subprocess.run(["sudo", "ufw", "allow", "80"])

    # Allow HTTPS
    subprocess.run(["sudo", "ufw", "allow", "443"])

    # Deny all incoming traffic by default
    subprocess.run(["sudo", "ufw", "default", "deny", "incoming"])

    # Enable firewall
    subprocess.run(["sudo", "ufw", "--force", "enable"])

    print("[+] Firewall configured successfully")
