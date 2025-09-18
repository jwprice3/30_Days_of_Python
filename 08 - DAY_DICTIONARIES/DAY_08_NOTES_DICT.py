################################
# Title: 30 Days of Python
# Description: Dictionaries
# Change Log:
# JP, Created, 9.18.25
################################


# A dictA dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
    # A dictionary is determined by {}
    # Dictionary with keys and data values
    # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
    # keys are normally strings as they are descriptors
    # person = { 'first_name':'Asabeneh', 'last_name':'Yetayeh','age':250, 'country':'Finland', 'is_marred':True, 'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address':{ 'street':'Space street', 'zipcode':'02210' }}


print('Begin: How to check the length of a dictionary.') # print(len(<variable/dic>))
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # value1
print('End: How to check the length of a dictionary.')

print('Begin: How to access items in a dictionary.') # print(<variavble/dct>['<key name>])
# accessing a key that does not exist will result in error
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
print('End: How to access items in a dictionary.')

print('Begin: How determine if a key exist in a dictionary.') # print(<varianble/dct>.get('<key>))
# .get 
# method
# output is none
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.get('key1'))
print(dct.get('key5')) # does not result in error
print('End: How determine if a key exist in a dictionary.')

print('Begin: How to add a new key and value pair to a dictionary.') # variable/dct[<'key'>] = <value>
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print('End: How to add a new key and value pair to a dictionary.')

print('Begin: How determine if a key exist in a dictionary') # print(<'key'> in <variable/dct>)
# booleon
# operator
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)
print('key5' in dct)
print('End: How determine if a key exist in a dictionary')

print('Begin: Multiple methods to remove key and value pairs from dictionary') # <variabel/dct>.pop('<key1>') <variabel/dct>.popitem() or del dct['key1']
# method
# .pop('<key>') removes the key but maintains the value, one at a time
# .popitem() removes the last item
# del['<key>'] removes the item with the specified key name can be multiple
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)
print(dct.pop('key1')) # can not use wildcard
print(dct)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() 
print(dct)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)
del dct['key2']
print(dct)


