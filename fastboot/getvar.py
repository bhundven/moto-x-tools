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
Commands to get variables from the bootloader.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013-2014, Bryan Hundven <bryanhundven@gmail.com>'

from subprocess import check_output, STDOUT

def getvar(variable):
    '''Return a dictionary from a single bootloader variable (don't use 'all')'''
    return dict([check_output(['fastboot', 'getvar', variable], stderr=STDOUT).split('\n')[0].replace(" ", "").split(":", 1),])
