import cv2
import datetime


# cap = cv2.VideoCapture("F:\\Computer Vision\\Images\\output.avi")
cap = cv2.VideoCapture(0)

print("Width === ", cap.get(3))
print("Height === ", cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        text = ' Height : ' + str(cap.get(4)) + ' Width : ' + str(cap.get(3))
        frame = cv2.putText(frame, text, (10,30), font,1,(100,155,255), 1, cv2.LINE_AA)
        date_data = "Date: " + str(datetime.datetime.now())
        frame = cv2.putText(frame, date_data, (20,70), font,1,(100,155,255), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(30) == ord('r'):
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()

