from setuptools import find_packages,setup
from typing import List

HYPHNE_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    '''
    This function will retun the list of requiremets listed in requirements.txt file(pandas,numpy,seaborn,etc)
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
       
        if HYPHNE_E_DOT in requirements:
            requirements.remove(HYPHNE_E_DOT)

    return requirements

setup(
    name='EndtoEndMLProject',
    versiion='0.0.1',
    author='Shubham_vaidya',
    author_email='shubhamvaidya0003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)