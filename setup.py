#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Jinja2==2.9.5',
    'xmltodict==0.10.2',
    'requests==2.18.4'

]

setup_requirements = []

test_requirements = []

setup(
    name='pylleida',
    version='0.4.0',
    description="A HTTP Python client to use the Lleida.net API",
    long_description=readme + '\n\n' + history,
    author="Nick M. Jaremek",
    author_email='nick13jaremek@gmail.com',
    url='https://github.com/reclamador/pylleida',
    packages=find_packages(include=['pylleida', 'pylleida.*']),
    package_data={'pylleida': ['templates/*']},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pylleida',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
