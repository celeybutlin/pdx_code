"""Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

    Have the user enter a number representing the grade (0-100)
    Convert the number grade to a letter grade


    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F"""
import random

grade = int(input("What was your grade? "))
rival = random.randint(0,100)

if grade <= 59:
    print("Your grade is an F")
elif grade <= 69:
    print("Your grade is a D")
elif grade <= 79:
    print("Your grade is a C")
elif grade <= 89:
    print("Your grade is a B")
elif grade <= 100:
    print("Your grade is an A!")
else: 
    print("Invalid answer. Please answer a number between 0 and 100")

if grade < rival:
    print("By the way, your rival beat you!")
elif grade > rival:
    print("You beat your rival! Good job!")
elif grade == rival:
    print("You and your rival tied. Nice.")