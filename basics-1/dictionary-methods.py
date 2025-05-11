user = {
    'basket': [1,2,3],
    'greet': 'hello'
}

user2 = dict(name = 'Joe')
print(user.get('age', 100))
print(user2)

print('basket' in user.values())
print('basket' in user)

print(user.items())

print(user.popitem()) 
print(user.update({'age': 55}))
print(user)