from setuptools import find_packages, setup
from typing import List

REQUIRMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open(REQUIRMENTS_FILE_NAME) as requirements_file:
        requirements_list = requirements_file.readlines()
        requirements_list = [requirements_name.replace("\n", "") for requirements_name in requirements_list]

    if HYPHEN_E_DOT in requirements_list:
        requirements_list.remove(HYPHEN_E_DOT)

    return requirements_list


setup(name = "Used_Bile_Price_prediction",
      version = "0.0.1",
      descriptions = "Machine_Learning_Used_bike__prediction",
      author = "Vishala Purnima",
      authod_email = "sushe9sushe@gmail.com",
      packages = find_packages(),
      install_requires =get_requirements() ,
          )