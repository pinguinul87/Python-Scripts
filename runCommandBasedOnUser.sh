#!/bin/bash
: '
This script will run a given command via the command line as the first argument, based on the privileges of a given user.
Useage : ./runCommandBasedOnUser.sh root ls -l
'

uid=$(cat /etc/passwd | grep $1 | cut -d : -f 3)
cmd=$2
 
find . -user $uid -exec $cmd {} \;
 
