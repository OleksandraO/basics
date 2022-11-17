# H/W: Problem-solving (amazon):
# write a functions that return letters with counts, i.e. how many times each letter is used 
# in the string (word, sentence, bigger text ..)
# Sample Input and Output: 'hello' -> {'h':1, 'e':1, 'l':2, 'o':1}
# album['letter'] += tracks  # adding the value to a previous value of the key in the dictionary
# album['letter'] = album['letter'] + tracks

###  H  e  l  l  o

#input('Enter the word')
word = input('Enter the word')
char_dict ={}
for char in word:
    if char not in char_dict:
        char_dict[char] = 0

    char_dict[char] += 1

print(char_dict)
