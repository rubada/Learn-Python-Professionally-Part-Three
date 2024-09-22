# Before discussing the "os" module, we need to understand the operating
# systems paths.
# A path is a way to describe the file location, we have two different types
# of paths:

# 1. Absolute Path:
# An absolute path specifies the full path from the root directory, (e.g., “/”
# in Mac, “~/” in Linux, and “C:\” in Windows), to the specific file or
# directory.
# It includes all necessary components, such as drive letters (for Windows) or
# mount points (for Mac and Linux).

# Example of an absolute path for different operations systems:

# Mac: /home/user/documents/file.txt
# Linux: ~/home/user/documents/file.txt
# Windows: C:\Users\User\Documents\file.txt

# An absolute path can contain "/../".

# To read the "text.txt" file, located in the same folder as the script file,
# without needing to change the folder where text files exist, we can use the
# absolute path, as shown below.
# I can define a variable that is equal to this path and open the text file:


path_text = "C:/Users/ruba.000/OneDrive/data_science/Ruba_courses/\
Python_Course/Learn_python/06.Python_I_O_files_and_os/02.Python_OS_Interface/\
text.txt"

# As shown above, we changed "\", the backslash, to "/", to slash, that is how
# we should write the path for Python to read it. If we keep the "\", as we
# get it from Windows, you will get a "SyntaxError". Why? because Python uses
# the "\" for line continuation.


with open(path_text, "r") as file:
    read_file = file.read()

# print()
# print(read_file)
# print()


# Now open a file in a different folder:
path_text1 = "C:/Users/ruba.000/OneDrive/data_science/Ruba_courses/\
Python_Course/Learn_python/06.Python_I_O_files_and_os/02.Python_OS_Interface/\
text_files/text1.txt"

with open(path_text1, "r") as file:
    read_file1 = file.read()

# print()
# print(read_file1)
# print()

# 2. Relative Path:
# The relative path is defined as the current working directory (pwd) (print
# working directory), it starts from your current location (here in VS code
# our current location is the “Learn_python” directory). That's why relative
# paths are shorter and more convenient to work with.

# There are two ways on how to get the relative path:
# First, "." (a single dot): Represents the current directory.
# In our case, the current directory is "Learn_python"
# Second, ".." (two dots): Represents the parent directory, the directory
# before the current directory.
# In our case, the parent directory is "Python_course"


# Let’s explore some examples of relative paths in Windows:

# 1. To open the "text.txt", which is in:
# "C:/Users/ruba.000/OneDrive/data_science/Ruba_courses/
# Python_Course/Learn_python/06.Python_I_O_files_and_os/02.Python_OS_Interface/
# text.txt"

# The relative paths for "text.txt" file:
# Current directory relative path:
path_text2 = "./06.Python_I_O_files_and_os/02.Python_OS_Interface/text.txt"

# or

# Parent directory relative path:
# path_text2 = "../Learn_python/06.Python_I_O_files_and_os/\
# 02.Python_OS_Interface/text.txt"

# with open(path_text2, "r") as file:
#     read_file2 = file.read()

# print()
# print(read_file2)
# print()

# 2. Now let's open a file in the current dirctory "learn_Python"
# Current directory relative path:
# path_text3 = "./example1.txt"

# or

# Parent directory relative path:
# path_text3 = "../Learn_python/example1.txt"

# with open(path_text3, "r") as file:
#     read_file3 = file.read()

# print()
# print(read_file3)
# print()


# Note: absolute, and relative paths can be used in Linux and Mac.

# Note: to open a files using the relative path, your terminal directory should
# be the current directory where the file may exist, otherwise use the
# absolute path.
