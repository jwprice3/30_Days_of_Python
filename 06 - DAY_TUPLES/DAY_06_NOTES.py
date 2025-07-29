################################
# Title: 30 Days of Python
# Description: Tuples
# Change Log:
# JP, Created, 7.17.25
################################

# 4 types of Data types
    # List
    # Tuple
        # A collection which is ordered and unchangeable or unmodifiable(immutable). 
        # Allows duplicate members.
        # Related to count()
        # Related to index()
    # Set
    # Dictionary

# How to create a tuple
    # Tuple are represented by ()
    # entries in a list a seperated by a , (comma)

print('Begin: What determines a Tuple.')
# <variable> = () or <variable> = tuple()
empty_tuple = ()
empty_tuple = tuple()
tpl = ('item1','item2','item3')
fruits = ('banana','orange','mango','lemon')
print('End: What determines a Tuple.')

print('Begin: How to determine a tuple length')
# print(len(<variable/tuple>))
tpl = ('item1','item2','item3')
print(len(tpl))
print('End: How to dertime a tuple length')

print('Begin: How to index tuples postive or negative.')
# <variable/tuple>[<integer>] or 
fruits = ('banana','orange','mango','lemon') #index values (-4,-3,-2,-1)
first_fruit = fruits[0]
last_fruit = fruits[-1]
print(first_fruit)
print(fruits[1])
print(last_fruit)
print('End: How to index tuples positive or negative')
