from os import name
from setuptools import setup, find_packages

setup(
    name="demopkg",
    version="0.0.1",
    package=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'megademo = demopkg.__main__:app',
            'megademodbdb = demopkg.db:app',
        ]
    }
)