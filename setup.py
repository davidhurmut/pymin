from setuptools import setup, find_packages

setup(
    name="pymin",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pymin=minify:main",
        ],
    },
    python_requires=">=3.9",
)
