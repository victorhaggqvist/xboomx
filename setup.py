from setuptools import setup


setup(
    name='xboomx',
    version='0.50',
    packages=['xboomx'],
    scripts=['xboomx/bin/xboomx_path.py',
             'xboomx/bin/xboomx_sort.py',
             'xboomx/bin/xboomx_update.py',
             'xboomx/bin/xboomx_urls.py',
             'xboomx/bin/web_xboomx',
             'xboomx/bin/xboomx'],
    license='BSD',
    long_description='wrapper for most common occurences in dmenu',
    install_requires=[],
    include_package_data=True,
    package_data={'shared': ["etc/config"]},
    author="Yuriy Netesov",
    author_email="retnuhed@gmail.com",
    url="https://bitbucket.org/dehun/xboomx/",
)
