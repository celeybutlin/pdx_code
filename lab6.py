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

if their_choice == computer_choice:
    print('Tie!')
elif their_choice == 'rock':
    if computer_choice == 'paper':
        print('You lose!')
    elif computer_choice == 'scissors':
        print('You win!')
elif their_choice == 'paper':
    if computer_choice == 'rock':
        print('You win!')
    elif computer_choice == 'scissors':
        print('You lose!')
elif their_choice == 'scissors':
    if computer_choice == 'rock':
        print('You lose!')
    elif computer_choice == 'paper':
        print('You win!')
else:
     print('Invalid input.')

print(f'The computer chose {computer_choice}')

# Advanced Version 2: Ask the user if they want to play again, using a while loop.

play_again = input('Do you want to play agian? ').lower()

while play_again == 'yes':
    their_choice = input('Rock, paper, or scissors? ')
    if their_choice == computer_choice:
     print('Tie!')
    elif their_choice == 'rock':
     if computer_choice == 'paper':
        print('You lose!')
     elif computer_choice == 'scissors':
        print('You win!')
    elif their_choice == 'paper':
     if computer_choice == 'rock':
        print('You win!')
     elif computer_choice == 'scissors':
        print('You lose!')
    elif their_choice == 'scissors':
        if computer_choice == 'rock':
         print('You lose!')
        elif computer_choice == 'paper':
         print('You win!')
    else:
     print('Invalid input.')
    print(f'The computer chose {computer_choice}')
    play_again = input('Do you want to play again? ').lower()