import cv2
import numpy as np
import sys

sys.path.append("./util")
sys.path.append("./rawreader")

from rawreader import raw_obj
import util_entry

raw_file_path = "/Users/henry/work/code/image_algo_own/own/open_isp_python/raw_reader/raw_img/raw_cluster/shading/norm_tl84.raw"
out_path = "./out_put_pic/norm_tl84_roll.jpg"

isp_module_list = [1,1] # hard code now; but will turn to xml in the future
                  # blk, rolloff 

if __name__ == '__main__':
	raw0 = raw_obj(4608,3456,0,raw_file_path,out_path)
	raw0.convert_to_normal()
	util_entry.process_request_to_all_module(raw0,isp_module_list)
	raw0.img_creater(1)

