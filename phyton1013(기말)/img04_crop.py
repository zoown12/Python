from PIL import Image,ImageFilter,ImageEnhance,ImageOps
img=Image.open("C:\photo/picture52.jpg")
img.show()
img=img.crop((100,100,600,600))
img.show()
