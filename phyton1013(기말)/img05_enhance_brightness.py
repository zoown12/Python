from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture06.jpg")
img.show()
img=ImageEnhance.Brightness(img).enhance(3.0)
img.show()
