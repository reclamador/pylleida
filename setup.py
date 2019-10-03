#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Jinja2==2.9.5',
    'xmltodict==0.10.2',
    'requests==2.20.0'

]

setup_requirements = []

test_requirements = []

setup(
    name='pylleida',
    version='0.2.1',
    description="A HTTP Python client to use the Lleida.net API",
    long_description=readme + '\n\n' + history,
    author="Nick M. Jaremek",
    author_email='nick13jaremek@gmail.com',
    url='https://github.com/reclamador/pylleida',
    packages=[
        'pylleida'
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pylleida',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
