import cv2
import os

vidcap = cv2.VideoCapture('1.mp4')
success,image = vidcap.read()
count = 0
i=0
path = 'D:/D/win10_desktop/projects/tensorflow/bottle/images'
while success:
	if count%2 == 0:
		i += 1
		cv2.imwrite(os.path.join(path,'frame%d.jpg' % i), image)     # save frame as JPEG file      
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1