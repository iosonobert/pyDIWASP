#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

		
setup(name='crude_readers',
      version='1.0.0',
      description='Python version of DIWASP',
      author='123',
      author_email='123@gxyz.com',
      #packages=['crude_readers'],
      packages=find_packages(),
      install_requires=['numpy','scipy','matplotlib','gsw','netcdf4','xarray'],
      license='see metocean/DIWASP',
      include_package_data=True,
      distclass=BinaryDistribution,
    )
