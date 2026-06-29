closet = ['shirt', 'pants', 'socks', 'hat']
print(closet)
print(id(closet))
closet.remove('hat')
print(closet)
print(id(closet)) # Id did not get change because lists are mutable, so a new list object is created when we concatenate.

words = "you are wearing that"
print(words)
print(id(words))

words = words + "because it look good on you" 
print(words)
print(id(words)) # Id got changed because strings are immutable, so a new string object is created when we concatenate.