#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages
setup(name='dcurooms',
      version='0.1.0',
      description='Shows room information around the DCU campus',
      author='theycallmemac',
      url='',
      license = 'GPL-3.0',
      scripts=['scripts/dcurooms'],
      install_requires=[
          'mechanize', 'bs4', 'requests'
      ],
      classifiers=[
            'Environment :: Console',
            'Natural Language :: English',
            'License :: GPL-3.0 License',
            'Operating System :: OS Independent',
            'Programming Language :: Python'
])
