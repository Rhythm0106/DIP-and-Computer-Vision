import cv2

# Open the video file
vidcap = cv2.VideoCapture("F:\\Computer Vision\\Images\\test2.mp4")
ret, image = vidcap.read()
count = 0
frame_interval = 100  # Interval in milliseconds

while ret:
    # Save the current frame as an image
    cv2.imwrite(f"F:\\Computer Vision\\frames\\img{count}.jpg", image)
    
    # Move to the next frame at the specified interval
    vidcap.set(cv2.CAP_PROP_POS_MSEC, count * frame_interval)
    ret, image = vidcap.read()
    
    # Display the current frame
    if ret:
        cv2.imshow("Frame", image)
    
    count += 1
    # Break the loop if 'r' is pressed
    if cv2.waitKey(1) == ord("r"):
        break

# Release resources
vidcap.release()
cv2.destroyAllWindows()
