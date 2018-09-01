import cv2
import numpy as np

import xml.etree.ElementTree as ET
import os
import sys



def module_test(type_mask):
	if type_mask == 1:
		print('xml called')
	if type_mask == 2:
		xmlFilePath = os.path.abspath("./util/test.xml")
		print(xmlFilePath)
		tree = ET.parse(xmlFilePath)
        print("tree type:", type(tree))
        root = tree.getroot()
        print (root.tag, "----", root.attrib)
        
        for child in root:
        	print ("root travel", child.tag, "----", child.attrib)
        	
        	
        
