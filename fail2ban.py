import subprocess

def install_fail2ban():

    print("[+] Installing Fail2Ban")

    # Install package
    subprocess.run(["sudo", "apt", "install", "-y", "fail2ban"])

    # Enable service
    subprocess.run(["sudo", "systemctl", "enable", "fail2ban"])

    # Start service
    subprocess.run(["sudo", "systemctl", "start", "fail2ban"])

    print("[+] Fail2Ban installed and running")
