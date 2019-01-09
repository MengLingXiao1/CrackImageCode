import tesserocr
from PIL import Image

image = Image.open('code4.png')
result = tesserocr.image_to_text(image)
print(result)
