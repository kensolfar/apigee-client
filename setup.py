from setuptools import setup, find_packages

setup(
    name="apigee-client",
    version="0.1.0",
    description="A Python SDK and CLI for interacting with the Apigee Management API.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "apigee-client==0.1.0",
        "certifi==2025.4.26",
        "charset-normalizer==3.4.2",
        "click==8.1.8",
        "coverage==7.8.0",
        "idna==3.10",
        "iniconfig==2.1.0",
        "packaging==25.0",
        "pluggy==1.5.0",
        "pytest==8.3.5",
        "pytest-cov==6.1.1",
        "pytest-mock==3.14.0",
        "requests==2.32.3",
        'importlib-metadata; python_version<"3.10"',
        "setuptools==80.1.0",
        "urllib3==2.4.0",
    ],
    entry_points={
        "console_scripts": [
            "apigee-client=cli.proxy_cli:cli"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)