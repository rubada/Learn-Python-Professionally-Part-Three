import re

text = "Hello, if have any problem with the project, \
please contact us:\n\
email: info+4_@example.com\n\
technical department email: tech.2003@example.com\n,\
phone number: 0056 55 6755677\n\
you can contact us on the above number from:\n\
      Monday to Friday\n\
      8:00 to 17:30\
The above information will be updated on February 10, 2024 \
and on 10-10-2024 or 10/10/2024"

#####################################################
# Finding the emails:
pattern_email = re.compile(r"\S+@\S+")
# pattern_email = re.compile(
#     r"[a-zA-Z-0-9._+-]+@[a-zA-Z-0-9._+-]+\.[a-zA-Z-0-9._+-]+"
#     )
find_emails = pattern_email.findall(text)
# print(find_emails)

#####################################################

# Finding the times:
pattern_time = re.compile(r"\d+:\d+")
find_time = pattern_time.findall(text)

# print(find_time)

#####################################################

# Finding the dates:
pattern_date = re.compile(r"[a-zA-Z]+\s\d+,\s\d+|\d+-\d+-\d+|\d+/\d+/\d+")
# Another simpler pattern:
# pattern_date = re.compile(r"[a-zA-Z]+\s\d+,\s\d+|\d+[-/]\d+[-/]\d+")
find_date = pattern_date.findall(text)

# print(find_date)

#####################################################

# Grouping the phone number
pattern_group = re.compile(r"(\d+)\s(\d+)\s(\d+)")
search_group = pattern_group.search(text)

# print(search_group.group())
# print(search_group.group(1))
# print(search_group.group(2))
# print(search_group.group(3))
