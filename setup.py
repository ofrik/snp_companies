import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='snp_companies',
    version='1.0',
    author="Ofri Masad",
    author_email="ofrik89@gmail.com",
    description="Fetches and construct the S&P 500 based on the Wiki page",
    url="https://github.com/ofrik/snp_companies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
