from cmath import pi
from csv import writer
from email import header
from msilib import add_data
from netrc import netrc
from ntpath import join
from operator import ne
from bs4 import BeautifulSoup
import requests
import csv

url ="https://www.celebritynetworth.com/richest-athletes/"

# page = requests.get(url)

# soup = BeautifulSoup(page.content, "html.parser")

# get_link = soup.find(class_ = "paginate_buttons navigation main_margin")

# get_href = get_link.a['href']

# print(get_href)

# pageall = requests.get(get_href)

# soupall = BeautifulSoup(pageall.content, "html.parser")
urlsfornext=[]

add_net = []
j = 0
def recursion(urlsfornext):
    urlsnet = urlsfornext[0]
    print(urlsnet)
    pageaa = requests.get(urlsnet)
    soupp = BeautifulSoup(pageaa.content,'html.parser')
    for av in soupp.find_all('a', href=True):
        
        bc = av['href']
        pagea2 = requests.get(bc)
        soupa2 = BeautifulSoup(pagea2.content,"html.parser")
    
        linkaa = soupa2.find(class_ = "value")
        linkba = soupa2.find(class_ = "celeb_stats_table_header")
        if  linkba or linkaa != None:
          aab = linkba.text
          bba = linkaa.text
          add_dataa = [aab , bba]
          print(add_dataa)            
    global j
    j +=1
    print(j)
    if j == 4:
        return print("this is ending ")
           
    else: 
        soupp.find(class_ = "paginate_buttons navigation main_margin" ) is not None
        get_linkaa = soupp.find(class_ = "paginate_buttons navigation main_margin")
        get_hrefaa = get_linkaa.a['href']
        urlsfornext.clear()
        print(get_hrefaa)
        urlsfornext.append(get_hrefaa)
        recursion(urlsfornext)     

# recursion(url)
# abcd(a)        
def networth(q):
    print(q)
    pageq = requests.get(q)
    soupq = BeautifulSoup(pageq.content,"html.parser")
    for a in soupq.find_all('a', href=True):
        b = a['href']
        page2 = requests.get(b)
        soup2 = BeautifulSoup(page2.content,"html.parser")
    
        linka = soup2.find(class_ = "value")
        linkb = soup2.find(class_ = "celeb_stats_table_header")
        if  linkb or linka != None:
            aa = linkb.text
            bb = linka.text
            add_data =[aa , bb]
            print(add_data) 
              
    if soupq.find(class_ = "paginate_buttons navigation main_margin") is not None:
        get_linka = soupq.find(class_ = "paginate_buttons navigation main_margin")
        get_hrefa = get_linka.a['href']
        print(get_hrefa)
        urlsfornext.append(get_hrefa)
        print(urlsfornext)
        return recursion(urlsfornext) 
       

networth(url)
