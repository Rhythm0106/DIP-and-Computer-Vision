import cv2
import numpy as np

frame = cv2.imread("F:\\Computer Vision\\Images\\color_balls.jpg")



while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    upper_value = np.array([48,255,248])
    lower_value = np.array([20,143,139])
    
    mask = cv2.inRange(hsv, lower_value, upper_value)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    
        
    cv2.imshow("balls", frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)
    
    if cv2.waitKey(1) == ord('r'):
        break
    
cv2.destroyAllWindows()

