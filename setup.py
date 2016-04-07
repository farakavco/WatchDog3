# -*- coding: utf-8 -*-

import os
import re
from setuptools import setup, find_packages

# reading package version (same way sqlalchemy does)
with open(os.path.join(os.path.dirname(__file__), 'watchdog3', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

requires = [
    'pymlconf',
    'requests',
    'grequests'
]


setup(
    name='watchdog3',
    version=package_version,
    description='Varzesh3 WatchDog',
    author='eteamin',
    author_email='aminetesamian1371@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'watchdog3 = watchdog3:main'
        ]
    },
    install_requires=requires,
    include_package_data=True,
)
