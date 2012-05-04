#!/usr/bin/env python
from setuptools import setup

requires = [
    'Django==1.4',
    'psycopg2==2.4.5',
]

setup(
    name='Django Multiple Enviroment Example',
    version='1.0',
    description='Mini app exploring an application working across multiple databases',
    author='Greg Reinbach',
    author_email='greg@reinbach.com',
    url='https://github.com/reinbach/django-multienv',
    install_requires=requires,
)