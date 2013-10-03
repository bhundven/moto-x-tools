from distutils.core import setup

setup(
    name='moto-x-tools',
    version='0.1.1',
    author='Bryan Hundven',
    author_email='bryanhundven@gmail.com',
    packages=['fastboot'],
    scripts=['bin/moto-x-flash'],
    url='https://github.com/bhundven/moto-x-tools',
    license='LICENSE.txt',
    description='Handy tools for your Motorola Moto X',
    long_description=open('README.txt').read(),
)
