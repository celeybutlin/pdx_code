"""# String methods
sentence = "This was the best programming class I have ever taken."
sentence = sentence.upper()
print(sentence)

sentence = sentence.split() #splits the sentence into words and puts it into a list
print(sentence)

# List methods
sentence.append("Dog")
print(sentence)

num = sentence.count("Dog") # need to save to a variable because it returns a value. when a method returns a value, you need to SAVE it to a variable
print(num)

sentence.reverse() # do not need to save to a variable because it's not returning anything. just reverses it."""


def funkyfunc(listylist):
    for item in listylist:
        print(item)

def count_words(listylist):
    output = {}
    for item in listylist:
        if item not in output:
            output[item] = 1
        elif item in output:
            output[item] += 1
    return output


fav_foods = ["ramen", "ramen", "celery", "blueberries", "avocado", "pizza", "pizza", "tacocat", "thai", "curry", "taco"]

# funkyfunc(fav_foods)
count = count_words(fav_foods)
# print(count)
funkyfunc(count)

