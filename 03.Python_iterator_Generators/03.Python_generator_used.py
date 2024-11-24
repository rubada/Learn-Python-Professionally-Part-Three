# Python Generators

# Generator Performance:
# 1. Using generators with large data.
# Generators are faster when dealing with large data.
# Let's take an example:
import csv
import time
import sys


# a. Create a function and a generator that open a "CSV" (Comma Separated
# Values) file, with "reader()", which is used to read the "CSV" file row by
# row with a "for" loop:

def csv_file_func(file_name):
    file = open(file_name, "r")
    data = csv.reader(file)
    return data


def csv_file_gen(file_name):
    file = open(file_name, "r")
    data = csv.reader(file)
    for line in data:
        yield line


# b. Let's calculate the time that the function and the generator take to read
# a "CSV" file, we will use the "time" module with the "perf_counter()" method:

def count_lines(data):
    count_lines = 0
    time_start = time.perf_counter()
    for line in data:
        count_lines += 1
    time_end = time.perf_counter()
    time_take = time_end - time_start
    return count_lines, time_take


read_csv_func = csv_file_func("./large_date.csv")
# print(read_csv_func)
# for line in read_csv_func:
#     print(line)

read_csv_gen = csv_file_gen("./large_date.csv")
# print(read_csv_gen)
# for line in read_csv_gen:
#     print(line)

# print("Function lines count:", count_lines(read_csv_func)[0])
# print("Function time to read in sec:", count_lines(read_csv_func)[1])

# print()

# print("Generator lines count:", count_lines(read_csv_gen)[0])
# print("Generator time to read in sec:", count_lines(read_csv_gen)[1])


# Let's store the data in a tuple and a generator and check their object
# size in bytes.
# We will use "sys.getsizeof()", that returns the size of an object in bytes:

data_tuple = tuple(line for line in csv_file_func("./large_date.csv"))
tuple_object_size = sys.getsizeof(data_tuple)
# print(f"Data size when stored as tuple {tuple_object_size} bytes")

print()

data_gen = (line for line in csv_file_func("./large_date.csv"))
gen_object_size = sys.getsizeof(data_gen)
# print(f"Data size when stored as generator {gen_object_size} bytes")


# As shown above the generator took less time to read the large file because
# the generator doesn't store all the data in memory. That's why generators are
# efficient when reading large data sets.


# 2. Using generators with infinite sequence.
# The same thing as large data, when using generators with infinite sequence.

def counter_gen():
    num = 0
    while True:
        yield num
        num += 1


data_inifinite = counter_gen()
# print(data_inifinite)

# print(sys.getsizeof(data_inifinite))

# As shown above, using a generator with an infinite loop will not store all
# the data in the generator object, and the data will be returned one value at
# a time, which is why the data size is small.

for i in data_inifinite:
    print(i)

# 3. Fetching data from external data sources: When working with external data
# sources like APIs or databases or a real time data such sensors, generators
# can be used to fetch data in chunks, reducing memory usage and improving
# performance.

# 4. In data processing pipelines, generators can be used to transform, filter,
# or aggregate data as it flows through different stages.
# Imagine you’re processing a large log file. Instead of loading the entire
# file into memory, you can create a generator that reads lines one by one.
# Each stage of your pipeline (e.g., filtering out specific entries,
# extracting relevant information) can be implemented as a separate generator
# function.
# This approach keeps memory usage low and allows you to process data
# incrementally.
