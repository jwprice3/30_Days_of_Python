################################
# Title: 30 Days of Python
# Description: Dictionaries
# Change Log:
# JP, Created, 9.18.25
################################


# A dictA dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
    # A dictionary is determined by {}
    # Dictionary has two components keys and values
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

print('Begin: How to add a key value pair to a dictionary.') # variable/dct[<'new key'>] = <new value>
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print(dct)
print('End: How to add a new key and value pair to a dictionary.')

print('Begin: How to add a value to an prexisting key.') # variable/dct[<'key'>] = <value>
# will overwrite previous value
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print(dct)
print('End: How to add a value to an prexisting key.')

print('Begin: How determine if a key exist in a dictionary.') # print(<'key'> in <variable/dct>)
# booleon
# operator
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)
print('key5' in dct)
print('End: How determine if a key exist in a dictionary.')

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

print('Begin: How to change from a dictionary to a list.') # <desired variable/list> = list(<variable/dictionary>.items())
# method
# .item()
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct)
print(type(dct))
dct = list(dct.items())
print(type(dct))
print(dct)
print('End: How to change from a dictionary to a list.')

print('Begin: How to copy a dictionary.') # <variable/new dict> = <variable/origianl dict>.copy()
# method
# copy()
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)
print('End: How to copy a dictionary.')

print('Begin: How to get dictionary keys as a list.') # <varibale/ dict keys = <variable/dict>.keys()
# method
# .keys()
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)
print(type(keys))
print(keys)
print('End: How to get dictionary keys as a list.')

print('Begin: How to get dictionary values as a list.') # <varibale/ dict values = <variable/dict>.values()
# method
# .values()
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)
print(type(values))
print(values)
print('End: How to get dictionary vaules as a list.')