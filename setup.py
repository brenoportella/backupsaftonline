from setuptools import find_packages, setup

setup(
    name='bpsaftonline',
    version='0.9',
    packages=find_packages(),
    py_modules=['backup'],
    entry_points={
        'console_scripts': [
            'backup = backup:main',
        ],
    },
)
