sentence = list(input("write a sentence:"))
letter_counts = {}# dict
for letter in sentence:
    #print(letter)
    if letter !=" ":
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
# print(letter_counts) # dict
letter_items = list(letter_counts.items())
letter_items.sort()
for char,count in letter_items:
      print(char,count)
