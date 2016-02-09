#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


long_description = (
    'A way to generate a markdown file with daily goals over a configurable '
    'amount weeks to help track projects.'
)


setup(
    name='markdownclerk',
    version='0.1.0',
    author='johnpneumann',
    author_email='john.p.neumann@gmail.com',
    url='https://github.com/johnpneumann/MarkdownClerk',
    download_url='https://github.com/johnpneumann/MarkdownClerk/tarball/0.1',
    description='A simple project goal generator.',
    long_description=long_description,
    license='MIT',
    keywords='markdown goal list',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=[
        'markdownclerk'
    ],
    install_requires=[
        'click',
        'Jinja2',
        'boltons',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'clerk = markdownclerk.clerk:main',
        ],
    },
)
