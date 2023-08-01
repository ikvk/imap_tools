import os
import re
import setuptools


def get_version(package: str) -> str:
    """Return package version as listed in __version__ variable at __init__.py"""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", init_py).group(1)


with open("README.rst", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='imap-tools',
    version=get_version('imap_tools'),
    packages=setuptools.find_packages(exclude=['tests']),
    url='https://github.com/ikvk/imap_tools',
    license='Apache-2.0',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='Vladimir Kaukin',
    author_email='KaukinVK@ya.ru',
    description='Work with email by IMAP',
    keywords=['imap', 'imap-client', 'python3', 'python', 'email'],
    package_data={"imap_tools": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    # install_requires=['typing>=3.6.2'],
)
