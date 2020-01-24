"""Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

    Define a list of eyes
    Define a list of noses
    Define a list of mouths
    Randomly pick a set of eyes
    Randomly pick a nose
    Randomly pick a mouth
    Assemble and display the emoticon
"""

import random

eyes = [':', ';', '=']
noses = ['-', 'o', '0']
mouths = [')', '(', '0', 'p', 'P', 'D', '*']

eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)

# print(f'{eye}{nose}{mouth}')
print(eye + nose + mouth)