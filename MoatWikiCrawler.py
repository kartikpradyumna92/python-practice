'''
Moat Code Challenge:
Question 8: WIKI CRAWLER
-------------------------------
author: Karteek Pradyumna Bulusu
date: 09/10/2016
-------------------------------
Explanation:
------------
This programs aims in solving the issue of wiki crawling where given a random wikipedia URL and any number of iterations
, it crawls till it reaches the terminating condition of reaching the wiki page of Philosophy.

This is a recursive script where URL is taken as input, opened and parsed into HTML file. Later, I select only the body
content of the page and ignore the rest since it is not necessary. In this, I look for first URL that is outisde the
brackets and not italicized and provides it to the function in a recursive way for all iterations.
'''

#Packages used. URLLIB2 for opening URL. bs4 for parsing HTML file. re for implementing regex operations.
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib.pyplot as plt
from decimal import *

#base_url is initial part of the URL which gets added to the extension obtained in the program
base_url="https://en.wikipedia.org"

#recursive function which takes the url which is in String format.
def wikicrawl(url, count, i):
    global list
    '''
    Terminating condition. Manually stopping the recurssion if count exceeds 50. Absence of this statement might
    lead to forever running of the code.
    '''
    if count > 40:
        global nocount
        nocount += 1
        print("Count of pages that don't lead to philosophy -->",nocount)
        print ("Not found. Reached Maximum limit!")
        return
    #Satisfying case. If philosphy wiki page is found within 50 web crawls
    elif "Philosophy" in url:
        print ("The number of crawls for reaching %s is %s" %(url, count-1))
        list.append(count-1)
        global yescount
        yescount += 1
        print("The list of crawl counts is %s" %(list))
        print("Count of Pages of leading to philosophy is %s " %(yescount))
        print ("Yes! Found the page!")
        return

    #urllib function to open the webpage.
    htmlpage = urlopen(url)

    #This would replace hyperlinks in the brackets with empty and hence avoids it from being considering for crawling.
    pattern = re.compile(r'\(...\)')
    htmlpage_content = re.sub(pattern,'',htmlpage.read())

    #OUTPUT print syntax.
    print (url)
    print ("count of the Crawl is %s" %(count))

    #html.parser will parse the html webpage in the format of .htm. Used Beautiful Soup for this task.
    bsoup = BeautifulSoup(htmlpage_content, 'html.parser')

    '''
    I find the div tags in the HTML page which has id as "bodyContent" and look for all the p tags. Since p tags will
    have the paragraphs of the content, I am looking for content in all the p tags. And "bodyContent" div has whole
    content of the wikipedia webpage.
    '''
    ptagcontent = bsoup.find("div", {"id": "bodyContent"}).findAll('p')

    #for every paragraph
    for para in ptagcontent:
        # All the links in the paragraph are stored in "links".
        links = para.findAll('a',href=True)
        # for each link
        for link in links:
            '''
            Only links that start with "\wiki" are accepted and others are ignored since it is "Wiki crawling task".
            '''
            if link['href'].startswith("/wiki") and "(" not in link.contents[0]:
                #This new URL goes to the method and repeats the process and again.
                print("Crawls to")
                count += 1
                wikicrawl(base_url+link['href'], count, i)
                return;
    return

#Declaration.
list = [] #for storing all path length values
yescount = 0 #to keep a count of instances where it leads to philosophy page
nocount = 0 #This keeps the count where it doesn't lead to philisophy page
rangeval = 50 #This sets of number of random wiki pages it should perform the wiki crawl on.

#This calls the function
for i in range(0,rangeval):
    wikicrawl("https://en.wikipedia.org/wiki/Special:Random", 0, i)

#calculate the percent of yescount.
total = rangeval
print(list)
getcontext().prec = 6
print("percent is occurence of philosophy wikipedia page in above iterations is: {percent:.2%}".format(percent = float(yescount)/float(total)))

'''
HISTOGRAM
Used numpy and Matplotlib.pyplot to plot the histogram
'''
ln = np.arange(len(list))
plt.bar(ln, list, width= 0.1)
plt.xticks(ln, list)
maxval = max(list) + 10
plt.ylim(0, maxval )
plt.xlabel('Each website')
plt.ylabel('Path length')
plt.title('Distribution of path length.')
plt.show()