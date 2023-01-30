# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont,ImageOps
import requests
import base64
import io
from io import BytesIO
def pillow_image_to_base64_string(img):
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Open an Image

im = Image.open('H:\practice of python august2022\Dark Blue Sea Photo Nature and Travel Personal Canva Banner - Edited.png')

# I1 = ImageDraw.Draw(Image1)

# Custom font style and font size
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
print(type(im))
img_byte_arr = io.BytesIO()
im.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()
print(img_byte_arr)
print(type(img_byte_arr))
# rgb_im = bytes(im.convert('RGB'))
# print(type(rgb_im))
# data_url = bytes('data:image/jpeg;base64,' + pillow_image_to_base64_string(rgb_im))
# img_data = requests.get(img_byte_arr).content
# print(img_data)
# aaa=data_url.save("https://theleafdesk.com/wp-content/uploads/2022/09/shutter_"+'.jpg')
# print(data_url)
# print(type(data_url))
# rgb_im = im.convert('RGB')
# print(type(rgb_im))
# img_data = requests.get(str(rgb_im)).content
# print(type(img_data))
# rgb_im.save('audacious.jpg')
# print(type(rgb_im))
# buffered = BytesIO(bytes(rgb_im))
# im.save(buffered, format="JPEG")
# img_str = base64.b64encode(buffered.getvalue())
# print(type(img_str))
# (print(img_str))

