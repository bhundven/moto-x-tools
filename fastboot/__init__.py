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
Python Fastboot frontend.

This library contains fastboot commands used to manage your android device that uses a fastboot bootloader.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013-2014, Bryan Hundven <bryanhundven@gmail.com>'
__version__ = (0, 0, 1)

__all__ = ['flash', 'erase', 'getvar', 'oem', 'reboot']

# flash
try:
    from . import flash
    from flash import *
except ImportError:
    pass

# erase
try:
    from . import erase
    from erase import *
except ImportError:
    pass

# getvar
try:
    from . import getvar
    from getvar import *
except ImportError:
    pass

# oem
try:
    from . import oem
    from oem import *
except ImportError:
    pass

# reboot
try:
    from . import reboot
    from reboot import *
except ImportError:
    pass
