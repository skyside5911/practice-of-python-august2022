from genericpath import isdir
from socket import timeout
from selenium import webdriver
import time
import sys
import requests
import json
import base64
import time
import shutil
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
from fake_headers import Headers
from os import listdir
from os.path import isfile, join
from sys import exit
from bs4 import BeautifulSoup
import codecs
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException  
from datetime import datetime
import mysql.connector
# driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver")
mydb = mysql.connector.connect(
  host="64.227.176.243",
  user="phpmyadmin",
  password="Possibilities123.@",
  database="automation"
)
driver_path='C:\\browserdrivers\\chromedriver.exe'
header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate only Windows platform
    headers=False # generate misc headers
)

chrome_options = Options()
chrome_options.add_argument("--user-agent={customUserAgent}")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
#driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
s = Service(driver_path) 
options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options, service=s)
def remove_non_ascii_1(data):
    return ''.join([i if ord(i) < 128 else ' ' for i in data])
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM destination_website where status = 1 ")
myresult = mycursor.fetchall()
listt=[]
for des_id in myresult:
  listt.append(des_id[0])
bfw_li=[]
for des in listt:
  mycursor.execute("SELECT * FROM bulk_feed_website where des_id=(%s)" %  (des))
  websites = mycursor.fetchall()
  bfw_li.extend(websites)
alll=[]
for bfw_idd in bfw_li:
  mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) and status is Null " % (bfw_idd[0]) )
  webs = mycursor.fetchall()
  alll.extend(webs)
  print(mycursor.rowcount, f"record fetched from {bfw_idd[1]} ")
count=0
image_link_srcset=[]
image_link_src=[]

for x in alll:
    newdata=remove_non_ascii_1(x[4])
    soup = BeautifulSoup(newdata, 'html.parser')
    # site_name=(bfw_li[0][1]).split("/feed/")[0]
    
    
    for tag in soup.findAll():
        if(tag.name=="img"):
            # image_link_srcset.clear()
            # image_link_src.clear()
            image_link_srcset.append(tag.get("srcset"))
            image_link_src.append(tag.get("src"))
        
print("src_",image_link_srcset)
print("src =",image_link_src)
        
#  print(im)

    #  img_data = requests.get(ig).content
    
    #  with open(f'image_name{countt}.jpg', 'ab') as handler:
    #     handler.write(img_data)
    #     print(countt)
    #     countt+=1
    
    # toUploadImagePath = "H:\\practice of python august2022\\image_name.jpg"
    # all_image_link=[]
    # for im in image_link:
    #   print(im)
    #   all_image_link.append(site_name+im)
    # for imageURL in all_image_link:
    #     print(imageURL)
    #   img_data = requests.get(imageURL).content
      
          

    #   uploadImageFilename = "661b943654f54bd4b2711264eb275e1b.jpg"
    #   curHeaders = {
    #   'Authorization': 'Bearer ' + '''token''',
    #   "Content-Type": "image/jpeg",
    #   "Accept": "application/json",
    #   'Content-Disposition': "attachment; filename=%s" % uploadImageFilename,
    #   }

    #   resp = requests.post(
    #   "https://theleafdesk.com/wp-json/wp/v2/media",
    #   headers=curHeaders,
    #   data=img_data,
    #   )
    # newDict=resp.json()
            
            
    #     if(tag.name=="a" and tag.has_attr('href')):
    #       value_list.append(str(tag))
    #       key_list.append(tag.text)
    # for key, value in zip(key_list, value_list):
    #     b[key] = value
    # print(b)
            
        
           
        #     if('twitter' in tag['href'] or 'instagram' in tag['href'] or 't.co' in tag['href']):
        #         continue
        #     tag.parent.a.unwrap()
        # if(tag.name=='li'):
        #     if(len(tag.findChildren('a'))>0):
        #         tag.decompose()
    