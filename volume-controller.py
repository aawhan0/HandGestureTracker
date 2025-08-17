import cv2
import mediapipe as mp
import pyautogui

webcam = cv2.VideoCapture(0)
while True:
    ret, image = webcam.read()
    if not ret:
        print("Failed to grab the frame")
        break

    cv2.imshow("Hand Volume Control using Python", image)

    key= cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
# Lets see if this works now or not...