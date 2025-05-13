#---------------------------------------------#
#Title: 30 Days of Python
#Description: Operators
#ChangeLog: Justin,3.13.2025,Created Script
#---------------------------------------------#

'''
The purpose of this is to be used as a reference document for 30 days of python. Note if running on 
a cmd shell <exit()> Reference: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md
Reference: https://docs.python.org/3.9/library/functions.html
'''

'''
Tip: python operators https://www.w3schools.com/python/python_operators.asp
Tip: do not develop a habit of declaring such types of variables. Variable names should be all the time mnemonic(spelled out)
Tip: try to avoid overriding built-in functions
Tip: label your print with some string, you never know where the result is coming from

Definitions:
Boolean: A boolean data type represents one of the two values: True or False. The use of these data types will be clear once we start using the comparison operator.
The first letter T for True and F for False should be capital

Assignment Operators: Operators are used to assign values to variables.
Comparison operator: Operators to compare two values in True or False. Can be by symbol, word, or logic
'''

# Arithmetic Operations in Python
# Integers
print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

#PRACTICE
# Declaring the variable at the top first
a = 3 #interger data type
b = 2 #interger data type

#Assigning the result of a variable #Try to label your outcome
total = a + b
diff = a-b
product = a * b
division = a/b
remainder = a %b
floor_division = a//b
exponentiation = a**b


print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a + b = ', exponentiation)

#Declaring Variables and Organizing
num_one = 3
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one

print('total', total)   # having a period after a string ex <'total' . total> throws an error 
print ('difference', diff)
print('product', product)
print('division', div)

#example | radius
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

#example | area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

#Comparison
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False, "len" compares the character amount
print(len('mango') != len('avocado'))  # True,  "len" compares the character amount
print(len('mango') < len('avocado'))   # True, "len" compares the character amount
print(len('milk') != len('meat'))      # False, "len" compares the character amount
print(len('milk') == len('meat'))      # True, "len" compares the character amount
print(len('tomato') == len('potato'))  # True, "len" compares the character amount
print(len('python') > len('dragon'))   # False, "len" compares the character amount

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

# Word operators are also True or False
#is: Returns true if both variables are the same object(x is y)
print('1 is 1', 1 is 1)
print('True - because the data values are the same')
#is not: Returns true if both variables are not the same object(x is not y)
print('1 is not 2', 1 is not 2)
print('True - because 1 is not 2')
#in: Returns True if the queried list contains a certain item(x in y)
print('A in Asabeneh', 'A' in 'Asabeneh')
print('A in Asabeneh', 'a' in 'Asabeneh')
print('True - the letter <A,a> found in the string')
print('B in Asabeneh', 'B' in 'Asabeneh')
print('False - the letter <B> there is no uppercase B')
#not in: Returns True if the queried list doesn't have a certain item(x in y)
print('a in an:', 'a' in 'an')
print('True - the letter <a> is in the word <an>')
print('4 is 2 ** 2:', 4 is 2 ** 2) 
print('True - the product of of 2**2 is equal to 4')
print('5 is 2 ** 2:', 5 is 2 ** 2) 
print('False - the product of of 2**2 is not equal to 5')

#logical operators still True of False questions
print(3 > 2 and 4 > 3)
print('True - because both statements are true, making 2 out of 2 factually correct statements')
print(3 > 2 and 4 < 3)
print('False - because the second statement is false, making 1 out of 2 factually incorrect statements')
print(3 < 2 and 4 < 3)
print('False - because both statements are false, making 2 out of 2 factually incorrect statements')
print('True and True: ', True and True)
print('True - because True and True are the same')
x = 5
print(5 > 4 and x > 3)
print('True - becuase the value of 5 and x are greater than 4, making 2 out of 2 factually correct statements')
print(3 > 2 or 4 > 3)
print('True - because both statements are true, making 2 out of 2 factually correct statements')
print(3 > 2 or 4 < 3)
print('True - because one of the statements is true, meeting the requirement of 1 out of 2 factually correct statements')
print(3 < 2 or 4 < 3)  # 
print('False - because both statements are false , not meeting the requirement of 1 out of 2 factually correct statement')
print('True or False:', True or False)
print('True - because one of the statements is the value of true, meeting the requirement of 1 out of 2 factually correct statements')

#Not examples | pretty much confirms yes and no
print(not 3 > 2)
print('Lawyers speak like this, is it NOT true that 3 is bigger than 2?” Since 3 is bigger, the answer is “No, it’s not NOT true,')
print(not True)
print('False - Negation, the not operator turns true to false')
print(not False)
print('True - is printing the opposite of False')
print(not not True)  # True
print('True - If I say that I am NOT, not mad at you, that means I am mad bruv')
print(not not False) # False
print('False - Start with False ("no"). First not: not False = True ("yes"). Second not: not True = False ("no"). So, print(not not False) prints False.')
print('Here is a real world example:')
print('I am building a toy robot, my robot will rust in the rain.')
print('Rain = True if "not raining"  if it is False for "not raining" (robot stays still).')
print('No rain = False if "not raining" if it is True "not raining" (robot moves!).') 
print('In code, it might look like: move_robot(not is_raining)')