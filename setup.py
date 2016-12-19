#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import ast
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('markdownclerk/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

setup(
    name='markdownclerk',
    version=version,
    author='John P. Neumann',
    description='A simple markdown project tracking generator.',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    license="MIT license",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'markdownclerk': ['templates/*']},
    zip_safe=False,
    platforms='any',
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'Click',
        'Jinja2',
        'boltons',
        'pyyaml',
    ],
    tests_require=[
        'mock',
        'pytest',
        'pytest-cov',
    ],
    entry_points={
        'console_scripts': [
            'clerk = markdownclerk.cmds.cli:markdownclerk'
        ]
    }
)
