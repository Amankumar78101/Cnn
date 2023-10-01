import os 
from pathlib import  Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

package_name= 'CNN_Classifier'

list_of_files=[
    ".github/wrokfloes/.gitkeep",
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/pipeline/__init__.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/constants/__init__.py',
    'tests/__init__.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'configs/config.yaml',
    'dvc.yaml',
    'params.yaml'
    'init_setup.sh',
    'requirements.txt',
    'requirements_dvc.txt',
    'setup.py'
]