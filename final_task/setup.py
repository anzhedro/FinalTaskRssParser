from setuptools import setup

setup(
    name='rss-reader',
    version='v2.0',
    packages=['rss_reader'],
    license="LICENSE.txt",
    install_requires=['feedparser', 'bs4'],
    url='',
    author='Evgeny Androsik',
    author_email='androsikei95@gmail.com',
    description='RSS Reader',
    entry_points={'console_scripts': ['rss-reader = rss_reader.rss_reader:main']}
)