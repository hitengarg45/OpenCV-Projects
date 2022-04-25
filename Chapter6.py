import cv2
import  numpy as np

img = cv2.imread("Resources/rose.png")

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("Vertical Image", imgVer)
cv2.imshow("Horizontal Image", imgHor)
cv2.imshow("Image", img)

cv2.waitKey(0)