"""Setup file for the library"""
from setuptools import setup, find_packages


setup(
    name='testlibrary',
    version='0.1',
    description='This is a test for a tutorial on how to create a python library',  # noqa
    url='https://github.com/matotias/test-library',
    # download_url='https://github.com/comparaonline/etl-builder/archive/v1.3.4.tar.gz',  # noqa
    author='matotias',
    author_email='matotias@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
    ]
)
