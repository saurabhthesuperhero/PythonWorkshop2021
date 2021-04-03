from PIL import Image,ImageFilter
file=Image.open("b.jpg")
#file.show()

#Image Rotation
#print(type(file))
#file=file.rotate(90)
#file.save("RotatedImage.jpg")
# blur

#file=file.filter(ImageFilter.BLUR)
#file.save("blurredImage.jpg")
#Crop
print(file.size)
file=file.crop((1,1,150,150))
file.show()
