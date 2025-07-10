from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirments
    """
    requirement_list:List[str]=[]

    try:
        #open and read requirements.txt file
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                #strip whitespace and newline charecters
                requirement =line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list
print(get_requirements())
setup(
    name="AI-TRAVEL-PLANNER",
    version="0.0.1",
    author="deepak",
    author_email="deepaktp.tech@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)             