from turtle import title
import pandas as pd
from bs4 import BeautifulSoup
import requests
url="https://www.celebritynetworth.com/richest-businessmen/richest-billionaires/jimmy-haslam-net-worth/"
page=requests.get(url)
content=page.content
soup=BeautifulSoup(content,'html.parser')
name=soup.find(attrs={'class':'title'}).text
worth=soup.find(attrs={'class':'value'}).text
para=soup.find(attrs={'class':'post_the_content'}).text


data=[[url,name,worth,para]]
dataframe=pd.DataFrame(data,columns={'url','name','worth','para'})
print(dataframe)
dataframe.to_csv('dat1aa.csv')