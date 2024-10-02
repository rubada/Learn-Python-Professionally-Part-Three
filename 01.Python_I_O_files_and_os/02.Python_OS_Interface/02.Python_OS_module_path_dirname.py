# Python "os" module (operating system interfaces)
# "os" module is a built-in module, where you can use the operating system
# dependent functionality (Windows, macOS, and Linux), such as:
# 1. Manipulate paths,
# 2. File and Directory Management: Create, remove, and modify files and
# directories.
# And many more.
# For more information check below link:
# https://docs.python.org/3/library/os.html#module-os

# Let's now check how we can use the "os" module
# First, we import the "os" module:

import os

# 1. Manipulate paths.
# Let's now try to open the "text.txt" file that exists in our folder
# "02.Python_OS_Interface", the same folder or directory of our script file,
# using what we learned:

# with open('text.txt', 'r') as file:
#     data = file.read()

# As shown we got "FileNotFoundError". Why?
# As we mentioned before to open a file using the above method, our terminal
# should have the same path as our script file path.

# To overcome the above issue and others that you may face when we want to
# open a file, we can use the "os" module:

# 1. We will use the "os.path" sub-module with "dirname()" function.
# The "dirname()" function is used to get "the directory name" from a specified
# path, let' take an example:

path_text = "C:/Users/ruba.000/OneDrive/data_science/Ruba_courses/\
    Python_Course/Learn_python/06.Python_I_O_files_and_os/02.Python_OS_Interface/\
    text.txt"

text_dir = os.path.dirname(path_text)

# print()
# print("Text directory:", text_dir)
# print()


# The result is the absolute path by stripping off the last component of the
# path, in our case the "text.txt"

# That's why we always use the "join()" with the "dirname()", as shown below:

# Path to the the directory "02.Python_OS_Interface", where our script
# file is located, "__file__" attribute refers to the path where our script
# file is located.

# print()
# print(__file__)
# print()

script_dir = os.path.dirname(__file__)

# print()
# print("Script file directory:", script_dir)
# print()

# Note: "dirname()" strips the "02.Python_OS_module_absolute_path.py" file.

# 2. Get the file name that exists in this directory.
file_name = "text.txt"

# 3. We use the "join()" function to join the path with the file we want to
# open.
file_path = os.path.join(script_dir, file_name)

# print()
# print("File path:", file_path)
# print()

with open(file_path, 'r') as file:
    data = file.read()

# print()
# print(data)
# print()
