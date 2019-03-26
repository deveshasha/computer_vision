import glob
from PIL import Image

images = [f for f in glob.glob('images/*.jpg')]

for image in images:
	im = Image.open(image)
	w = im.size[0]
	h = im.size[1]
	ratio = 500/w
	w *= ratio
	h *= ratio
	print('Saving...',image)
	im.resize((int(w),int(h))).save(image)
