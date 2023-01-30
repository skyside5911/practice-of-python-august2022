#find anything by giving 2 variables using re module and search function
import re

import requests

from bs4 import BeautifulSoup
url="https://www.celebritynetworth.com/category/richest-businessmen/richest-billionaires/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
# detail= soup.find(attrs={'class':'post_items'})
# hello = detail.find_all(class_="post_item")
# nn=str(hello)
a=input("enter what you want ")
b=input("enter the another variable ")
result=re.search('{}(.*){}'.format(a,b),str(soup))
try:
  print(result.group(1))
except AttributeError:
    print("not found")


