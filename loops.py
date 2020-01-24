emoticons = [':-)', ':-(', ':/', ':|']

for face in emoticons:
    print(face)

for i in range(5): # 5 is the number of times we want to do this
    print('Hello class!')
    print(i) # i is the index


x = 0
while x < 5:
    x += 1 
    if x == 3:
        continue # go back to top of loop. essentially skips 3 and never makes it to the smiley face
    print(x, ':-)')  
    if x == 3: # this no longer runs because when x == 3, it goes back to the top and does not continue down. It adds 1 and becomes 4 before it ever hits this line
        break
else:
    print(x, ':-(')