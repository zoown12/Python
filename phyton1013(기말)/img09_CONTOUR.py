from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture83.jpg")
img.show()
img=img.filter(ImageFilter.CONTOUR)
img.show()
