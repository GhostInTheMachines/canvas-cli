# canvas_cli

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
    - macOS: ssh-agent is present by default, but ssh-add does not persist across logins. Do ssh-add <keyfile>
  - Python 3
  
## Docker container includes
- Python library canvasapi is already setup to run inside the container

## Steps once Prereqs are met
1. Clone this repository into your working folder
2. Use VS Code command pallet to run Remote open container from folder
3. Create a folder inside the root of this repo named "vault" (without the quotes)
4. Create a file inside the vault folder named dmc_creds.py
5. Setup a class with two properties (API_KEY and API_URL)
    set them equal to your Canvas url and API key

