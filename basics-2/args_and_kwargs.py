def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(list(x for x in kwargs.values()))

print(super_func(1,2,3,4,5, n1 = 45, n2 = 90))