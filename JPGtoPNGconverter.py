from PIL import Image, ImageFilter
import sys
import os

#grab the input and output folder
input_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if output folder exist, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#convert images to PNG and save it
for filename in os.listdir(input_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{input_folder}{filename}')
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')




