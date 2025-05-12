def highest_even(li):
    evens = []
    for item in li:
        if is_even(item):
            evens.append(item)
    
    return max(evens)

def is_even(n):
    return n % 2 == 0

print(highest_even([10,2,3,4,8,11]))