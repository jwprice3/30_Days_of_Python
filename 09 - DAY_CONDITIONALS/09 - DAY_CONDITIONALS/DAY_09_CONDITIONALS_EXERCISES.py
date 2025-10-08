################################
# Title: 30 Days of Python
# Description: Condtionals | Notes
# Change Log:
# JP, Created, 9.24.25
################################

print('Level 1: Question 1:Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:')
print('Enter your age:')
# to determine the type of input, it must come before the input function
user_age = int(input())


# Set up conditional for age
user_age
if user_age > 18:
    print('You are old enough to drive.')
else:
    print('You need',18 - user_age,'years to learn to drive.')


print('Level 1: Question 2: Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print "year" for 1 year difference in age, "years" for bigger differences, and a custom text if my_age = your_age.')
print('Enter your age:') # print statement needs to come before input
your_age = int(input())
my_age = 30

# Have the user enter their age
your_age
if your_age >= my_age:
    print('You are', your_age - my_age, 'years older than me')
else:
    print('You are', my_age - your_age,'years younger than me.')
    
print('Level 1: Question 3:Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.')
# Enter A
print('Enter A:')
a = int(input())
#print(a)
# Enter B
print('Enter B:')
b = int(input())
#print(b)
if a > b:
    print(a, 'is greater than', b)
elif b > a:
    print(b, 'is greater than', a)
elif a == b:
    print('We are not so different you and I.')
else:
    print('We are done comparing')
    
print('Level 1: Question 1: Write a code which gives grade to students according to theirs scores:\n')
print('80-100 A, 70-89 B, 60-69 C, 50-59 D, 0-49 F.')
# Set grade variables
a_grade = 80
b_grade = 70
c_grade = 60
d_grade = 50
f_grade = 0

# have user input
print('Enter student grade.')
student_grade = int(input())

if student_grade >= a_grade:
    print('You have an A.')
elif student_grade >= b_grade:
    print('You have a B.')
elif student_grade >= c_grade:
    print('You have a C.')
elif student_grade >= d_grade:
    print('You have a D.')
elif student_grade >= f_grade:
    print('You have a F.')
else:
    print('You do not have a grade!') # unecessary since you clarified that input is an integer.

print('Level 1: Question 2: Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer')
winter = ['December','January','February']
autumn = ['September','October','November']
spring = ['March', 'April','May']
summer = ['June', 'July','August']

print('Enter a season:')
season = str(input())

if season in winter:
    print("The season you entered is in winter.")
elif season in spring:
    print("The season you entered is in spring.")
elif season in autumn:
    print("The season you entered is in autumn.")
elif season in summer:
    print("The season you entered is in summer.")
else:
    print('You did not enter a season')

print("Level 2: Question 3: If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print'That fruit already exist in the list")
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Enter fruit:')
new_fruit = str(input())


if new_fruit in fruits:
    print('Fruit already exist.')
elif new_fruit not in fruits:
    fruits.append
print(fruits)

print('Level 3: Question 1: Here we have a person dictionary. Feel free to modify it!')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if skills exist in person
print('Check if the person dictionary has skills key, if so print out the middle skill in the skills list.\n')
if 'skills' in person:
    print('Skills are in person.')
else:
    print('Skills are not there.')

# convert dictionary to list
middle_skill = list(person.get('skills'))
print(middle_skill)

# confirm is variable is a list
print(type(middle_skill))

# print middle entry
print(middle_skill[2])

# print('Check if the person dictionary has skills key, if so check if the person has "Python" skill and print out the result.\n')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if skills exist in person
if 'skills' in person:
    print('Skills are in person.')
    is_there_python = middle_skill = list(person.get('skills'))
    # confirm if Python exist
    print('Python' in is_there_python)
else:
    print('Skills are not there.')

print('If a person skills has only JavaScript and React, print("He is a front end developer"), if the person skills has Node, Python, MongoDB, print("He is a backend developer"), if the person skills has React, Node and MongoDB, Print("He is a fullstack developer"), else print("unknown title") - for more accurate results more conditions can be nested!\n')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['React','Node','MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print('Skills are in person.')
    # Confirm variabless
    career_path = set(person.get('skills'))
    print(career_path)
    print(type(career_path))
    # Best practice is to compare type to type
    # List did not work becuase it was order dependent
    # Sets is uncategorized
    if career_path == {'JavaScript','React'}:
        print('He is a front end devloper!')
    elif career_path == {'Node','MongoDB','Python'}:
        print('He is a back end devloper!')
    elif career_path == {'Node','React','MongoDB'}:
         print('He is a fullstack developer!')
    else:
        print('Uknown Title')
        
print('If the person is married and if he lives in Finland, print the information in the following format:')
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'first_name' and 'last_name' and 'country' and 'is_marred' in person:
    print(person.get('first_name'),person.get('last_name'),'lives in',person.get('country'),'.','He is married.')


