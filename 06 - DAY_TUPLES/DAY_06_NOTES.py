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

print('Begin: How to index tuples postive or negative numbers.')
# <variable/tuple>[<integer><begin>:<step>:<end>]]
# this
fruits = ('banana','orange','mango','lemon') #index values (-4,-3,-2,-1)
first_fruit = fruits[0]
last_fruit = fruits[-1]
print(first_fruit)
print(fruits[1])
print(last_fruit)
print('End: How to index tuples positive or negative')

print('Begin: How to slice a tuple with with positive and negative numbers.')
# <variable/tuple>[integer<begin>:<step>:<end>]
fruits = ('banana','orange','mango','lemon')
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_mango = fruits[-3:-1] # doesn't include item at index 3
orange_to_the_rest =fruits[1:]
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)
print('End:  How to slice a tuple with with positive and negative numbers.')

print('Begin: How to change from a tuple to a list and vice versa.')
# <variable/tuple> = <<input desired data structure type><list/tuple>(variable/tuple)
fruits = ('banana','orange','mango','lemon')
print(fruits)
print(type(fruits))
fruits = list(fruits)
print(type(fruits))
print('End: How to change from a tuple to a list and vice versa.')

print('Begin: How to check if an an item exist in a Tuple.')
# print('<item name>"" in <variable/tuple)
# boolean logic
fruits = ('banana','orange','mango','lemon')
print('orange' in fruits)
print('apple' in fruits)
print('End: How to check if an an item exist in a Tuple.')

print('Begin: How to join tuples.')
# <new variable/tuple> = tuple1 + tuple2
fruits_1 = ('banana','orange','mango','lemon')
fruits_2 = ('strawberry','grape','watermelon','mango')
fruits_3 = fruits_1 + fruits_2 
print(fruits_3)
('End: Begin: How to join tuples.')

print('Begin: How to delete a tuple.')
# del <variable/tuple>
fruits = ('banana','orange','mango','lemon')
del fruits
# print(fruits) 
# NameError: name 'fruits' is not defined. Did you mean: 'fruits_1'?
print('End: How to delete a tuple.')
