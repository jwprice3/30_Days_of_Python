################################
# Title: 30 Days of Python
# Description: Loops
# Change Log:
# JP, Created, 10.21.25
################################

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
# print('Level | Question: Iterate 0 to 10 using for loop, do the same using while loop.')
# count = [0,1,2,3,4,5,6,7,8,9,10]
# # Remember: For is used in data sets
# for n in count:
#     print(n)
# print('Count finished with a <for> loop.')

# # or

# for n in range(10):
#     print(n)
# print('Count finished with the range().')

# count_to_ten = 0 

# while count_to_ten < 11:
#     print(count_to_ten)
#     count_to_ten = count_to_ten + 1

# print('Level | Question: Iterate 0 to 10 using for loop, do the same using while loop.')
# count = [10,1,2,3,4,5,6,7,8,9,0]

# # Remember: For is used in data sets
# for n in count:
#     count.reverse() # This started with the first entry and then reversed
#     print(n)
# print('Descending count finished with a <for> loop.')

# # or
# count = 10
# while count > 0:
#     print(count)
#     count = count - 1

# print('Descending count finished with a <while> loop.')

# print('Level | Question: Write a loop that makes seven calls to print(), so we get on the output the following triangle:')

# number_icon = '#'
# print(number_icon)
# while (number_icon) < '########':
#     print(number_icon)
#     number_icon = number_icon + '#'

# number_icon = '# # # # # # # #'



# print('Level | Question: Write a loop that makes seven calls to print(), so we get on the output the following triangle:')

# limit = 0
# while limit < 9: 
#     print(number_icon)
#     limit = limit + 1

# # or 

# for i in range(8):
#     print(number_icon)

# print('Level: | Question: Print the following pattern:')
# pattern = ['0 x 0 = 0', '1 x 1 = 1', '2 x 2 = 4', '3 x 3 = 9', '4 x 4 = 16', '5 x 5 = 25', '6 x 6 = 36', '7 x 7 = 49', '8 x 8 = 64', '9 x 9 = 81', '10 x 10 = 100']
# print(len(pattern))

# for i in pattern:
#     print(i)

# print('Level | Question: Iterate through the list, Python, Numpy,Pandas,Django, Flask using a for loop and print out the items.:')
# words = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for i in words:
#     print(i)

# print('Level | Question: Use for loop to iterate from 0 to 100 and print only even numbers.')

# count = 0

# while count < 101:
#     print(count)
#     count = count + 2

# print('Level | Question: Use for loop to iterate from 0 to 100 and print only odd numbers.')

# count = 100
# while count > -1:
#     print(count)
#     count = count - 2

# print('Level 2 | Question: Use for loop to iterate from 0 to 100 and print the sum of all numbers.')

# number = 0

# for n in range(101):
#     number = number + n
#     print(f'After adding {n}, total is {number}')
# print(f'The sum of all numbers is {number}.')


# print('Level 2 | Question: Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.')

# even_number = 0
# odd_number = 0 

# for n in range(0,101,2): # range  can have steps
#     even_number = even_number + n
#     print(f'After adding {n}, total is {even_number}')
# for n in range(1,101,2):
#     odd_number = odd_number + n
#     print(f'After adding {n}, total is {odd_number}')
# print(f'The sum of all even numbers is {even_number}. The sum of all even numbers is {odd_number}')
 

print('Level 3 | Question: Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.')
print('The exercise is in the countries list file.')

print('Level 3 | Question:This is a fruit list, banana orange mango lemon" reverse the order using loop.')

fruits = ['banana', 'orange', 'mango', 'lemon']

for fruit in range(1):
    fruits.reverse()
    print(fruits)
