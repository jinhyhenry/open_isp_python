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
		self.normal_buf_length = width*height
		self.ori_buf = np.zeros(self.ori_buf_length)
		self.normal_buf = np.zeros(self.normal_buf_length)

		print(self.ori_buf_length)

		raw_file = open(raw_path,'rb+')
		raw_file.seek(0,0)
		
		i=0
		for i in range(self.ori_buf_length):
			self.ori_buf[i] = ord(raw_file.read(1))
		raw_file.close()

	def convert_to_normal(self):
		i = 0
		j = 0
		while i<self.normal_buf_length:
			common_byte = int(self.ori_buf[i])
			self.normal_buf[j] = (int(self.ori_buf[i+4])<<2)+(0x03&common_byte) #P0
			j += 1
			self.normal_buf[j] = (int(self.ori_buf[i+3])<<2)+(0x0C&common_byte) #P1
			j += 1
			self.normal_buf[j] = (int(self.ori_buf[i+2])<<2)+(0x30&common_byte) #P2
			j += 1
			self.normal_buf[j] = (int(self.ori_buf[i+1])<<2)+(0xC0&common_byte) #P3
			j += 1
			i=i+5
		print('convert_to_normal done')

	def obj_test(self,need_dump):
		print(self.ori_buf)


if __name__ == '__main__':
	raw0 = raw_obj(4608,3456,0)
	raw0.obj_test(0)
	raw0.convert_to_normal()
