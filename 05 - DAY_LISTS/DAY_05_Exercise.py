# ----------------------------------- #
# Title: 30 Days of Python
# Description: List Exercises
# Change Log:
# JP, Created, 6.25.2025
# ----------------------------------- #

print('Question 1: Declare an empty list ')
mylist = []
print(mylist)

print('Question 2: Declare a list with more than 5 items')
mylist = ('Rams', 'Seahawks','Cardinals','49ers','NFC West')
print(mylist)

print('Question 3: Find the length of your list')
mylist = ['Rams', 'Seahawks','Cardinals','49ers', 'NFC West']
print(len(mylist))

print('Question 4: Get the first item, the middle item and the last item of the list')
mylist = ['Rams', 'Seahawks','Cardinals','49ers','NFC West']
print(mylist[0:5:2]) # slice 

print('Question 5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address')
mixed_data_types = ['JP', '34','6ft 1in', 'Single','NJ']
print(mixed_data_types)

print('Question 6: Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print('Question 7: Print list using print()')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)

print('Question 8: Print the number of companies in the list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(len(it_companies))

print(' Question 9: Print the first, middle and last company')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies[0:7:3]) # slice

print('Question 9: Print the list after modifying one of the companies')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
it_companies[-2] = 'GitHub' # index and slice
print(it_companies)

print('Question 11: Add an IT company to it_companies.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
it_companies.append('GitHub') # append method
print(it_companies)

print('Question 12: Insert an IT company in the middle of the companies list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
it_companies.insert(4,'Github') # insert method
print(it_companies)

print('Question 13: Change one of the it_companies names to uppercase (IBM excluded!)')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
it_companies[5] = 'ORACLE' # index and slice
print(it_companies)

print("Question 14: Join the it_companies with a string '#;'")
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
new_string = [';#'] 
it_companies = it_companies + new_string # concatenation
print(it_companies)
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
new_string = [';#']
it_companies.extend(new_string) # extend method
print(it_companies)

print('Question 15: Check if a certain company exists in the it_companies list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print('Oracle' in (it_companies))

print('Question 16: Sort the list using sort() method.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.sort()
print(it_companies)

print("Question 17: Reverse the list in descending order using reverse() method.")
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(sorted(it_companies,reverse=True)) # sorted method
# or
it_companies.sort(reverse=True) # sort method
print(it_companies)

print('Question 18: Slice out the first 3 companies from the list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies[0:3]) # slice

print('Qustion 19: Slice out the last 3 companies from the list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(len(it_companies))
print(it_companies[4:7]) # slice

print('Question: Slice out the middle IT company or companies from the list')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies[4]) # slice

print('Question 21: Remove the first IT company from the list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.remove('Facebook') # remove method
print(it_companies)
# or 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
del it_companies[0] # del method
print(it_companies)

print('Question 22: Remove the middle IT company or companies from the list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
del it_companies[4] # del method
print(it_companies)

print('Question 23: Remove the last IT company from the list')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
del it_companies[6:7] # del method , remove method, pop method
print(it_companies)
# or 
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.pop(6) #pop method
print(it_companies)


print('Question 24: Remove all IT companies from the list.')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
del it_companies[0:7] # del methond
print(it_companies,'list is 0')

print('Question 25: Destroy the IT companies list')
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
del it_companies # del method
# print(it_companies)

print('Question 26: Join the following lists.')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end) # extend method
print(front_end)
# or
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end # concatonate
print(full_stack)

print('Question 27: After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.')
full_stack.append('Python, SQL')
print(full_stack)

print('Exercise 2 | Part 1')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# step 1
print('The length of the variable ages is:', (len(ages)))
ages.sort()
# step 2
print('The min age and the max age again to the list')
ages.append(19)
ages.append(26)
ages.sort()
print('The length of th list is now:',len(ages))
# step 3
print(ages)
print('The meadian age is:', (ages[0]+ ages[11]) // 2)
# step 4
average_age = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9] + ages[10]
print('The average sum of all the numbers is:', average_age // 12)
# step 5
print('The range of the ages is:', ages[11] - ages[0])
# step 6
print('The absolute value of (min-average) is:',abs(ages[0]),'The absolute value of (max-average) is:',abs(ages[11]))

print('Exercise Level 2 | Part 2')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(len(countries)) # 193
# question 1
print(countries[96:98])
countries_1 = countries[0:96] # 96 and 97 but minus 1
countries_2 = countries[96:193] # List has to from part 1 to 2 has to end and start on the same

# question 2
print(len(countries_1)) # 96
print(len(countries_2)) # 96
print(countries_1)
print('---------------------BreaK-------------------------')
print(countries_2)

# question 3
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country_1,country_2,country_3, *rest_of_countries = countries
print(country_1)
print(country_2)
print(country_3)
print(rest_of_countries) #unpacking items method
# or
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country_1,country_2,country_3,*rest_of_countries = countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(country_1)
print(country_2)
print(country_3)
print(rest_of_countries)


