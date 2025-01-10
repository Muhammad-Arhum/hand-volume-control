import math
from ctypes import POINTER, cast

import cv2
import mediapipe as mp
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

img = cv2.VideoCapture(0)
flag = True
print("Press Escape Key to Quit")

MIN_DIST = float('inf')
MAX_DIST = float('-inf')
ABS_VALUE = 0
while(flag):
    _, image = img.read()
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            THUMB_TIP = hand_landmarks.landmark[4]
            INDEX_TIP = hand_landmarks.landmark[8]

            h,w,_ = image.shape

            THUMB_TIP_X, THUMB_TIP_Y = int(THUMB_TIP.x * w), int(THUMB_TIP.y * h)
            INDEX_TIP_X, INDEX_TIP_Y = int(INDEX_TIP.x * w), int(INDEX_TIP.y * h)
            
            X_DIST = math.pow(THUMB_TIP_X - INDEX_TIP_X, 2)
            Y_DIST = math.pow(THUMB_TIP_Y - INDEX_TIP_Y, 2)
            DISTANCE = int(math.sqrt(X_DIST + Y_DIST))

            MIN_DIST = min(MIN_DIST, DISTANCE)
            MAX_DIST = max(MAX_DIST, DISTANCE)
            if(MIN_DIST != MAX_DIST):
                ABS_VALUE = int((((DISTANCE - MIN_DIST)/(MAX_DIST - MIN_DIST)) * 100))

            volume_level = ABS_VALUE / 100
            volume.SetMasterVolumeLevelScalar(volume_level, None)
            
            print(f"MAX DISTANCE: {MAX_DIST}, MIN DISTANCE: {MIN_DIST}, CURRENT DISTANCE: {DISTANCE}, VOLUME: {ABS_VALUE}", end='\n')

            for idx, landmark in enumerate(hand_landmarks.landmark):
                h, w, _ = image.shape
                x, y = int(landmark.x * w), int(landmark.y * h)

                cv2.putText(image, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    text_x = 15
    text_y = 15
    cv2.putText(image, f"volume level: {ABS_VALUE}", (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0))
    cv2.imshow("Hand Landmarks with Numbers", image)


    key = cv2.waitKey(10)
    if key == 27:
        break

img.release()
cv2.destroyAllWindows()
