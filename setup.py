import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    "numpy",
    "pandas",
    "requests",
    "geopandas"
]

setuptools.setup(
    name="npd_data",
    version="0.1.3",
    author="Merouane Hamdani",
    author_email="merouaneh@yahoo.fr",
    description="Wraper NCS data from NPD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    python_requires='>=3.6',
    install_requires=REQUIREMENTS,
)