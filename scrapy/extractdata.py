
import requests
from bs4 import BeautifulSoup
url="https://www.celebritynetworth.com/richest-celebrities/singers/michael-jackson-net-worth/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
# for link in soup.find_all('a'):
#     print(link.get('href'))
# for tag in soup.find_all(True):
#     print(tag.name)
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# soup.find_all(has_class_but_no_id)
# print(soup)
results=soup.find_all("p")
list_of_info=[]
j = 0
for result in results:
    j += 1
    title= result.text
    dataa=(f"{j} = {title}")
    list_of_info.append(dataa)
print(list_of_info)

# for string in soup.strings:
#     print(repr(string))
# results=soup.find_all('div',id_="mosaic-zone-jobcards")
# # print(page
# print(results)