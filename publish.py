from genericpath import isdir
from socket import timeout
from selenium import webdriver
import time
import requests
import json
import base64
import time
import shutil
#driver = webdriver.PhantomJS('/opt/homebrew/bin/phantomjs')
#driver = webdriver.Remote(
 # desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
#driver = webdriver.Chrome()
#from webdriver_manager.chrome import ChromeDriverManager
#Timer starts 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
from fake_headers import Headers
# %%
from os import listdir
# %%
from os.path import isfile, join
#import sys
from sys import exit
import mysql.connector
mydb = mysql.connector.connect(
  host="64.227.176.243",
  user="phpmyadmin",
  password="Possibilities123.@",
  database="automation"
)

#sitepath="/Users/rishi/Dropbox/sites/"
#mypath="/Users/rishi/Google Drive/My Drive/sites/editorials24.com/"
#processed_path=mypath+"processed/"
#dirs = [f.name for f in os.scandir(sitepath) if f.is_dir()]
dirs = ["www.therconline.com"]
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#if not onlyfiles:
#   exit("no files to process")

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate only Windows platform
    headers=False # generate misc headers
)
#customUserAgent = header.generate()['User-Agent']


#start = timeit.default_timer()
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
#chrome_options.add_argument("--user-data-dir=chrome-data")
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
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'D:\\work\\python\\webscrape\\chromedriver.exe')
#driver.set_window_size(1920, 1080)

wp_user = "gh1YcBHVrq"
wp_pwd = "zd2eW0Aj6F"


for dir in dirs:
    domain=dir
    auth_url = "https://"+domain+"/wp-json/jwt-auth/v1/token"
    

    auth_data = {
            "username":wp_user,
            "password":wp_pwd
        }
    auth_responce = requests.post(auth_url , json=auth_data)
    token = auth_responce.json().get('data').get('token')
    print(auth_responce.json().get('data').get('token'))
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM bulk_quill where publish_status is null limit 10")
    myresult = mycursor.fetchall()
    print(mycursor.rowcount, "record inserted.")
    for x in myresult:
        url = "https://"+domain+"/wp-json/wp/v2/posts"
        #user = "rishi"
        #password = "271191.rishi"
        #credentials = user + ':' + password
        #token = base64.b64encode(credentials.encode())
        #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2NhbGhvc3Q6ODEiLCJpYXQiOjE2NDkzMjU5MjEsIm5iZiI6MTY0OTMyNTkyMSwiZXhwIjoxNjQ5OTMwNzIxLCJkYXRhIjp7InVzZXIiOnsiaWQiOjEsImRldmljZSI6IiIsInBhc3MiOiI3YWQ3MjcwODkzNDgyNmVhMmVhZTI1YjQ2NjA2N2I3NyJ9fX0.i_TkLtUBl-RAdDwuik3czhFL1mXaa1Da9wiWrH1AeQM"
        header = {'Authorization': 'Bearer ' + token}
        current=time.strftime("%Y-%m-%dT%H:%M:%S",time.localtime())
        print(current)
        title = x[2]
        print(title)
        post = {
        'title'    : title,
        'status'   : 'draft', 
        'content'  : x[4],
        'categories': 16
        }
        sql = "update bulk_quill set publish_status=%s where wcid=%s"
        val = (1, x[0])
        mycursor.execute(sql, val)
        #'date'   : '2022-04-07T10:00:00'
        responce = requests.post(url , headers=header, json=post)
        
        #print(responce.text)
#driver.quit()