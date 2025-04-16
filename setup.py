from setuptools import setup, find_packages

setup(
    name="ad_system",
    version="0.1.0",
    description="Ad Agency Budget Management System",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
