'''

fruits = [] # empty list
fruits = ["apple", "banana", "cherry"] # initialized list with three items
print(fruits) #outcome: ["apple", "banana", "cherry"]

# print the item at this index position
print(fruits[0]) #outcome: "apple"
print(fruits[1]) #outcome: "banana"
print(fruits[2]) #outcome: "cherry"

# for each item in the fruit list, print the item and its index
for fruit in fruits:
  print(f"{fruit} has an index of {fruits.index(fruit)}")

  '''
my_list = ["crimson", "violet", "teal", "pink", "grey"]

print(my_list[0])
print(my_list[-1])
# print(my_list[5]) # index out of range, so this will result in an error message
print(my_list)

# print each item at a time on its own line. Use a "for loop"
for item in my_list:
    print(item)

grades = [98, 74, 36, 88, 70]
for grade in grades:
    print(grade + 5)

grades.append(80) #add something to the end of the list. .append is a list method

print(grades)

grades.pop(2) # remove an item. number represents index

print(grades)

i = grades.index(70) # finds the index number for 70

grades.pop(i) #remove item at index i (which is 70 from above)

print(grades)

grades.insert(2, "apple") # inserts item in list. number is index, then you write what you want to insert
print(grades)