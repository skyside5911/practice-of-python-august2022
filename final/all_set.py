import requests
import json
import imageio.v2 as iio
import os
import base64
auth_url = "https://www.onlinecasinogames777.com/wp-json/jwt-auth/v1/token"
auth_data = {
      "username":"admin",
    "password":"pwd12345"
}
auth_responce = requests.post(auth_url , json=auth_data)
token = auth_responce.json().get('data').get('token')
print(auth_responce.json().get('data').get('token'))
source_url = "https://theleafdesk.com/wp-json/wp/v2/posts?_embed"
destination_url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/posts/"
url ="https://www.onlinecasinogames777.com/wp-json/wp/v2"
count=0
data = requests.get(source_url).json()
for p in data:
    count+=1
    title=p['title']['rendered']
    content=p['content']['rendered']
    slug=p['slug']
    categoryy=1
    date=p['date']
    imageURL=p['_embedded']['wp:featuredmedia'][0]['source_url']
    header = {'Authorization': 'Bearer ' + token}
    post = {
    'title'    : title,
    'status'   : 'draft', 
    'content'  : content,
    'categories': categoryy,
    'date'   : date,
    'slug':slug,
    'featured media':3999,
    #  "featured_image":(), # IMPORTANT
    # '_knawatfibu_url': imageURL ,
    # 'featured_image_urls': imageURL ,
    # 'jetpack_featured_media_url': imageURL ,
    
    }  
    responce = requests.post(destination_url , headers=header, json=post)
    img_data = requests.get(imageURL).content
    

    uploadImageFilename = "661b943654f54bd4b2711264eb275e1b.jpg"
    curHeaders = {
    'Authorization': 'Bearer ' + token,
    "Content-Type": "image/jpeg",
    "Accept": "application/json",
    'Content-Disposition': "attachment; filename=%s" % uploadImageFilename,
    }

    resp = requests.post(
    "https://www.onlinecasinogames777.com/wp-json/wp/v2/media",
    headers=curHeaders,
    data=img_data,
    )
    newDict=resp.json()


    link = newDict.get('id')
    print(link)
    if count==1 :
      break
postid = str(json.loads(responce.content)['id'])
updatedpost = {'title'    : title,
    'status'   : 'draft', 
    'content'  : content,
    'categories': 48,
    'date'   : date,
    'slug':slug,"featured_media":int(postid)+1}
update = requests.post(url + '/posts/' + postid, headers=header, json=updatedpost)
print("postid = " ,postid)
link1=update.json().get('id')
print("link1id = ",link1)