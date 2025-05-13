#---------------------------------------------#
#Title: 30 Days of Python
#Description: Operators
#ChangeLog: Justin,3.19.2025,Created Script
#---------------------------------------------#

'''
The purpose of this is to be used as a reference document for 30 days of python. Note if running on 
a cmd shell <exit()> Reference: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md
Reference: https://docs.python.org/3.9/library/functions.html
'''

'''
Day 3
#Exercise
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text python and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    Enter number of years you have lived: 100
    You have lived for 3153600000 seconds.
23. Write a Python script that displays the following table
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
'''
# my_age = 30
# my_height = 6.1
# my_complex_number = 3 + 4j

# #Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
# print('Find the area of a tringle')
# print('Enter Base:')
# base = input()
# print('Enter Height')
# height = input()
# area_of_trianle = .5 * int(base) * int(height) #this will throw an error unless you specify what the variable will be ex. int(base)
# print('The area of the triangle is', area_of_trianle)

# #Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# print('Enter side a:')
# side_a = input()
# print('Enter side b:')
# side_b = input()
# print('Enter side c:')
# side_c = input()
# perimeter_of_triangle = int(side_a) + int(side_b) + int(side_c)
# print('The perimeter of the triangle is', int(perimeter_of_triangle))

# #Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# print('Find the area and perimeter of a rectangle.')
# print('Enter side a:')
# side_a_w = input()
# print('Enter side b:')
# side_b_l = input()
# area_of_rectangle = int(side_a_w) * int(side_b_l)
# perimeter_of_rectangle = (int(side_a_w) + int(side_b_l)) * 2
# print('The area of the rectangle is', int(area_of_rectangle))
# print('The perimeter of a rectangle is', int(perimeter_of_rectangle))

# #Get radius of a circle using prom1
# #Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# print('Get the radius and circumference of a circle')
# print('Enter Radius:')
# raidus = input()
# area_of_a_cirlce = 3.14 * int(raidus)**2
# circumference = 2 * 3.14 * int(raidus)
# print('Get the radius and circumference of a circle')
# print('Enter Radius:', int(raidus))
# print('Area is', int(area_of_a_cirlce))
# print('Circrumference is', int(circumference))

# #Calculate the slope, x-intercept and y-intercept of y = 2x -2
# print('Find the slope')
# print('Enter x:', )
# x = input()
# y_slope = (2*int(x)-2)
# print(y_slope)

# #Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# print('Point one is (2,2)')
# print('Point one is (6,10)')
# slope = (10 - 2) / (6 - 2)
# print(slope)

# #Compare the slopes in tasks 8 and 9.
# print('y slope is', y_slope, 'and', 'slope is', slope)

# #Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# print('Enter x:', )
# x = input()
# print(int(x)**2)
# value_of_y = int(x)**2 + 6*(int(x)) + 9
# print('y =',value_of_y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# python = 'python'
# dragon = 'dragon'
# print(len(python) != len(dragon))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# print('Is on is in python?', 'on' in ('python' and 'dragon'))
# print('Is on is in  dragon?', 'on' in 'dragon')
# print('True - on is found in dragon and python.')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# print('Is jargon in this sentence? I hope this course is not full of jargon', 'jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
# print('Is there <no> in python and dragon?', 'no' in (python and dragon))

# Find the length of the text python and convert the value to float and convert it to string
# print("What is length of python?")
# print(len(python))
# print(float(len(python)))
# python = str(float(len(python)))
# print(type(python))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# y = 2
# print("Is this number divisible by 2?:")
# x = int(input())
# print("The number is", x)
# print((x/2) == (x//2))

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# print("Is 7//2 equal to 2.7?", "Answer:", (7//2) == (2.7))

# Check if type of '10' is equal to type of 10
# print("Q: Is type of '10' is equal to type of 10?", type("10") == type(10))

# Check if int('9.8') is equal to 10
# print("Q: Check if int('9.8') is equal to 10", int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# print("Q: Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?")
# hours = int(input())
# rate_per_hour = 28
# weekly_earning = hours * rate_per_hour

# print("Please enter the amount the worked.")
# print("Enter the amount of hours worked.", hours)
# print("Your hourly rate is:", "$", rate_per_hour)
# print("Weekly total is:", "$", weekly_earning, "Uncle Sam withstanding.")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
print("Q: Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years")
print("How many years have you lived?","Enter a number between 0 - 100.")
age = int(input())
print("The user is",age, "years old")
seconds_lived = age * 31536000
print("You have lived",seconds_lived,"seconds.")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
print("Write a Python script that displays the following table")
print("1 1 1 1 1\n""2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")