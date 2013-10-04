# -*- coding: utf-8 -*-

"""
Commands to send oem commands to the bootloader.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013, Bryan Hundven <bryanhundven@gmail.com>'

from subprocess import call

def oem(command):
    '''Run oem command'''
    retval = 0
    print("\nRunning: fastboot oem " + command)
    if call('fastboot' + ' oem ' + command, shell=True) < 0:
        print("*** oem command failed! ***")
	retval = 4
    return retval
