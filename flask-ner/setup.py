from distutils.core import setup

from setuptools import find_packages

setup(name='flaskner',
      version='0.0.1',
      description='A simple NER API',
      packages=find_packages(where='src'),
      package_dir={'': 'src'})
