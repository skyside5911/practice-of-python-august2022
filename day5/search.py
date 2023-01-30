from urllib import request
from bs4 import BeautifulSoup
import re
import requests
url="https://www.celebritynetworth.com/category/richest-businessmen/richest-billionaires/"
listt=[]
def networth(q):
    print(q)
    global listt
    pageq = requests.get(q)
    soupq = BeautifulSoup(pageq.content,"html.parser")
   
    for a in soupq.find_all('a', href=True):
        b = a['href']
        page2 = requests.get(b)
        soup2 = BeautifulSoup(page2.content,"html.parser")
        aa= soup2.find(attrs={'class':'title celeb_stats_table_header'})
        all=str(soup2.find(attrs={'class':'details'}))
        matcher=re.findall('<p>.*</p>',all)
        if matcher !=None:
            print(matcher)
        # bbb = matcher.group()


        
        # for match in matcher:
        #     bbb = match.group()
        #     listt.append(bbb)
networth(url) 
# list_of_info=[]
# j = 0
# for result in listt:
#     j += 1
#     dataa=(f"{j} = {result}")
#     list_of_info.append(dataa)
#     ll=str(list_of_info)
#     pa=re.sub('<p>','',ll)
#     pb=re.sub('</p>','',pa)
#     print(pb)
    # a=str(list_of_info).replace('<p>','')
    # b=[str(a).replace('</p>','')] 
    # for i in b:
    #     print(i)


  
  
                      

