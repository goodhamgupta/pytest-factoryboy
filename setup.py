#!/usr/bin/env python
"""pytest-factoryboy package config."""

import codecs
import os
import re
from setuptools import setup

dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, "README.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "AUTHORS.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "CHANGES.rst"), encoding="utf-8").read()
)

with codecs.open(os.path.join(dirname, 'pytest_factoryboy', '__init__.py'), encoding='utf-8') as fd:
    VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(fd.read()).group(1)

setup(
    name="pytest-factoryboy",
    description="Factory Boy support for pytest.",
    long_description=long_description,
    author="Oleg Pidsadnyi, Anatoly Bubenkov and others",
    license="MIT license",
    author_email="oleg.pidsadnyi@gmail.com",
    url="https://github.com/pytest-dev/pytest-factoryboy",
    version=VERSION,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "inflection",
        "factory_boy>=2.10.0",
        "pytest>=4.3",
        'funcsigs;python_version<"3.0"',
    ],
    # the following makes a plugin available to py.test
    entry_points={
        "pytest11": [
            "pytest-factoryboy = pytest_factoryboy.plugin",
        ],
    },
    tests_require=["tox"],
    packages=["pytest_factoryboy"],
    include_package_data=True,
)
