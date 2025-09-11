################################
# Title: 30 Days of Python
# Description: Sets
# Change Log:
# JP, Created, 9.10.25
################################

# A Set is collection of items that are un-indexed distinct elements
    # set() is a built in function

# How to create a Set
    # <set/variable()>
    # <varaible> = {<data>,<data>}
    # seems to be alphabetical

print('Begin: How to determing a set.')
st = set()
st = {'item1','item2','item3','item4'}
print('End: How to determing a set.')

print('Begin: How to determine the length of a set.') # len<set/variable>{item,item,item}
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
print('End: How to determine the length of a set.')

print('Begin: How to confirm if an item is an a set.') # print('item" in)
# Boolean
fruits = {'banana', 'orange', 'mango', 'lemon'} 
print('mango' in fruits)
print('End: How to confirm if an item is an a set.')

print('Begin: How to add items to a set.') # <variable/set>.add('item) or <variable/set.update(['item','item'])
# add is one entry
# update() includes multiple entries
# method
fruits = {'banana', 'orange', 'mango', 'lemon'} 
print(fruits)
fruits.add('lime')
# or
fruits.update(['tomato','clementine'])
print(fruits)
print('End: How to add items to a set.')

print('Begin: How to remove items from a set') # <variable/>set.pop() or <variable/set.remove('item') or <variable/set/.clear()
# methods
# remove is only one item
# clear is the entire set
# pop() is at random
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
print(fruits)
# To find pop item
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)
print(fruits)
# remove specfic item
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove('banana')
print(fruits)
# clear set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)
print('End: How to remove items from a set')