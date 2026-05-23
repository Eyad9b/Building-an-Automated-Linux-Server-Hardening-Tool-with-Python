import subprocess
import shutil

# Backup SSH configuration
def backup_ssh_config():

    # Source file
    source = "/etc/ssh/sshd_config"

    # Backup file
    backup = "/etc/ssh/sshd_config.bak"

    # Copy original config
    shutil.copy(source, backup)

    print("[+] SSH config backup created")

# Harden SSH settings
def harden_ssh():

    ssh_config = "/etc/ssh/sshd_config"

    # Read existing config
    with open(ssh_config, "r") as file:
        lines = file.readlines()

    new_lines = []

    # Loop through each line
    for line in lines:

        # Disable root login
        if line.startswith("PermitRootLogin"):
            new_lines.append("PermitRootLogin no\n")

        # Disable password login
        elif line.startswith("PasswordAuthentication"):
            new_lines.append("PasswordAuthentication no\n")

        # Limit authentication attempts
        elif line.startswith("MaxAuthTries"):
            new_lines.append("MaxAuthTries 3\n")

        else:
            new_lines.append(line)

    # Write new configuration
    with open(ssh_config, "w") as file:
        file.writelines(new_lines)

    print("[+] SSH configuration hardened")

    # Restart SSH service
    subprocess.run(["sudo", "systemctl", "restart", "ssh"])

    print("[+] SSH service restarted")
