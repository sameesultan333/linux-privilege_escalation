import subprocess

def run():

    print("\n[+] Kernel Information\n")

    subprocess.run(
        "uname -a",
        shell=True
    )

    print("\nRecommendation:")
    print("Check kernel version against public CVE databases.")
