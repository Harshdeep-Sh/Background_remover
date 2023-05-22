from rembg import remove
from PIL import Image

input_path = input("Enter image path: ")
output_path =input("Enter output file name(without extension): ")
inpu = Image.open(input_path)
output = remove(inpu)
output.save(output_path+'.png')
