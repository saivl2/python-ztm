# What variables do I have access to?
total = 0

def count(total):
    # global total 
    total += 1
    return total


print(count(count(total)))
# print(count())
# print(count())