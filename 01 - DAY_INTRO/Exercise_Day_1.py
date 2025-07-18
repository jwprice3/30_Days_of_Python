# ------------------------------------------------- #
# Title: 30 Days of Python - Exercise_Day_1
# # Description: Intro & Simple Math
# ChangeLog: Justin,2.26.2025,Created Script
# ------------------------------------------------- #

'''
Directions
Reference: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme.md

        addition(+)
        subtraction(-)
        multiplication(*)
        modulus(%)
        division(/)
        exponential(**)
        floor division operator(//)
Write strings on the python interactive shell. The strings are the following:
        Your name
        Your family name
        Your country
        I am enjoying 30 days of python
Check the data types of the following data:
        10
        9.8
        3.14
        4 - 4j
        ['Asabeneh', 'Python', 'Finland']
        Your name
        Your family name
        Your country

Exercise: Level 2

    Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

Exercise: Level 3

    Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
    Find an Euclidian distance between (2, 3) and (10, 8)

'''
#Excersise 1
print( 3 + 4) # addition(+)
print(4 -3) # subtraction(-)
print(3*4) # modulus(%)
print(4%3) # modulator/remainder (%)
print(3/4) # division(/)
print(3**4)
print(3//4)

#Exercise 2
print("Justin")
print("Price")
print("USA")
print("I am enjoying 30 days of Python")

#Exercise 3
number = 10
print(type(number))
decimal = 9.8
print(type(decimal))
pie = 3.14
print(type(3.14))
complex = 4-4j
print(type(complex))
list = ['Asabeneh',"Python",'Finland']
print(type(list))
first_name ='Justin'
print(type(first_name))
last_name = 'Price'
print(type(last_name))
country = 'USA'
print(type(country))

eculidean_distance = (2** - 3**2)*2 + (10**2 - 8**2)*2 # ( x 2 − x 1 ) 2 + ( y 2 − y 1 ) 2
print(eculidean_distance)


