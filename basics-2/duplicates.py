some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
new_list = []

for item in some_list:
    if some_list.count(item) > 1:
        new_list.append(item)
    
print(list(set(new_list)))
        