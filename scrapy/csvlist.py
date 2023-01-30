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
# aaa  = soup.find(class_ = " ")


# alldetails = [name, worth]

# print(alldetails)

# print(worth)
results=soup.find_all("p")
list_of_info=[]
j = 0
for result in results:
    j += 1
    title= result.text
    dataa=(f"{j} = {title}")
    list_of_info.append(dataa)
# print(list_of_info)

# data_text = results.text
data=[[url,name,worth,list_of_info]]
# print(data)
dataframe=pd.DataFrame(data,columns=['url','name','networth','data_text'])
dataframe.to_csv('csvdata2.csv')