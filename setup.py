# !/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(name='dcurooms',
      version='1.0.0',
      description='Shows room information around the DCU campus',
      author='theycallmemac',
      url='https://github.com/theycallmemac/dcurooms',
      license='GPL-3.0',
      scripts=['scripts/dcurooms', 'scripts/index.py', 'scripts/controls.py', 'scripts/builders.py', 'scripts/checks.py'],
      install_requires=[
          'MechanicalSoup', 'bs4', 'requests'
      ],
      classifiers=[
            'Environment :: Console',
            'Natural Language :: English',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'])

