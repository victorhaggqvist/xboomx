# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='xboomx',
    version='0.7.0',
    packages=['xboomx'],
    scripts=['xboomx/bin/xboomx_path.py',
             'xboomx/bin/xboomx_sort.py',
             'xboomx/bin/xboomx_update.py',
             'xboomx/bin/xboomx',
             'xboomx/bin/xboomx_python2mirgation.py'],
    license='GPL-2.0',
    long_description='A wrapper for most common occurrences in dmenu',
    install_requires=[],
    include_package_data=True,
    package_data={'shared': ["etc/config"]},
    author="Victor Häggqvist",
    author_email="victor@hggqvst.com",
    url="https://github.com/victorhaggqvist/xboomx",
)
