# ------------------------------------------- #
# Title: 30 Days of Python
# Description: 04 Strings
# Change Log: 
# Justin, 5.13.25, Created Script
# ------------------------------------------- #

'''
Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types.
To check the length of a string use the len() method.
'''
print('-----------------------------')
print('\\Topic: How to Create a String\\')

# A string can be a single character or a bunch')
letter = 'P' # A string can be a single character or a bunch')
print(letter) # P
print(len(letter)) # character length is 1
#  String could be made using a single or double quote,"Hello, World!"
greeting = 'Hello, World' 
# Hello, World!
print(greeting)
# character length is 12
print(len(greeting))
# A string can be a sentence
sentence = 'I hope you are enjoying 30 days of Python Challenge' 
print(sentence) # I hope you are enjoying 30 days of Python Challenge

# A string can be a block of text
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print('-----------------------------')
print('\\Topic: How to concatenate a string\\')
print('String Concatenation - is the process of merging strings together')
first_name = 'Justin'
last_name = 'Price'
space = ' '
full_name = first_name + space +last_name
# Justin Price
print(full_name)
# character length is 6
print(len(first_name))
# character length is 5
print(len(last_name))
print(len(full_name))
print('-----------------------------')

print("\\Escape Sequences in Strings\\")

# \n: new line
print('I hope everyone is enjoying the Python Challenge.\nAre you?')
# \t: Tab means(8 spaces)
print('Days\tTopics\tExercise')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
# \\: Back slash
print('This is a backlash symbol (\\)') # fyi print('(how\ bout this)') looks the same
# \': Single quote (')
print('In Every programming lanuge it starts with \'Hello, World\'')
# \": Double quote (")
print('In Every programming lanuge it starts with \"Hello, World\"')
print('-----------------------------')

print("\\Topic: Old Verion of String Formatting\\")
# %s - String (or any object with a string representation, like numbers)
# the %s is the place holder for the actual variable itself
# place the %s before the () to format within the ()
first_name = 'Justin'
last_name = 'Price'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
# %d - Integers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle witha a radius %d is %.2f.' %(radius, area) # 2 refers the the amount of spaces after the decimal
# library annotated with [] 
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)
                                                            
# %f - Floating point numbers

# "%.number of digitsf" - Floating point numbers with fixed precision
print('-----------------------------')

print("\\Topic: How to create a New Verion of String Formatting\\")
first_name = 'Justin'
last_name = 'Price'
language = 'Python'
formated_string = 'I am {} {}. i teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3
# the {} is a place holder and assumes the properties of the variable
# .format is the function that enables the brackets
# the .format goes before the variables in the parantheses 
# this is cleaner code
print('{} + {} = {}'.format(a,b, a + b)) # addition
print('{} - {} = {}'.format(a,b, a - b)) # subtraction
print('{} * {} = {}'.format(a,b, a * b)) # multiplication
# :.2f is to format a long decimal number, <number> + : (sepearates the decimal indicator) + . (indicates the decimal) + number (indicates the amount of places I want after the decimal) + f (format) + f = 3.14:.2ff
print('{} / {} = {:.2f}'.format(a,b, a / b)) # division
print('{} % {} = {}'.format(a,b, a % b)) # percentage
print('{} // {} = {}'.format(a,b, a // b)) # division with remainder 
print('{} ** {} = {}'.format(a,b, a ** b)) # exponents

print('-----------------------------')

print('\\Topic: f-strings Python 3.6+')
a = 4
b = 3
# using f' before at the beginging of the line formats the whole string
# it replaces the .format
# the variable must be placed inside the bracket
print(f'{a} + {b} = {a + b}') # addition
print(f'{a} - {b} = {a - b}') # substraction
print(f'{a} * {b} = {a * b}') # multiplication
# :.2f is to format a long decimal number, <number> + : (sepearates the decimal indicator) + . (indicates the decimal) + number (indicates the amount of places I want after the decimal) + f (format) + f = 3.14:.2ff
print(f'{a} / {b} = {a / b:.2f}') # division
print(f'{a} % {b} = {a % b}') # percentage
print(f'{a} // {b} = {a // b}') # division with remainder
print(f'{a} ** {b} = {a ** b}') # exponents
print(f'A equals {a} and B equals {b}.')
print('End of f-strings')
print('-----------------------------')

print('\\Topic: How to have Python Strings as Sequence Characters')
# to have something printed out in sequence the letters an variables must match
# Does not Work if sequence characters don't match the characters in the variable
# language = 'Python'
# a,b,c,d,e,f,g = language
# print(a)
# a,b,c,d,e,f,g = language
    # ^^^^^^^^^^^^^
    # ValueError: not enough values to unpack (expected 7, got 6)
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print('-----------------------------')

print('\\Topic: How to access characters in a string by index')
# Indexing: Accessing a single character at a specific position.
# note that python starts counting at Zero. Zero is ALWAYS the first space
# [] are used for indexing
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1] # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n


# this variable last_index uses the <len> function to index each letter
# negative indexing: the - 1 starts from the back as apposed to + 1 starts from the front
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2] # o
print(second_last)

