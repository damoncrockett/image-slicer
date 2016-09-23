import image_slicer
import glob
import os
import sys

BASE = "/Users/damoncrockett/Desktop/Seoul_selfies/"
input_path = BASE+"seoul/"


targets = [
BASE+"slices_2/",
BASE+"slices_4/",
BASE+"slices_8/",
BASE+"slices_32/",
BASE+"slices_64/"
]

nums_slices = [2,4,8,32,64]

filetype = "jpg"

for i in range(len(targets)):
	target = targets[i]
	num_slices = float(nums_slices[i])
	counter=-1

	for file in glob.glob(os.path.join(input_path,'*.'+filetype)):
		counter +=1
		print num_slices,counter
		try:
			tiles = image_slicer.slice(file,num_slices,save=False)
			image_slicer.save_tiles(tiles,
								directory=target,
								prefix=str(counter))
		except:
			print 'err'
