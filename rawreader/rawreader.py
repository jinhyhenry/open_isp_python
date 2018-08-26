import cv2
import numpy as np
import sys

raw_path = "test.raw"
#raw_path = "test.dat"

class image_base:
	def wait_for_key(self):
		while True:
			k = cv2.waitKey(0)
			if k==27:
				cv2.destroyAllWindows()
				break
		cv2.destroyAllWindows()

class raw_obj(image_base):
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
		while i<self.ori_buf_length:
			common_byte = int(self.ori_buf[i])
			#print('common_byte %d' %(common_byte))
			self.normal_buf[j] = (int(self.ori_buf[i+4])<<2)+(0x03&common_byte) #P0
			#print('i %d ori_buf %d normal_buf %d' %(i,self.ori_buf[i+4],self.normal_buf[j]))
			j += 1
			self.normal_buf[j] = (int(self.ori_buf[i+3])<<2)+(0x0C&common_byte) #P1
			#print('i %d ori_buf %d normal_buf %d' %(i,self.ori_buf[i+3],self.normal_buf[j]))
			j += 1
			self.normal_buf[j] = (int(self.ori_buf[i+2])<<2)+(0x30&common_byte) #P2
			#print('i %d ori_buf %d normal_buf %d' %(i,self.ori_buf[i+2],self.normal_buf[j]))
			j += 1
			self.normal_buf[j] = (int(self.ori_buf[i+1])<<2)+(0xC0&common_byte) #P3
			#print('i %d ori_buf %d normal_buf %d' %(i,self.ori_buf[i+1],self.normal_buf[j]))
			j += 1
			i=i+5
		print('convert_to_normal done')


	#BGBG....BGBG  0
	#GRGR....GRGR  1
	#0123
	#

	def loc_pixel_x(self,index):
		return (int(index/(self.width)))

	def loc_pixel_y(self,index):
		return (int(index%(self.width)))

	#R 1, G 2, B 2
	def decide_which_pixel(self,index):
		if (self.loc_pixel_x(index)%2): #GRGR
			if(self.loc_pixel_y(index)%2): #R
				return 1
			else:
				return 2
		else:
			if(self.loc_pixel_y(index)%2): #B
				return 3
			else:
				return 2

	def img_creater(self,type_mask):
		if type_mask == 1:
			print('going to create a 10th rgb')
			img = np.zeros((self.width,self.height,3), np.uint16)
			for i in range(self.normal_buf_length):
				tmp = self.decide_which_pixel(i)
				'''
				if(tmp == 1):
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][0] = tmp
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][1] = 0
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][2] = 0
				if(tmp == 2):
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][0] = 0
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][1] = tmp
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][2] = 0
				if(tmp == 3):
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][0] = 0
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][1] = 0
					img[self.loc_pixel_x(i)][self.loc_pixel_y(i)][2] = tmp
				'''
				if(tmp == 1):
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][0] = self.normal_buf[i]
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][1] = 0
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][2] = 0
				if(tmp == 2):
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][0] = 0
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][1] = self.normal_buf[i]
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][2] = 0
				if(tmp == 3):
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][0] = 0
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][1] = 0
					img[self.loc_pixel_y(i)][self.loc_pixel_x(i)][2] = self.normal_buf[i]
				#print('index %d y %d , x %d, tmp %d, val %d' %(i, self.loc_pixel_y(i), self.loc_pixel_x(i), tmp, self.normal_buf[i]))
			#cv2.imshow('test',img)
			cv2.imwrite('res1.jpg',img)

		if type_mask == 9:
			#test mode
			img = np.zeros((512,512,3), np.uint8)
			img.fill(128)
			cv2.imshow('test',img)
			self.wait_for_key()

	def obj_test(self,type_mask):
		if type_mask == 1:
			print(self.ori_buf)
		if type_mask == 2:
			print(self.normal_buf)
		if type_mask == 3:
			#test locate function
			for i in range(self.normal_buf_length):
				#print('index %d , decide_which_pixel %d' %(i,self.decide_which_pixel(i)))
				print('i %d,x %d,y %d' %(i,self.loc_pixel_x(i),self.loc_pixel_y(i)))
				#print('y %d' %(self.loc_pixel_y(i)))









