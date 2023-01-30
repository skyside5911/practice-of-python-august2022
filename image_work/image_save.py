# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
# Open an Image

Image1 = Image.open('H:\practice of python august2022\Dark Blue Sea Photo Nature and Travel Personal Canva Banner - Edited.png')

I1 = ImageDraw.Draw(Image1)

# Custom font style and font size
myFont = ImageFont.truetype('arial.ttf', size=30)

# Add Text to an image
I1.text((50, 50), "onlinecasinogames777", font=myFont, fill =(255, 0, 0))
im=Image1.copy()
Image2 = Image.open('H:\practice of python august2022\gfg1.png')
im2=Image2.copy()
a=(im.paste(im2, (0, 0)))
print(type(im))
a.show()
ima = Image.open(a)
rgb_im = ima.convert("RGB")
rgb_im.show()

# # Call draw Method to add 2D graphics in an image
# I1 = ImageDraw.Draw(img)

# # Custom font style and font size
# myFont = ImageFont.truetype('arial.ttf', size=30)

# # Add Text to an image
# I1.text((50, 50), "onlinecasinogames777", font=myFont, fill =(255, 0, 0))
# # I1.Im((50, 50), "onlinecasinogames777", font=myFont, fill =(255, 0, 0))
# a=img.paste(Image1, (0, 0))

# a.show()

# # Save the edited image
# # img.save("car3.png")
