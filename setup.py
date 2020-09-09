#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from setuptools import setup, find_packages


def get_requires():
    def _filter(requires):
        return [req.strip() for req in requires if req.strip()]

    filename = "requirements.txt" if sys.version_info.major >= 3 \
                                  else "requirements27.txt"

    with open(filename, "r") as fh:
        return _filter(fh.readlines())


with open("README.md") as fh:
    long_description = fh.read()


setup(
    name='osc-tiny',
    version='0.2.4',
    description='Client API for openSUSE BuildService',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Andreas Hasenkopf',
    author_email='ahasenkopf@suse.com',
    url='http://github.com/crazyscientist/osc-tiny',
    download_url='http://github.com/crazyscientist/osc-tiny/tarball/master',
    packages=find_packages(),
    license='MIT',
    install_requires=get_requires(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ]
)
