# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:52:38 2015

@author: FB
"""

from setuptools import setup, find_packages


setup(name='encrypt',
      version='0.0.8',
      description='python utility for encrypting files',
      author='Freddy Bihozagara',  
      author_email='support@imenasoftware.com',
      url='http://imenasoftware.wordpress.com/encrypt/',
      packages=['bin'],
      install_requires=[
          "python >= 2.7",
          ],
      long_description='README.rst',
      license='MIT',      
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        
    ],
      platforms='linux, Mac, Windows',
      )