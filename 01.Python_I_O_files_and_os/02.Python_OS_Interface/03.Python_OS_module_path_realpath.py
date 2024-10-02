# Python "os" module (operating system interfaces)
# For more information check below link:
# https://docs.python.org/3/library/os.html#module-os

import os

# 1. Manipulate paths, cont'd.

# Now let's check how to open different text files located inside the current
# directory "Learn_python":


# First, let's create a function to join, open, and read files, to D.R.Y. in
# our code:

def read_file(real_path):
    with open(real_path, "r") as file:
        data = file.read()
    return data


# Secondly, to get the path to the "Learn_python" directory, we will use
# the “realpath()”, where the “realpath()” is used to get the
# canonical path to a specified filename in the current directory, by
# eliminating any symbols that exist, such as: "../", "./", or "../../", that's
# why an absolute path can be canonical, but not vice versa.
# For more information about "realpath", check the below link:
# https://docs.python.org/3/library/os.path.html#os.path.realpath

file_name = "example1.txt"
real_path = os.path.realpath("example1.txt")

# print()
# print("Real path:", real_path)
# print()

# print()
# print(read_file(real_path))
# print()

# Using "dirname()" to get our current directory, stripping off the "file":
file_name = "./text/text3.txt"
real_path1 = os.path.realpath(file_name)

# print()
# print("Current Directory:", real_path1)
# print()

# print()
# print(read_file(real_path1))
# print()

path_file = "./../example4.txt"
real_path = os.path.realpath(path_file)
print()
print(real_path)
print()

# There are many methods or functions that you can use to manipulate paths,
# you can check them in the above link.
