
import json
import requests
import time
import imageio.v2 as iio
import os
import base64
auth_url = "https://thestiflerstories.com/wp-json/api/v1/token"
auth_data = {
      "username":"banturana5911@gmail.com",
    "password":"rbe!&#_583-*^)@TV"
}
auth_responce = requests.post(auth_url , json=auth_data)
tokenn = auth_responce.json().get("jwt_token")
print(tokenn)
source_url = "https://theleafdesk.com/wp-json/wp/v2/posts?_embed"
destination_url ="https://www.thestiflerstories.com/wp-json/wp/v2/posts/"
data = requests.get(source_url).json()
count=0
for p in data:
    count+=1
    title=p['title']['rendered']
    content=p['content']['rendered']
    slug=p['slug']
    header = {'Authorization': 'Bearer ' + tokenn}
    post = {
    'title'    : title,
    'status'   : 'draft', 
    'content'  : content,
    'slug':slug,
    }  
    print(post)
    responce = requests.post(destination_url , headers=header, json=post)
    print(responce)
    if count==4:
        break