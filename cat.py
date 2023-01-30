import requests
import json
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
count=0
data = requests.get(source_url).json()
category_list=[]
for p in data:
    count+=1
    title=p['title']['rendered']
    content=p['content']['rendered']
    slug=p['slug']
    categoryy=p['categories']
    category_list.append(categoryy)
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
dataa = requests.get(source_urll).json()
list_of_id=[]
c=0
for q in dataa:
    c+=1
    id=q['id']
    name=q['name']
    slug=q['slug']
    categorii= {id:[name,slug]}
    list_of_id.append(categorii)
print(category_list)
print(list_of_id)
for i in category_list:
    for j in i:
        for e in list_of_id:
            if j in e.keys():
                value=e.values()
                for f in value:
                    namee=f[0]
                    slugg=f[1]
                    posttt= { 'name':name, 'slug':slug
                      
                    }
respp = requests.post(url+'categories/' , headers=header, json=posttt)                  
category_id=str(json.loads(respp.content)['id'])
postid = str(json.loads(responce.content)['id'])
updatedpost = {'title'    : title,
    'status'   : 'draft', 
    'content'  : content,
    'categories': categoryy,
    'date'   : date,
    'slug':slug,"featured_media":int(postid)+1,'cat_id':category_id}
update = requests.post(url + '/posts/' + postid, headers=header, json=updatedpost)
print("postid = " ,postid)
link1=update.json().get('id')
print("link1id = ",link1)