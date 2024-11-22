# Python Generators

# Let's take an example:

def generator_loop(x):
    for i in range(x):
        yield i


x = 4
gen = generator_loop(x)
# print(gen)
# print(hasattr(gen, "__iter__"))
# print(hasattr(gen, "__next__"))

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# As discussed before if "next()" is used beyond the last value in the
# iteration, "StopIteration" exception is raised:

# print(next(gen))

# Or we can use a "for" loop:
# for j in gen:
#     print(j)

# We can store the generator values in an iterable such as list, tuples,
# set, etc.

# gen_values = list(gen)
# gen_values = set(gen)
gen_values = tuple(gen)
# print(gen_values)


# More than one "yield" statement can be used in a single generator:
def generator_yield():
    yield "This"
    yield "is"
    yield "Pyhton"


# for num in generator_yield():
#     print(num)


# Another way to create a generator is to use round brackets, with a list
# comprehension expression, as discussed before in list comprehension, to
# create a tuple we use the "tuple()", while "()" are used to create a
# generator object:

my_gen = (num for num in range(5))
# print(my_gen)

# Then using "list()" or "for" loop to get the values:
numbers = list(my_gen)
# print(numbers)


# An important note:
def after_yeild():
    yield "This"
    yield "is"
    yield "Pyhton"
    print("stop")


for line in after_yeild():
    print(line)
