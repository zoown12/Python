from PIL import Image, ImageFilter, ImageEnhance,ImageOps
img=Image.open("C:\photo/picture01.jpg")
img.show() #이미지 보이기
img2=img.resize((500,500)) #이미지 RESIZE 설정 
img2.save("C:\photo/output01.jpg") #이미지 다시저장 
