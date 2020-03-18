#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='python-sample-package-with-data',
    version='0.0.3',
    description='My short description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cirosantilli/python-sample-package-with-data',
    author='Ciro Santilli',
    author_email='ciro.santilli.contact@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    scripts=['python-sample-package-with-data'],
)
