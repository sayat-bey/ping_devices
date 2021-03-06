import subprocess
import yaml
from datetime import datetime


with open("devices.yaml", "r") as file:
    devices = yaml.load(file, yaml.SafeLoader)  # hostname : ip

print("-------------------------------------------------------------------------------------------------------")

try:
    i = 1
    while True:
        output = []
        for hostname, ip in devices.items():
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            result = subprocess.run(["ping", "-c", "2", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)             
            if result.returncode == 0:
                print(f'\r[PING OK],    timestamp: {current_time}, {hostname:22} cycle: {i}', end='')
            else:
                print(f'\n[PING ERROR], timestamp: {current_time}, {hostname:22} cycle: {i}')
        i += 1

except KeyboardInterrupt:
    print("\n")
    print("-------------------------------------------------------------------------------------------------------")
    print("script cancelled")
