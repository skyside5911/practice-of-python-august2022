#find anything by giving 2 variables using re module and search function
import re
import requests

from bs4 import BeautifulSoup
a=input("enter what you want ")
b=input("enter the another variable ")

with open ('csvdata.csv', 'r') as file:
    for url in file:
        
        page=requests.get(url)
        soup=BeautifulSoup(page.content,"html.parser")

        result=re.search('{}(.*){}'.format(a,b),str(soup))
        try:
            print(result)
        except AttributeError:
            print("not found")