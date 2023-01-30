from ntpath import join
import scrapy
from datetime import datetime,timedelta
from urllib.parse import urlparse
import os
import csv
import mysql.connector

# driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver")
mydb = mysql.connector.connect(
  host="64.227.176.243",
  user="phpmyadmin",
  password="Possibilities123.@",
  database="automation"
)
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
print(bfw_li)
for bfw_idd in bfw_li:
  mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) and status is Null " % (bfw_idd[0]) )
  webs = mycursor.fetchall()
  print(webs)
  # bfw_list=[]
  # for bfw_id in websites:
  #  bfw_list.append(bfw_id)
  # print(bfw_list)
  # for aa in bfw_list:
  #   mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) " % (aa) )
  #   webs = mycursor.fetchall()
  # print(webs)
# listt=[]
# for i in websites:
#   listt.append(i[0])
# for aa in listt:
#   mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) " % (aa) )
#   webs = mycursor.fetchall()
#   print(webs)
# print(listt)


