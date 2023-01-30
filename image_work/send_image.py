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
# driver_path=sys.argv[1]
#driver_path=sys.argv[1]
#sitepath=sys.argv[2]
driver_path='C:\\browserdrivers\\chromedriver.exe'
# driver_path=r'/usr/bin/chromedriver'
#sitepath="D:\\work\\python\\webscrape\\"
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
def check_exists_by_xpath(xpath):
    try:
        #driver.find_element_by_xpath(xpath)
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True
def quill_login(driver):
    wp_user = "gh1YcBHVrq"
    wp_pwd = "zd2eW0Aj6F"
    #driver.get("https://quillbot.com")
    driver.get("https://quillbot.com/login")
    quill_user = "sahil.17.chopra@gmail.com"
    quill_pwd = "thealtweb123"
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/input[1]')))
        #print("Page is ready!")
    except TimeoutException:
        print("1Loading took too much time!")
    #username = driver.find_element_by_xpath("//*[@id='mui-3']")
    username = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/input[1]")
    username.clear()
    username.send_keys(quill_user)
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[5]/div[1]/div[1]/input[1]')))
        #print("Page is ready!")
    except TimeoutException:
        print("2Loading took too much time!")
    #password = driver.find_element_by_xpath("//*[@id='mui-4']")
    password = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[5]/div[1]/div[1]/input[1]")
    password.clear()
    password.send_keys(quill_pwd)
    #driver.find_element_by_xpath("//*[@id='loginContainer']/div/div[6]/button").click()
    driver.find_element(by=By.XPATH, value="//*[@id='loginContainer']/div/div[6]/button").click()
    #time.sleep(5)
          
    status = check_exists_by_xpath('//div[contains(@class,"MuiDialogContent-root")]/button')
    if(status):
        #element=driver.find_element_by_xpath('//div[contains(@class,"MuiDialogContent-root")]/button')
        element=driver.find_element(by=By.XPATH, value='//div[contains(@class,"MuiDialogContent-root")]/button')
        print(status)
        driver.execute_script("arguments[0].click();", element)
def process_soup(soup):
    """ def findchild(tag):
        print(tag.name)
        if(len(tag.findChildren())>0):
            for childtag in tag.findAll():
                findchild(childtag)

    for tag in soup.findAll(recursive=False):            
        findchild(tag)
    """
    for tag in soup.findAll():
        if(tag.name=="img"):
            tag.decompose()
        # if(tag.name=="a" and tag.has_attr('href')):
        #     if('twitter' in tag['href'] or 'instagram' in tag['href'] or 't.co' in tag['href']):
        #         continue
        #     tag.parent.a.unwrap()
        # if(tag.name=='li'):
        #     if(len(tag.findChildren('a'))>0):
        #         tag.decompose()
    p=soup.findAll()
    print(p)
    newtext=[None]*len(p)
    i=-1
    for tag in p:
        i+=1
        if(tag.name=='p'):
            if(tag.findParent().name=='blockquote'):
                continue
            if(len(tag.findChildren('p'))>0):
                continue
            if(tag.text=='' or tag.get_text(strip=True)==''):
                continue
            #newtext=newtext + tag.text + "\n\n\n"
            #newtext[i]=tag.find(text=True, recursive=False)
            newtext[i]=tag.get_text(strip=True)
        
    #list=[str(newtext.index(x))+"."+x for x in newtext if x is not None and x is not '']
    list=[x for x in newtext if x != None and x != '']
    print("quilling p count:",len(list))
    str1=""
    for ele in list: 
        str1 += ele + "\n\n\n"
    print("word count:-",len(str1.split()))
    return str1  
