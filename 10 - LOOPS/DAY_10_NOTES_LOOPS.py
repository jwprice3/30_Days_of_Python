################################
# Title: 30 Days of Python
# Description: Loops
# Change Log:
# JP, Created, 10.14.25
################################


# The purpose of loops in python is do handle repetitive programming task.
# There are two types of loops
#   # While Loops
#       # repeats statements until it a condition is satisfied
#   # For Loops
#       # A loop that goes through a sequence through data
#       # list, tuple, dictionary, set, or string

print('Begin: What is a while loop?')
# while <condtion>
#   <code>
count = 0
while count < 5: # if the <variable>/integer> is less than 0
    print(count) # print the <variable>/integer>
    count = count + 1 # add 1 to the original current number
    # the second iteration will be 1
    # the third iteration will be 2
    # the fourth iteration will be 3
    # the fifth iteration will be 4
    # the sixth iteration will will not meet the while condition and moves to else/false
else:
    print('The while condition is no longer true and the count equals:',count)
print('End: What is a while loop?')

print('Begin: Break explained.')
# syntax
# while condition:
#    code goes here
#    if another_condition:
#        break
count = 0
while count < 5: # if the <variable>/integer> is less than 0
    print(count) # print the <variable>/integer>
    count = count + 1 # add 1 to the current number
    if count == 3: # <variable>/integer> is now three and meets a new condition 
        break # this stops the loop
print('End: Break explained.')

print('Begin: Continue explained.')
# syntax
# while condition:
#    code goes here
#    if another_condition:
#       continue
count = 0
while count < 5: # if the <variable>/integer> is less than 0
    if count == 3: # <variable>/integer> is now three and meets a new condition 
        count = count + 1 # add 1 to the current number
        continue # the <variable>/integer> is now 3 but it does not print becuase it is not specified to do so, so move to the next iteration
    print(count) # print the <variable>/integer>
    count = count + 1 # add 1 to the original number
print('End: Continue explained.')


print('Begin: For loop explained.')
# syntax
# for iterator in string:
#    code goes here

# List example
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# String example
city_name = 'Madrid'
for letter in city_name: # python inteprets the string variable
    print(letter)

# Tuple example
numbers = (0,1,2,3,4,5,6) # python inteprets the list variable
for n in numbers:
    print(n)

# Dictionary  example
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

# for key, value in person.items():
    #print(key, value) # this way we get both keys and values printed out
