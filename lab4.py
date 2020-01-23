"""Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

    Have the user enter a number representing the grade (0-100)
    Convert the number grade to a letter grade

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: 
"""
import random

grade = int(input("What was your grade? "))
rival = random.randint(0,100)
remainder = grade % 10

if remainder % 2 == 0:
    plus_minus = "+"
else:
    plus_minus = "-"

if grade <= 59:
    print("Your grade is an F", plus_minus)
elif grade <= 69:
    print("Your grade is a D", plus_minus)
elif grade <= 79:
    print("Your grade is a C", plus_minus)
elif grade <= 89:
    print("Your grade is a B", plus_minus)
elif grade <= 100:
    print("Your grade is an A!", plus_minus)
else: 
    print("Invalid answer. Please answer a number between 0 and 100")

# advanced version 1: Use randint() from the random module to determine the user's rival's score. Let the user know if they did better than their rival.
if grade < rival:
    print("By the way, your rival beat you!")
elif grade > rival:
    print("You beat your rival! Good job!")
elif grade == rival:
    print("You and your rival tied. Nice.")

# advanced version 2: Use % to get the remainder of the grade when divided by ten, which is the same as the number in the ones digit. The number in the ones digit will determine whether they will get a '+' or a '-' appended to the end of their grade. For example, the grade 81 would be a 'B'. 81 % 10 would give you 1, which is a low number, so you would add a '-' to the end of the grade.

    
   