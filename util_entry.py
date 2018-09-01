import cv2
import numpy as np
import sys

sys.path.append("./rawreader")
sys.path.append("./blk")
sys.path.append("./rolloff")

import blk
import util_xml
import rolloff_module
from rawreader import raw_obj

def process_request_to_all_module(raw_obj,mod_table):
	if (mod_table[0] == 1):
		print('blk enabled , now process')
		blk.process_capture_request(raw_obj)
	if (mod_table[1] == 1):
		print('rolloff enabled , now process')
		rolloff_module.process_capture_request(raw_obj)



