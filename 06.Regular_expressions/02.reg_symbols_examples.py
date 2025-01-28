# How to write regular expressions?
import re


# Note: You can use any RegEx function with patterns you will create from the
# RegEx characters:

# 1. The asterisk character "*":

pattern_astrisk = re.compile("ab*c")

my_string = "ac, abc, abbc, abbbc, ebbf, ebbbr"

str_asterisk = pattern_astrisk.findall(my_string)
# print(f"Using astresk: {str_asterisk}")

#####################################################

# 2. The Plus character "+":

pattern_plus = re.compile("ab+c")

my_string = "ac, abc, abbc, abbbc, ebbf, ebbbr"

str_plus = pattern_plus.findall(my_string)
# print(f"Using plus: {str_plus}")

#####################################################

# 3. The curled brackets "{ … }":

my_string = "ac, abc, abbc, abbbc, ebbf, ebbbr"

# pattern_curl = re.compile("ab{2}c")
pattern_curl = re.compile("ab{0,3}c")

str_curl = pattern_curl.findall(my_string)
# print(f"Using curled brackets: {str_curl}")

#####################################################

# 4. Wildcard ".":

my_string = "ac, abc, abbc, abbbc, axc, ebbf, ebbbr"

# pattern_wild = re.compile("a.c")
# pattern_wild = re.compile("a.*c")
# pattern_wild = re.compile("a.{1,3}c")
pattern_wild = re.compile(".b+.")

str_wild = pattern_wild.findall(my_string)
# print(f"Using wildcard: {str_wild}")

#####################################################

# 5. Question mark character "?":
pattern_ques = re.compile("xlsx?")

text_data = "The file name is data.xls or data.xlsx data.xlsxx"

str_ques = pattern_ques.findall(text_data)
# print(f"Using question mark: {str_ques}")

#####################################################

# 6. The caret "^" character:

pattern_caret = re.compile("^Excel.")

start_with = "Excel1 file extension is xls or xlsx\
that is how you save an Excel2.\n\
Excel3 file"

str_caret = pattern_caret.findall(start_with)
# print(f"Using the caret: {str_caret}")

#####################################################

# 7. The dollar character "$":

pattern_dollar = re.compile("Excel.$")

end_with = "Excel1 file extension is xls or xlsx\
that is how you save an Excel2.\n\
\n\
Excel3 ww"

str_dollar = pattern_dollar.findall(end_with)
# print(f"Using dollar: {str_dollar}")

#####################################################

# 8. Special Characters:
# a. \s and \S

pattern_bs = re.compile(r"\s")
pattern_BS = re.compile(r"\S")
# The "r" at the beginning of a string pattern designates a “raw” string,
# treating the "\" to be used as a backslash not as an escape character.

str_bSs = "Hello, how are you?"

space_tab = pattern_bs.findall(str_bSs)
space_non = pattern_BS.findall(str_bSs)
# print(f"Using '\\s' to find whitespace and tabs: {space_tab}")
# print(f"Using '\\S' to find non whitespace characters: {space_non}")

# -----------------------------------------------------

# b. \d and \D

pattern_bd = re.compile(r"\d")
pattern_BD = re.compile(r"\D")
# The "r" at the beginning of a string pattern designates a “raw” string,
# treating the "\" to be used as a backslash not as an escape character.

str_bDd = "The temperature is 35.6 degrees centigrade #$"

digits_num = pattern_bd.findall(str_bDd)
space_non = pattern_BD.findall(str_bDd)
# print(f"Using '\\d' to find digits: {digits_num}")
# print(f"Using '\\D' to find non digits characters and spaces: {space_non}")

# -----------------------------------------------------

# c. \w and \W

pattern_bw = re.compile(r"\w")
pattern_BW = re.compile(r"\W")
# The "r" at the beginning of a string pattern designates a “raw” string,
# treating the "\" to be used as a backslash not as an escape character.

str_bWw = "The temperature is 35.6 degrees centigrade !$&_"

any_word = pattern_bw.findall(str_bWw)
non_word = pattern_BW.findall(str_bWw)
# print(f"Using '\\w' to find digits and word characters and '_' : {any_word}")
# print(f"Using '\\W' to find non word character and whitespace: {non_word}")

# -----------------------------------------------------

