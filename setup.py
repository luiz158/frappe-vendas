# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='rg_vendas',
    version=version,
    description='Gerenciamento de venda de produtos',
    author='Regis da Silva',
    author_email='regis.santos.100@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
