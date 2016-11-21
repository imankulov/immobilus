#!/usr/bin/env python

from setuptools import setup

setup(
    name='immobilus',
    version='0.1.0',
    description='Say `Immobilus!` to freeze your tests',
    author='Eugene Pokidov',
    author_email='pokidovea@gmail',
    url='https://github.com/pokidovea/immobilus',
    packages=['.'],
    install_requires=['python-dateutil'],
    include_package_data=True,
    license='Apache 2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
