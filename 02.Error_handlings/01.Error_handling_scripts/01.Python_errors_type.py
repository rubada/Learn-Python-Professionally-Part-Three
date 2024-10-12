import math

# Python Error Handling.
# Let's check some common errors that we may face.
# For more information about the errors in Python check the below site:
# https://docs.python.org/3.11/library/exceptions.html#built-in-exceptions

# 1. SyntaxError:
# These errors happen when Python encounter an invalid or incorrect syntax,
# such missing parentthese, or keyord etc.
# This type of error needs to be fixed.
# print 1+2


# df add():
#     pass

# if 1 < 2
#     print(True)

# 2. TypeError: Incorrect data type usage.
# Examples:
# Using different data types in unsupported operations:
name = "Tom"
num = 4
# print(name + num + name)

# Calling a non callable object.
greet = "Hello World"
# print(greet())

# There are many executions that can raise a TypeError.

# 3. ValueError: Invalid argument value.
# Example:
a = 4
# a = -4
sqroot = math.sqrt(a)
# print(sqroot)


# 4. IndexError: Accessing an out-of-range index.
# Example:
num = [1, 3, 7, 4]
# print(num[4])

# 5. NameError: When a name being accessed is not defined in the local, global
# scope, or built-in scope.
# Examples:
name = "Mary"
# Print(name)

# print(fullname)

# 6. KeyError: Accessing a non-existent dictionary key.
person = {"name": "John", "age": 35}
# print(person["last"])

# 7. ZeroDivisionError: Division by zero.
# print(10/0)
