# Creatin environments
## 1. Using the Create Environment command
To create local environments in VS Code using virtual environments or Anaconda, you can follow these steps: open the Command Palette (Ctrl+Shift+P), search for the Python: Create Environment command, and select it.

The command presents a list of environment types: Venv

## 2. Create a virtual environment in the terminal
If you choose to create a virtual environment manually, use the following command (where "myenv" is the name of the environment folder):
```sh
# macOS/Linux
# You may need to run `sudo apt-get install python3-venv` first on Debian-based OSs
python3 -m venv myenv

# Windows
# You can also use `py -3 -m venv .venv`
python -m venv myenv
```