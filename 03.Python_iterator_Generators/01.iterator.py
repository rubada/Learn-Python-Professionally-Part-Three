# The "iter" is used to return an iterator object, and it is used to convert an
# iterable to an iterator.

# Let's take an example on how to create an iterator:
import math


def my_iterator(numbers, power):

    my_iter = iter(numbers)
    while True:
        try:
            item = math.pow(next(my_iter), power)
            print(item)
        except StopIteration:
            break


numbers = [2, 9, 6, 5, 7]
power = 2

# my_iterator(numbers, power)


# In the above example, we convert the iterable "list" to an iterator, to get
# each item inside it.

# How to build an iterator?

class MyIterator:

    def __init__(self, num, power):
        self.num = num
        self.power = power
        self.counter = 1

    # Use the "__iter__" to return the object "self" as an iterator
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.num:
            item = self.counter
            self.counter += 1
            return math.pow(item, self.power)
        else:
            raise StopIteration


number = 5
power = 2
iterate = MyIterator(number, power)

# If we want to iterate one item at time using "next" function:
# print(next(iterate))
# print(next(iterate))
# print(next(iterate))
# print(next(iterate))
# print(next(iterate))

# # This will raise a "StopIteration" exception:
# print(next(iterate))


# Or use a "for" loop:
# for num in iterate:
#     print(num)

# Where iterators are used?
# "for" loops, map(), and list comprehension, etc., use iterators to get each
#  item (one by one) inside an iterable.
