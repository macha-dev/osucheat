import cv2
import numpy as np
from mss import mss
from PIL import Image
import time
import mouse
from playsound import playsound
wavfile = "71283.wav"

bounding_box = {'top': 0, 'left': 0, 'width': 800 , 'height':630}

sct = mss()

while True:
    start_time = time.time()
    sct_img = sct.grab(bounding_box)
    img = np.array(sct_img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #circle detection
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 1, minRadius = 10, maxRadius= 100, param1=70)

    # ensure at least some circles were found
    if circles is not None:
        
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(img, (x, y), r, (0, 255, 0), 5) #was 4
            if r<45:
                #mouse.move(x,y)
                playsound(wavfile)
                                
                #cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    

    #cv2.rectangle(img, (200, 500), (200+400, 500+100), (255, 0, 0), 2)

    elapsed_time = str(time.time() - start_time)
    cv2.putText(img, elapsed_time, (5,20), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)

    cv2.imshow('screen', img)

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindow()
        break

#this is the epic pogchamp gamer moment #fornite is epic - Bertie 12:55 5/11/20
