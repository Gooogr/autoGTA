'''
Use polinom to select road region
'''
import sys
import numpy as np
from PIL import ImageGrab
import cv2
import time

from  directkeys import PressKey, ReleaseKey
from directkeys import W, A, S, D, SPACE

def select_road_region(img, vertices):
	'''
	Masked image part roughly above the horizon and in the car cabin. 
	It`s useless information for training
	'''
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked

def process_img(original_image):
	# road split line detection
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) #data simplify
	processed_img = cv2.Canny(processed_img, threshold1 = 100, threshold2 = 120) #dark night 40-100 night with light 100 - 120
	# Add brightness adaptation? Calculate mean brightness and select proper thresholds?
	
	vertices = np.array([[10,500],[10,300], [300,200], [500,200], [800,300], [800,500]], np.int32)
	processed_img = select_road_region(processed_img, [vertices])

	return processed_img
	

def screen_record(print_loop_time = False): 
	last_time = time.time()
	while(True):
		# 800x600 windowed mode for GTA 5, at the top left position of your main screen.
		# 26 px accounts for title bar (default value). 
		title_bar_size = 26
		screen =  np.array(ImageGrab.grab(bbox=(0,title_bar_size,
												800,600 + title_bar_size)))
		new_screen = process_img(screen)
		if print_loop_time:
			print('loop took {} seconds'.format(time.time()-last_time))
		last_time = time.time()
		cv2.imshow('window', new_screen)
		#cv2.imshow('window2',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

# Counting down, give you time to enter into the game's window.
def count_down(start_sec = 5):
	for i in range(start_sec,0,-1):
		sys.stdout.write(str(i)+' ')
		sys.stdout.flush()
		time.sleep(1)

# Direct input test
def test_key(key_name):
	print('down')
	PressKey(key_name)
	time.sleep(3)
	print('up')
	ReleaseKey(key_name)

# ~ test_key(SPACE)
# ~ test_key(D)
# ~ test_key(A)
# ~ test_key(S)
# ~ test_key(W)


print('Script is running!\n')

screen_record()


	
