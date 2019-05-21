import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record(): 
    last_time = time.time()
    while(True):
    
        printscreen =  np.array(ImageGrab.grab(bbox=(0,80,1600,1024)))
        print('it take {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        #cv2.write(printscreen)
        if cv2.waitKey(15000) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        
screen_record()