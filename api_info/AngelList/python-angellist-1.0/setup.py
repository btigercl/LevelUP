#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name        = 'python-angellist',
    version     = "1.0",
    license     = "MIT",
    author      = "Sandeep Bhaskar",
    author_email= 'sandeep.bhaskar19@gmail.com',
    url         = 'https://github.com/sandeepbhaskar/python-angellist',
    packages    = ['angellist'],
    description = 'Light wrapper around AngelList API',
)