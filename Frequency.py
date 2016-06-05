# WORK MARKET CODE CHALLENGE-- Postion: Data Analyst
# QUESTION: Counting Vitae
#Take the plaintext version of your resume (or linkedin profile) and create a bar chart of character frequency. (Bonus programmatically strip out punctuation and whitespace.)
#Author: Karteek Pradyumna Bulusu.

import numpy as npy
import pylab as plab

#Read the text file
file = open('resume.txt')

#Reading the file.
data = file.read()
#creating the dictionary. This will store the characters as key-value pair.
cha = {}

#for every line in the file, I am converting it into lower case. Further I am removing all special characters and punctuations.
#I am considering only alphabets and numbers.
#Logic: If the element already exists in the dictionary, I am incrementing the count. If it is not present in the dictionary I am assigning the value = 1.
#Key represents the character and value represents the frequency.
for line in data:
    line = line.lower()
    new = ''.join(e for e in line if e.isalnum())
    if new in cha:
        cha[new] += 1
    else:
        cha[new] = 1
    if '' in cha:
        del cha['']
#Printing all the characters with frequency stored in dictionary 'cha'.
print(cha)

# GENERATING THE HISTOGRAM.
len = npy.arange(len(cha))
plab.bar(len, cha.values(), width=1.0, align='center')
#x axis has the keys in the dictionary.
plab.xticks(len, cha.keys())
#Maximum value of y axis is max value of dictionary added to 50.
max_Value = max(cha.values()) + 50
plab.ylim(0, max_Value)
plab.title('Character frequency of my Resume')
plab.show() #printing the histogram.
