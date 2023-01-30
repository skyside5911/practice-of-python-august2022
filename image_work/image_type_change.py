import base64
import io
import requests
from PIL import Image


def pillow_image_to_base64_string(img):
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def base64_string_to_pillow_image(base64_str):
    return Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))


# Example for Converting pillow image to base64 data URL to view in browser
my_img = Image.open(r'H:\practice of python august2022\audacious.jpg')
data_url = 'data:image/jpeg;base64,' + pillow_image_to_base64_string(my_img)
img_data = requests.get(data_url).content
print(type(img_data))
# You can put this data URL in the address bar of your browser to view the image