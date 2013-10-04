# -*- coding: utf-8 -*-

"""
Commands to erase partitions.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013, Bryan Hundven <bryanhundven@gmail.com>'

from subprocess import call

def erase(partition):
    '''Erase a flash partition'''
    retval = 0
    print("\nRunning: fastboot erase " + partition)
    if call('fastboot' + ' erase ' + partition, shell=True) < 0:
        print("*** Erase command failed! ***")
	retval = 3
    return retval
