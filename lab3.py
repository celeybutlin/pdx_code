"""Let's write a program to simulate the classic "Magic Eight Ball"

    Print a welcome screen to the user.
    Prompt the user to ask the 8-ball a question.

    For example: "Will I win the lottery tomorrow?"

    Use the random module's random.choice() to choose a prediction.
    Display the result of the prediction.
"""
import random

print("Welcome to the Magic 8 Ball!")
question = input("What would you like for me to answer? ")

answer = ["Yes, it is likely!", "Oh HELL no!", "Maybe, but I cannot be sure", "Wouldn't you like to know!"]

print(random.choice(answer))