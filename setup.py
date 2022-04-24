from setuptools import setup, find_packages


__version__ = "0.2.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bails-lambda-utils",
    version=__version__,
    license="MIT",
    author="Bailey Everts",
    author_email="me@baileyeverts.net",
    description="For making lambdas easier",
    url="https://github.com/beverts312/lambda-utils",
    packages=find_packages(),
    install_requires=["pynamodb"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
