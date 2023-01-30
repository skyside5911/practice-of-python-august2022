from ntpath import join
import scrapy
from datetime import datetime,timedelta
from urllib.parse import urlparse
import os
import csv
import requests
import mysql.connector
mydb = mysql.connector.connect(
            host="64.227.176.243",
            user="phpmyadmin",
            password="Possibilities123.@",
            database="automation")
name = "quotes"
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM destination_website where status = 1 ")
myresult = mycursor.fetchall()
for dir in myresult:
    domain=dir[1]
    auth_url = "https://"+domain+"/wp-json/jwt-auth/v1/token"
    wp_user = dir[2]
    wp_pwd = dir[3]


    auth_data = {
            "username":wp_user,
            "password":wp_pwd
        }
    auth_responce = requests.post(auth_url , json=auth_data)
    token = auth_responce.json().get('data').get('token')
    print(auth_responce.json().get('data').get('token'))
    mycursor = mydb.cursor()
    # mycursor.execute("SELECT * FROM destination_website where status = 1 ")
    # myr = mycursor.fetchall()
    mycursor.execute("SELECT * FROM bulk_feed_website where des_id=(%s)" %  (dir[0]))
    # mycursor.execute("SELECT * FROM destination_website where username=(%s)" %  (myresult[2]))

    websites = mycursor.fetchall()
    alll=[]
    for i in websites:
  
        mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) and status = 1    " % (i[0]) )
        webs = mycursor.fetchall()
        alll.extend(webs)
        
        
    print(alll)
    print(mycursor.rowcount, "record inserted.")
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


