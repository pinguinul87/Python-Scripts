#!/usr/bin/python3
"""
This script will return info from a given domanin.
Will return the location, city, country and IP address beased on the data stored on ipinfo.io
"""

import sys
import json
import socket
import pprint
import requests

#How to use the script
if len(sys.argv) < 2:
    print("Use script like this: " + sys.argv[0] + "URL")
    sys.exit(1)

#Make request and print http header info
rqst_one = requests.get("https://"+sys.argv[1])
print("\n"+pprint.pprint(str(rqst_one.headers)))

#Get IP address
getIP = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+getIP + "\n")

rqst_two = requests.get("https://ipinfo.io/"+getIP +"/json")
resp = json.loads(rqst_two.text)
pprint.pprint(resp)

#List information regarding domain location
print("The city is : "    + resp["city"])
print("The country is : " + resp["country"])
print("The region is : "  + resp["region"])
print("The location is : "+ resp["loc"])


