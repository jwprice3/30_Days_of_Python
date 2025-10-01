################################
# Title: 30 Days of Python
# Description: Condtionals | Notes
# Change Log:
# JP, Created, 9.24.25
################################

print('Question 1:Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:')
print('Enter your age:')
 # to determine the type of input, it must come before the input function
user_age = int(input())


# Set up conditional for age
user_age
if user_age > 18:
    print('You are old enough to drive.')
else:
    print('You need',18 - user_age,'years to learn to drive.')