# Python Error Handling Exceptions.
# As mentioned before error handling is an important issue when writing robust
# and reliable Python code.

# How can we write handling exceptions?
# As we discussed before, there are many exceptions in Python,
# https://docs.python.org/3.11/library/exceptions.html#built-in-exceptions
# to handle these exceptions, Python provides the try, except, else, and
# finally blocks.
# "try" contains the code that might raise an exception.
# "except" catches specific exceptions and provides error-handling logic.
# "else" is executed if no exceptions occur in the try block.
# "finally" is always executed, whether an exception occurred or it did not.
# Try, Except, else, and finally Syntax
# try:
#     the code ....
# except:
#     where errors are handled
# else:
#     optional if no exception occurs
# finally:
#     optional some code that is always executed

# An important note:
# Try to limit the code inside the "try" block to a specific operation that
# might raise an exception.
# When writing smaller "try" blocks it will be easier to identify the source of
# errors and improve code readability.


# Example:
def division(x, y):
    result = x / y
    return result


# print(division(4, 2))
# print(division(4, 0))
# print(division(6, 3))

# Python stops the execution and raises an error


# Let's now handle the above error:
def division_rev(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Warning: 'y' shouldn't be zero"


print(division_rev(4, 2))
print(division_rev(4, 0))
print(division_rev(6, 3))

# Using error handling exceptions, Python didn't stop the execution but raises
# an exception.
