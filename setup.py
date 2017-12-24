#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages
setup(name='dcurooms',
      version='1.0.0',
      description='Shows room information around the DCU campus',
      author='theycallmemac',
      url='https://github.com/theycallmemac/dcuroomsi',
      license = 'GPL-3.0',
      scripts=['scripts/dcurooms', 'scripts/dcurooms.py'],
      install_requires=[
          'MechanicalSoup', 'bs4', 'requests'
      ],
      classifiers=[
            'Environment :: Console',
            'Natural Language :: English',
            'License :: GPL-3.0 License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
])
