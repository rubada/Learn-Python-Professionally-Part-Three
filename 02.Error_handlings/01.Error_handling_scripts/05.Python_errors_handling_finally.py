import os

# "finally" in error handling.
# As mentioned before "finally" will always be executed whether there is an
# exception or not.
# Let's take an example:
x = 8
y = 4
# y = 0

# try:
#     result = x / y
# except ZeroDivisionError:
#     print("Warning: 'y' shouldn't be zero")
# else:
#     print(f"The result is {result}")
# finally:
#     print("'finally' is always executed")

# Why use "finally" in error handling?

# 1. It ensures that essential clean up the code (such as closing files or
# database connections, such as when working "SQL database") is executed,
# regardless of whether an exception occurred in the try block or not.
# Whether an exception is raised or not, the "finally" block ensures that
# critical operations are completed, and execution is guaranteed.

# Example:
script_dir = os.path.dirname(__file__)

file_path = "my_file.txt"

abs_file_path = os.path.join(script_dir, file_path)

data = 0

# try:
#     file = open(abs_file_path, "r")
#     data = file.readlines()
#     print(data[4])
# except FileNotFoundError:
#     print("File not found.")
# except IndexError:
#     print("Index is out of range")
# else:
#     print(data)
# finally:
#     if data:
#         file.close()
#         print("The file is closed")
#     else:
#         print("Check if the opened file is available in the folder")


# 2. It ensures that the code will return an output even if there is an
# exception.

# Another example:

def string_processing(data):
    try:
        # Change the data letters to upper case and create a list:
        processed_data = [letter.upper() for letter in data]
    except Exception as e:
        print("Error:", str(e))
        print()
    else:
        # Using "else" to values to modify data:
        processed_data.append("A")
    finally:
        # local() returns a dictionary of the function local variables and
        # its parameters
        print(locals())
        if 'processed_data' in locals():
            print("Finished. Try another data to process.")
            return processed_data
        else:
            print(f"data = {data}, should be a string or list of strings")


# Here we can assign the function to a variable and use it result in our code.
# data = string_processing("hello")
# print("Final data processed: ", data)

# If another data types are used:
# print(string_processing(9))
# print(string_processing([2, 4, 5]))
print(string_processing(["a", "4", "5"]))
