from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture24.jpg")
img.show()
img=img.filter(ImageFilter.FIND_EDGES)
img.show()
