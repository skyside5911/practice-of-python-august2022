import re
import requests
from bs4 import BeautifulSoup
url="https://www.celebritynetworth.com/category/richest-businessmen/richest-billionaires/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
detail= str(soup.find(attrs={'class':'details'}))
match=re.finditer(input('enter the variable you want to find'),detail)
print(type(match))
for m in match:
    print(type(m))
    print(m.group())
    print(m.start())