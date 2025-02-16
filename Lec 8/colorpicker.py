import cv2
import numpy as np

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Color Picker")

def default(x):
    pass

s1 = "0:OFF\n1:ON"

cv2.createTrackbar(s1, "Color Picker",0, 1, default)

# For RGB

cv2.createTrackbar("R", "Color Picker", 0, 255, default)
cv2.createTrackbar("G", "Color Picker", 0, 255, default)
cv2.createTrackbar("B", "Color Picker", 0, 255, default)


while True:
    cv2.imshow("Color Picker", img)
    if cv2.waitKey(1) == ord('r'):
        break
    
    s = cv2.getTrackbarPos(s1, "Color Picker")
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]
        
cv2.destroyAllWindows()