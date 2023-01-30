from ntpath import join
import scrapy
from datetime import datetime,timedelta
from urllib.parse import urlparse
import os
import csv
import mysql.connector
import pandas as pd

# driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver")
mydb = mysql.connector.connect(
  host="64.227.176.243",
  user="phpmyadmin",
  password="Possibilities123.@",
  database="automation"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM bulk_feed_content where bfc_id=319 ")
myresult = mycursor.fetchall()
for des_id in myresult:
  
  bb=(des_id[4])
  print(bb)
  # csvdata = pd.DataFrame(bb)
  # csvdata.to_csv("output.csv",index = False)
  # for tag in bb.findAll():
  #       if(tag.name=="img"):
  #         tag.show()
    # mycursor.execute("SELECT * FROM bulk_feed_website where bfc_id=(%s)" %  (des_id[0]))
    # websites = mycursor.fetchall()
    # print(websites)
# listt=[]
# for des_id in myresult:
#   listt.append(des_id[0])
# print(listt)
# bfw_li=[]
# for des in listt:
#   mycursor.execute("SELECT * FROM bulk_feed_website where des_id=(%s)" %  (des))
#   websites = mycursor.fetchall()
#   bfw_li.extend(websites)
# for bfw_idd in bfw_li:
#   mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) " % (bfw_idd[0]) )
#   webs = mycursor.fetchall()
#   print(webs)
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


