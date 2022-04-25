import  cv2
import numpy as np

img = cv2.imread("Resources/Card2.jpg")

width, height = 250, 350

#Coordinates of the object in src image
pts1 = np.float32([[419, 110], [542, 153], [368, 303], [491, 347]])
#Coordinates of the object in dst image
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Warp Image", imgOutput)
cv2.imwrite("Resources/Card3.jpg", imgOutput)

cv2.waitKey(0)