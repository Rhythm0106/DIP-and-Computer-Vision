import cv2

cap = cv2.VideoCapture(0)
print(cap)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame,0)
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)
        output.write(frame)
        output.write(gray)
        k = cv2.waitKey(25)
        if k == ord("r"):
            break
    

cap.release()
output.release()
cv2.destroyAllWindows()
    