# Slicing Python Strings
# format variable[<number>(where it starts):<number>(where it ends)]
language = 'Python'
first_three = language[0:3] 
print(first_three) #Pyt 0 is the first letter
last_three = language[3:6]
print(last_three) # hon
# another way
last_three = language[-3:]
print(last_three) # hon
last_three = language[3:0]
print(last_three) # hon

# Reverse a string
# the first : in the sequence acts as a null
greeting = 'Hello, World!'
# forward
print(greeting[::1])
# reverse
print(greeting[::-1])

# How to skip characters while slicing
language = 'Python'
# format variable[<number>(index place):<number>(index place):<number>(index place)]
# remeber each index must correspond with a character
pto = language[0:6:2]
print(pto)
print('End topic: How to access characters in a string by index')
print('-----------------------------')

print('\\Topic: How to format strings utilizing different methods')
# using .<method> is the format used to initialize the method

# How to capitalize the first letter of a string .capitalize()
challenge = 'thirty days of python'
print(challenge.capitalize()) # Thirty days of python
print('end .capatalize()')

# How to check if the STRING is a valid variable name print(<variable>).isidentifier())
# Boolean
challenge = 'thirty days of python'
print(challenge.isidentifier()) # no spaces
challenge = '30daysofpython'
print(challenge.isidentifier()) # variable can not begin with number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())
print(('end .isidentifier()'))

# How to check if the string has all lowercase alpha text print('<text>).islower())
# does not check for #'s
# Boolean
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())
challenge = '30 days of python' #
print(challenge.islower())
print('end .islower()')

# How to check if the string has all uppercase alpha text print('<text>).isupper())
# does not check for #'s
# Boolean
challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())
challenge = '30 days of python' #
print(challenge.isupper())
print('end .isupper()')


# How to join a concatenated string using print('<amount of spaces needed>.join(<variable>))
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech) # amount of spaces between '' can be changed
print(web_tech)
print(result)
print(''.join(web_tech))
print('end .join()')

# How to remove characters in a string print(<variable>.strip('<text to strip>'))
challenge = 'thirty days of python'
print(challenge.strip('th'))
print(challenge.strip('b')) # does not return error
print('end .strip()')

# How to take out and replace string characters
# Case sensitive
# Does not change stored value of variable
challenge = 'thirty days of python'
print(challenge)
print(challenge.replace('python','anaconda'))
# print(challenge.replace('python', 2)) # results in an error as it is not a string
print('end .replace()')

# How to create a title case for a string print(<variable>.title())
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
print('end .title()')

# How to do a swap case for a string, it makes capital to lowercase and vice versa print(<variable>.swapcase())
challenge = 'thirty days of python'
print(challenge.swapcase())
print('end .swapcase')

# How to check if a string starts with a specific character print(<variable>.startswith('<text>'))
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
print(challenge.startswith('Thirty')) # case sensitive
print(challenge.startswith('30')) # alphanumeric sensitive 
print('end .startswith')


