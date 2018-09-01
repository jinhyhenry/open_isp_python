import cv2
import numpy as np

default_total_gain = 0.3
default_raw_limit = 1023

def limit_pixel_stren(stren,limit):
	if(stren>limit):
		return limit
	else:
		return int(stren)

def calc_dist(x_centre,y_centre,x_cur,y_cur):
	sum = pow((x_cur-x_centre),2) + pow((y_cur-y_centre),2)
	return np.sqrt(sum)

def calc_gain(dist,total_gain,total_dist):
	return ((dist/total_dist)*total_gain)+1

def calc_centre_and_total(width,height):
	ret = [0,0,0]
	ret[0] = width/2
	ret[1] = height/2
	ret[2] = calc_dist(ret[0],ret[1],0,0)
	return ret

def process_capture_request(raw_obj):
	print('ratio rolloff request E')
	param = calc_centre_and_total(raw_obj.width,raw_obj.height)
	for i in range(raw_obj.normal_buf_length):
		gain = calc_gain(calc_dist(param[0],param[1],raw_obj.loc_pixel_x(i),raw_obj.loc_pixel_y(i)),default_total_gain,param[2])
		raw_obj.normal_buf[i] = limit_pixel_stren(gain*raw_obj.normal_buf[i],default_raw_limit)


	