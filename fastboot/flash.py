# -*- coding: utf-8 -*-

"""
Commands to flash partitions.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013, Bryan Hundven <bryanhundven@gmail.com>'

from subprocess import call

def flash(filename, partition):
    '''Flash a file to a partition'''
    retval = 0
    print("\nRunning: fastboot flash " + partition + " " + filename)
    if call('fastboot' + ' flash ' + partition + " " + filename, shell=True) < 0:
        print("*** Flash command failed! ***")
	retval = 1
    return retval
