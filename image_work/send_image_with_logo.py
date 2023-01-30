import requests
import json
import io
import PIL
import imageio.v2 as iio
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont,ImageOps
from io import BytesIO
import urllib.request
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
count=0
def pillow_image_to_base64_string(img):
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")
for page in range(1,40):
    source_urll = "https://theleafdesk.com/wp-json/wp/v2/categories"
    source_url = "https://theleafdesk.com/wp-json/wp/v2/posts?_embed&&page={a}".format(a=page)
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
        se = requests. get(imageURL)
        im = Image. open(BytesIO(se. content))
        myFont = ImageFont.truetype('arial.ttf', size=30)
        f = ImageFont.load_default()
        txt=Image.new('L', (500,500))
        d = ImageDraw.Draw(txt)
        d.text( (0, 0), "onlinecasinogames777",  font=myFont, fill=255)
        w=txt.rotate(0,  expand=50)
        im.paste( ImageOps.colorize(w, (0,0,0), (255,255,84)), (100,560),  w)
        Image2 = Image.open('H:\practice of python august2022\gfg1.png')
        im2=(Image2).resize((200,100),Image.Resampling.LANCZOS).copy()
        im.paste(im2, (0, 0))
        img_byte_arr = io.BytesIO()
        im.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        # rgb_im = im.convert('RGB')
        # data_url = 'data:image/jpeg;base64,' + pillow_image_to_base64_string(rgb_im)
        # print(type(data_url))
        # img_data = requests.get(data_url).content
        # aaa = str("https://theleafdesk.com/wp-content/uploads/2022/09/shutter_"+str(count)+'.jpg')
        # aaa=str(im).save("https://theleafdesk.com/wp-content/uploads/2022/09/shutter_"+str(count)+'.jpg')
        
        
        

        uploadImageFilename = "{}.jpg".format(title)
        curHeaders = {
        'Authorization': 'Bearer ' + token,
        "Content-Type": "image/jpeg",
        "Accept": "application/json",
        'Content-Disposition': "attachment; filename=%s" % uploadImageFilename,
        }

        resp = requests.post(
        "https://www.onlinecasinogames777.com/wp-json/wp/v2/media",
        headers=curHeaders,
        data=img_byte_arr,
        )
        newDict=resp.json()
        categoryy=p['categories'][0]
        
        # link = newDict.get('id')
        # category_list=[]
        # c=0
        # for p in data:
            
        #     categoryy=p['categories']
        #     category_list.append(categoryy) 
            # if c==1:
            #   break
            

        dataa = requests.get(source_urll).json()
        list_of_id=[]

        # for q in dataa:
            
        #     id=q['id']
        #     name=q['name']
        #     slug=q['slug']
        #     categorii= {id:[name,slug]}
        #     list_of_id.append(categorii)
            
        # print(category_list)
        # print(list_of_id)
    

        # for i in category_list:
        #         b=i[0]
        #         compare=[]
        #         compare.append(b)
        #         print(compare)
        #         for c in compare:
        # for e in list_of_id:
        #     if categoryy in e.keys():
        #         # print(c)
        #         value=e.values()
                # print(value)
        id_name_id = [{6: ['CBD &amp; Hemp', 119]}, {4: ['Industry',118]}, 
                            {3: ['Lifestyle', 117]}, {2: ['Medical', 116]}, 
                            {13: ['News', 120]}, {5: ['Regulation', 115]}, 
                            {1: ['Uncategorised', 1]}]
        for i in id_name_id:
                    if categoryy in i.keys():
                        for ee in (i.values()):
                            print(ee)
        final_category=(ee[1])
        print(final_category)
                        # name_list=[]
                        # for f in value:
                            
                        #     namee=f[0]
                        #     slugg=f[1]
                        #     name_list.append(namee)
                        #     print(namee)
                        #     print(slugg)
                        #     print(name_list)
                            
                            # poost={ 'name':namee,
                            # 'slug':slugg
                            # }
                            
        header = {'Authorization': 'Bearer ' + token}
                            # id_name=[
                            #      {'Uncategorised':1},
                            #             {'CBD & Hemp':119},
                            #             {'Industry':118},
                            #             {"Lifestyle":117},
                            #             {'Medical':116},
                            #             {'Regulation':115}
                            
                            # for na in name_list:
                            #  print(na)
                            #  for ie in id_name:                
                            #   if na in ie.keys():
                                
                            #       valuee=ie.values()
                            #       for val in valuee:
                            #           print(val)
                            #           print(val)
                                
                                
                                # id_of_category=ie.values()
                                # print(id_of_category)
                                # print('done')
                            # re = requests.post(category_urll , headers=header, json=poost)
                            # if poost in re:
                            #     continue
                            # print(str(json.loads(re.content)))
                            
                            # postid_category = str(json.loads(re.content)['id'])
                            # print(postid_category)
                            # post_author = {
                                
                            #     'username':'aman'+str(count),
                            #     'email':'raj@gmail.com'+str(count),
                            #     'password':'aman_@'+str(count),
                            #     }  
                            # resp_author = requests.post(user_url , headers=header, json=post_author)
                            # id_author=str(json.loads(resp_author.content)['id'])
                            # print(id_author)                   
        postid = str(json.loads(responce.content)['id'])
        updatedpost = {'title'    : title,
            'status'   : 'draft', 
            'content'  : content,
            
            'date'   : date, "categories":int(final_category),"author":int(12),
            'slug':slug,"featured_media":int(postid)+1}
        update = requests.post(url + '/posts/' + postid, headers=header, json=updatedpost)
        print("postid = " ,postid)
        link1=update.json().get('id')
        print("link1id = ",link1)
        if count==2:
            break