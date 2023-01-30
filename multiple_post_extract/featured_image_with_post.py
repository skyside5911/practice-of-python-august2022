import requests
import json
import os
import base64
auth_url = "https://www.onlinecasinogames777.com/wp-json/jwt-auth/v1/token"
auth_data = {
    #   "username":"gh1YcBHVrq",
    # "password":"zd2eW0Aj6F"
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
    # featured_media=p['featured_media']
    idd=146
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
    if count==1 :
        break
    # toUploadImagePath = "C:\\Users\\Acer\\Downloads\\shutterstock.jpg"
    # mediaImageBytes = open(toUploadImagePath, 'rb').read()
    # image = requests.post(url + '/media', headers=header, files=mediaImageBytes,json=post)
    # imageURL=p['_embedded']['wp:featuredmedia'][0]['source_url']
postid = str(json.loads(responce.content)['id'])
updatedpost = {'title'    : title,
    'status'   : 'draft', 
    'content'  : content,
    'categories': categoryy,
    'date'   : date,
    'slug':slug,"featured_media":293}
update = requests.post(url + '/posts/' + postid, headers=header, json=updatedpost)

    

    
    # y=BeautifulSoup(content, "lxml").text
#token = base64.b64encode(credentials.encode())
#token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2NhbGhvc3Q6ODEiLCJpYXQiOjE2NDkzMjU5MjEsIm5iZiI6MTY0OTMyNTkyMSwiZXhwIjoxNjQ5OTMwNzIxLCJkYXRhIjp7InVzZXIiOnsiaWQiOjEsImRldmljZSI6IiIsInBhc3MiOiI3YWQ3MjcwODkzNDgyNmVhMmVhZTI1YjQ2NjA2N2I3NyJ9fX0.i_TkLtUBl-RAdDwuik3czhFL1mXaa1Da9wiWrH1AeQM"
