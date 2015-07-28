# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

url="https://github.com/OctavianLee/Bauhinia"
VERSION = "0.0.1"

setup(
    name="bauhinia",
    version=VERSION,
    license='MIT',
    description="The data structures implemented by Python.",
    author="Octavian Lee",
    author_email="octavianlee1@gmail.com",
    url = url,
    packages=find_packages('bauhinia'),
    package_dir = {'': 'bauhinia'}
)
