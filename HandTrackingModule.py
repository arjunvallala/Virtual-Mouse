import cv2 
import mediapipe as mp
import time
import math

class HandDetector:
    def __init__(self,mode=False,maxhands =2,detectioncon=0.5,trackcon=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.detectioncon = detectioncon
        self.trackcon= trackcon
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxhands,
            min_detection_confidence=self.detectioncon,
            min_tracking_confidence=self.trackcon
        )
        self.mpdraw = mp.solutions.drawing_utils
        self.tipIds = [4,8,12,16,20]
        
    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLm in self.results.multi_hand_landmarks:
                if draw:   self.mpdraw.draw_landmarks(img,handLm,self.mphands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,handNo=0,draw=True):
        # imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # self.results = self.hands.process(imgRGB)
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myhand.landmark):
                    h,w,c = img.shape
                    cx ,cy= int(lm.x * w),int(lm.y * h)
                    self.lmList.append([id,cx,cy])
            for handLm in self.results.multi_hand_landmarks:
                if draw: self.mpdraw.draw_landmarks(img,handLm,self.mphands.HAND_CONNECTIONS)
        return self.lmList
    def fingersUp(self):
        if len(self.lmList)==0:
            return []
        fingers=[]

        if self.lmList[3][1]<self.lmList[20][1]:
            if self.lmList[self.tipIds[0]][1]>self.lmList[self.tipIds[0]-1][1]:
                fingers.append(0)
            else:
                fingers.append(1)
        else :
            if self.lmList[self.tipIds[0]][1]>self.lmList[self.tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        for id in range(1,5):
            if self.lmList[self.tipIds[id]][2]<self.lmList[self.tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers
        

    def findDistance(self, img, p1, p2, draw=True):
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
    
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
    
        distance = math.hypot(x2 - x1, y2 - y1)
        if distance<40 and draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (x1, y1), 8, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 8, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (cx, cy), 8, (220, 20, 20), cv2.FILLED)
    
        return distance, img, [x1, y1, x2, y2, cx, cy]
            
            
        
        
        
        