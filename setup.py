import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="physunits",
    version="1.0.0",
    author="pacosalces",
    author_email="pacosalces@gmail.com",
    description="Physical units as global variables for simple numerical propagation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pacosalces/physunits",
    license='LICENSE.txt',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)