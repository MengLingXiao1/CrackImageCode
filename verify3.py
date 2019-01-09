import tesserocr
from PIL import Image

img = Image.open('code.jpg')
print (img.format, img.size, img.mode)
img = img.convert('L')
table=[]
print (img)
print (img.format, img.size, img.mode)
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        table.append(img.getpixel((i, j)))
        print (img.getpixel((i, j)))

