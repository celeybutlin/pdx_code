"""Let's play rock-paper-scissors with the computer.

    The computer will ask the user for their choice (rock, paper, scissors)
    The computer will randomly choose rock, paper or scissors
    Determine who won and tell the user

Let's list all the cases:

    rock vs rock (tie)
    rock vs paper
    rock vs scissors
    paper vs rock
    paper vs paper
    paper vs scissors
    scissors vs rock
    scissors vs paper
    scissors vs scissors
"""
import random

options = ['rock', 'paper', 'scissors']
computer_choice = random.choice(options)
their_choice = input('Rock, paper, or scissors? ').lower()

if computer_choice == their_choice:
    print('Tie!')
elif computer_choice == 'rock':
    if their_choice == 'paper':
        print('You win!')
    elif their_choice == 'scissors':
        print('You lose!')
    else:
        print('Invalid input.')
elif computer_choice == 'paper':
    if their_choice == 'rock':
        print('You win!')
    elif their_choice == 'scissors':
        print('You lose!')
    else:
        print('Invalid input.')
elif computer_choice == 'scissors':
    if their_choice == 'rock':
        print('You win!')
    elif their_choice == 'paper':
        print('You lose!')
    else:
        print('Invalid input.')

print(f'The computer chose {computer_choice}')


