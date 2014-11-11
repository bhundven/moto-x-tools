# -*- coding: utf-8 -*-

"""
Commands to reboot from the bootloader.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013-2014, Bryan Hundven <bryanhundven@gmail.com>'

from subprocess import call

def reboot():
    '''Reboot the connected device'''
    retval = 0
    print("\nRunning: fastboot reboot")
    if call('fastboot' + ' reboot', shell=True) < 0:
        print("*** Reboot command failed! ***")
	retval = 4
    return retval

def reboot_bootloader():
    '''Reboot the connected device back into fastboot'''
    retval = 0
    print("\nRunning: fastboot reboot-bootloader")
    if call('fastboot' + ' reboot-bootloader', shell=True) < 0:
        print("*** Reboot-bootloader command failed! ***")
        retval = 4
    return retval
