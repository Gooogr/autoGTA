import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 26 px accounts for title bar (default value).
        # Read more here about windos title bar: https://superuser.com/questions/952395/how-to-change-window-title-bar-size-in-windows-10  
        title_bar_size = 26
        screen =  np.array(ImageGrab.grab(bbox=(0,title_bar_size,
												800,600 + title_bar_size)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
	


