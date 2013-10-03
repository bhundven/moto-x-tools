# -*- coding: utf-8 -*-

"""
Python Fastboot frontend.

This library contains fastboot commands used to manage your android device that uses a fastboot bootloader.
"""

__author__ = 'Bryan Hundven'
__maintainer__ = 'Bryan Hundven'
__email__ = 'bryanhundven@gmail.com'
__copyright__ = 'Copyright (C) 2013, Bryan Hundven <bryanhundven@gmail.com>'
__version__ = (0, 1, 1)

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
