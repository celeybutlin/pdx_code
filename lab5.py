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

eyes = [':', ';', '=', 'X']
noses = ['-', 'o', '0', '*']
mouths = [')', '(', '0', 'p', 'P', 'D', '*']

eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)

face = eye + nose + mouth
print(face)

# Advanced version 1: Use a for loop to generate 5 emoticons.

for face in range(5):
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    face = eye + nose + mouth
    print(face)


# Advanced Version 2: In a while loop, ask the user if they want another emoticon

repeat = input('Do you want another emoticon? ').lower()

while repeat == 'yes':
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    face = eye + nose + mouth
    print(face)
    repeat = input('Do you want another emoticon? ').lower()
else:
    print('Ok! No more smiley faces for you!')


# Advanced version 3: Ask the user if they want to choose each part of the face. If they do, let the user choose that part of the face. If they don't, randomly generate that part.

eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)
face = eye + nose + mouth

eyes_choice = input('Do you want to pick the eyes? ').lower()
if eyes_choice == 'yes':
    eye = input('What do you want for eyes? ')

nose_choice = input('Do you want to pick the nose? ').lower()
if nose_choice == 'yes':
    nose = input('What do you want for a nose? ')

mouth_choice = input('Do you want to pick the mouth? ').lower()
if mouth_choice == "yes":
    mouth = input('What do you want for a mouth? ')

print(eye + nose + mouth)