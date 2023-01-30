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
source_url = "https://theleafdesk.com/wp-json/wp/v2/posts?_embed"
source_urll = "https://theleafdesk.com/wp-json/wp/v2/categories"
destination_url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/posts/"
url ="https://www.onlinecasinogames777.com/wp-json/wp/v2"
count=0
data = requests.get(source_url).json()
category_list=[]
for p in data:
    count+=1
    categoryy=p['categories']
    category_list.append(categoryy) 
    if count==5:
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
                # print(type(e.values()))
        # if j in list_of_id:
        #     print(q['name'],q['slug'])
            
        # else:
        #     print('no')
        # if j == q['id']:
        #     print(q['name'],q['slug'])
        # if b in list_of_id:
            
        #   name=dataa['name']
        #   slug=dataa['slug']
        
# match_id = []   
# for i in list_of_id:
#     if i in category_list:
#         match_id.append(i)
#         print(i)
        
# sub_listof_caegory = [] 


       
# for b in category_list:
#     if len(b) == 1:
#         print(f' this is single index value ={b}')  
        
#     else:
#           for j in b:
#               sub_listof_caegory.append(j)
              
          
             
# print(sub_listof_caegory)
# ggh = match_id[0]

# for z in sub_listof_caegory:
#     print(z)
#     if z in ggh:
#         for zz in sub_listof_caegory:
#             ggg = dataa[zz]
#             Name = ggg['name']
#             slug = ggg['slug']
#             print(Name) 
#             print(slug)
            
    

# hh = match_id[0]

# tt = hh[0]
# ggg = dataa[tt]

# Name = ggg['name']

# slug = ggg['slug'] 

# print(Name)
# print(slug)  

    
# for qq in data:
    
#     id=qq['categories']
#     print(id)
#     if id in list_of_id:
#         id=qq['id']
#         name=qq['name']
#         slug=qq['slug']
#         print(id)
#     else:
#         print("no id found")    