from setuptools import setup, find_packages
setup(
    name="employment-in-latin-america-database-by-country-evolution-2000-2020",
    version="1.0.0",
    description="Employment in Latin America: Database by Country with Evolution 2000-2020 (every 5 years). DOI: 10.6",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/employment-in-latin-america-database-by-country-evolution-2000-2020",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)