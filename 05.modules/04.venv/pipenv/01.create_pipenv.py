# Using "pipenv" to create a virtual environment
# 1. Install the "pipenv" package.
# pip install pipenv

# 2. In your project folder type:
# pipenv shell
# To create and activate the virtual enviroment.

# To install a package that are needed in the project development and
# production:
# pipenv install <package-name>

# To install packages that are needed in the project development, and but are
# not needed in production:
# pipenv install <package-name> --dev

# If another developers want to work on the project, they would get the code,
# with the "pipfile", and type in the terminal where the "pipfile" is:

# pipenv install --dev

# This will install all the dependencies needed for development, which includes
# both the production and development dependencies.

# Push the project into production

# Lock the environment to ensure the same one is in production, to update your
# “pipfile.lock”:
# pipenv lock

# Get the code and “pipfile.lock” in the production environment, and then type:
# pipenv install --ignore-pipfile

# This will ignore the “Pipfile" and use the “Pipfile.lock.” Then, "pipenv"
# will create the same environment with all sub-dependencies that was created
# when "pipenv lock" was done.
