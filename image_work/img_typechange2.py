

# Importing Image module from PIL package
from PIL import Image
import io
# creating a image object
img = Image.open("H:\\practice of python august2022\\audacious.jpg")
print(type(img))
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='JPEG')
img_byte_arr = img_byte_arr.getvalue()
print(type(img_byte_arr))
