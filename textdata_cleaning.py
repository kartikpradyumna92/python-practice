'''
DATA CLEANING AND PREPARATION PROJECT.
SENTIMENT ANALYSIS OF TWITTER DATA AFTER PERFORMING CLEANING OVER IT.
Author: Karteek Pradyumna Bulusu
'''

import csv
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
import itertools as it
import re

#STEMMING FUNCTION
st = LancasterStemmer()
#TO MAINTAIN THE COUNT OF NUMBER OF TWEETS
count = 0
#OPEN THE CSV FILE.
op = open ('Cleaned.csv','w')
third = []
csv_writer = csv.writer(op,lineterminator='\n',delimiter=',', quoting=csv.QUOTE_ALL)
with open('dclean_final.csv', newline='', encoding='utf8', mode='r', errors='ignore') as f:
    #READ THE CSV FILE.
    reader = csv.reader(f)
    #FOR EVERY ROW IN THE FILE
    for row in reader:
        t=0
        var=[]
        #FOR EVERY WORD IN THE ROW
        for word in row:

            #Convert all the words to lower case
            lower = word.lower()

            #Replace '!', '=' and '-' with '' (Empty)
            exclamation = lower.replace('!','').replace('=','').replace('-','').replace(',','').replace(';','').replace(':','').replace('(','').replace('"','').replace(')','').replace('^','').replace('#','')

            #STEMMING
            double = ''.join(ch for ch, _ in it.groupby(exclamation))

            #Removing usr names tagged in the tweets as well as Hyperlinks in the tweet.
            no_user = re.sub(r"(?:\@|https?\://)\S+","", exclamation)

            #all the stop words are removed
            no_user = ' '.join([xyz for xyz in no_user.split() if xyz not in stopwords.words("english")])

            #To the resultant, replace @ with empty.
            third = no_user.replace('@','').replace('http','').replace('?','').replace('*','').replace('%','')
            third = third.split(',')

            if ('www') in third:
                third.remove(third)

            #Final Clean data
            count += 1
            var.append(third)
            if (t%2 is not 0):
                #var=var.split(',')
                z=zip(var[0],var[1])
                for x in z:
                    csv_writer.writerow(x)
            t=t+1
            #sv_writer.writerow('\t')
            #csv_writer.writerow('\n')
    #print(count)