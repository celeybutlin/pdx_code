import random

# from random import randint >> this just imports the RANDINT function from the RANDOM module/file

print()
int()
# input("How are you? ") #what goes inside the parenthesis is called an ARGUMENT

def dogsarecool(text="dog", potato="tater"): # def defines the function. defaults to "dog" if no text entered. otherwise, whatever is passed through becomes text
    if "dog" in text:
        print(f'{text} is cool')
    else:
        print("That's just ok")

# user = input("Enter a string. ")
# dogsarecool(user)

user = int(input("Enter your grade. "))
rival = random.randint(40, 100)

def check_grade(score):
    if 90 < score <= 100:
        return("A")
    elif score >= 80:
        return("B")
    elif score >= 70:
        return("C")
    elif score >= 60:
        return("D")
    elif score >= 0:
        return("F")
    else:
        return("Invalid score.")

user_grade = check_grade(user)
rival_grade = check_grade(rival)

# print(user_grade)
# print(rival_grade)

print(f'You had a score of {user} {user_grade}. Your rival had a score of {rival} {rival_grade}')

