import image_slicer
import glob
import os
import sys

BASE = "/Users/damoncrockett/Desktop/Seoul_selfies/"
input_path = BASE+"tokyo/"


targets = [
BASE+"tokyo_slice_16/",
BASE+"tokyo_slice_256/"
]

nums_slices = [16,256]

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
