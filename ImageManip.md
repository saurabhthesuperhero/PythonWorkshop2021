## Image Manipulation

#### Installing Pillow using pip

To install pillow using pip, just run the below command in your command prompt :

```python
python -m pip install pip
python -m pip install pillow
```

#### Image Rotation

```python
from PIL import Image
#Open image using Image module
im = Image.open("images/cuba.jpg")
#Show actual Image
im.show()
#Show rotated Image
im = im.rotate(45)
im.show()
```

#### Attributes of Image Module

```python
>>>image = Image.open('beach1.jpg')
>>> image.filename
>>> image.format
>>> image.mode
>>> image.size
>>> image.width
>>> image.height
```

#### Reading an Image

```python
# Image.open(fp, mode=’r’) #opening way
from PIL import Image
image = Image.open('beach1.jpg')
image.show()

##  Saving an Image

image.save('beach1.bmp') #storing in diff format
image1 = Image.open('beach1.bmp')
image1.show()
```

#### Python Pillow - Blur an Image

```python
#Open existing image
image = Image.open('images/boy.jpg')
image.show()

#Simple Blur
blurImage = OriImage.filter(ImageFilter.BLUR)
# Gaussian Blur
gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))

blurImage.show()
#Save blurImage
blurImage.save('images/simBlurImage.jpg')
```

#### Python Pillow - Cropping an Image

```python
#left, upper, right, lowe
#Crop
cropped = im.crop((1,2,300,300))

#Display the cropped portion
cropped.show()

#Save the cropped image
cropped.save('images/croppedBeach1.jpg')
```

#### Python Pillow - Flip and Rotate Images

- **Image.FLIP_LEFT_RIGHT** − For flipping the image horizontally
- **Image.FLIP_TOP_BOTTOM** − For flipping the image vertically
- **Image.ROTATE_90** − For rotating the image by specifying degree

#### Python Pillow - Adding Filters to an Image

```python
from PIL import Image, ImageFilter

im = Image.open('jungleSaf2.jpg')

im1 = im.filter(ImageFilter.BLUR)
im1.show()

im2 = im.filter(ImageFilter.MinFilter(3))
im2.show()

im3 = im.filter(ImageFilter.MinFilter) # same as MinFilter(3)
im3.show()
```

##### 	Filters:

- BLUR
- CONTOUR
- DETAIL
- EDGE_ENHANCE
- EDGE_ENHANCE_MORE
- EMBOSS
- FIND_EDGES
- SHARPEN
- SMOOTH
- SMOOTH_MORE

#### Gray Image

from PIL import Image,ImageEnhance
import os
#make grayscale/-b/w for all files at one click

# print(os.listdir()) 
```python
for i in os.listdir('.'):# print(i)
	try:
		im2=Image.open(i).convert('RGB')
		im3=im2.convert('L')
		im3.save('gray/'+i)
		print(i)
	except:
		pass
```

