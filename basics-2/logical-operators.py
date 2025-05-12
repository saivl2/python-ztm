print('a' > 'A')
print(1 < 2 > 3 < 4)
print(1 >= 0)
print(0 != 0)

print(not(True))
print(not False)

print('*' * 24)

is_magician = False
is_expert = True

if is_magician and is_expert:
    print('You are a mater magician')
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print('You need magic powers')