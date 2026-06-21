import subprocess

def run():

    print("\n[+] Checking Cron Jobs\n")

    subprocess.run(
        "crontab -l",
        shell=True
    )

    subprocess.run(
        "ls -la /etc/cron*",
        shell=True
    )
