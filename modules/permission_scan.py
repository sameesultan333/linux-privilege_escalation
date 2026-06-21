import subprocess

def run():

    print("\n[+] Scanning World Writable Files\n")

    subprocess.run(
        "find / -type f -perm -0002 2>/dev/null",
        shell=True
    )

    print("\n[+] Scanning World Writable Directories\n")

    subprocess.run(
        "find / -type d -perm -0002 2>/dev/null",
        shell=True
    )
