# To use "pipenv" virtual environment in Jupyter Notebook.
# 1. Create your project folder.

# 2. Type in terminal:
# pipenv shell

# Then either you install Jupyter Notebook in the "pipenv" shell if you want
# to run Jupyter Notebook from within the pipenv shell, it will automatically
# use the Python interpreter and packages from the environment.

# Or, if you want to create a custom Jupyter kernel with your pipenv
# environment, then select it from Jupyter Notebook's interface.

# You should install ipykernel:
# pipenv install ipykernel

# Then create a custom kernel for Jupyter:
# python -m ipykernel install --user --name=my_pipenv_kernel --display-name "pipenv-name"
