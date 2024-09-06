# Python File Handling
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

# Let's take an example on "mode" "r":

# Note: to open the file as shown below, "relative path" your terminal path
# should be the path where your file exists, otherwise use "the absolute path".
# This will be discussed latter in this section.

# First we will change our directory to where our script and text files exist:

file = open("example.txt", "r")

# To read the file use the read() function or method:
data = file.read()

# After you finished reading or writing the file, use the close() function or
# method to close the file:
file.close()

# print(data)cl

# Create a list:
data_list = data.split()
# print(data_list)


# Another example where you can use "read()" to select the first number of
# characters you want to read:

file1 = open("example.txt", "r")

data1 = file1.read(29)

file1.close()

# print(data1)

# Create a list:
data_list1 = data1.split()
# print(data_list1)

# Two notes:
# The "read()" method reads all the file unless a specific numbers is assigned.
# The "open()" function opens the data as strings


# Another example where you can use "readlines()" to get a list containing the
# text lines:
file2 = open("example.txt", "r")
data2 = file2.readlines()
line1 = data2[0]

file2.close()

# "data2" will be a list
# print()
# print(data2)
# print(line1)
# print()


# or
file3 = open("example.txt", "r")
line = file3.readline()
# while line:
#     print()
#     print(line)
#     line = file3.readline()
#     print()

file3.close()

# Using the context manager "with" to read a file is a better approach, because
# in this case you don't need "close()" to close your file, in case you forgot
# to use it.
# Let's take an example where we want to read specific lines:

lines_to_read = [0, 2, 3]

lines_required = []

# Use "with" as shown below:
with open('example.txt', 'r') as file:
    for index, line in enumerate(file):
        if index in lines_to_read:
            lines_required.append(line)

# print(lines_required)
