#!/usr/bin/env python3

import os
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as _test


class test(_test):
    def finalize_options(self):
        _test.finalize_options(self)
        self.test_args.insert(0, 'discover')

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

def version():
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", read("src/kaptos/_version.py"), re.M)
    if not match:
        raise RuntimeError("failed to parse version")
    return match.group(1)

install_requires = [
    "appdirs==1.4.3",
    "toml==0.10.0",
]

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.7",
    "Topic :: Communications :: Ham Radio"
]

setup(
    name = "kaptos",
    version = version(),
    description = "Distributed radio direction finding service.",
    long_description = read("README.md"),
    long_description_content_type = "text/markdown",
    author = "Paul Bryan",
    author_email = "pbryan@anode.ca",
    classifiers = classifiers,
    url = "https://kaptos.org/",
    packages = find_packages("src"),
    package_dir = {"": "src"},
    python_requires = ">= 3.7",
    install_requires = install_requires,
    keywords = "amateur radio direction finding",
    test_suite = "tests",
    cmdclass = {"test": test}
)
