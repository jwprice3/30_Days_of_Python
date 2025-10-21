################################
# Title: 30 Days of Python
# Description: Loops
# Change Log:
# JP, Created, 10.21.25
################################


print('Level: Iterate 0 to 10 using for loop, do the same using while loop.')
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

print('Level: Iterate 0 to 10 using for loop, do the same using while loop.')
count = [10,1,2,3,4,5,6,7,8,9,0]

# Remember: For is used in data sets
for n in count:
    count.reverse() # This started with the first entry and then reversed
    print(n)
print('Descending count finished with a <for> loop.')

# or
count = 10
while count > 0:
    print(count)
    count = count - 1

print('Descending count finished with a <while> loop.')