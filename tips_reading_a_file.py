f = open('text.txt', 'r')
file_contents = f.read()
f.close()

words = file_contents.split(' ')
word_count = len(words)

# print(word_count)

# Syntax Can be simplified below

with open('text.txt', 'r') as f:
    file_contents = f.read()

# ***
