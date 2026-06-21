import subprocess

def run():

    print("\n[+] Collecting System Information\n")

    subprocess.run("whoami", shell=True)
    subprocess.run("id", shell=True)
    subprocess.run("uname -a", shell=True)
    subprocess.run("cat /etc/os-release", shell=True)
