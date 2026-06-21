import subprocess

def run():

    print("\n[+] Checking Services\n")

    subprocess.run(
        "systemctl list-unit-files --type=service",
        shell=True
    )
