# ----------------------------------- #
# Title: 30 Days of Python
# Description: Day 4 Exercises
# ChangeLog: 
# JP, Created, 5.23.25
# ----------------------------------- #

print('Question 1: Concatenate the string ''Thirty'', ''Days'', ''Of'', ''Python'' to a single string')
thirty = 'Thirty'
days = 'Days'
of = 'Of'
python = 'Python'
space = ' '
print(thirty + space + days + space + of + space + python)

print('Question 2:Concatenate the string ''Coding'', ''For'' , ''All'' to a single string, ''Coding For All'' ')
coding = 'Coding'
for_for = 'For'
all = 'All'
coding_for_all = 'Coding', 'For' , 'All'
print(f'{coding} {for_for} {all}')

print('Question 3: Declare a variable named company and assign it to an initial value "Coding For All" ')
company = 'Coding For All'

print('Question 4 Print the variable company using print()')
print(company)

print('Question 5: Print the length of the company string using len() method and print()')
print(len(company))

print('Question 6:Change all the characters to uppercase letters using upper() method')
print(company.upper())

print('Question 7: Change all the characters to lowercase letters using lower() method')
print(company.lower())

print('Question 8:Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.')
print('I used capatlize():',company.capitalize()) # Note this reversed 'For' and 'All'
print('I used title():', company.title()) # no change to the varable
print('I used swapcase():', company.swapcase())

print('Question 9: Cut(slice) out the first word of Coding For All string.')
print(len(company))
print(len('Coding'))
# take result and calculate
slice_coding = company[0:6]
print(slice_coding)

print('Question 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.')
print(len(company))
print(len('Coding'))
coding = company[0:6]
print(coding) # This way checks if the characters are actually there
# or
print(company.find("Coding")) # This checks if the value actually there by stating its place in the string

print('Question 11: Replace the word coding in the string ''Coding For All'' to Python for Everyone.')
print('The variable value for company is:',company)
print(company.replace('Coding For All','Python for Everyone')) # comma is necessary

print('Question 12: Change Python for Everyone to Python for All using the replace method or other methods.')
company = 'Python for Everyone'
print('The variable value for company is:',company)
print(company.replace('Everyone','All'))

print('Question 13: Split the string ''Coding For All'' using space as the separator (split())')
company = 'Coding For All'
print(company.split())

print('Question 14:"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma. ')
print(("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon").split())

print('Question 15:What is the character at index 0 in the string Coding For All.')
print(company.index('Coding For All'))

print('Question 16: What is the last index of the string Coding For All.')
print(company.index('ll'),'Add +2 spaces to the end of the number, that equals 14.') 
print(len(company))

print('Question 17: What character is at index 10 in "Coding For All" string')
print(company.index('Coding For All'))

print('Question 18: Create an acronym or an abbreviation for the name ''Python For Everyone''')
poe = 'Python For Everyone'
print(str(poe))

print('Question 19: Create an acronym or an abbreviation for the name ''Coding For All''')
coe = company
print(str(coe))

print('Question 20: Use index to determine the position of the first occurrence of C in Coding For All.')
print(company.index('C'))

print('Question 21: Use index to determine the position of the first occurrence of F in Coding For All.')
print(company.index('F'))

print('Question: Use rfind to determine the position of the last occurrence of l in Coding For All People.')
company = 'Coding For All People'
print(company.index('l'), 'Is the first occurrence')
print(company.rindex('l'),'Is the last occurrence')

print('Question 23: Use index or find to find the position of the first occurrence of the word ''because'' in the following sentence: ''You cannot end a sentence with because because because is a conjunction')
find_because = 'You cannot end a sentence with because because because is a conjunction'
print(find_because.index('because'))
# or
print(('You cannot end a sentence with because because because is a conjunction').index('because'))

print('Question 24: Use rindex to find the position of the last occurrence of the word because in the following sentence: ''You cannot end a sentence with because because because is a conjunction''')
rindex_example = 'You cannot end a sentence with because because because is a conjunction'
print(rindex_example.rindex('conjunction'))

print('Question 25: Slice out the phrase' '''because because because'''  'in the following sentence:' '''You cannot end a sentence with because because because is a conjunction''')
slice_example = 'You cannot end a sentence with because because because is a conjunction'
print(slice_example.index('because'))
print(slice_example.rindex('because'))
print(slice_example[31:54])

print('Question 26: Find the position of the first occurrence of the word "because" in the following sentence: "You cannot end a sentence with because because because is a conjunction"')
first_occurence = 'You cannot end a sentence with because because because is a conjunction'
print(first_occurence.find('because'))

print('Question 28: Does ''Coding For All'' start with a substring Coding?')
print(company.startswith('Coding'))

print('Question 29: Does "Coding For All" end with a substring coding')
print(company.endswith('coding'))

print('Question 30: '   'Coding For All'      '  , remove the left and right trailing spaces in the given string ')
print('''   Coding For All      '''.strip('  '))

print("Question 31: Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python")
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

print("Question 32: The following list contains the names of some of python libraries: "'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'" ''Join the list with a hash with space string.")
my_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(my_list)
print(' # '.join(my_list))

print('Question 33: Use the new line escape sequence to separate the following sentences. I am enjoying this challenge. I just wonder what is next.')
print('I am enjoying this challege.\n''I just wonder what is next.')

print('Question 34: Use the tab escape to write the following lines Name: Justin, Age:250, Country:Finland, City:Helsinki')
print('Name\tAge\tCountry\tCity\t\nJustin\t250\tFinlad\tHelsinki')

print('Question 35: Use the string formatting method to display the following:\nradius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.')
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square')

print('8 + 6 = 14\t8 - 6 = 2\t8 * 6 = 48\t8 / 6 = 1.33\t8 % 6 = 2\t8 // 6 = 1\t8 ** 6 = 262144')
a = 6
b = 8
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{b} ** {a} = {b ** a}')