from setuptools import setup, find_packages

setup(
    name='music',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'factory-boy==2.9.2',
        'pytest'
    ],
)
