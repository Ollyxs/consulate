import setuptools

__version__ = "1.0.0"

__author__ = "Gavin M. Roy"
__email__ = "gavinr@aweber.com"

__maintainer__ = "Lucas Ollarce"
__maintainer_email__ = "luk5ollarce@gmail.com"

install_requires = [
    "requests>=2.24.0",
]

install_extra_requires = ["requests-unixsocket>=0.1.4,<=1.0.0"]


install_tests_requires = [
    "requests-mock>=1.8.0",
    "coverage>=5.3",
    "pytest>=6.1.0",
    "pytest-cov>=2.10.1",
    "pytest-docker>=0.10.1",
    "pylint>=2.6.0",
    "flake8>=3.8.2",
    "tox>=3.20.0",
    "bandit>=1.6.2",
    "safety==1.9.0",
    "mypy>=0.782",
    "pre-commit>=2.8.1",
    "black>=20.8b1",
    "isort>=5.6.4",
    "httmock>=1.4.0",
]

setuptools.setup(
    name="py-consulate-ms",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="A Client library and command line application for the Consul",
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    url="https://consulate.readthedocs.org",
    install_requires=install_requires,
    extras_require={"unixsocket": install_extra_requires, "tests": install_tests_requires},
    tests_require=install_requires + install_tests_requires,
    setup_requires=[
        "pytest-runner>=5.2",
    ],
    license="BSD",
    package_data={"": ["LICENSE", "README.rst"]},
    packages=["consulate", "consulate.api", "consulate.models"],
    entry_points=dict(console_scripts=["consulate=consulate.cli:main"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Clustering",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    zip_safe=True,
)