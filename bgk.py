#make a program to calculate the number of fingers using mediapipe and opencv
import cv2 as cv
import numpy as np
import mediapipe as mp
import math
import random
import autopy

global player
global computer
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv.VideoCapture(1)

hands = mp_hands.Hands()

def rock():
    player = 1
    computer = random.randint(1,3)
    if computer == 1:
        autopy.alert.alert("The Computer chose rock, IT'S A TIE")
    elif computer == 2:
        autopy.alert.alert("The Computer chose paper, YOU LOSE HAHA LOSER!")
    else:
        autopy.alert.alert("The Computer chose scissors, YOU WIN")

def paper():
    player = 2
    computer = random.randint(1,3)
    if computer == 1:
        autopy.alert.alert("The Computer chose rock, YOU WIN")
    elif computer == 2:
        autopy.alert.alert("The Computer chose paper, IT'S A TIE")
    else:
        autopy.alert.alert("The Computer chose scissors, YOU LOSE HAHA LOSER!")

def scissors():    
    player = 3
    computer = random.randint(1,3)
    if computer == 1:
        autopy.alert.alert("The Computer chose rock, YOU LOSE HAHA LOSER!")
    elif computer == 2:
        autopy.alert.alert("The Computer chose paper, YOU WIN")
    else:
        autopy.alert.alert("The Computer chose scissors, IT'S A TIE")

def play():              
    # if cv.waitKey(1) & 0xFF == ord('a'): 
    player = 0
    computer = 0
    if finger == 0:
        rock()
    elif finger == 3:
        paper()
    elif finger == 2:
        scissors()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print ("ga bisa buka kamera woe")
        continue


    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    if results.multi_hand_landmarks :
        for hand_landmarks in results.multi_hand_landmarks:
            for id, landmark, in enumerate(hand_landmarks.landmark):
                x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])

                if id == 8:
                    x1 = x
                    y1 = y

                elif id == 12:
                    x2 = x
                    y2 = y

                elif id == 9:
                    x4 = x
                    y4 = y

                if id == 16:
                    x5 = x
                    y5 = y

            length1 = math.hypot(x1 - x4, y1 - y4)
            length2 = math.hypot(x2 - x4, y2 - y4)
            length3 = math.hypot(x5 - x4, y5 - y4)

            finger = 0
            if length1 > 100:
                finger += 1
            if length2 > 100:
                finger += 1
            if length3 > 100:
                finger += 1

            print ("finger: ", finger)
            
            play()
                    

            # mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv.imshow("camera", cv.flip(image,1))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


    

