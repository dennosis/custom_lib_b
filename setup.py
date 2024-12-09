from io import open
from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8-sig") as f:
    requirements = f.readlines()


def readme():
    with open("README.md", encoding="utf-8-sig") as f:
        README = f.read()
    return README


setup(
    name="customlibb",
    packages=find_packages(include=["customlibb", "customlibb.*"]),
    version="0.0.1",
    install_requires=requirements,
    description="Teste de lib b",
    long_description=readme(),
    author="Time Dev",
    author_email="time_dev@generic.com",
    keywords=["test lib b"],
)
