import pandas as pd
import requests
from bs4 import BeautifulSoup
url="https://www.celebritynetworth.com/richest-celebrities/singers/michael-jackson-net-worth/"
page=requests.get(url)
content=page.content
soup=BeautifulSoup(content,"html.parser")
# para=soup.findAll(attrs={'class':'post_the_content'})
name=soup.find(attrs={'class':'title'}).text
worth=soup.find(attrs={'class':'value'}).text


# alldetails = [name, worth]

# print(alldetails)

# print(worth)
results=soup.find("p")

data_text = results.text
data=[[url,name,worth,data_text]]
print(data)
dataframe=pd.DataFrame(data,columns=['url','name','networth','data_text'])
dataframe.to_csv('csvdata1.csv')
# print(dataframe)