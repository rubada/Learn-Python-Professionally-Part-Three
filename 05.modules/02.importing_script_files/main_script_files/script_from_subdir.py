# 2. Importing from a Subdirectory.

# main_script_files/
#       caloperations/
#               __pycache__/
#               addition.py
#               subtraction.py
#       script_from_subdir.py

from caloperations import addition
from caloperations.addition import adding
import caloperations as cal
import caloperations.subtraction as sub


print(addition.adding(1, 2))

print(adding(1, 2))

print(cal.subtraction.subtract(6, 8))

print(sub.subtract(3, 5))
