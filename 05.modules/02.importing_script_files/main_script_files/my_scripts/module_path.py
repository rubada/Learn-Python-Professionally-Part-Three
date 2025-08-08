import sys
import os


# First get the script file folder using the "os" "dirname()"
path_to_script = os.path.dirname(__file__)

# print()
# print(path_to_script)
# print()

# Second usin the "join()" to join the "path_to_script" with "../" to get
# the main module folder "main_script_files".
# Using "../" will remove the "my_scripts" folder when used with "abspath"
# module_path = os.path.abspath(os.path.join(path_to_script, "../"))
module_path = os.path.abspath(os.path.join(path_to_script, os.path.pardir))


# print()
# print(module_path)
# print()

# Then use "sys.path.append" method is used to add a specific directory to
# the list of paths that the interpreter searches for modules.
sys.path.append(module_path)
