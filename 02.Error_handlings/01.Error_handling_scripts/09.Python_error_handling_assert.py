# Python Assert
# The "assert" keyword is used for debugging, testing, and ensuring that your
# code runs correctly without any errors.
# Syntax: assert condition, error_message(optional)
# assert condition: this a boolean condition, which will return True or False,
# if True, the code will continue to run, if False an "AssertionError"
# exception will be raised, and Python will stop the execution.

# The difference between assertions and error handling:
# 1. The assertion is used to test whether certain assumptions remain true as
# you develop your code. Once you’ve debugged and tested your code using
# assertions, you can turn them off to optimize the code for production.
# The assertions are used for development checks.
# 2. Error handling is used to handle runtime errors, such as division by
# zero, file not found, invalid input, etc...

# Let's check how "assert" is used:
# 1. Debugging, use "assert" if you to quickly debug your code, to find errors
# quickly, as shown below:

def divide(a, b):
    assert b != 0, f"b = {b} shouldn't be zero."
    return a / b


a = 5
b = 0
# print(divide(a, b))


# 2. Documentation: use "assert" to return documentation on your code:
def list_sum(data):
    """
    This function returns the sum of a list, the list length should be > 1
    """
    return sum(data)


# Adding assert:
data = [1]
assert len(data) > 1, f"{list_sum.__doc__}"
# print(list_sum(data))

# 3. Assertion is used in code testing.

# Beware, "assert" is not an error-handling statement, it is mainly used in
# debugging and testing during your project development, when your project
# is ready for production the "assert" statement should be removed.
