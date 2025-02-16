import cv2 
import  numpy as np

img1 = cv2.imread("F:\\Computer Vision\\Images\\tree.jpg")
img1 = cv2.resize(img1,(700,700))
img2 = cv2.imread("F:\\Computer Vision\\Images\\thor.jpg")
img2 = cv2.resize(img2,(700,700))


#v2.imshow("tree", img1)
#v2.imshow("thor",img2)


def nothing(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('win')
cv2.createTrackbar('trackbar', 'win', 1, 100, nothing)

switch = '0: OFF \n 1: ON'
cv2.createTrackbar(switch, 'win', 0, 1, nothing)


while True:
    s = cv2.getTrackbarPos(switch, "win")
    a = cv2.getTrackbarPos("trackbar","win")
    n = float(a/100)
    print(n)
    
    if s==0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
    
    cv2.imshow("dst",dst)
    if cv2.waitKey(1) == ord('q'):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
