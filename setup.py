from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(path: str) -> List[str]: # it takes the path of the file and returns the list of requirements
    requirements = [] # empty list
    with open(path) as file:# it open the file
        requirements = file.readlines()# it reads the file and store it in the list
        requirements = [i.replace('/n','') for i in requirements]# it replace the /n with blamnk space from the list

        if HYPEN_E_DOT in requirements:# if the HYPEN_E_DOT is present in the list then it will remove it
            requirements.remove(HYPEN_E_DOT)   # it removes the HYPEN_E_DOT from the list

    return requirements

setup(

    name = 'dimondpriceprediction',
    author = 'dabgar shreyash',
    author_email='dabgarshreyahs199@gmail.com',
    version = '0.0.1',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)