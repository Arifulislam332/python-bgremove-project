from PIL import Image
from rembg import remove

# INPUT IMAGE
input_image=("car_pic.jpeg")

# OPEN IMAGE
input_image_open= Image.open(input_image)

# BG REMOVE OUTPUT
output_image= remove(input_image_open)

# OUTPUT SAVE

output_image.save('output_img.png')
print("Output Image create Successfuly 😱")