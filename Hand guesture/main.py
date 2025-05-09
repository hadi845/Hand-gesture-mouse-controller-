import cv2
import mediapipe as mp
import pyautogui


cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = (1920/frame_width)*x
                    index_y = (1080/frame_height)*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = (1920/frame_width)*x
                    thumb_y = (1080/frame_height)*y
                    print('Outside ', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 25:
                        print('click')
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse',frame)
    cv2.waitKey(1)
