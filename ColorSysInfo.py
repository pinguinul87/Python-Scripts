#!/usr/bin/python3
"""
Returns some system information like IP address, top 10 procs and disk space.

"""
import subprocess
import psutil
import os

class colors():
     red='\033[31m'
     green='\033[32m'
     END = '\033[0m'  #end of color


def uname_func():
    try:
        uname = "uname"
        uname_arg = "-a"
        print (f"{colors.green}[+] Gathering system information with {uname} command:\n{colors.END}")
        subprocess.call([uname, uname_arg])
        print("")
    except:
        print(f"{colors.red}[-] Error: {uname} not found{colors.END}")

def disk_func():
    try:
        diskspace = "df"
        diskspace_arg = "-h"
        print (f"{colors.green}[+] Gathering diskspace information {diskspace} command:\n{colors.END}") 
        subprocess.call([diskspace, diskspace_arg])
        print("")
    except:
        print(f"{colors.red}[-] Error: {diskspace} not found{colors.END}")

def tmp_space():
    try:
        tmp_usage = "du"
        tmp_arg = "-h"
        path = "/tmp"
        print (f"{colors.green}[+] Space used in /tmp directory:\n{colors.END}")
        subprocess.call([tmp_usage, tmp_arg, path])
        print("")
    except:
        print(f"{colors.red}[-] Error: {tmp_usage}  not found{colors.END}")

def ip_addr():
    try:
        print(f"{colors.green}[+] Ip address is:\n{colors.END}")
        os.system("ifconfig | grep inet | awk '{ print $1  $2 }'")
        print("")
    except:
        print(f"{colors.red}[-] Error: ifconfig not found{colors.END}")
        
def top_10_procs():
    for proc in psutil.process_iter():
        try:
            procName = proc.name()
            procID = proc.pid
            print(procName, ' ---> ', procID)
        except (psutil.NoSuchProcess, psutil.AccesssDenied, psutil.ZombieProcess):
            print(f"{colors.red}[-] System Error\n{colors.END}")


def main():
    uname_func()
    disk_func()
    tmp_space()
    ip_addr()
    top_10_procs()

main()
