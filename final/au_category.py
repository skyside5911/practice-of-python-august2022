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
source_urll = "https://theleafdesk.com/wp-json/wp/v2/categories"
source_url = "https://theleafdesk.com/wp-json/wp/v2/posts?_embed"
destination_url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/posts/"
url ="https://www.onlinecasinogames777.com/wp-json/wp/v2"
user_url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/users"
category_urll ="https://www.onlinecasinogames777.com/wp-json/wp/v2/categories/"
data = requests.get(source_url).json()
count=0
for p in data:
    count+=1
    title=p['title']['rendered']
    content=p['content']['rendered']
    slug=p['slug']
    
    date=p['date']
    imageURL=p['_embedded']['wp:featuredmedia'][0]['source_url']
    header = {'Authorization': 'Bearer ' + token}
    post = {
    'title'    : title,
    'status'   : 'draft', 
    'content'  : content,
    'date'   : date,
    'slug':slug,
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
    if count==2 :
      break
category_list=[]
c=0
for p in data:
    c+=1
    categoryy=p['categories']
    category_list.append(categoryy) 
    if c==1:
      break
    

dataa = requests.get(source_urll).json()
list_of_id=[]

for q in dataa:
    
    id=q['id']
    name=q['name'] 
    slug=q['slug']
    categorii= {id:[name,slug]}
    list_of_id.append(categorii)
    
print(category_list)
print(list_of_id)

for i in category_list:
    b=i[0]
    compare=[]
    compare.append(b)
    for c in compare:
        for e in list_of_id:
            if c in e.keys():
                value=e.values()
                
                for f in value:
                    
                    namee=f[0]
                    slugg=f[1]
                    print(namee)
                    print(slugg)
                    
                    poost={ 'name':namee,
                    'slug':slugg
                    }
                    header = {'Authorization': 'Bearer ' + token}
                    re = requests.post(category_urll , headers=header, json=poost)
                    print(re)
postid_category = str(json.loads(re.content)['id'])
print(postid_category)
post_author = {
    
    'username':'aman',
    'email':'raj@gmail.com',
    'password':'aman_@sunda',
    }  
resp_author = requests.post(user_url , headers=header, json=post_author)
id_author=str(json.loads(resp_author.content)['id'])
print(id_author)                   
postid = str(json.loads(responce.content)['id'])
updatedpost = {'title'    : title,
    'status'   : 'draft', 
    'content'  : content,
    
    'date'   : date, "categories":int(postid_category),"author":int(id_author),
    'slug':slug,"featured_media":int(postid)+1}
update = requests.post(url + '/posts/' + postid, headers=header, json=updatedpost)
print("postid = " ,postid)
link1=update.json().get('id')
print("link1id = ",link1)