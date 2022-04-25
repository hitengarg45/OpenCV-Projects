import cv2
import numpy as np

# img = cv2.imread("Resources/rose.png")
# kernel = np.ones((5, 5), np.uint8)
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv2.Canny(img, 100, 100)
# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgErode = cv2.erode(imgDilation, kernel, iterations=1)
#
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Edged Image", imgCanny)
# cv2.imshow("Dilated Image", imgDilation)
# cv2.imshow("Eroded Image", imgErode)
#
# cv2.waitKey(0)

#Image Capture on WebCam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

kernel = np.ones((5, 5), np.uint8)

while True:
    success, img = cap.read()
    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cannyFrame = cv2.Canny(grayFrame, 50, 50)
    dilatedFrame = cv2.dilate(cannyFrame, kernel, iterations=1)
    erodeFrame = cv2.erode(dilatedFrame, kernel, iterations=1)

    cv2.imshow("WebCam", img)
    cv2.imshow("GrayWebcam", grayFrame)
    cv2.imshow("Canny Frame", cannyFrame)
    cv2.imshow("Dilated Frame", dilatedFrame)
    cv2.imshow("Eroded Frame", erodeFrame)

    if cv2.waitKey(1) == 27:
        break
