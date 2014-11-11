#!/usr/bin/env python
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

from distutils.core import setup

setup(
    name='pyfastboot',
    version='0.0.1',
    author='Bryan Hundven',
    author_email='bryanhundven@gmail.com',
    packages=['fastboot'],
    url='https://github.com/bhundven/pyfastboot',
    license='GPLv2+',
    description='A python wrapper for fastboot',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Plugins',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: System :: Recovery Tools',
        'Topic :: Utilities',
    ],
)
