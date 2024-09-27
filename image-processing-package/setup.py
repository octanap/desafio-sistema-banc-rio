from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements= f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="author",
    description="Pacote que processa imagens.",
    long_description=page_description,
    packages=find_packages(),
    install_requires=requirements,
)