################################
# Title: 30 Days of Python
# Description: Dictionaries | Exercices
# Change Log:
# JP, Created, 9.23.25
################################


print('Question 1: Create an empty dictionary called dog.')
dog = {}
print(type(dog))

print('Question 2: Add name, color, breed, legs, age to the dog dictionary.')
dog = {'name':'Bruno','breed':'Husky','legs':'4','age':'3'}
print(dog)

print('Question 3: Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.')
student = {'first_name':'Steve','last_name':'Rogers',
           'gender':'male','age':'95','marital status':'singlish',
           'skills':'leadership ,hand to hand, super strength',
           'country':'USA','city':'Brooklyn','address':'Avengers Tower'}
print(student)

print('Question 4: Get the length of the student dictionary.')
print(len(student)) # note it counts the amount of vaules

print('Question 5: Get the value of skills and check the data type, it should be a list.')
print(student['skills'])
# or
print(student.get('skills'))

print('Question 6: Modify the skills values by adding one or two skills.')
student['skills'] = 'leadership ,hand to hand, super strength, tall'
print(student)

print('Question 7: Get the dictionary keys as a list.')
student_keys = student.keys()
print(student_keys)

print('Question 8: Get the dictionary values as a list.')
student_values = student.values()
print(student_values)

print('Question 9: Change the dictionary to a list of tuples using items() method.')
student = {'first_name':'Steve','last_name':'Rogers',
           'gender':'male','age':'95','marital status':'singlish',
           'skills':'leadership ,hand to hand, super strength',
           'country':'USA','city':'Brooklyn','address':'Avengers Tower'}
student = list(student.items()) 
print(student)
print(type(student))

print('Question 10: Delete one of the items in the dictionary.')
student = {'first_name':'Steve','last_name':'Rogers',
           'gender':'male','age':'95','marital status':'singlish',
           'skills':'leadership ,hand to hand, super strength',
           'country':'USA','city':'Brooklyn','address':'Avengers Tower'}

print(student)
popped_item = student.popitem() # renoves the last item
print(student)
print(popped_item) 
# or 
student = {'first_name':'Steve','last_name':'Rogers',
           'gender':'male','age':'95','marital status':'singlish',
           'skills':'leadership ,hand to hand, super strength',
           'country':'USA','city':'Brooklyn','address':'Avengers Tower'}
del student['age'] # specific
print(student)
# or
student = {'first_name':'Steve','last_name':'Rogers',
           'gender':'male','age':'95','marital status':'singlish',
           'skills':'leadership ,hand to hand, super strength',
           'country':'USA','city':'Brooklyn','address':'Avengers Tower'}
popped_item = student.pop(('first_name'))
print('The poped item is:',popped_item)
print(student)

print('Question 11: Delete one of the dictionaries.')
del student
print('------------ Result below is on purpose, as you deleted the dictionary---------------')
print(student)