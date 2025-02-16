import cv2
import numpy as np
'''
img = cv2.imread("F:\\Computer Vision\\Images\\tree.jpg")

print("The rows,columns and channels of image are:", img.shape)
print("The number of pixels are:",img.size)
print("The datatype of the array in image is:", img.dtype)
print("The Imagetype is:", type(img))

# print(cv2.split(img))
b,g,r = cv2.split(img)


cv2.imshow("blue",b)
cv2.imshow("green",g)     Spliting of images into channels
cv2.imshow("red",r)

# Now merging the Channels 
mr1 = cv2.merge((r,g,b)) # Passed r,g,b instead of b,g,r so orignal image will not come
cv2.imshow("merge", mr1)
cv2.imshow("nature", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Accessing a pixel value from given row,column values

img = cv2.imread("F:\\Computer Vision\\Images\\tree.jpg")

print("The rows,columns and channels of image are:", img.shape)
print("The number of pixels are:",img.size)
print("The datatype of the array in image is:", img.dtype)
print("The Imagetype is:", type(img))


px = img[520,580]
print("The pixel of the coordinates are: ",px)

# Accessing the value of pixels of individual channels

blue = img[520,580,0]
print("pixel of blue channel", blue)

# Similarly for green - 1  and  for red - 2

cv2.waitKey(0)
cv2.destroyAllWindows()


















