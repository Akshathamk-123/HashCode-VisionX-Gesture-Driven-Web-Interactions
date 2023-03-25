import cv2 
from cvzone.HandTrackingModule import HandDetector
import math
import mediapipe as mp
from time import sleep
import cvzone
import numpy as np
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 728)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        ["_","|"]]
finalText = ""

keyboard = Controller()

# def drawAll(img, buttonlist):
#     for button in buttonlist:
#         x,y =button.pos
#         w,h = button.size
#         cv2.rectangle(img, button.pos, (x+w , y+h), (255,0,255), cv2.FILLED)
#         cv2.putText(img,button.text, (x +20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),4)
#     return img

def drawAll(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
                      (255, 0, 255), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 40, y + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    print(mask.shape)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out


class Button():
    def __init__(self,pos, text, size=[85, 85]):
        self.pos =pos
        self.size =size
        self.text =text
       
buttonList = []

def calculate_distance(lmList, point1, point2):
    x1, y1 = lmList[point1][1], lmList[point1][2]
    x2, y2 = lmList[point2][1], lmList[point2][2]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            buttonList.append(Button([100*j+50,100*i+50],key))

while True:
    success, img= cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]
    img= drawAll(img, buttonList)

    if hands and lmList1:
        for button in buttonList:
            x, y = button.pos
            w,h = button.size

            if x <lmList1[8][0] < x+w and y < lmList1[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
            
                l = calculate_distance(lmList1, 8, 12)
                #_ is used in Python for ignoring the variables
                print(l)

                #When click
                if l<30:
                    if button.text == "_":
                        keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, " ", (x + 20, y + 65),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText += " "
                    elif button.text == "|":
                        keyboard.press("\b")
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, "\b", (x + 20, y + 65),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText = finalText[:len(finalText)-1]
                    else:
                        keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText += button.text
                    sleep(0.20)

    ##This is for bar in which the final text was displayed 
    cv2.rectangle(img, (50, 450), (700,550), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 540),cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)        
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)

