# qr-app

Generates a qr based on an user input

# Get started

## Unix

Install pipenv:

```bash
sudo apt install python3-venv
pip3 install pipenv
```

Install python3 tkinter for UI:

```bash
sudo apt install python3-tk
```

Install libzbar0 for decoding:

```bash
sudo apt install libzbar0
```

Then create the folder for allocate the virtual environment:

```bash
mkdir .venv
```

Launch pipenv:

```bash
pipenv install
```

Then activate the virtual env:

```bash
pipenv shell
```

Run command inside virtualenv:

```bash
pipenv run
```

Exit virtual env:

```bash
exit
```

or

```bash
deactivate
```

# set up

For generate requirements.txt file please execute:

```bash
pip3 freeze > requirements.txt
```

# launch

## Unix

```bash
python3 qr/app.py
```
