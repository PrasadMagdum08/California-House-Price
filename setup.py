from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str) -> List[str]:

    requirements = []

    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

    return requirements

setup(
    name='California_House_Price_Prediction',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)