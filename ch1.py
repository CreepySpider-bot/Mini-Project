import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print("Package imported")

img =  cv2.imread("Data\A\Image_1678373626.619295.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(img,(7,7),0)

imgCanny = cv2.Canny(img,100,100)
imgDialate = cv2.dilate(img,kernel,iterations=1)
imgErode = cv2.erode(img,kernel)

# cv2.imshow("Gray",imgGray)
cv2.imshow("img",img)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
# cv2.imshow("Dilated img",imgDialate)
cv2.imshow("Eroded img",imgErode)
cv2.waitKey(0)