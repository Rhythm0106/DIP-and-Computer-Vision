import cv2
import numpy as np

def draw(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100,(125,0,255),5)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x,y),(x+100,y+200),(125,255,125),5)
        

cv2.namedWindow(winname = "res")

img = np.zeros([512, 512, 3], np.uint8)*255
cv2.setMouseCallback("res", draw)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) == ord('r'):
        break
    
cv2.destroyAllWindows()