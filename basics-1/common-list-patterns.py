basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

basket.sort()
basket.reverse()
# print(basket[::-1])
# print(basket)

# print(list(range(1,100)))

sentence = ' '
new_sentence = sentence.join(basket)
print(new_sentence)
#fix this code so that it prints a sorted list of all of our friends (alphabetical)
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)

friends.sort()
print(friends)
