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

# "a" mode will not overwrite the file's existing contents; it will
# simply add new data to the end of the file.
# If the file doesn’t exist, it will be created automatically.

# Using "append" to create a new file:
# file = open("append.txt", "a")
# file.write("Hello, how are you?")
# file.close()


# Using "append" to add new contents at the end of the file:
# with open('append.txt', 'a') as file:
#     file.write("\nThis is a Python course.")


# To write and read a file you can use "a+":
with open('append.txt', 'a+') as file:

    # First write to a file:
    file.write("\nHow do you find Python?")

    # Then jump to the beginning of the file:
    file.seek(0)

    # Then read the file:
    data = file.read()

print(data)
