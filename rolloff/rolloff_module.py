import cv2
import numpy as np

import ratio_rolloff

default_algo_type = 1 
# 1 -- ratio;   2 -- mesh;  3 -- adaptive

def process_capture_request(raw_obj):
	if default_algo_type == 1:
		print('use ratio rolloff')
		ratio_rolloff.process_capture_request(raw_obj)
	if default_algo_type == 2:
		print('use mesh rolloff')
	if default_algo_type == 3:
		print('use adaptive rolloff')

