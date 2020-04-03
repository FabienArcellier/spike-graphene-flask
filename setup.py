#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='graphene_spike',
    version='1.0.0',
    packages=find_packages(exclude=["*_tests"]),
    license='MIT license',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points = {
        'console_scripts': [
            'graphene_spike = graphene_spike.cli:cli',
        ],
    },
    install_requires = [
        'click',
        'decorator',
        'graphene'
    ],
    extras_require={
        'dev': [
            'pylint',
            'coverage',
            'tox',
            'twine'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Environment :: Console"
    ]
)
