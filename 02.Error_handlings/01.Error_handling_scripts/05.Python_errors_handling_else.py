import os

# "else" in error handling.
# As mentioned before "else" will be executed when no exception is raised.
# Let's take an example:
x = 8
y = 4

# try:
#     result = x / y
# except ZeroDivisionError:
#     print("Warning: 'y' shouldn't be zero")
# else:
#     print(f"The result is {result}")

# Why use "else" in error handling?

# 1. By using "else" with "try-except" you will separate the code that manages
# the exceptions from the code that will run when there is no exception, this
# will enhance your code readability and clarity.

# 2. The code inside that "else" block will be executed only if there are no
# exceptions raised, which allows us to specify and execute the related code
# only when everything goes smoothly without exceptions.

# Examples:

script_dir = os.path.dirname(__file__)

# The my_file.txt was placed in the script file’s  directory
# file_path = "my_file.txt"

# If there is no text file:
file_path = "my_file1.txt"

abs_file_path = os.path.join(script_dir, file_path)

# Without "else" block:

try:
    # Open a file
    file = open(abs_file_path, "r")
except FileNotFoundError:
    print("File not found.")

# The code below will be executed whether the file is found or not and an
# error will be raised if the file is not found:

print("File opened successfully.")
print(file.read())
file.close()

# With "else" block:

# try:
#     # Open a file
#     file = open(abs_file_path, "r")
# except FileNotFoundError:
#     print("File not found.")
# else:
#     # If there is no exceptions
#     print("File opened successfully.")
#     # Read and print the contents of the file
#     print(file.read())
#     # Close the file
#     file.close()

# Here is another example on how to use "else" block:

# try:
#     num = int(input("Enter an integer number: "))
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
# else:
#     # If the input is successfully converted to an integer, then the
#     # "else" block will be executed, we don't want the below code to
#     # be executed if the in number is not an integer.
#     if num % 2 == 0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")
