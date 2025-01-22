# Python RegEX

import re

# The "re" module functions, cont'd:
# For more information about all the "re" module functions, check below link:
# https://docs.python.org/3.11/library/re.html#functions

# 5. "compile" is used to compile a regular expression pattern into a regex
# pattern object. This allows us to reuse the pattern for multiple times,
# without repeating the same pattern.
my_string = "Hello, welcome to Learn Python Professionally, Python is a\
 powerful programming language."

pattern = re.compile("Python")

str_search1 = pattern.search(my_string)
# print(str_search1)

str_split1 = pattern.split(my_string)
# print(str_split1)

# Why use compile()?
# a. Efficiency: If you need to use the same regular expression multiple times
# compiling it first improves performance, especially in loops

# b. Readability: It allows you to keep your regex pattern separate from the
# other regex functions such as "search", etc.

# c. Reusability: Once compiled, you can use the regex object multiple times
# with different regex functions.

# 6. "fullmatch" if the whole string matches the regular expression pattern,
# it will return a corresponding match, otherwise, it will return "None".
my_string = "Hello, welcome to Learn Python Professionally, Python is a\
 powerful programming language."

pattern1 = re.compile("Hello, welcome to Learn Python Professionally, Python\
 is a powerful programming language.")

str_fullmatch1 = pattern1.fullmatch(my_string)
print(str_fullmatch1)
# print(my_string[0:89])

pattern2 = re.compile("Welcome, Hello to Learn Python Professionally, Python\
 is a powerful programming language.")

str_fullmatch1 = pattern2.fullmatch(my_string)
print(str_fullmatch1)
