import subprocess
import shutil

# -----------------------------
# Check open ports
# -----------------------------
def check_ports():

    print("\n[+] Open Ports:\n")

    subprocess.run(["ss", "-tulnp"])

# -----------------------------
# Check failed logins
# -----------------------------
def failed_logins():

    print("\n[+] Failed Login Attempts:\n")

    # safer fallback instead of lastb
    if shutil.which("lastb"):
        subprocess.run(["lastb"])
    else:
        subprocess.run([
            "journalctl",
            "-u", "ssh",
            "--no-pager"
        ])

# -----------------------------
# Check running services
# -----------------------------
def running_services():

    print("\n[+] Running Services:\n")

    subprocess.run([
        "systemctl",
        "list-units",
        "--type=service",
        "--state=running"
    ])
