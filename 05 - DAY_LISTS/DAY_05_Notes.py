# ----------------------------------- #
# Title: 30 Days of Python
# Description: List
# Change Log:
# JP, Created, 6.11.2025
# JP, Updated, 6.25.2025
# ----------------------------------- #


# 4 types of Data types
    # List
        # a collection which is ordered and changeable(modifiable). 
        # Allows duplicate members.
    # Tuple
    # Set
    # Dictionary

print('Begin: What determines a list')
    # List are represented by [] (brackets)
    # entries in a list a seperated by a , (comma)
    # brackets can be put inside list
list = list()
lst = []
list_2 = ['Justin', 250, True, {'country':'Finland','city':'Helsinki'}]
print(list_2)
print('End: What determines a list.')

# How to create a list <variable> = [<alphanumeric>,<alphanumeric>]
print('Begin: How to create a list.')
fruits = ['bananas', 'orange', 'mango', 'lemon' ]
vegatbles = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrort']
animal_products = ['milk','meat', 'butter', 'yogurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Estonia', 'Denmark', 'Sweeden','Norway']
print('End: How to create a list.')

# How to print a list print(<list name>)
print("Begin: How to print a list")
print('Fruits:',fruits) 
print('Number of fruits:', len(fruits))
print('Vegatables:',vegatbles) 
print('Number of vegetables:', len(vegatbles))
print('Animal Products:',animal_products) 
print('Number of Animal Products:', len(animal_products))
print('Web Techs:',web_techs) 
print('Number of Web Techs:', len(web_techs))
print('Countries:', countries)
print('Number of Countries:', len(countries))
print('End: How to print a list')

# How to use positive index list fruits = ['<entry><0 place>','<entry><1 place>','<entry><2 place>']
# index starts from 0 moves to the right unless told otherwise
# slice step can not be zero
print('Begin: How to do positive and negative indexing.')
fruits = ['bananas', 'orange', 'mango', 'lemon' ]
first_fruit = fruits[0]
second_fruit = fruits[1]
last_fruit = fruits[2]
print(first_fruit)
print(second_fruit)
print(last_fruit)
# or
print(fruits[0])
print(fruits[1])
print(fruits[2])

# How to use negative index list fruits = ['<entry><0 place>','<entry><1 place>','<entry><2 place>']
# starts from the left but moves to the right unless specified
fruits = ['bananas','orange','mango','lemon']
first_fruit = fruits[-4]
second_fruit = [-3]
last_fruit = [-1]
#or
print(fruits[-4])
print(fruits[-3])
print(fruits[-1])
print('End: How to do negative and negative indexing.')

# How to unplack items in a list,  <variable/item1>,<variable/item2>, <*>(wilcard)<list name>
# print(<variable/item1>), print(<variable/item1>), print(rest)
# this will unpack the rest of the list
print('How to unpack items in a list.')
fruits = ['banana','orange','mango','lemon','lime'] 
first_fruit, second_fruit, third_fruit, *rest_of_fruit = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest_of_fruit)
# or 
# print(<variable/item1>), print(<variable/item2>), print(rest), print(<variable/item5>)
# this will unpack the rest of the list until a new variable needs to be unpacked
first,second,third,*rest_of_numbers, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest_of_numbers)
print(tenth)
# or
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia',]
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
print(countries)
print('End: How to unpack items in a list.')

print('Begin: How to slice items in a list.')
# How to slice items from a list. <list variable> = <new list variable>[start:end:step]
# positive and negative slicing
# index starts from 0
# slice step can not be zero
fruits = ['banana','orange','mango','lemon']
all_fruits = fruits[0:4] #  returns all fruits
all_fruits_v2 = fruits[0:] # starts from 0 and prints the rest becuase there is no stopping point
orange_and_mango = fruits[1:3] # does not include the first index
orange_mango_lemon_b = fruits[1:0] # only returns brackets
orange_mango_lemon = fruits[1:] # starts from first index
orange_and_lemon = fruits[::2] # starts 0 index, goes to the end, Does every 2nd step
print(all_fruits)
print(all_fruits_v2)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)
# or
fruits = ['banana','orange','mango','lemon']
print(fruits[-4]) # returns the first index left to right starts at the begining and goes forward
print(fruits[-4:]) 
print(fruits[:-4]) # returns brackets -4 is the same as index 0, it means “start at the beginning and stop before the beginning”
print(fruits[-3:-1])
print(fruits[-3:-2]) # stops at -2 index but does not include
print(fruits[-3:]) # starts at -3 and goes forward
print(fruits[::-1]) # list it in reverse order
print(fruits[-1::-3]) # starts at the end of the list and moves left because of -
print('End: How to slice items in a list.')

print('Begin: How to modify list.')
# How to modify list. <list/variable>[index place] = <new list item[start:end:step]>. 
# Replaces the item one for one
# index starts from 0
# slice step can not be zero
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits[0] = 'avacado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)
fruits[0::2] = 'blueberry', 'raspberry'
print(fruits)
print('End: How to modify list.')

print('Begin: How to check if an item in a list.')
# How to check if an item exist in a list <variable> = 'string'/integer in <list variable> or print(string/variable in <list variable>)
# Uses comparison operators
# Booleon Logic
fruits = ['banana','orange','mango','lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)
print('lime' or 'apple' in fruits)
# or
print('lime' in fruits)
print('End: How to check if an item is in a list ')

print('Begin: How to append items to a list.')
# How to add/append items to a list <list variable>.append(<string or integer>)
# method
# can not append inside a print statement
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)
print('End: How to append items in to a list.')

