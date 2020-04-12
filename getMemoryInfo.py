#!/usr/bin/python3
#Script that will return information about all system memory.

import re
import subprocess

#get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0].decode()
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode()

#Itetare procese
processLines = ps.split('\n')
sep = re.compile('[\s]+')
rssTotal = 0 # kB

for row in range(1, len(processLines)):
    rowText = processLines[row].strip()
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except:
        rss = 0 #ignora
    rssTotal += rss

#process vm_stat
vmLines = vm.split('\n')
sep = re.compile(':[\s]+')

vmStats = {}

for row in range(1, len(vmLines)-2):
    rowText = vmLines[row].split()
 
print ('Wired Memory:\t\t%d MB' & ( vmStats["Pages wired down"]/1024/1024 ))
print ('Active Memory:\t\t%d MB' % ( vmStats["Pages active"]/1024/1024 ))
print ('Inactive Meomory:\t\t%d MB' % ( vmStats["Pages inactive"]/1024/1024 ))
print ('Free Memory:\t\t%d MB ' % ( vmStats["Pages free"]/1024/1024 ))
print ('Total Memory (ps):\t%.3f MB' % ( rssTotal/1024/1024 ))
