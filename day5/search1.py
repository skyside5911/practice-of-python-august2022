from urllib import request
from bs4 import BeautifulSoup
import re
import requests
url="https://www.celebritynetworth.com/category/richest-businessmen/richest-billionaires/"

pageq = requests.get(url)
soupq = BeautifulSoup(pageq.content,"html.parser")


all=soupq.find(attrs={'class':'post_items'})
getlink = all.a['href']
print(getlink)
pageaa = requests.get(url)
soupp = BeautifulSoup(pageaa.content,'html.parser')
for av in soupp.find_all('a', href=True):
    ab = av['href']
    print(ab)
        
    # bc = av['href']
    # pagea2 = requests.get(bc)
    # soupa2 = BeautifulSoup(pagea2.content,"html.parser")
    # if soupa2.find(class_ = "post_items") is not None:
    #     linkaa = soupa2.find(class_ = "post_items")
    #     getlinka = linkaa.a['href']
    #     print(getlink)
  



  
  
                      

