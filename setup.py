from setuptools import setup, find_packages

version = "1.2.0"

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="jsonfeed-util",
    version=version,
    packages=find_packages(),
    # metadata for upload to PyPI
    author="Lukas Schwab",
    author_email="lukas.schwab@gmail.com",
    description="Python package for parsing and generating JSON feeds.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="json feed jsonfeed",
    url="https://github.com/lukasschwab/jsonfeed",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
