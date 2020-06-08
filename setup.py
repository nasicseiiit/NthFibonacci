import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NthFibonacciAndIsItPrime",
    version="0.0.1",
    author="Nasimunni",
    author_email="nasicseiiit@gmail.com",
    description="NthFibonacci",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nasicseiiit/NthFibonacciAndIsItPrime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)