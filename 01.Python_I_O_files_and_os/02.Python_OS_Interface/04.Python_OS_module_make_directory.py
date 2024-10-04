# Python "os" module (operating system interfaces)
# "os" module is a built-in module, where you can use the operating system
# dependent functionality (Windows, macOS, and Linux), such as:
# 1. Manipulate paths,
# 2. File and Directory Management: Create, remove, and modify files and
# directories.
# And many more.
# For more information check below link:
# https://docs.python.org/3/library/os.html#module-os

import os

# 2. File and Directory Management: Create, remove, and modify files and
# directories.

# To create a directory, using the "os" module, we can use:
# a. "mkdir()".
# b. "makedirs()"

# a. "mkdir()".

# There are three points that we should take into account when using "mkdir()":
# 1. It is used to create a single directory.
# 2. It will raise an error if a parent or a current directory doesn't exist.
# 3. It will raise an error if the directory already exists.

# 1. Get the path where you want to make a directory, including the directory
# name you want to create, as shown below:

path_new_dir = "./06.Python_I_O_files_and_os/02.Python_OS_Interface/new_dir"

# Using "path_new_dir" directly:
# os.mkdir(path_new_dir)


# "mkdir()" is used to create a single directory.
os.mkdir("./dir/new_dir")


# b. "makedirs()".

# There are two points that we should take into account when using
# "makedirs()":

# 1. It creates directories recursively, that means it will create nested
# directories recursively, as shown below.

# Example:
path_new_dir2 = "./main_dir/dir1/dir2"

# os.makedirs(path_new_dir2)

# 2. It doesn’t raise an error if the directories already exist. By assigning
# the "exist_ok" parameter to "True", the default value is "False".

# os.makedirs(path_new_dir2, exist_ok=True)


# To create sub-directories inside a directory, we can use the "for" loop,
# with both "mkdir()" or "makedirs()":

# 1. Create the main directory:
os.mkdir("./main")

# 2. List of sub-directories:
list_of_folders = ["subdir1", "subdir2", "subdir3"]

# 3. Using the "for" loop to create the sub-directories:

# for subdir in list_of_folders:
#     os.mkdir(os.path.join("main", subdir))

# for subdir in list_of_folders:
#     os.makedirs(os.path.join("main", subdir))
