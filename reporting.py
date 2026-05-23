import subprocess
from datetime import datetime

# -----------------------------
# Generate Full Security Report
# -----------------------------
def generate_report():

    print("\n==============================")
    print("   LINUX SECURITY REPORT")
    print("==============================\n")

    print(f"Generated at: {datetime.now()}\n")

    # ---------------- OPEN PORTS ----------------
    print("[1] Open Ports:\n")
    subprocess.run(["ss", "-tulnp"])

    # ---------------- FAILED LOGINS ----------------
    print("\n[2] Failed Login Attempts:\n")
    subprocess.run([
        "journalctl",
        "-u", "ssh",
        "--no-pager"
    ])

    # ---------------- RUNNING SERVICES ----------------
    print("\n[3] Running Services:\n")
    subprocess.run([
        "systemctl",
        "list-units",
        "--type=service",
        "--state=running"
    ])

    print("\n==============================")
    print("     END OF REPORT")
    print("==============================\n")
