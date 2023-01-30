import requests
import json
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


toUploadImagePath = "C:\\Users\\Acer\\Downloads\\shutterstock2.jpg"
mediaImageBytes = open(toUploadImagePath, 'rb').read()
# b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\.....'

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
  data=mediaImageBytes,
)
newDict=resp.json()

newID= newDict.get('id')
print(newID)
link = newDict.get('guid').get("rendered")
print(link)