import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="downloadisimg",
    version="1.0.0",
    description="It download an image from its URL.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hafsadev290/downloadthisimage",
    author="Hafsa Yaqoubi",
    author_email="h.y1qoubi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["downloadisimg"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "downloadisimg=downloadisimg.__main__:main",
        ]
    },
)