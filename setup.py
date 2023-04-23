"""Python setup.py for seg2faang_python package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("seg2faang_python", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="seg2faang_python",
    version=read("seg2faang_python", "VERSION"),
    description="Awesome seg2faang_python created by AppleKid7",
    url="https://github.com/AppleKid7/seg2faang-python/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="AppleKid7",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["seg2faang_python = seg2faang_python.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
