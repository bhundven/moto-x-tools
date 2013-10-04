# -*- coding: utf-8 -*-

"""
Commands to get variables from the bootloader.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013, Bryan Hundven <bryanhundven@gmail.com>'

from subprocess import check_output, STDOUT

def getvar(variable):
    '''Return a dictionary from a single bootloader variable (don't use 'all')'''
    return dict([check_output(['fastboot', 'getvar', variable], stderr=STDOUT).split('\n')[0].replace(" ", "").split(":", 1),])
