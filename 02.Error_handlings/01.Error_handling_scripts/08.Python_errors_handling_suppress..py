# Python Error Handling, Suppressing Exceptions:
# Suppressing exceptions can be useful in specific scenarios where you want to
# ignore exceptions rather than handling them with try-except blocks.
# Youn can use "suppress" which is a context manager provided by
# Python’s "contextlib" module.
# Using "suppress" your code will run smoothly with interruptions.

from contextlib import suppress
import os

# When to use Suppressing Exceptions:
# Let's say you are working on a project, and you want to remove a file from
# your project you can use the contextlib.suppress to ignore the error
# exception that will be raised,when you try to remove this file again.

with suppress(FileNotFoundError):
    os.remove("suppress.py")

# This is better than:
# try:
#     os.remove("my_file.py")
# except FileNotFoundError:
#     pass

# Your code will run smoothly with interruptions.


# Finally, keep in mind that not all exceptions should be suppressed.
# For example IndexError, TypeError, NameError, etc., can't be suppressed and
# the code should raise an exception, to reveal if there is hidden bugs.
