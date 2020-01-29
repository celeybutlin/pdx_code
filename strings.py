"""# including the string module in our file
import string

# string.ascii_letters returns all upper and lower capital letters
letters = string.ascii_letters

print(letters)
# outcome: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'"""

import string
import random

print(string.ascii_letters) #prints all letters, upper and lower
print(string.ascii_lowercase) #prints all lowercase letters

letters = string.ascii_lowercase + string.ascii_uppercase
print(letters)

# new_word = random.choice(letters) + random.choice(letters) + random.choice(letters)
new_word = ""

for letter in range(5): #prints 5 random letters
    new_word += random.choice(letters) #saves each letter into new_word to create a new word
print(new_word)


# print(new_word)
