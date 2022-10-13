from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture05.jpg")
img.show()
img=img.rotate(45,expand=True)
img.show()
