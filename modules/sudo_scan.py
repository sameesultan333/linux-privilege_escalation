import subprocess

def run():

    print("\n[+] Checking Sudo Rules\n")

    subprocess.run(
        "sudo -l",
        shell=True
    )
