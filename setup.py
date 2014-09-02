# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='xboomx',
    version='0.60',
    packages=['xboomx'],
    scripts=['xboomx/bin/xboomx_path.py',
             'xboomx/bin/xboomx_sort.py',
             'xboomx/bin/xboomx_update.py',
             'xboomx/bin/xboomx_urls.py',
             'xboomx/bin/web_xboomx',
             'xboomx/bin/xboomx'],
    license='GPLv2',
    long_description='wrapper for most common occurences in dmenu',
    install_requires=[],
    include_package_data=True,
    package_data={'shared': ["etc/config"]},
    author="Victor Häggqvist",
    author_email="victor@hggqvst.com",
    url="https://github.com/victorhaggqvist/xboomx",
)
