# Python RegEX Functions:

import re

# The "re" module functions.
# For more information about all the "re" module functions, check below link:
# https://docs.python.org/3.11/library/re.html#functions

# 1. "search" returns a match object if there is a match anywhere in the
# string.
my_string = "Hello, welcome to Learn Python Professionally, Python is a\
 powerful programming language."

str_search = re.search("Python", my_string)
# str_search = re.search("python", my_string)
print(str_search)

# To get the word indices:
# print(str_search.span())
# print(str_search.start())
# print(str_search.end())

# The "search" returned the first "Python" word:
# print(my_string[24:30])

# 2. "findall" returns a list containing all matches.
# Returns an empty list if there is no match.
# str_findall = re.findall("Python", my_string)
str_findall = re.findall("on", my_string)
# print(str_findall)


# 3. "split" returns a list where the string has been split at each match.
str_split = re.split("Python", my_string)
# print(str_split)

# 4. "sub" replaces one or many matches with a string
str_sub = re.sub("Python", "JavaScript", my_string)
# print(str_sub)
