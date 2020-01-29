super_heroes = ['hero1', 'hero2', 'hero3']

# while True: # continues while true, which it always will be
#     fav_hero = input("what is your favorite super hero?")
#     if fav_hero not in super_heroes:
#         super_heroes.append(fav_hero) #adds input to end of list
#         # can also use super_heroes.insert(0, fav_hero). the "insert" adds to index 0
#     else:
#         print(super_heroes)
#         break

for num in range(5, 10): # one number creates a counting list, 2 numbers creates list between the two numbers, and third number is the iterator, or what it counts by
    print(num)