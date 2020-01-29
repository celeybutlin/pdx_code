"""Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.

ADVANCED VERSION 1: Allow the user to choose how many characters the password will be.
"""

import random
import string

password = ''
characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("How many characters do you want your password to be? "))

for letter in range(length):
    password += random.choice(characters)

print(f'Your password is {password}')