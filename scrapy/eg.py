from http.client import PARTIAL_CONTENT
from bs4 import BeautifulSoup
import requests
import pandas as pd
url='https://www.celebritynetworth.com/richest-celebrities/'
page=requests.get(url)
content=page.content
soup=BeautifulSoup(content,'html.parser')
for link in soup.find_all('a'):
    aa = link.get('href')

    pagee=requests.get(aa)
    contentt=pagee.content
    soupp=BeautifulSoup(contentt,'html.parser')
    name= soupp.find(class_ ="celeb_stats_table_header")
    worth=soupp.find(class_="value")
    
    # worth= soupp.find(class_ ="value").text
    if (name) != None:
        bbb = name.text
    if worth!=None:
        ccc=worth.text
        print(bbb)
        print(ccc)
data=[[bbb,ccc]]
dataframe=pd.DataFrame(data,columns={'name','worth'})
dataframe.to_csv("worth.csv")

        # print(worth)

    # name=soupp.find(attrs={'class':'title'}).text
    # worth=soupp.find(attrs={'class':'value'}).text 
# data=[[urll,name,worth]]
# print(soupp)
# dataframe=pd.DataFrame(soup,columns=['url'])
# dataframe.to_csv('csvdata22.csv')

