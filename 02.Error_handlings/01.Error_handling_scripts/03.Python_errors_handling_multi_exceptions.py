# Python Error Handling Exceptions, Multiple Exceptions:
# 1. Using multiple "except" statements:

def division(x, y):
    try:
        result = x / y
        return result
    except TypeError:
        return "\nTypeError: Parameters 'x' and 'y' must be numbers\n"
    except ZeroDivisionError:
        return "ZeroDivisionError: Warning: 'y' must not be zero\n"


# print(division(6, "Hello"))
# print(division(4, 0))


def division_rev(x, y):
    try:
        result = x / y
        return result
    except TypeError:
        return "\nTypeError: Parameters 'x' and 'y' must be numbers\n"
    except ArithmeticError as e:
        # return f"{type(e).__name__}: Warning: 'y' must not be zero\n"
        return f"{type(e).__name__}: {e}\n"


# print(division_rev(6, "Hello"))
# print(division_rev(4, 0))

# For more informationa about all built-in exception check below link:
# https://docs.python.org/3/library/exceptions.html#built-in-exceptions

# This approach is used when you need to handle different exceptions
# differently.

# 2.Using a tuple in the except statement:
x = 9
# y = 0
y = "hello"
# try:
#     result = x / y
#     print(result)
# except (ZeroDivisionError, TypeError) as e:
#     print(f"\n{type(e).__name__}: {e}\n")

# This approach is used when you want to catch different exceptions and handle
# them in the same way.

# 3. Using "Exception":
# a. If you want to use one except statement to handle multiple exceptions, use
# "Exception" class with "except" as shown below:
a = 9
# b = 0
b = "hello"

try:
    result = a / b
    print(result)
except Exception as e:
    print(f"\n{type(e).__name__}: {e}\n")


# Finally, choosing one of the above depends on your specific use case, that
# aligns with your code’s readability, maintainability, and error-handling
# requirements.
