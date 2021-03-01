from PIL import Image,ImageChops
img1 = Image.open('C:\\Users\\lenovo\\Desktop\\11.jpg')
img2 = Image.open('C:\\Users\\lenovo\\Desktop\\22.jpg')
diff = ImageChops.difference(img1,img2)
if diff.getbbox():
   diff.show()

