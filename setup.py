#Able to build ML applicationas as a package even deploy in pip

from setuptools import find_packages, setup
from typing import List

HYPEN_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''This is function will return the List of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
setup(
    name='MLproject',
    version='0.0.1',
    author='Sandeep',
    author_mail = 'bandisandeep1423@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)