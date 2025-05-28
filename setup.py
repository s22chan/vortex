from setuptools import setup, find_packages

setup(
    name="vtx",
    version="1.0.6",
    description="Inference and utilities for convolutional multi-hybrid models",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Michael Poli",
    url="http://github.com/zymrael/vortex",
    packages=find_packages(include=["vortex", "vortex.*"]),
    python_requires=">=3.10",
    zip_safe=False,
    include_package_data=False,
)
