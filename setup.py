try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A library to use tinder in python',
	'author': 'Tom Koker',
	'url': 'https://github.com/tomkoker/tinder',
	'download_url': 'Download Url',
	'author_email': 'me@tomkoker.com',
	'version': '0.1',
	'install_requires': ['requests'],
	'packages': ['tinder'],
	'scripts': [],
	'name': 'tinder'
}

setup(**config)