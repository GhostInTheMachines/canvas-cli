# canvas-cli

## Prerequisites

- Mac Docker Desktop 2.0+
- VS Code
- VS Code Extensions
  - Docker
  - Python
  - Pylance
  - Remote Containers
  - Remote Development
  - Remote SSH
    - macOS: ssh-agent is present by default, but ssh-add does not persist across logins. Do ssh-add <keyfile>. We recommend configuring VS Code to run this command on terminal startup with terminal.integrated.shellArgs.osx or otherwise configuring a startup script. You can also manually run that command each login.
  - Python 3
  
  ## Docker container includes
  - Python library canvasapi is already setup to run inside the container

  ## Steps once Prereqs are met
  1. Clone this repository into your working folder
  2. Use VS Code command pallet to run Remote open container from folder


create a file inside the vault folder named dmc_creds.py
setup a class with two properties (API_KEY and API_URL)
set them equal to your Canvas url and API key

