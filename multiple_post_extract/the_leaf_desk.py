import requests
import json
import base64
auth_url = "https://onlinecasinogames777.com/wp-json/jwt-auth/v1/token"
auth_data = {
      "username":"admin",
    "password":"MlT6qUtAXfb6FdI8tG31TlW0"
}
auth_responce = requests.post(auth_url , json=auth_data)
token = auth_responce.json().get('data').get('token')
print(auth_responce.json().get('data').get('token'))
url = "https://onlinecasinogames777.com/wp-json/wp/v2/posts"
user = "rishi"
password = "271191.rishi"
credentials = user + ':' + password
#token = base64.b64encode(credentials.encode())
#token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2NhbGhvc3Q6ODEiLCJpYXQiOjE2NDkzMjU5MjEsIm5iZiI6MTY0OTMyNTkyMSwiZXhwIjoxNjQ5OTMwNzIxLCJkYXRhIjp7InVzZXIiOnsiaWQiOjEsImRldmljZSI6IiIsInBhc3MiOiI3YWQ3MjcwODkzNDgyNmVhMmVhZTI1YjQ2NjA2N2I3NyJ9fX0.i_TkLtUBl-RAdDwuik3czhFL1mXaa1Da9wiWrH1AeQM"
header = {'Authorization': 'Bearer ' + token}
post = {
 'title'    : 'Hello World',
 'status'   : 'publish', 
 'content'  : 'This is my first post created using rest API',
 'categories': 5,
 'date'   : '2022-01-05T10:00:00'
}
responce = requests.post(url , headers=header, json=post)
print(responce)