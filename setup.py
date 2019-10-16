import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="equal-area-breaks",
    version="0.0.1",
    author="John Kastner",
    author_email="john.h.kastner@gmail.com",
    description="An extension to the mapclassify package to support equal area breaks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackastner/equal_area_breaks",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'mapclassify'])
