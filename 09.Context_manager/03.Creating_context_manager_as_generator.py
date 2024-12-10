# Context Managers
# To create a generator context manager first we should import the "contextlib"
# module.
# Let's take an example:
import contextlib
import os


# Then use "contextlib.contextmanager" decorator
@contextlib.contextmanager
def file_IO(file_name, mode):
    file = open(file_name, mode)
    try:
        yield file
    except FileNotFoundError as e:
        print(e)
    finally:
        file.close()


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'text.txt')

with file_IO(file_path, 'r') as file:
    data = file.read()

print(data)

# When creating a user-defined context, using a generator will have several
# benefits:
# 1. The code is simpler and more readable than defining a class with
# "__enter__" and "__exist__" methods.
# 2. Less code to write and maintain.
# 3. Using a generator context manager will let you handle the errors
# efficiently, and simply use the "finally" block, for example, to close your
# file, disconnect from the database, etc.
