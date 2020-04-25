# ~ import numpy as np
# ~ from PIL import ImageGrab


# ~ from mss import mss
# ~ from PIL import Image
# ~ from time import time
# ~ import cv2

# ~ # https://python-mss.readthedocs.io/examples.html

# ~ def capture_screenshot():
	# ~ with mss() as sct:
		# ~ monitor_number = 2
		# ~ mon = sct.monitors[monitor_number]
		
		# ~ # The screen part to capture 800x600
		# ~ monitor = {
			# ~ "top": mon["top"] + 45,  # 100px from the top
			# ~ "left": mon["left"] + 0,  # 100px from the left
			# ~ "width": 800,
			# ~ "height": 580,
			# ~ "mon": monitor_number,
			# ~ }
		# ~ output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)
		
		# ~ # Grab the data
		# ~ sct_img = sct.grab(monitor)
		
		# ~ # Convert to PIL/Pillow Image
		# ~ img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
		# ~ img.show()

# ~ last_time = time()
# ~ while True:
	# ~ capture_screenshot()
	# ~ print('loop took {} seconds'.format(time()-last_time))
	# ~ last_time = time()
	# ~ if cv2.waitKey(25) & 0xFF == ord('q'):
            # ~ cv2.destroyAllWindows()
            # ~ break
            
            
            
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
	


