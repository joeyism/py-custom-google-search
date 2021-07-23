from setuptools import find_packages, setup
import re

PACKAGE_NAME = "custom-google-search"
PACKAGE_NAME_UNDERLINE = PACKAGE_NAME.replace("-", "_")

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open(f'{PACKAGE_NAME_UNDERLINE}/__init__.py').read(),
    re.M
    ).group(1)

setup(
    name=PACKAGE_NAME,
    packages=find_packages(exclude=["tests"]),
    version=version,
    description='Performs custom google search programmatically',
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    author='joeyism',
    url='https://github.com/joeyism/py-custom-google-search',
    download_url='https://github.com/joeyism/py-custom-google-search/archive/{}.tar.gz'.format(version),
    install_requires=[package for package in open("requirements.txt").read().split("\n")],
    keywords=["custom", "google", "search", "image", "api", "program"],
    entry_points={},
    package_data={"": ["*.txt", "*.cfg"]},
    include_package_data=True,
)
