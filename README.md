# qr-app

Generates a qr based on an user input

---

## 🚀 Getting Started

### 1. Prerequisites

Install libzbar0 for decoding:

```bash
sudo apt install libzbar0
```

Ensure you have the modern Poetry package manager installed globally on your machine:

```bash
curl -sSL [https://install.python-poetry.org](https://install.python-poetry.org) | python3 -
```

### 2. Useful commands

Init repo:

```bash
poetry new qr-app
```

Create the virtual env folder:

```bash
mkdir .venv
```

Install all the dependencies in the project (clean-state):

```bash
poetry install
```

Install any dependency you need:

```bash
poetry add lib_here
```

Remove a dependency you don't need:

```bash
poetry remove lib_here
```

```bash
poetry remove lib_here
```

Audit/Scan for vulnerabilities

Install audit plugin (if required)

```bash
poetry self add poetry-audit-plugin
```

Vulnerability check

```bash
poetry audit
```

Typosquatting, lock file integrity check

```bash
poetry check
```

### 3. Set up

Activate using the command:

```bash
source .venv/bin/activate
```

Exit virtual env:

```bash
exit
```

or

```bash
deactivate
```

### 4. Advanced use cases

If multiple python versions are found in the operative system, then

- use pyenv to handle the versions
- if needed set the local python for this project, like

```bash
pyenv local 3.14.3
```

- you can confirm all good by checking

```bash
pyenv which python
```

- set the specific python version like

```bash
poetry env use $USER_HOME/.pyenv/versions/3.14.3/bin/python
```

- then install using commands like the ones in the previous section

### 5. Requirements file

For generate requirements.txt file please execute:

```bash
pip3 freeze > requirements.txt
```

### 6. Launch

```bash
python3 qr/app.py
```
