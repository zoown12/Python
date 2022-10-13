from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture07.jpg")
img.show()
img=ImageEnhance.Brightness(img).enhance(0.4)
img.show()
