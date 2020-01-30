pets = {
    "Kona": "cat",
    "Lucifern": "rat",
    "Marco": "dog",
    "Cloud": "dog",
}

pets.pop("Cloud") # remove item from dictionary
pet = pets.get("Marco", "alternative value") # looks for Marco, but if it can't find it, then return "alternative value"

print(pet)



print(pets["Marco"]) #prints "dog"

pets["Herman"] = "snake" # adds key of Herman, with value of "snake" to the "pets" dictionary

print(pets)

print(pets["Cloud"]) #access the VALUE of the KEY (Cloud) that's passed through

pet_names = list(pets.keys()) # using LIST makes this a NEW list called pet_names

print(pet_names) # prints all pet names in a list, which are the keys from the PETS list

pet_types = list(pets.values()) #creates a new list of just the pets VALUES

print(pet_types) # prints the new list of pet VALUES, which are the types above


for key in pets: # for loop loops over the KEY when looping over a dictionary
    pets[key] = "dog" # makes all the values "dog", for each key
    print(f'{key}: {pets[key]}') 


count = 0
for key in pets:
    if pets[key] == "dog":
        count += 1

print(f"There are {count} dogs")

multiple = {
    "two": 2,
    "three": 3,
    "four": 4
}

num = 10

num = num * multiple["two"] #accesses the VALUE of KEY "two"

for key in multiple:
    print(f' {num * multiple[key]}') #adds a space before printing the number




