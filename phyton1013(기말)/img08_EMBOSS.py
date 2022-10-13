from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture73.jpg")
img.show()
img=img.filter(ImageFilter.EMBOSS)
img.show()
