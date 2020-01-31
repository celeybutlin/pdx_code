"""Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirty room.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

    Convert the strings into lists (list)
    Sort the letters of each word (sort)
    Check if the two are equal

enter the first word: dormitory
enter the second word: dirtyroom
'dormitory' and 'dirtyroom' are anagrams
"""

# takes in a string from the use
first_string = input("Enter the first word: ").lower()
second_string = input("Enter the second word: ").lower()

# function that splits each string into words, and then each word into a master list of letters, and then sorts the list alphabetically
def letter_splitter(user_input):
    str_to_words = user_input.split() 
    all_letters = list()
    for word in str_to_words:
        letter = list(word)
        all_letters += letter
        all_letters.sort()
    return all_letters

if letter_splitter(first_string) == letter_splitter(second_string):
    print(f'{first_string} and {second_string} are anagrams!')
else:
    print(f'{first_string} and {second_string} are not anagrams!')

    


