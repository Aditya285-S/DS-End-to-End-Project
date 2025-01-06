from setuptools import find_packages, setup
from typing import List

hypen_e_dot = '-e .'
def get_requirements(path:str)->List[str]:

    requiremnts = []
    with open(path) as f:
        requiremnts = f.readlines()
        requiremnts = [req.replace('\n','') for req in requiremnts]

        if hypen_e_dot in requiremnts:
            requiremnts.remove(hypen_e_dot)

    return requiremnts

setup(
    name='DS-Project',
    version='0.0.1',
    author='Aditya',
    author_email='adityashe2004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)