print('Begin: How to insert an item in to a list')
# How to insert an item to a list. <list variable>.insert(<index>,string or integer)
# method
# can not insert inside a print statement
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits.insert(0,'watermelon')
print(fruits)
fruits.insert(3,'blueberry')
print(fruits)
print('End: How to insert items in to a list')

print('Begin: How to remove an item from a list.')
# How to insert an item to a list. <list variable>.remove(string or integer)
# method
# can not insert inside a print statement
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits.remove('banana')
print(fruits)
print('End: How to to remove and item from a list.')

print('Begin: How to remove an item from a list using with pop.')
# How to remove an item using the pop method <list variable>.pop(index integer)
# Trying <list variable>.pop() will the last index
# Trying print(< list variable>.pop(index integer)) will pop out the item only
# pop()  removes the specified index or the last item if not specified 
# method
# index can only be an integer, not a string
# rember last place in the index is not an actual value
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits.pop()
print(fruits)
# or 
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits.pop(1)
print(fruits)
# or
fruits = ['banana','orange','mango','lemon']
print(fruits)
print(fruits.pop(1))
print('End: How to remove an itm from a list with pop.')

print('Begin: How to clear a list')
# How to clear a list <list variable>.clear()
# method
# Can not insert inside a print statement
fruits = ['banana','orange','mango','lemon']
fruits.clear()
print(fruits)
print('End: How to clear a list.')

print('How to remove and item from a list.')
# How to remove and item from a list <variable/list>.remove(<string/int>)
# method
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits.remove('banana')
print(fruits)
print('End: How to delete/remove an item from the list.')

print('Begin: How to delete an item from the list.')
# How to delete an item from a list del <variable/list>[start:end:step]
fruits = ['banana','orange','mango','lemon']
print(fruits)
del fruits[0]
print(fruits)
fruits = ['banana','orange','mango','lemon']
print(fruits)
del fruits[0:2]
print(fruits)
fruits = ['banana','orange','mango','lemon']
print(fruits)
del fruits[1:4:2]
print(fruits)
print('End: How to delete an item from the list.')

print('Begin: How to copy a list.')
# How to copy a list <copy list/variable> = <orignal list/variable.copy()
# 2nd option overwrites the original the 1st option maintains the original data/item
# method
# Can not insert inside a print statement
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits_copy = fruits.copy()
print(fruits_copy)
# or 
print(fruits)
fruits2 = fruits
print(fruits2)
print(fruits2.pop(1))
print(fruits)
print('End: How to copy a list.')

print('Begin: How to join multiple lists.')
# How to join a list <combined list variable> = <list1> + <list2>
# method
fruits = ['banana','orange','mango','lemon']
print(fruits)
vegatbles = ['carrot','potato','broccoli','celery']
print(vegatbles)
groceries = fruits + vegatbles
print(groceries)
print('End: How to join multiple lists.')

print('Begin: How to join multiple list by extending.')
# How to join list using extend. list1.extend(list2) -> print(list1)
# method
# can not use in print statement
fruits = ['banana','orange','mango','lemon']
print(fruits)
vegatbles = ['carrot','potato','broccoli','celery']
print(vegatbles)
fruits.extend(vegatbles)
print(fruits)
print('How to join join multiple list by extending.')

print('Begin: How to count the amount of occurences of an item in a list.')
# How to count the amount of occurences of an item in a list. print(<variable/list>.count(<string/int))
# method
fruits = ['banana','orange','mango','lemon']
print(fruits)
print(fruits.count('banana'))
print(fruits.count(1))
print('End: How to count the amount of occurences of an item in a list.')

print("Begin: How to find an item index in a list using the index().")
# How to find an item index in a list. print(<variable/list>.index(<str/int>))
# method
fruits = ['banana','orange','mango','lemon']
print(fruits.index('orange'))
print('End: How to find an item index in a list using index().')

print('Begin: How to reverse a list..')
# How to reverse a list using reverse() <variable/list>.reverse() -> print(<variable.list)
# method
# Can not be used inside a print statement
fruits = ['banana','orange','mango','lemon']
print(fruits)
fruits.reverse()
print(fruits)
print('End: How to reverse a list.')

print('Begin: How to sort items in a list.')
# How to sort items <variable/list>.sort()
# <variable/list>.sort(reverse=True) 100 - 0 or Z - A
# List entries in alphabetical or numerical order 0 - 100, or A - Z
# permanently changes the list
# method
# Can not be used in a print statement
fruits = ['banana','orange','mango','lemon']
numbers = [11,4,1,6,26]
print(fruits)
fruits.sort()
print(fruits)
fruits = ['banana','orange','mango','lemon']
fruits.sort(reverse=True)
print(fruits)
print(numbers)
numbers.sort()
print(numbers)
fruits = ['banana','orange','mango','lemon']
print('End: How to sort items in a list.')

print('Begin: How to sort items in a list with SORTED')
# Ascending sorted(<variable/list)  0 - 100, or A - Z
# Descending sorted(<variable/list,reverse=True) 100 - 0 or Z - A
# Can be used in a print statement
fruits = ['banana','orange','mango','lemon']
print(fruits)
print(sorted(fruits))
print(sorted(fruits,reverse=True))
# or 
fruits = ['banana','orange','mango','lemon']
print(fruits.sort(reverse=True))


