import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="argparse-graph",
    version="0.0.1",
    author="Quentin Le Baron",
    description="yaml to add logique with argparse object.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["yamllint"],
    tests_require=["pytest"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
