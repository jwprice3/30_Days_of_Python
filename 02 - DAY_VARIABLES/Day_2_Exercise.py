#---------------------------------------------------------#
# Title: 30 Days of Python
# Description: Built in Funcitons
# ChangeLog: Justin, 3.5.2025
#---------------------------------------------------------#
'''
#Day: 30 days of python programming
Exercise 1:
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line

Exercise 2
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters.
    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area.
13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
'''
#Exercise 1
#Variables
first_name = 'Marshall' #note: wihtout comments python does not determin if it is string
last_name = 'Faulk'
full_name = first_name + ' ' + last_name #note: added qoutes to create a space
country = 'USA'
city = 'St.Louis'
age = 28
year = 1999
_is_married = True
is_light_on = True
#or
first_name_2, last_name_2, full_name_2, country_2, city_2, age_2, year_2, _is_married_2, is_light_on_2 = 'Marshall', 'Faulk', 'Marshall Faulk', 'USA', 'St.Louis', 28, 1999, True, True

#Exercise 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(_is_married))
print(type(is_light_on))
print(len(first_name))
print(len(last_name))
num_one = 5
num_two = 4
question_5 = num_one + num_two
question_6 = num_two - num_one
question_7 = num_two * num_one
question_8 = num_one / num_two
question_9 = num_two%num_one
question_10 = num_one**num_two
question_11 = num_one//num_two
print(question_5)
print(question_6)
print(question_7)
print(question_8)
print(question_9)
print(question_10)
print(question_11)

radius = 30
area_of_circle = (3.4*radius)**2 #A=πr2
circum_of_circle = 2*3.14*radius #C=2πr
print('Enter Radius:')
input_radius = int(input())*3.4**2
print('Area is: ', input_radius)
print(area_of_circle)
print(circum_of_circle)

print('Enter first name')
input_firstname = ('First Name is: '+ input(""))
print('Enter last name')
input_lastname = ('Last Name is: '+ input(""))
print(input_lastname)
print('Enter country')
input_country = ('Country is: '+ input(""))
print('Enter age name')
input_age = ('Age is: '), int(input())

help('keywords')
help(print)
help(print(input_firstname))
print(' end help input_firstname')
help(print(radius))
print('end help radius')
help(print(first_name))
print('endfirst_name')
print('done')

print(dir())
print('end dir()')
print(dir(first_name))
print('dir first_name done')