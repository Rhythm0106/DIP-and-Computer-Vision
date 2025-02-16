import cv2

path = input("What is your file path: ")
print(path)

img1 = cv2.imread(path,0)
img1 = cv2.resize(img1,(560,700))
cv2.imshow("Converted image to gray ",img1)



k = cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("G:\\firstprojectoutput.png",img1)
else:
    cv2.destroyAllWindows()