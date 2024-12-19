# 1. Importing from the Same Directory:

# caloperations/
#        __pycache__/
#       addition.py
#       script_same_dir.py
#       subtraction.py


from addition import adding
# Or
import subtraction as sub

print(adding(1, 2))
print(sub.subtract(4, 5))
