import subprocess

def run():

    print("\n[+] Scanning SUID Binaries\n")

    subprocess.run(
        "find / -perm -4000 2>/dev/null",
        shell=True
    )
