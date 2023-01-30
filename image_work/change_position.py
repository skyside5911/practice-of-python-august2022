from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont, ImageOps

im=Image.open(r"H:\practice of python august2022\audacious.jpg")

f = ImageFont.load_default()
txt=Image.new('L', (500,50))

d = ImageDraw.Draw(txt)
d.text( (0, 0), "Someplace Near Boulder",  font=f, fill=255)
w=txt.rotate(17.5,  expand=50)

im.paste( ImageOps.colorize(w, (0,0,0), (255,255,84)), (242,260),  w)
im.show()