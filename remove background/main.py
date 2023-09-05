from rembg import remove
from PIL import Image


input_path = '123.jpg'
output_path = "321.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)