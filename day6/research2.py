import re
import requests
import csv
from bs4 import BeautifulSoup
url="https://www.celebritynetworth.com/category/richest-businessmen/richest-billionaires/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
detail= str(soup.find(attrs={'class':'post_items'}))
# print(detail)

s = 'asdf=5;iwantthis123jasd'
result = re.search('asdf=5;(.*)123jasd', s)
print(result.group(1))

a=input("enter what you want ")
if a not in detail:
    print('variable is not in object ')
else:   
    sp=re.split(a,detail)
    print(sp)
    sp1=sp[1]
    b=input("enter the another variable ")
    if b not in sp1:
      print("variable is not in object ")
    else:
        sp2=re.split(b,sp1)
        print(sp2[0])
        with open('raj1.csv','w') as file:
            raj=csv.writer(file)
            raj.writerow([sp2[0]])
    
