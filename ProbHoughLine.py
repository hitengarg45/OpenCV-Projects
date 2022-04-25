import cv2
import numpy as np
from StackImages import stackImages

###################################################
widthImg = 640
heightImg = 480
###################################################

cap = cv2.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10, 150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, 50, 150, apertureSize=3)
    cv2.imshow("Image Canny", imgCanny)
    return imgCanny

while True:
    success, img = cap.read()
    imgCanny = preProcessing(img)
    kernel = np.ones((5, 5))
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDilation, kernel, iterations=1)
    lines = cv2.HoughLinesP(imgThres, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(imgThres, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    cv2.imshow("Result", img)
    
    if cv2.waitKey(1) == 27:
        break


#img = cv2.imread("Resources/Sudoku1.jpg")
#img = cv2.resize(img, (widthImg, heightImg))