
###
#Take a loot at the essay.txt file tab. That file contains some text.
# You should create a program that reads the essay.txt file, converts the first letter of each word to uppercase and prints out the converted text.

file = open('Files/essay.txt','r')
content = file.read().split(' ')
for word in content:
    print(word.capitalize(),'', end='')
file.close()
##
# Write a program that reads the essay.txt file and returns the number of characters contained in the file.
print("\n")
file = open('Files/essay.txt','r')
content2 = file.read()
print(len(content2))
file.close()