# Adding setup file for backward compatability if needed
# Will be removed in future versions

from setuptools import setup, find_packages

long_description: str

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Operating System :: OS Independent",
]

setup(
    name="PyNotion",
    version="0.0.6",
    description="Python wrapper for Notion API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vetrichelvan",
    author_email="pythonhub.py@gmail.com",
    license="MIT",
    url="https://github.com/pythonhubpy/PyNotion",
    packages=find_packages(exclude=["tests"]),
    install_package_data=True,
    install_requires=["requests", "pydantic", "python-dotenv", "pytest", "pytest-cov"],
    classifiers=classifiers,
    python_requires=">=3.8",
)
