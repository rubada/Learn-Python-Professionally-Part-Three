# Context Managers
# Let's take an example to understand the concept behind a context manager.
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'text.txt')

file = open(file_path)
data = file.readlines()

for item in data:
    print(float(item))

file.close()

# As shown above a value error is raised, and Python stops the execution,
# the file is still open, let me show you how:

# try:
#     for item in data:
#         # print(item)
#         print(float(item))
# except ValueError as e:
#     print(f"ValueError: {e}")
# else:
#     file.close()

# print(file.closed)

# As shown in the above example when we tried to convert the data to a float
# type data, Python raises an error because "hello" is a string and can't be
# converted to a float. When the error is raised it stops the code execution,
# and that leaves the file open because Python will never reach the
# "file.close()" statement, imagine if you are working with databases
# connections or you want to open and work with a large file, this will this
# may lead to resource leakages and slowing of your system or you may even face
# system crash.

# We can add a "finally" block to close the file, but using error handling will
# complicate the code.


# Python provides an easy way to manage resources, which is context manager.

# with open(file_path) as file:
#     data = file.readlines()
#     for item in data:
#         print(float(item))


# Let me show you that the with statement will close the file:

with open(file_path) as file:
    data = file.readlines()
    for item in data:
        try:
            print(float(item))
        except ValueError as e:
            print(f"ValueError: {e}")


print(file.closed)

# The "with" statement creates a runtime context that allows you to run a
# group of statements under the control of a context manager.
# Compared with the error handling "try, except, and finally" the "with"
# statement is clearer, safer, and reusable.
