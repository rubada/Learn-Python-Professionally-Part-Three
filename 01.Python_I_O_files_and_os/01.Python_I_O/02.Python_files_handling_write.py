# Python Files Handling
# In Python, you can handle files using the open() function.
# Syntax:
# open(filename, mode)
# “mode” has several options:

# Read Only ('r'): Opens a file for reading.
# Read and Write ('r+'): Opens a file for both reading and writing.
# Write Only ('w'): Opens a file for writing content.
# Write and Read ('w+'): Opens a file for both reading and writing.
# “read” and “write” modes will read or write to the file at the beginning of
# the file.

# Append Only ('a'): Opens a file for writing.
# Append and Read ('a+'): Opens a file for both reading and writing.
# The append mode will write to the file at the end of the file. If the file
# doesn't they will create one.

# Binary ('b'): Opens the file in binary mode.

# For more information about open() check below link:
# https://docs.python.org/3/library/functions.html#open

# In this course, we will discuss the read, write, and append modes.

# Let's take an example on "mode" "w":
# Using write will create a new file.
# file = open("example1.txt", "w")

# To write a file, use the write() method or function:
# file.write("Hello, and welcome.\n")

# Using write more than one time will create lines inside your file.
# file.write("This is a Python Course.")

# file.close()

# Beware that when writing to a file using open(), be sure that there is no
# data inside the file, because the existing contents will be overwritten and
# replaced when using the write mode.

# with open("example1.txt", "w") as file:
#     file.write("My name is Ruba Dabbas")

# You can use writelines() to create a file with more than one line:

# Create a list that contains the lines you want to add to your file:
lines_to_write = ["My first line\n", "This is my second line\n",
                  "And here the third line"]

# Beware to use "\n" at the end of each list item, so that you can create
# different lines.

# with open('example1.txt', 'w') as file:
#     file.writelines(lines_to_write)
