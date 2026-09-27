from PIL import Image
from term_image.image import AutoImage

img = Image.open("try.png")
image = AutoImage(img)
image.draw()