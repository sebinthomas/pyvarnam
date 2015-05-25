#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
from pyvarnam import __author__, __email__,  __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=  "pyvarnam",
    version= __version__,
    description= 'Pyvarnam provides python bindings for libvarnam',
    long_description= long_description,
    url= 'https://github.com/sebinthomas/pyvarnam',
    author= __author__,
    author_email= __email__,
    license= 'MIT',
    include_package_data=True,
    setup_requires=['setuptools-git'],
    packages=find_packages(exclude= 'tests'),
    install_requires= ['setuptools'],
    zip_safe= False
)
