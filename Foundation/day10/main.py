import os
from PIL import Image

str_img = 'data.PNG'

# Create Image contain 'X' shape:
def create_image_X_shape(file_name, rgb_point, width_height = 1):
    img = Image.new('RGB', (width_height, width_height), (255, 255, 255))
    for i in range(0, width_height):
        for j in range(0, width_height):
            if ((i == j) or j == (width_height - i - 1)): img.putpixel((i, j), rgb_point)
    img.save(file_name, 'PNG')
    img.close()

# Get number of pixel by RGB
def counter_color_by_pixel(file_name, rgb_point):
    counter = 0
    img = Image.open(file_name)
    for pixel in img.getdata():
        if pixel == rgb_point: counter += 1
    return counter


if(not os.path.exists(str_img)):
    create_image_X_shape(str_img, (255, 0, 0), 10)

print('Tổng số ô có màu đỏ: %d' %counter_color_by_pixel(str_img, (255, 0, 0)))


