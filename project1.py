#importing necessary modules

from operator import itemgetter
from collections import Counter



file = open('text.txt')# opening a file
# Initializing a dictionary

D = dict()


for line in file:
    # removing extra spaces and converting to small letters
    line = line.rstrip().lstrip().lower()
    # removing special characters
    for char in '-.,(){}[]\':;*!"?\n':
        line = line.replace(char,'')
    # to verify print(line)
    words = line.split()
    # to verify print(words)
# Filling the Dictionary
for w in words:
    D[w] = D.get(w,0)+1

#print(D)

part2=open('text.txt','r')
x=part2.read()
total_words = len(x.split(' '))
#print('Total number if words is ' + str(total_words))
#print(v)
import csv
allwords = (sorted(D.items(), key = itemgetter(1)))
allwords.reverse()

for each in allwords:
    word,number = each
# print(word,number,number/float(total_words))
# writing all contents to a .csv file
with open ('results.csv','w') as f:
    for word,number in allwords:
        print(word,',',number,',',number/float(total_words),file =f)

with open('text.txt', 'r') as file:
    file_contents = file.read()
    # counting total number of stops like . ? and !
    Total_stops = (file_contents.count('.')+ file_contents.count('?')+file_contents.count('!'))
    # Sentences that start with the
    Sentences_The = (file_contents.count('. The') +file_contents.count('? The')+file_contents.count('! The')+file_contents.count('The ') )
    # total number of words
    print('Total words:   ', len(file_contents.split()))
    # total number of sentences
    print('Total number of sentences:    ', Total_stops )
    # Code for question 2 of project
    print('Total sentences starting with THE:    ', Sentences_The )
    print('Frequency of sentences with THE:     ',Sentences_The/Total_stops)

# Code for question 3 of project
with open('text.txt') as f:
    words = f.read().splitlines() # read lines from the text
#Creating a list of word pairs using zip function
Word_Pair = [b for l in words for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
#Counting the most common word
print('Most common word pair and its count is  ',Counter(Word_Pair).most_common(1))

