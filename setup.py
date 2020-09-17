import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="physunits", # Replace with your own username
    version="0.0.3",
    author="pacosalces",
    author_email="pacosalces@gmail.com",
    description="Physical units as global variables for simple numerical propagation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pacosalces/physunits",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)