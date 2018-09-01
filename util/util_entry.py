import cv2
import numpy as np
import sys

sys.path.append("../rawreader")
sys.path.append("../blk")

import blk
import util_xml
from rawreader import raw_obj

def process_request_to_all_module(raw_obj,mod_table):
	if (mod_table[0] == 1):
		print('blk enabled , now process')
		blk.process_capture_request(raw_obj)



