# 3. Importing from a Subdirectory to a script file that is located in another
# Subdirectory.

# main_script_files/
#       caloperations/
#               __pycache__/
#               addition.py
#               subtraction.py
#       my_scripts/
#               module_path.py
#               script_from_to_dir.py

# To do this, I should add my module path to the list of paths the interpreter
# searches in for modules.


# The "module_path" module has added the path to the directory
# "main_script_files" to the list of paths where the Python interpreter
# searches for modules.
import module_path

from caloperations import addition
import caloperations
import caloperations.subtraction

# This line is added to remove this "Flake8" message:
# "'module_path' imported but unused".
# This line is unnecessary it may be removed, and won’t affect the code.
module_path.module_path

print(addition.adding(1, 2))


print(caloperations.subtraction.subtract(6, 8))
