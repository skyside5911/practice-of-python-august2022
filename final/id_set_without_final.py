import requests
import json
import time
auth_url = "https://www.onlinecasinogames777.com/wp-json/jwt-auth/v1/token"
auth_data = {
      "username":"admin",
    "password":"pwd12345"
}
auth_responce = requests.post(auth_url , json=auth_data)
token = auth_responce.json().get('data').get('token')
print(auth_responce.json().get('data').get('token'))
source_url = "https://theleafdesk.com/wp-json/wp/v2/posts?_embed"
source_urll = "https://theleafdesk.com/wp-json/wp/v2/categories"
destination_url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/posts/"
url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/categories/"
urll ="https://www.onlinecasinogames777.com/wp-json/wp/v2"
count=0
data = requests.get(source_url).json()
category_list=[]
for p in data:
    count+=1
    categoryy=p['categories']
    category_list.append(categoryy) 
    if count==1:
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
                    print(namee)
                    print(slugg)
                    
                    post={ 'name':namee,
                    'slug':slugg
                    }
                    header = {'Authorization': 'Bearer ' + token}
                    responce = requests.post(url , headers=header, json=post)
                    postid = str(json.loads(responce.content)['id'])
                    print(postid)
                    print(responce)
                    
                    
