from modules import system_info
from modules import suid_scan
from modules import permission_scan
from modules import sudo_scan
from modules import cron_scan
from modules import service_scan
from modules import capability_scan
from modules import kernel_scan

print("=" * 60)
print("LINUX PRIVILEGE ESCALATION AUTOMATION TOOLKIT")
print("=" * 60)

system_info.run()
suid_scan.run()
permission_scan.run()
sudo_scan.run()
cron_scan.run()
service_scan.run()
capability_scan.run()
kernel_scan.run()

print("\nScan Completed")
