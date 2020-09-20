# PR

## Requirements
1. Python >= 3.6
2. SQLite

## Installation
- Virtualenv properly set-up with the LATEST version of setuptools and pip.
You may create one with:
    - Linux:

        `$ python<version> -m venv <path to virtualenv>`

    - Windows:
        
        `c:\>c:\Python36\python -m venv c:\path\to\myenv`

- Activate virtual environment:
   - Linux :

        `$ source <path to virtualenv>/bin/activate`
    - Windows:
    
        In the terminal navigate to the folder that contains your virtual environment using the change directory (cd) command. Once there, try typing:
    
        `source ./venv/Scripts/activate`
        
- Clone the project

- Navigate to the project directory

- Install package requirements:

    `pip install -r requirements.txt`
    
- Apply migrations:

    `...\> py manage.py migrate` 
    
- Populate db:

    `...\> py manage.py loaddata dump.json`

## Run project
In projects directory:

    ...\> py manage.py runserver
