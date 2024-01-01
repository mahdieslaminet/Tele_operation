import cv2
import serial
import time
import random
arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)
cap = cv2.VideoCapture(0)
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=2)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if len(hands) == 1:
        finger1 = detector.fingersUp(hands[0])
        c = str(finger1[0]) + "," + str(finger1[1]) + "," + str(finger1[2]) + "," + str(finger1[3]) + "," + str(finger1[4])
        #print(write_read(c))
        write_read(c)
    cv2.imshow("image", img)
    cv2.waitKey(1)
