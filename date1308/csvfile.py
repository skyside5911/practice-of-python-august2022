#find anything by giving 2 variables using re module and search function
import re
import bs4
import requests
import csv
from bs4 import BeautifulSoup
url="https://www.celebritynetworth.com/richest-businessmen/richest-billionaires/vladimir-potanin-net-worth/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

# detail= soup.find(attrs={'class':'post_item'})
a=input("enter what you want ")
b=input("enter the another variable ")
hello = soup.find(attrs={'class':'primary'})

result=re.search('{}(.*){}'.format(a,b),str(hello))
try:
  print(result.group(1))
except AttributeError:
    print("not found")


