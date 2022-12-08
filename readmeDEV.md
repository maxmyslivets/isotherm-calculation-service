## Preparing system for development
- install choco
- install make
- create virtual environment
- install requirements

### Install choco from PowerShell
```shell
> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### Install make
```bash
choco install make
```

### Create virtual environment in ./ directory
```bash
# your directory for project
cd C:\Projects\isotherm-calculation-service

py -m venv venv
```

### Install requirements
```bash
pip install -r requirements.txt
```

## Run commands

### Activate venv
```bash
# your directory for project
cd C:\Projects\isotherm-calculation-service

venv\Scripts\activate
```

### Run server
```bash
make s
```

### Run client for test
```bash
make c
```
