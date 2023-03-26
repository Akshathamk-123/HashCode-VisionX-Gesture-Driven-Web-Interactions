from flask import Flask,render_template,Response
import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

app=Flask(__name__)
camera=cv2.VideoCapture(0)

mpHands = mp.solutions.hands #detects hand/finger
hands = mpHands.Hands()   #complete the initialization configuration of hands
mpDraw = mp.solutions.drawing_utils

#To access speaker through the library pycaw 
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volbar=400
volper=0
 
volMin,volMax = volume.GetVolumeRange()[:2]

def generate_frames():
    while True:
        #Read the camera frame
        success, img=camera.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convert to rgb
    
        #Collection of gesture information
        results = hands.process(imgRGB) #completes the image processing.
    
        lmList = [] #empty list
        if results.multi_hand_landmarks: #list of all hands detected.
            #By accessing the list, we can get the information of each hand's corresponding flag bit
            for handlandmark in results.multi_hand_landmarks:
                for id,lm in enumerate(handlandmark.landmark): #adding counter and returning it
                    # Get finger joint points
                    h,w,_ = img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy]) #adding to the empty list 'lmList'
                mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
        
        if lmList != []:
            #getting the value at a point
                            #x      #y
            x1,y1 = lmList[4][1],lmList[4][2]  #thumb
            x2,y2 = lmList[8][1],lmList[8][2]  #index finger
            #creating circle at the tips of thumb and index finger
            cv2.circle(img,(x1,y1),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
            cv2.circle(img,(x2,y2),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
            cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)  #create a line b/w tips of index finger and thumb
    
            length = hypot(x2-x1,y2-y1) #distance b/w tips using hypotenuse
    # from numpy we find our length,by converting hand range in terms of volume range ie b/w -63.5 to 0
            vol = np.interp(length,[30,350],[volMin,volMax]) 
            volbar=np.interp(length,[30,350],[400,150])
            volper=np.interp(length,[30,350],[0,100])
            
            
            print(vol,int(length))
            volume.SetMasterVolumeLevel(vol, None)
            
            # Hand range 30 - 350
            # Volume range -63.5 - 0.0
            #creating volume bar for volume level 
            cv2.rectangle(img,(50,150),(85,400),(0,0,255),4) # vid ,initial position ,ending position ,rgb ,thickness
            cv2.rectangle(img,(50,int(volbar)),(85,400),(0,0,255),cv2.FILLED)
            cv2.putText(img,f"{int(volper)}%",(10,40),cv2.FONT_ITALIC,1,(0, 255, 98),3)
            #tell the volume percentage ,location,font of text,length,rgb color,thickness
            if not success:
                break
            else:
                ret,buffer=cv2.imencode('.jpg',img)
                frame=buffer.tobytes()

            yield(b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True, port=8000)