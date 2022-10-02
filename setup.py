from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in first_app/__init__.py
from first_app import __version__ as version

setup(
	name="first_app",
	version=version,
	description="Trying all sorts of things",
	author="Gabishi",
	author_email="gabishi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
