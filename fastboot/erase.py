# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014 Bryan Hundven
#
# This file is part of pyfastboot.
#
# pyfastboot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfastboot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfastboot.  If not, see <http://www.gnu.org/licenses/>.

"""
Commands to erase partitions.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013-2014, Bryan Hundven <bryanhundven@gmail.com>'

from subprocess import call

def erase(partition):
    '''Erase a flash partition'''
    retval = 0
    print("\nRunning: fastboot erase " + partition)
    if call('fastboot' + ' erase ' + partition, shell=True) < 0:
        print("*** Erase command failed! ***")
	retval = 3
    return retval
