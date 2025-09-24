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
# this statemen was not true and went to else
a = 3
if a > 0:
    print('A is a negative number.')
else:
    print('A is a positive number')

print('End: How to use the "if else" condition.')

print('Begin: How to use the "elif" condition.')

# This checks for multiple conditions
a = 0
if a > 0:
    # This is checking if <variable> is less than zero
    print('A is a postive number.')
elif a < 0:
    # If <variable> so happens to be less than zero then it is a negative number
    print('A is a negative number.')
else:
    # The <variable> has not met either of these conditions, so therefore
    print('A is zero or behaps greater.')

