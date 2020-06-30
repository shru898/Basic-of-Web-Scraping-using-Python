# -*- coding: utf-8 -*-
"""data_collect.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jc-pnHVP7JtCecb507vd3L3WapE_JqXT
"""

from bs4 import BeautifulSoup as bs  #for pulling data out of HTML and XML files
import pandas as pd  #data analysis and manipulation tool
pd.set_option('display.max_colwidth', 500)
import time
import requests  #allows HTTP requests to be sent using Python
import random  #to generate psuedo random numbers

page = requests.get("http://quotes.toscrape.com/")
page  #returns a response status code showing that the request has been completed successfully

#parsing website using BeautifulSoup
soup = bs(page.content)
soup

"""There are two ways of finding quotes from the website. First is by finding it in the parsed HTML document. Second is by using *.find_all()* in the code. This function will return desired lines of code based on the class mentioned within."""

soup.find_all(class_='text')

quotes = [i.text for i in soup.find_all(class_='text')]  #for retrieving the test and excluding the unnecessary code 
quotes

authors = [i.text for i in soup.find_all(class_='author')] #for retrieving author names
authors

#accessing multiple pages of a single website
urls=[f"http://quotes.toscrape.com/page/{i}/" for i in range(1,11)]
urls

"""Some websites do not allow scraping. It has a limited number of requests from user end. In order to avoid this, requests can be randomized to mimic human interation."""

rate = [i/10 for i in range(10)]  #to generate list of values
time.sleep(random.choice(rate))  #for pausing the code for selected amount of time

#this is for slowing down the code in order to avoid detection of many requests at a time

authors = []
quotes = []

for url in urls:
  
    page = requests.get(url)  #for accessing the Webpage
    
    soup = bs(page.content)  # for getting the webpage's content in pure html

    authors.extend([i.text for i in soup.find_all(class_='author')]) #adding authors to the list

    quotes.extend([i.text for i in soup.find_all(class_='text')])  #adding quotes to the list
       
    time.sleep(random.choice(rate))  #randomizing request rate

authors[0:4]

quotes[0:3]

# Creating a DataFrame to store our newly scraped information
d={'Author':authors,'Quote':quotes}
df=pd.DataFrame(d)
df.head(5)