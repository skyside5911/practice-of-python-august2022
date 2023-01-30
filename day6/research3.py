import re
import bs4
import requests
import csv
from bs4 import BeautifulSoup
url="https://www.celebritynetworth.com/category/richest-businessmen/richest-billionaires/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
detail= soup.find(attrs={'class':'post_items'})
# print(type(detail))
for i in detail:
        
    
    if type(i) is not bs4.element.NavigableString :
      
      nn=str(i)
      a=input("enter what you want ")
      b=input("enter the another variable ")

      result=re.search('{}(.*){}'.format(a,b),i)
 
      print(result.group(1))
        
                
            



    


    
