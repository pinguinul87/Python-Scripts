#!/usr/bin/env python
#Script that will return system information.

import os
import platform

print (os.name)
print(platform.machine())
print(platform.version())
print(platform.platform())
print(platform.uname())
print(platform.system())
print(platform.processor())
print(platform.node())

#processor
print("Processors: ")
with open("/proc/cpuinfo", "r") as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]

for index, item in enumerate(cpuinfo):
    print("   " + str(index) + ": " + item)

#memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("   " + lines[0].strip())
print("   " + lines[1].strip())

#average load
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())

#uptime
uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()

uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

print("Private IP: ")
os.system("ifconfig | grep inet")
print("Public IP: ")
os.system("nslookup myip.opendns.com resolver1.opendns.com")
