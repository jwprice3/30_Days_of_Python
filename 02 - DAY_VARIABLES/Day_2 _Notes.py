# ------------------------------------------------- #
# Title: 30 Days of Python 
# Description: Built in Functioons
# ChangeLog: Justin,3.4.2025,Created Script
# ------------------------------------------------- #


'''
The purpose of this is to be used as a reference document for 30 days of python. Note if running on 
a cmd shell <exit()> Reference: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md
Reference: https://docs.python.org/3.9/library/functions.html
'''

'''
Tip: to get help type help(<python keyword>)
Tip: dir(((<python keyword>)))
Tip: len(<vairable>) will give the amount of character spaces the variable has 
Tip: input() allows the user to pass in data
Tip: to quit help() press<q>
Error: SyntaxError: invalid syntax File "<stdin>", line 1
    A: Terminal for some reason is not executing in python, close and reopen

Definitons
help: ython provides detailed information about objects, modules, or functions. It retrieves documentation from docstrings and built-in
references to explain how different components work.
dir: ries to return a valid list of attributes of the object it is called upon. Also, dir() function behaves rather differently with different type of objects, as it aims to produce the most relevant one, 
rather than the complete information. 

Variables: store data in a computer memory. They are case sensitive. It can not have a number, special character or hyphen at the begining.
The equal sign is an assignment operator. Assigning mea

Casting: Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error.

'''
#help https://www.geeksforgeeks.org/python-difference-between-dir-and-help/
o = 35
help('keywords')
help(print)
help(print(o))



#dir
dir_function = 1
print(dir())
print("space")
print(dir(dir_function))

#variable name formats
firstname = "J"
first_name = 'P'
_first_name = 'JP'
num1 = 1
print(_first_name)

#variables in Python
firstname = "Justin"
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS']
personal_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

#Print length of a variable
print(firstname)
print('First name length:', len(firstname))
print(len(firstname))

#multiple variables on one line
first_name_1, last_name_1, country_1, age_1, is_married_1 = 'Mark', 'Andrews', 'Helsink', 250, True
print(first_name_1)
print(last_name_1)


#input
first_name_2 = input('What is your name: ')
age_3 = input('How old are you? ')
print(first_name_2)
print(age_3)

#checking data type
print(type('J'))   #str
print(type(personal_info))  #dict
print(type(skills)) #list

#casting data
#int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']



