from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e.'

def get_requirements(file_path:str)->list[str]:
    '''Reads the requirements file and returns a list of requirements'''

    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        [req.replace("\n"," ") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
            return requirments


setup(
name='ml_project',            # Correct naming convention for the package
version='0.1.0',
author='Jayesh Kadam',         # Full name for author
author_email='jayeshkadam0305@gmail.com',
packages=find_packages(),     # Automatically finds all packages
install_requires=get_requirements('requirements.txt'), # Load dependencies from requirements.txt
)
