import cv2
import numpy as np

def module_test(type_mask):
	if type_mask == 1:
		print('blk called')

default_blk_val = [65,65,65]

def process_capture_request(raw_obj):
	img = np.zeros((raw_obj.width,raw_obj.height,3), np.uint16)
	for i in range(raw_obj.normal_buf_length):
		tmp = raw_obj.decide_which_pixel(i)

		if tmp == 3: #R
			if(raw_obj.normal_buf[i]-default_blk_val[0] >= 0):
				raw_obj.normal_buf[i] = raw_obj.normal_buf[i] - default_blk_val[0]
			else:
				raw_obj.normal_buf[i] = 0
		if tmp == 2: #G
			if(raw_obj.normal_buf[i]-default_blk_val[1] >= 0):
				raw_obj.normal_buf[i] = raw_obj.normal_buf[i] - default_blk_val[1]
			else:
				raw_obj.normal_buf[i] = 0
		if tmp == 1: #B
			if(raw_obj.normal_buf[i]-default_blk_val[2] >= 0):
				raw_obj.normal_buf[i] = raw_obj.normal_buf[i] - default_blk_val[2]
			else:
				raw_obj.normal_buf[i] = 0