def paraphrase_soup(driver,str1):
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'inputText')))
            #print("Page is ready!")
    except TimeoutException:
        print("3Loading took too much time!")
    status = check_exists_by_xpath('//*[@id="max-width-dialog-title"]/button')
    if(status):
            #element=driver.find_element_by_xpath('//*[@id="max-width-dialog-title"]/button')
        element=driver.find_element(by=By.XPATH, value='//*[@id="max-width-dialog-title"]/button')
        print(status)
        driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.ID,'inputText').clear()
    driver.find_element(By.ID,'inputText').send_keys(str1)
    time.sleep(2)       
        #element=driver.find_element_by_xpath('//button/div[text()="Paraphrase"]')
    element=driver.find_element(by=By.XPATH, value="//*[@id='InputBottomQuillControl']/div/div/div/div[2]/div/div/div/div/button")
    driver.execute_script("arguments[0].click();", element)
        #print(driver.current_url)
        #time.sleep(10)
    timeout = 20 # seconds
    status = check_exists_by_xpath('//*[@id="max-width-dialog-title"]/button')
    if(status):
            #element=driver.find_element_by_xpath('//*[@id="max-width-dialog-title"]/button')
        element=driver.find_element(by=By.XPATH, value='//*[@id="max-width-dialog-title"]/button')
        print(status)
        driver.execute_script("arguments[0].click();", element)
    try:
        myElem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//button/div[text()="Rephrase"]')))
        print("paraphrase Page is ready!")
    except TimeoutException:
        print("4Loading took too much time!")
        
    #time.sleep(20)
        #content = driver.find_element_by_xpath("//*[@id='editable-content-within-article']").text
    status = check_exists_by_xpath('//*[@id="max-width-dialog-title"]/button')
    if(status):
            #element=driver.find_element_by_xpath('//*[@id="max-width-dialog-title"]/button')
        element=driver.find_element(by=By.XPATH, value='//*[@id="max-width-dialog-title"]/button')
        print(status)
        driver.execute_script("arguments[0].click();", element)
    time.sleep(30) 
    delay = 10 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='editable-content-within-article']")))
            #print("Page is ready!")
    except TimeoutException:
        print("3Loading took too much time!")
    content = driver.find_element(by=By.XPATH, value="//*[@id='editable-content-within-article']").text
    return content

# datetime object containing current date and time
now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	
#sitepath="/Users/rishi/Dropbox/sites/"
#o_path = r"F:\\My Drive\\sites\\www.therconline.com\\raw\\data_output.html"
#dirs = [f.name for f in os.scandir(sitepath) if f.is_dir()]
dirs = ["www.therconline.com"]

quill_login(driver)

# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM bulk_feed_content where status is null")
# myresult = mycursor.fetchall()
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM destination_website where status = 1 ")
myresult = mycursor.fetchall()
listt=[]
for des_id in myresult:
  listt.append(des_id[0])
print(listt)
bfw_li=[]
for des in listt:
  mycursor.execute("SELECT * FROM bulk_feed_website where des_id=(%s)" %  (des))
  websites = mycursor.fetchall()
  bfw_li.extend(websites)
alll=[]
print(bfw_li)
for bfw_idd in bfw_li:
  mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) and status is Null " % (bfw_idd[0]) )
  webs = mycursor.fetchall()
  alll.extend(webs)
  print(mycursor.rowcount, f"record fetched from {bfw_idd[1]} ")
print(alll)
count=0
for x in alll:
    
    newdata=remove_non_ascii_1(x[4])
    soup = BeautifulSoup(newdata, 'html.parser')
    
    #soup.find_all('p')[-1].decompose()
    ### <figure> Tags

    str1=process_soup(soup)
    if(len(str1.split())<10):
        #shutil.move(file_path,discarded)
        mycursor.execute("update bulk_feed_content set content_modify=%s,status=0 where bfc_id=%s", (None,x[0]))
        mydb.commit()
        continue    
    content=paraphrase_soup(driver,str1)

    quilled_text=content.split('\n\n\n')
    print("quilled p count:",len(quilled_text))
    #print("p count:",len(soup.find_all('p',recursive=False)))
    #for x in quilled_text:
    #    i=int(x.split(".",1)[0])
    #    p[i].string=x.split(".",1)[1]

    p=soup.findAll()
    i=-1
    j=0
    flag=1
    for tag in p:
        i+=1
        if(tag.name=='p'):
            if(tag.findParent().name=='blockquote'):
                continue
            if(len(tag.findChildren('p'))>0):
                continue
            if(tag.text=='' or tag.get_text(strip=True)==''):
                continue
            #newtext=newtext + tag.text + "\n\n\n"
            #newtext[i]=tag.find(text=True, recursive=False)
            try:
                p[i].string=quilled_text[j]
                j+=1
            except IndexError:
                mycursor.execute("update bulk_feed_content set content_modify=%s,status=0 where bfc_id=%s", (str(soup),x[0]))
                mydb.commit()
                print("exception")
                flag=0
                break

    #f = open(spinned,"w",encoding='utf-8')
    #with codecs.open(spinned, 'w',encoding="utf-8") as f:
    #f.write(str(soup)) 
    print("The End")
    if flag==1:
        mycursor.execute("update bulk_feed_content set content_modify=%s,status=1 where bfc_id=%s", (str(soup),x[0]))
        mydb.commit()
        count+=1
    if count==3:
        break
    #shutil.move(file_path,processed)
driver.quit()
