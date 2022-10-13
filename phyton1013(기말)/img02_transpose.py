from PIL import Image,ImageFilter,ImageEnhance, ImageOps
img=Image.open("C:\photo/picture02.jpg")
img.show()
img=img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()
img=img.transpose(Image.FLIP_TOP_BOTTOM)
img.show()
