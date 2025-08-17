import cv2
import mediapipe as mp
import pyautogui

webcam = cv2.VideoCapture(0)
myHands = mp.solutions.hands.Hands()
drawingUtils= mp.solutions.drawing_utils
while True:
    ret, image = webcam.read()
    if not ret:
        print("Failed to grab the frame")
        break

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = myHands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawingUtils.draw_landmarks(image,hand)
    cv2.imshow("Hand Volume Control using Python", image)
    key= cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
