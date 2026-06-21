import subprocess

def run():

    print("\n[+] Checking Linux Capabilities\n")

    subprocess.run(
        "getcap -r / 2>/dev/null",
        shell=True
    )