# How to count the number of occurences for a given set of character
# You must include the characters .count('<character>')
challenge = 'thirty days of python'
print(challenge.count('y')) # there are 3 occurunces of 'y' in the challenge variable
# To look for a character in a a given range the format is .count('<character>',<number of pos start>,<number of pos end>) 
print(challenge.count('y',7,14)) # there is once occurence of 'y' from index pos 7 to 14
# the amount of occuronces in a given range
print(challenge.count('y',-1,-2)) # there are zero occuronces of 'y' from range -1 to -2
print(challenge.count('th')) # 2
print('end .count()')

# How to check if a string ends with specific characters using print(<variable>.endswith('<text>'))
# This is a True of False question
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False
print('end .rfind()')


# How to replace tab < \ > character with spaces print(<variable>.expandtabs(<number of desired spaces>)
challenge = 'thirty\tdays\tof\tpython'
# \t: Tab means(8 spaces)
print(challenge) 
# Default space is 8
print(challenge.expandtabs())
print(challenge.expandtabs(10))
print('end .expandtabs()')

# How to find the first ocurrence of a specific characters using print(<variable>.find(<'text'>)
challenge = 'thirty days of python'
print(challenge.find('y')) # 'y' appears at inex point 5
print(challenge.find('th')) # 'th' appears at index point 0
print('end .find()')

# How to find the last ocurrence of a specific characters using print(<variable>.find(<'text'>)
challenge = 'thirty days of python'
print(challenge.rfind('y')) # the last appearance of 'y' appears at inex point 16
print(challenge.rfind('th')) # the last appearance of 'th' appears at index point 17 
print('end .rfind()')

# How to find the lowest occurence of specific characters print(<variable>.index(<sub string variable or <'text'>,<specified index>))
# Specfied index not necessary 
# Often used for list
# Boolean Logic
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
# print(challenge.index(sub_string,9)) results in error because it is not in that position
print(challenge.index('da'))
print('end .index()')

# How to find the highest occurence of specific characters print(<variable>.rindex(<sub string variable or <'text'>))
# Often used for list
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))
print(challenge.rindex('on', 8)) #19 
print('end .rindex()')

# How to create a list from a variable print(<variable>.split())
# Eacg word will be an entry into a list []
print(challenge.split())
print('end .split()')

# How to check if a string or variable is alphanumeric print(<variable>.isalnum(<accepts index>))
# Boolean Logic
# spaces not alllowed
challenge = 'thirty days of python' # False
# A space is not alpha or numeric and will result in False
print(challenge.isalnum())
challenge = 'Thirtydaysofpython' 
print(challenge.isalnum()) 
challenge = 'Thirtydaysofpython19' 
print(challenge.isalnum()) # True 19 is numeric
print('end .isalnum()')

# How to check if string or variable is only alphabetical characters print(<variable>.isalpha(<accepts index>))
# Boolean Logic
# spaces not alllowed
challenge = 'thirty days of python'
# A space is not alpha or numeric and will result in False
print(challenge.isalpha())
challenge = 'Thirtydaysofpython'
print(challenge.isalpha())
print('end .isalpha()')

# How to check if string or variable is are decimal characters print(<variable>.isdecimal())
# check from 0 - 9
# spaces not alllowed
challenge = 'thirty days of python'
print(challenge.isdecimal())
challenge = '1234'
print(challenge.isdecimal())
challenge = '10.5'
print(challenge.isdigit()) # does not accept 10.5
print('end .isdecimal()')
# print(challenge.isdecimal('123',0)) # does not take argruments
# print(challenge.isdecimal('12')) # does not take argruments

# How to check if string or variable is are digit characters print(<variable>.isdigit())
# check from 0 - 9
# spaces not alllowed
challenge = 'thirty days of python'
print(challenge.isdigit())
challenge = '1234'
print(challenge.isdigit())
challenge = '10.5'
print(challenge.isdigit()) # does not accepts 10.5
print('end .isdigit()')

# How to check if string or variable is are numeric characters print(<variable>.isdigit())
# check from 0 - 9
# spaces not alllowed
challenge = 'thirty days of python'
print(challenge.isdigit())
challenge = '1234'
print(challenge.isdigit())
challenge = '10.5'
print(challenge.isdigit()) # des not accepts 10.5
print('end .isnumeric()')

# How to use regex (regular expression)
#import re
#pattern = "^Coding"
#re.search(pattern, string)

# How 