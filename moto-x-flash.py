#!/usr/bin/env python
# moto-x-flash.py - a script to read moto-x firmware xml files to run fastboot
# for you.
#
# Copyright (C) 2013 Bryan Hundven <bryanhundven@gmail.com>
# 
# This file is released under the GPLv2.

import os, sys
import xml.etree.ElementTree as ET
import hashlib as HL
from subprocess import call

# TODO: This code should be functionalized. I did this as a quick hack, but should work properly.
# Tested on:
#     AT&T XT1058 - 16G.

firmware_xml = sys.argv[1]
fail = 0

tree = ET.parse(firmware_xml)
root = tree.getroot()

for i in root.iter('step'):
    # Skip getvar operations.
    if i.get('operation') == 'getvar':
        continue
    elif i.get('operation') == 'flash':
        MD5 = i.get('MD5').lower()
        f2flsh = i.get('filename')
        part = i.get('partition')
        f2flshMD5 = HL.md5(open(f2flsh).read()).hexdigest()
        if f2flshMD5 != MD5:
            print("MD5 Checksum for " + f2flsh + " did not match!")
            print("MD5SUM in the xml file:      " + MD5)
            print("MD5SUM calculated from file: " + f2flshMD5)
            fail = 1
            break
        print("Running: fastboot flash " + part + " " + f2flsh)
        if call('fastboot' + ' flash ' + part + ' ' + f2flsh, shell=True) < 0:
            print("Command failed!")
            fail = 1
            break
    elif i.get('operation') == 'erase':
        part = i.get('partition')
        print("Running: fastboot erase " + part)
        if call('fastboot' + ' erase ' + part, shell=True) < 0:
            print("Command failed!")
            fail = 1
            break
    elif i.get('operation') == 'oem':
        var = i.get('var')
        print("Running: fastboot oem " + var)
        if call('fastboot' + ' oem ' + var, shell=True) < 0:
            print("Command failed!")
            fail = 1
            break

if fail == 1:
    print("Something bad happened!")
    sys.exit(1)
else:
    print("Flashing was successful!")
    sys.exit(0)
