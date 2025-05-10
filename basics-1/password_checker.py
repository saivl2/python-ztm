password = input('Enter password: ')

masked_password = '*' * len(password)

print(f"Hey, your password {masked_password} is {len(password)} letters long.")