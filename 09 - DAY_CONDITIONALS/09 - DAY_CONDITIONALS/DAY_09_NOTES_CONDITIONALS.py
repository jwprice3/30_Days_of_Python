################################
# Title: 30 Days of Python
# Description: Condtionals | Notes
# Change Log:
# JP, Created, 9.24.25
################################


# Conditional is having an action done base if the condtion is True or False
    # Python runs sequntially, from top to bottom and will do so unless specifically directed otherwise
    # A condition can repeat infinitly unless specfically told not to for any reason
    # : symbol can dictate that it is a condition
    # Conditions can be: if, if else or elif
    # Condtions can be nested

print('Begin: How to use the "if" condition.') # if <variable> <operator> <comparative variable>: (identation) print(<string>)
# if <higlighted because it is hard coded>
# this example is true
a = 2
if a > 0:
    print('A is a positive number.')
print('Begin: How to use the "if" condition.')

print('Begin: How to use the "if else" condition.')
# if <variable> <operand> <comparative variable>: (identation) print(<string>) else(must be aligned with if): (indentation) print(<string>) 
# this statement was not true and went to else
a = 3
if a > 0:
    print('A is a negative number.')
else:
    print('A is a positive number')

print('End: How to use the "if else" condition.')

print('Begin: How to use the "elif" condition.')
# This checks for multiple conditions
# Elif is used as an intermediary step before the final else statement
a = 0
if a > 0:
    # This is checking if <variable> is less than zero
    print('A is a postive number.')
elif a < 0: 
    # If <variable> so happens to be less than zero then it is a negative number
    print('A is a negative number.')
else:
    # The <variable> has not met either of these conditions, so therefore
    print('A is zero or perhaps greater.')

# or
a = 3
# Do X if <conditional> otherwise do Y
print('A is positive') if a > 0 else print('A is negative.')
print('End: How to use the "elif" condition.')

print('Begin: How to use nested positions.')
# Nested positions are a way to test multiple conditions before and elif and else statement
a = 0
if a > 0: # if the variable is greater than zero then continue to nested condition
# if the there is no remainder then it is an even integer it wil read like (8 = 4*2 + 0) 
# if there is a remainder then it is an odd number it would read like (9=4*2 +1)
    if a % 2 == 0: 
        print('A is a positive and even integer')
# the variable is greater than zero and even    
    else: 
        print('A is a positive')
# the variable is exactly zero
elif a == 0: 
    print('A is zero')
else:
# the variable is less than zero    
    print('A is a negative number.')
print('End: How to use nested positions.')

print('Begin: If condition "and" logical operators.')
# Combining "if" conditions "and" condittion:
    # code
a = 0
# if the there is no remainder then it is an even integer it wil read like (8 = 4*2 + 0) 
# if there is a remainder then it is an odd number it would read like (9=4*2 +1)
if a > 0 and a % 2 == 0: 
    print('A is an even positive integer.')
# the variable is not equal to zero so it has to be either a 1 and above
elif a > 0 and a % 2 != 0:
    print('A is a positive integer.')
# the varbiable 
elif a == 0:
    print('A is zero.')
else:
    print('A is a negative mumber.')

print('End: If condition "and" logical operators.')

print('Begin: "If "and" "or" Logical')
user = 'James'
access_level = 3
if user =='admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')