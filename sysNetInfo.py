#!/usr/local/bin/python3
#This script will output information regarding disk, network and processes 

import subprocess, ipaddress
from subprocess import Popen, PIPE

def df():
    df = "df"
    df_arg = "-h"
    print("disk free: ")
    subprocess.call([df, df_arg])
    print('done')


def netstat():
    netstat = "netstat"
    netstat_arg = "-rs"
    subprocess.call([netstat, netstat_arg])
    print('done')


def mynet():

    net = ipaddress.ip_network('192.168.1.0/24')  #add your network here in CIDR notation

    for i in net.hosts():
        i=str(i)
        toPing = Popen(['ping', '-c', '1', i], stdout=PIPE)
        output = toPing.communicate()[0]
        hostAlive = toPing.returncode
        if hostAlive == 0:
            print(i, "is alive")
        else:
            print(i, "is dead")

def proc_stuff():
    for i in ('/proc/*'):
        x = Popen(['lsof'], stdout=PIPE)       

def main():
    df()
    netstat()
    mynet()
    proc_stuff()

main()

