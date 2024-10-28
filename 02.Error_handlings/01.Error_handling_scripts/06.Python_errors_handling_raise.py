# "raise" in error handling.
# "raise" keyword is used to raise an exception or errors.
# "raise" can be used directly in the code.

x = 3
# if x % 2 == 0:
#     print(f"x = {x} and it is an even number.")
# else:
#     raise Exception("'x' should be an even integer number.")

# print(x)

# But when "raise" raises an execution, Python will stop the code execution.

# It can be used in "try" and "except" blocks, but beware that it will stop
# the execution:

a = 3
b = 0

# try:
#     result = a / b
# except ZeroDivisionError:
#     raise ZeroDivisionError(f"b = {b}, shouldn't be zero")

# print("hello")


# Another way:

def division(x, y):
    if y == 0:
        raise ZeroDivisionError(f"y equals {y}, it shouldn't be zero")
    else:
        return x / y
    # return x / y


try:
    result = division(a, b)
except Exception as e:
    print(f"Process Failed, ZeroDivisionError: {e}")

print("hello")


# What are "raise" benefits?

# 1. When you encounter situations where execution cannot proceed, you can use
# "raise" to stop the execution and raise an exception to solve this error, in
# this case, you will prevent silent failures, without using "raise", the code
# might continue running with incorrect values, leading to hidden bugs that
# are difficult to trace.

# Example:

def string_list(data):

    if not isinstance(data, list):
        raise TypeError("'data' should be list type.")

    for s in data:
        if not isinstance(s, str):
            raise TypeError("list items should be of string type.")

    return data


num = 6
# print(string_list(num))

list_num = [1, 3, 5]
# print(string_list(list_num))

list_str = ["h", "e", "l", "l", "o"]
# print(string_list(list_str))

# 2. Using "raise", you can provide custom error messages as shown above. This
# will make it easier to understand what went wrong when an error occurs to
# whoever uses the code, and this will improve debugging, the message will be
# clear and it will be easier to find the error source.

# 3. "raise" allows us to throw an exception anytime.

# 4. "raise" is used in custom exception, custom exception will be discussed
# in the next video.
