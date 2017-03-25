#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = []
test_requirements = []

setup(
    name="zcred",
    version="0.0.0",
    description="Modern authoriZation-centric credential format",
    long_description="Modern authoriZation-centric credential format, ala SPKI/SDSI, Macaroons, and Vanadium",
    author="Tony Arcieri",
    author_email="bascule@gmail.com",
    url="https://github.com/zcred/zcred",
    packages=["zcred"],
    package_dir={"zcred": "zcred"},
    include_package_data=True,
    install_requires=[],
    license="MIT license",
    zip_safe=False,
    keywords=["authentication", "cryptography", "security", "serialization", "merkle"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
    test_suite="tests",
    tests_require=[]
)
