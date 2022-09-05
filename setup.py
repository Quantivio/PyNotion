from setuptools import setup, find_packages

classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        ]

setup(
        name="PyNotion",
        version="0.0.1",
        description="Python wrapper for Notion API",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        author="Vetrichelvan",
        author_email="pythonhub.py@gmail.com",
        license="MIT",
        url="https://github.com/pythonhubpy/PyNotion",
        packages=find_packages(exclude=["tests"]),
        install_package_data=True,
        install_requires=["requests", "pydantic", "python-dotenv", "pytest", "pytest-cov"],
        classifiers=classifiers,
        python_requires=">=3.7",
        )
