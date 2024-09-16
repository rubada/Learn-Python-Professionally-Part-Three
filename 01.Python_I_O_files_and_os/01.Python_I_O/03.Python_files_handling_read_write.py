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

# "r+" mode first reads the file and then writes to it, that is why the file
# should be exist when using "r+", when writing it will add the line at the
# end of the file:

# with open("read_write.txt", "r+") as file:
#     data = file.read()

#     file.write("\nHello how are you?\n")

#     file.write("This is my channel?")

# print(data)

# “w+” mode first writes to the file and then reads it, using “w+”, you can
# create a new file, if a file has contents, the existing contents will be
# overwritten and replaced.

# lines_to_write = ["My first line1\n", "This is my second line1\n",
#                   "And here the third line1"]

# with open("write_read.txt", "w+") as file:
#     file.writelines(lines_to_write)
#     file.seek(0, 0)
#     data = file.read()

# print(data)
