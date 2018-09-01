import sys

import rolloff_module
import ratio_rolloff

width = 4608
height = 3456

if __name__ == '__main__':
	ret = ratio_rolloff.calc_centre_and_total(width,height)
	print('centre x %d, y %d, tt %d' %(ret[0],ret[1],ret[2]))
	dist = ratio_rolloff.calc_dist(ret[0],ret[1],2304,1728)
	print('dist %d' %(dist))
