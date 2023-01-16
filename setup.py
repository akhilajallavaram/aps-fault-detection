from setuptools import find_packages,setup

from typing import List

requirement_file_name = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:

    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name = "Sensor",
    version = "0.0.2",
    author = "Akhila",
    author_email= "jallavaramakhila2409@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)