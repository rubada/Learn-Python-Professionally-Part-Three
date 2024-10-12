# 1st Question:
# Write a function that can get the courses' names in Intuidemy, and raise an
# indexerror and valueerror exceptions if the course is not found and if the
# index number is not an integer.
# use input() function to enter an integer number.

courses_names = ["Python Course", "Machine Learning Course", "Deep Learning",
                 "OOP Course"]
# Outputs:
# If the course is found, the output is:
# Course number 0 is: Python Course
# Try another number

# If the index is not an integer, the output is:
# 5.5 should be an integer
# Try another number

# If the index is out of range, the output is:
# Course number 7, is not found.
# Try another number


def get_course(index, courses_names):
    try:
        course = courses_names[int(index)]
        new_course = f"Course number {index} is: {course}"
        print(new_course)
    except ValueError:
        print(f"{index} should be an integer")
    except IndexError:
        print(f"Course number {index}, is not found.")
    finally:
        return "Try another number"


# index = input("Choose an integer number 0 is included: ")
# print(get_course(index, courses_names))


# 2nd Question:
# Create a code for a bank that will raise a custom exception if the credit
# card expires date is expired, or the credit amount is insufficient.


class CreditCardDateException(Exception):

    def __init__(self):
        super().__init__("Credit card date is Expired.")


class CreditCardAmountException(Exception):

    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Card withdraw amount = {amount} exceeds card\
 balance = {balance}")


class CreditCard:

    def __init__(self, card_date, card_balance):
        self.card_date = card_date
        self.card_balance = card_balance

    def check_date(self, card_date):

        try:
            if card_date != self.card_date:
                raise CreditCardDateException()

        except CreditCardDateException as e:
            print(e)

        finally:
            if card_date == self.card_date:
                return "Credit Card is valid"
            else:
                return "Check your bank to change your credit card."

    def card_transaction(self, amount):

        if self.card_balance < amount:
            try:
                raise CreditCardAmountException(amount, self.card_balance)
            except CreditCardAmountException as e:
                return e
        else:
            self.card_balance -= amount
            return f"A Trx using Card XXXX1234 withdraw ${amount}. Available\
 balance ${self.card_balance}"


use_card = CreditCard("5/25", 2000)
# print(use_card.check_date("5/25"))
# print(use_card.check_date("1/26"))

amount_withdraw = 2500
# print(use_card.card_transaction(amount_withdraw))
