from PIL import Image
import os
import sys

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check exist output, if not then create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


for image in os.listdir(image_folder):
	lean_image = os.path.splitext(image)[0]
	img = Image.open(f'.\\{image_folder}\\{image}')
	img.save(f'.\\{output_folder}.\\{lean_image}.png', 'png')
	print("all done!")