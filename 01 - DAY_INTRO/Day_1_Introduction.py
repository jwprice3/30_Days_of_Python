# ------------------------------------------------- #
# Title: 30 Days of Python - Introduction
# # Description: Intro & Simple Math
# ChangeLog: Justin,2.25.2025,Created Script
# ------------------------------------------------- #

'''
The purpose of this is to be used as a reference document for 30 days of python. Note if running on 
a cmd shell <exit()> Reference: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme.md#introduction
'''

''' 
Tips

Tip: python uses indentation to create blocks of code ex. <enter> then <tab>
Tip: <#> excludes the text and or code
Tip: code will not give an output with out a print()
Tip: to exit the shell type exit()
Tip: type(<variable) will display the data type
'''
"""
Definitions

Integer: negative and positive numbers 
    
Float: Decimal number

Complex Notation: a + bj a<real number> + b<imaginary> j(imaginary unit √-1)

String: A collection  of one or more characters under a single ' ' or double qoute " ". 
Even as a varaible it needs to be in qoutes.
    
Boolean: A data type that is True of False. It is case sensitive 

List: An ordered collection which allows to store different data types. A list can indlucde multiple
data types. Data contained in [] indicates a list.

Dictionary: A python object(Day 21) is an underscored collection of data in a key va
dictionary {} can indlucde multiple data types.

Tuple: A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
It can only store unique items. The order is not important.

Set: A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics,
"""
#Integers
integer_example = -3
print(-3, -2, -1, 0, 1, 2, 3)
print(type(integer_example))

#Float
decimal_example = -3.5
print(-3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5)
print(type(decimal_example))

#Boolean
yes = True
no = False
print(yes)
print(no)
print(type(yes))

#complex numbers
c1 = complex(3, 4) #(3+4j)
c2 = complex(5) #(5+0j)
c3 = complex() #0j

print(c1)
print(c2)
print(c3)
print(type(c1))

#String
print("I love python") #needs qoutes

#Simple Math
print(2 + 5) #spacing does not matter could be 2+5
print(3 - 2)
print(3 *2) # use <*> instead of x for multiplication
print(3/2) #use </> for division
print(3 % 2) # <%> is used to find the remainder/modulus
print(3//2) # <//> is floor division which means it returns the quotient and rounds down the nearest whole integer.
print(3**4) # ** is exponents three to the fourth power

#List
list_example = ([0, 1, 2, 3, 4, 5]) 
print([0, 1, 2, 3, 4, 5])  # all are the same data types - a list of numbers
print(['Banana', 'Orange', 'Mango', 'Avocado']) # all the same data types - a list of strings (fruits)
print(['Finland','Estonia', 'Sweden','Norway']) # all the same data types - a list of strings (countries)
print(['Banana', 10, False, 9.81]) # different data types in the list - string, integer, boolean and float)
print(type(list_example))

#Dictionary
character_one = {
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python'] #stores info about character_one
}
print(type(character_one))

#Tuple
tuple_example = ('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya')
print('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
print(type(tuple_example))

#Set
print({2,4,3,5})
print({3.14, 9.81, 2.7})