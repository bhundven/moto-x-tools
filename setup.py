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
