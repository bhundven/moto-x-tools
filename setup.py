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
    license='LICENSE.txt',
    description='A python wrapper for fastboot',
    long_description=open('README.rst').read(),
)
