import cv2
import numpy as np
import sys

sys.path.append("./rawreader")
sys.path.append("./blk")

import blk
from rawreader import raw_obj

if __name__ == '__main__':
	raw0 = raw_obj(4608,3456,0)
	blk.module_test(1)
	raw0.convert_to_normal()
	raw0.img_creater(1)

