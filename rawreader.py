import cv2
import numpy as np

raw_path = "test.raw"
#raw_path = "test.dat"

class raw_obj:
	def __init__(self,width,height,type_mask):
		self.width = width
		self.height = height
		self.type = type_mask
		self.ori_buf_length = int(((width*height)/4)*5)
		self.ori_buf = np.zeros(self.ori_buf_length)

		print(self.ori_buf_length)

		raw_file = open(raw_path,'rb+')
		raw_file.seek(0,0)
		
		i=0
		for i in range(self.ori_buf_length):
			self.ori_buf[i] = ord(raw_file.read(1))
		raw_file.close()

	def obj_test(self,need_dump):
		print(self.ori_buf)


if __name__ == '__main__':
	raw0 = raw_obj(4608,3456,0)
	raw0.obj_test(0)