# d. \b and \B

# pattern_bb = re.compile(r"\btem.")
pattern_bb = re.compile(r"grees.\b")
pattern_BB = re.compile(r"\Btem.")
# The "r" at the beginning of a string pattern designates a “raw” string,
# treating the "\" to be used as a backslash not as an escape character.

str_bBb = "The tem1perature is 35.6 degrees1 centigrade, he agrees2 the\
 tem2perature is high degrees3 hello_tem3 eve_tem4_rr "

beg_end = pattern_bb.findall(str_bBb)
not_beg_end = pattern_BB.findall(str_bBb)
# print(f"Using '\\b' to find any characters at the beginning or at the end of\
# #  a word: {beg_end}")
# print(f"Using '\\B to find any characters not at the beginning or at the end\
# of a word: {not_beg_end}")

# -----------------------------------------------------

# e. \A

pattern_BA = re.compile(r"\AThe.")
# The "r" at the beginning of a string pattern designates a “raw” string,
# treating the "\" to be used as a backslash not as an escape character.

str_BA = "The1 temperature is 35.6 degrees Centigrade. The2 temperature is \
high.\n\
The3"

beg_str = pattern_BA.findall(str_BA)
# print(f"Using '\\A' to find characters at the beginning of a string:\
#  {beg_str}")

#####################################################

# 9. Set of Characters []:
# a. [aty] or [235]
pattern_spec = re.compile("[atyT]")
# pattern_spec = re.compile("[ATY]")
# pattern_spec = re.compile("[235]")

str_spec = "The temperature is 35.6 degrees Centigrade."

spec_char = pattern_spec.findall(str_spec)
# print(f"Using specific characters or digits: {spec_char}")

# -----------------------------------------------------

# b. [a-z] or [0-9]
pattern_range = re.compile("[a-n]")
# pattern_range = re.compile("[A-N]")
# pattern_range = re.compile("[0-5]")

str_range = "The temperature is 35.6 degrees Centigrade. It is Hot"

range_char = pattern_range.findall(str_range)
# print(f"Using range: {range_char}")

# -----------------------------------------------------

# c. [^aty]
pattern_not = re.compile("[^aty]")
# pattern_not = re.compile("[^TI]")

str_not = "The temperature is 35.6 degrees Centigrade. It is Hot"

range_not = pattern_not.findall(str_not)
# print(f"Except specific characters: {range_not}")

# -----------------------------------------------------

# d. [0-9][0-9]
pattern_two = re.compile("[0-4][0-9]")


str_two = "35.6 degrees Centigrade is 96.08 degrees Fahrenheit."

range_two = pattern_two.findall(str_two)
# print(f"Checking two numbers: {range_two}")

# -----------------------------------------------------

# e. [a-zA-Z] or [a-zA-Z0-9]
# pattern_diff_range = re.compile("[a-eA-H]")
pattern_diff_range = re.compile("[c-h4-9]")

str_diff_range = "35.6 degrees Centigrade is 96.08 degrees Fahrenheit."

range_diff = pattern_diff_range.findall(str_diff_range)
# print(f"Checking different range of characters and digits: {range_diff}")

#####################################################

# 10. The Escape Symbol "\":

pattern_escape = re.compile(r"[+-]\d+\.\d+")

str_escape = "+35.6 degrees Centigrade is -96.08 degrees Fahrenheit."

escape_char = pattern_escape.findall(str_escape)
# print(f"Using Escape \\: {escape_char}")

#####################################################

# 11. Vertical Bar "|":

pattern_either = re.compile("35.6|no")
# pattern_either = re.compile("[A-Z]|[0-9]")


str_either = "35.6 degrees Centigrade is 96.08 degrees Fahrenheit."

either_bar = pattern_either.findall(str_either)
# print(f"Using Vertical Bar: {either_bar}")

#####################################################

# 12. Grouping the Characters & Symbols "( ... )"

pattern_group = re.compile(r"(\d{2})/(\d{2})/(\d{4})")

grouping_str = "24/05/2020"

group_all = pattern_group.match(grouping_str)

# print("Full match:", group_all.group(0))
# print("Day:", group_all.group(1))
# print("Month:", group_all.group(2))
# print("Year:", group_all.group(3))

#####################################################
