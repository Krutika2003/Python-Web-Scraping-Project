# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SF64zyoWM0UESxcMxHedq3W5pD4-WL_V
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.nykaa.com/search/result/?q=nykaa%20jewellery&root=search&searchType=Manual&sourcepage=home"
URL

r = requests.get(URL)
htmlcontent = r.content
htmlcontent

soup = BeautifulSoup(htmlcontent,"html.parser")
print(soup)
soup.prettify

title = soup.title
print(type(soup))
print(type(title))

jewellery_name = soup.find_all("div",class_="css-xrzmfa")
print(jewellery_name)

jewellery_name_list = []
for i in range(0,len(jewellery_name)):
  jewellery_name_list.append(jewellery_name[i].get_text())
print(jewellery_name_list)

"""**MRP/PRICE/DISCOUNT%**"""

price= soup.find_all("div",class_="css-1d0jf8e")
print(price)

price_list = []
for i in range(0,len(price)):
  price_list.append(price[i].get_text())
print(price_list)

"""**REVIEWS**"""

reviews= soup.find_all("div",class_="css-wskh5y")
print(reviews)

reviews_list = []
for i in range(0,len(reviews)):
  reviews_list.append(reviews[i].get_text())
print(reviews_list)

"""**IMPORT PANDAS**"""

import pandas as pd
df = pd.DataFrame({"Jewellery_Name":jewellery_name_list,"Price":price_list,"Reviews":reviews_list})
print(df)

"""**TO STORE IN CSV FILE**"""

import os
os.getcwd()

df.to_csv("Nykaa_jewellery.csv",index = False)

df1 = pd.read_csv("Nykaa_jewellery.csv")
df1

