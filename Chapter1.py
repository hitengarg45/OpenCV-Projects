import cv2
print("Package Imported")

#Reading Image
#img = cv2.imread("Resources/ColoredImage.png")
#cv2.imshow("Our Output", img)
#cv2.waitKey(0)

#Reading Video
# cap = cv2.VideoCapture("Resources/TestVideo.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Our Video", img)
#     if cv2.waitKey(1) == 27:
#         break

#Reading Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Our Video", img)
    if cv2.waitKey(1) == 27:
        break

