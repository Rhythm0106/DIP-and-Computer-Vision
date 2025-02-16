import cv2
import numpy as np

img = cv2.imread("F:\\Computer Vision\\Images\\hand.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


blur = cv2.medianBlur(img1,9)
ret,thresh = cv2.threshold(blur, 240, 255, cv2.THRESH_BINARY_INV)



# find contour
cnts,heir = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


#Loop over the contours
for c in cnts:
    epsilon = 0.0001*cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, epsilon, True)
    
    hull = cv2.convexHull(data)
    
    cv2.drawContours(img, [c], -1, (50,50,150),2)
    cv2.drawContours(img, [hull], -1, (0,255,0),1)


# Convexity defect 

hull2 = cv2.convexHull(cnts[0],returnPoints=False) # Here we are not creating loop as there is only one contour 
# return points = false will also return the actual coordinates and this is needed when are calculating defects 

defect = cv2.convexityDefects(cnts[0],hull2)

for i in range(defect.shape[0]):
    s,e,f,d = defect[i,0] # all four paramters - start point , end point , farthest point and approximate distance to the farthest point
    print(s,e,f,d)
    start = tuple(c[s][0])
    end = tuple(c[e][0])
    far = tuple(c[f][0])
    #cv2.line(img,start,end,[255,0,0],2)
    cv2.circle(img,far,5,[0,0,255],-1) # far values are printed 




# Extreme Points

c_max = max(cnts, key = cv2.contourArea)

# We convert into tuple so that we can use coordinates easily 

extLeft = tuple(c_max[c_max[:, :, 0].argmin()][0])
extRight = tuple(c_max[c_max[:, :, 0].argmax()][0])
extTop = tuple(c_max[c_max[:, :, 1].argmin()][0])
extBot = tuple(c_max[c_max[:, :, 1].argmax()][0])


cv2.circle(img, extLeft, 8, (255, 0, 255), -1)  #pink
cv2.circle(img, extRight, 8, (0, 125, 255), -1) #brown
cv2.circle(img, extTop, 8, (255, 10, 0), -1)  #blue
cv2.circle(img, extBot, 8, (19, 152, 152), -1) #green



cv2.imshow("threshold",thresh)
cv2.imshow("image ", img)
cv2.imshow("image1 ", img1)




cv2.waitKey(0)
cv2.destroyAllWindows()
