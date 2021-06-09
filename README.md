# qr-app

# Get started

## Unix

sudo apt install python3-venv
Install python3 tkinter for UI:
sudo apt install python3-tk
Install libzbar0 for decoding:
sudo apt install libzbar0
Install pipenv:
pip3 install pipenv
Then create the folder for allocate the virtual environment:
mkdir .venv
Launch pipenv:
pipenv install --skip-lock
Then activate the virtual env:
pipenv shell
Run command inside virtualenv:
pipenv run
Exit virtual env:
exit or deactivate

## Windows

Update pip:
py -m pip install --upgrade pip
Install python3-venv:
py -m pip install virtualenv
Then create the folder for allocate the virtual environment:
py -m virtualenv env
Then activate the virtual env:
Set-ExecutionPolicy Unrestricted -Scope Process (run if UnauthorizedAccess in powershell console)
.\venv\Scripts\activate.ps1
Now you can install python libs as you need it

# set up

For generate requirements.txt file please execute:
pip3 freeze > requirements.txt

# launch

## Unix

python3 qr/app.py

## Windows

py qr/app.py
