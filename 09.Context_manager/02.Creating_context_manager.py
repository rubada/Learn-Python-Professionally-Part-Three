# Context Managers
# A context manager is an object that controls the environment within a "with"
# statement. It returns the context manager protocol:
# 1- "__enter__(self)" is called by the "with" statement to start the runtime
# context.
# 2- "__exit__(self, exc_type, exc_value, exc_tb)" is called when the "with"
# statement execution is ended.

# The __exit__ method takes three arguments, as shown above, these arguments
# will be effective if an exception occurs, if there is no exception their
# values are "None":
# exc_type: Represents the type of the exception (e.g., Exception, ValueError,
# etc.).
# exc_value: Contains the exception instance (the actual exception object),
# that means the actual message of the exception.
# exc_tb: Holds the traceback information.

# When handling exception, the "__exit__" method should return "True" or
# "False",
# "True" will suppress or silence the exception, and return how the error is
# handled.
# "False" will not suppress or silence the exception, and return how the error
# is handled.
# If there is no return statement with "True" or "False", Python will raise
# the exception.


# Let's take an example on how to write canotext manager:
import traceback
import os


class FileIO:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f'The file {self.filename} is opened.')
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'The file {self.filename} is closed.')
        if not self.__file.closed:
            self.__file.close()
        # return True
        return False


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'text.txt')

# with FileIO(file_path, 'r') as file:
#     data = file.read()


# with FileIO(file_path, 'r') as file:
#     for line in file:
#         print(float(line))

# print(file.closed)
