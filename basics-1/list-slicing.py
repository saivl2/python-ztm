amazon_cart = [
    'apples',
    'sunglasses',
    'notebooks',
    'grapes'
]

print(amazon_cart[1])
print(amazon_cart[1:3])

# Mutable
amazon_cart[-2] = 'laptop'
print(amazon_cart)

new_cart = amazon_cart[:] # Maing a copy of the original list
new_cart[0] = 'Pineapple'

print(new_cart)
print(amazon_cart)
