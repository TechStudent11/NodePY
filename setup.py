"""setup.py: setuptools control."""


import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('nodepy/cli.py').read(),
    re.M
).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="nodepy",
    packages=["nodepy"],
    entry_points={
        "console_scripts": ['nodepy = nodepy.cli:main']
    },
    version=version,
    description="The NodeJS of Python.",
    long_description=long_descr,
    author="TechStudent11",
    author_email="mohammeddam1@outlook.com",
    url="https://github.com/TechStudent11/NodePY",
    install_requires=[
        'click'
    ]
)