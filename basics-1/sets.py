my_set = {1,2,3,4,5,3,4,5}
my_set.add(100)
print(my_set)
# print(my_set[3]) - cannot index a set
print(3 in my_set)

li = [1,2,3,4,5,5]
print(list(set(li)))
