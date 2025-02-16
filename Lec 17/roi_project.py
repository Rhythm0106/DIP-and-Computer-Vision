import cv2 

img1 = cv2.imread("F:\\Computer Vision\\Images\\tree.jpg")
img2 = cv2.imread("F:\\Computer Vision\\Images\\thor.jpg")

img1 = cv2.resize(img1, (1024,650))
img2 = cv2.resize(img2, (300,300)) #The dimension of the image should be less from which object is extracted than the dimensions of the image it is placed in 

img_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
r,c,ch = img2.shape

print(r,c,ch)

# Create an ROI --> where we need to place the image 
roi = img1[0:r,0:c]

_, mask = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY_INV)


mask_inv = cv2.bitwise_not(mask) # ---> not needed as background automatically turns white after masking 

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

res = cv2.add(img1_bg,img2_fg)

final = img1

final[0:r,0:c] = res

# cv2.imshow("tree", img1)
# cv2.imshow("thor", img2) 
#cv2.imshow("roi",roi)
cv2.imshow("thor_gray",img_gray)
cv2.imshow("mask",mask)
cv2.imshow("bitwise",img2_fg)
cv2.imshow("mask_inverse",mask_inv)
cv2.imshow("final1", img1_bg)
cv2.imshow("result",res)
cv2.imshow("Output",final)


cv2.waitKey(0)
cv2.destroyAllWindows()