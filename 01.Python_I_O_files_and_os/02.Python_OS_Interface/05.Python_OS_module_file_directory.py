# Python "os" module (operating system interfaces)
# "os" module is a built-in module, where you can use the operating system
# dependent functionality (Windows, macOS, and Linux), such as:
# 1. Manipulate paths,
# 2. File and Directory Management: Create, remove, and modify files and
# directories.
# 3. "read" and\or "write" files using the open(),
# For more information check below link:
# https://docs.python.org/3/library/os.html#module-os

# First, we import the "os" module:

import os

# 2. File and Directory Management, cont'd: Create, remove, and modify files
# and directories.

# To remove this directory, we use the "rmdir()":

new_dir = "./new_dir"

# os.mkdir(new_dir)

os.rmdir(new_dir)


# Note: If the directory is not empty, it has files or sub-directories,
# "rmdir()" will raise an error.
# Let's add a file inside "new_dir", because rmdir() is used to remove or
# delete an empty directory.

def write_file(real_path_dir, file_name, text):
    file_path = os.path.join(real_path_dir, file_name)
    with open(file_path, "w") as file:
        return file.write(text)


text = "Hello, I am new file hello.txt"
file_name = "hello.txt"
write_file(new_dir, file_name, text)

# os.rmdir(new_dir)

# To remove a directory with files in it using "os" module, use "remove()"
# to remove the file:

# os.remove(os.path.join(new_dir, "hello.txt"))

# Then use the "rmdir()"
os.rmdir(new_dir)

# If multiple files or sub-directories exist, you can use another module
# "shutil", by using the "shutil.rmtree()", it will remove the directory with
# all the files and sub-directories inside it, but "shutil" module is out of
# the scope of this course.

# Exercise 1: Try to rename a file or directory using the "os" module.
# Exercise 2: Try to count the number of files in one directory and files in
# sub-directories using the "os" module.
