from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-dataforjapan',
    version=version,
    description="the ckan extension package for Data for Japan",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Fumihiro Kato',
    author_email='fumi@fumi.me',
    url='http://dataforjapan.org',
    license='Affero GNU',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.dataforjapan'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.dataforjapan.plugin:PluginClass
        dataforjapan_theme=ckanext.dataforjapan.plugin:DataForJapanThemePlugin
    ''',
)
