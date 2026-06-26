# software_development_tools
Basic of Development Environments

## One environment workflow

Use a single project environment named `.venv` for this workspace.

1. Create it once:
	```bash
	python3 -m venv .venv
	```
2. Activate it:
	```bash
	source .venv/bin/activate
	```
3. Install the packages you need while it is active:
	```bash
	python -m pip install --upgrade pip ipykernel numpy matplotlib
	```
4. Register it as a notebook kernel:
	```bash
	python -m ipykernel install --user --name software_development_tools --display-name "Python (.venv)"
	```
5. In VS Code, open the notebook and select the kernel named `Python (.venv)`.

Do not mix `.venv`, `venv`, and the system Python in the same project. Install packages into only one environment and keep the notebook kernel pointed at that same environment.
