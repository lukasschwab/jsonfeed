from setuptools import setup

version = "1.0.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jsonfeed",
    version=version,
    py_modules=['jsonfeed', 'jsonfeed.converters.feedparser'],
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
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
