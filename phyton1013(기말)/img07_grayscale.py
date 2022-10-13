from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture55.jpg")
img.show()
img=ImageOps.grayscale(img)
img.show()
