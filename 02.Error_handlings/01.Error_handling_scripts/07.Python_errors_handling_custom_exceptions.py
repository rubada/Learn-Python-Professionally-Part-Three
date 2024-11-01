# Python Custom Exceptions.
# In Python, you can create your custom exceptions to handle specific
# errors in your code.
# Let's now learn how to define and use custom exceptions:
# To define a custom exception, we define a class that inherits the "Exception"
# class.
# All Built-in exceptions classes in Python inherit the "Exception" class.

# Example:
class EvenNumberException(Exception):
    """Return an error if the number is not an even integer number"""
    pass


# number = float(input("Choose a number: "))

# try:
#     if number % 2 != 0:
#         raise EvenNumberException
#     else:
#         print(int(number))
# except EvenNumberException:
#     print("Number should be an even integer number")


# Another example on how to add a message inside the custom exception class:
class AccountExcption(Exception):

    def __init__(self):
        super().__init__("Incorrect username or password")


class Account:

    def __init__(self, stored_data):
        self.stored_data = stored_data

    def log_in(self, data_input):

        try:
            if data_input != self.stored_data:

                raise AccountExcption

        except AccountExcption as e:
            print(f"{e}")

        # Here we can also add a finaly block
        finally:
            if data_input == self.stored_data:
                return "Accessing your account"
            else:
                return "Check your account data and try again"


stored_account = {"username": "John", "password": "Hello555"}
my_account = Account(stored_account)

# username = input("username: ")
# password = input("password: ")

# data_input = {"username": username, "password": password}

# print(my_account.log_in(data_input))


# You can create multiple custom exceptions, but this will be an exercise you
# can practice. Check our exercise section on GitHub.


# Let's take another example, to show how to add methods inside the custom
# exception:

class ConnectToServerException(Exception):

    def __init__(self, failed_login, server_url, num_of_tries):
        super().__init__(failed_login)
        self.server_url = server_url
        self.num_of_tries = num_of_tries

    def login_failed(self):
        print()
        print(f"Failed to connect to {self.server_url}")
        print(self.args[0])
        print()

    def try_again(self):
        print(f"You have {self.num_of_tries} tries.")

        for try_num in range(1, self.num_of_tries + 1):
            print(f"Trying to connect to {self.server_url}....")
            server = input("Type 'OK' to connect to server: ")
            print()
            if server == "OK":
                print()
                print("Logging to the server....")
                print()
                break
            else:
                print(f"Try {try_num} Failed")
                print()
            # This will initiate the object again to execute the second
            # except block when the attempts are finished.
            if try_num == self.num_of_tries:
                raise self


server = "busy"
server = "OK"

# try:
#     if server == "busy":
#         raise ConnectToServerException("Try again.", "ruba.server.com", 2)

# except ConnectToServerException as e:
#     e.login_failed()
#     try:
#         e.try_again()
#     except ConnectToServerException:
#         print("The server is busy. Try to connect later.")
# else:
#     print()
#     print("Logging to the server....")
#     print()
