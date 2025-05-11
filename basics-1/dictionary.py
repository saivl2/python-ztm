dictionary = {
    'a': [1,2,3],  
    'b': 'hello',
    'x' : False
}

# Get the values of a dict
print(dictionary['a'][2])
print(dictionary.get('c', 'Does not exist'))