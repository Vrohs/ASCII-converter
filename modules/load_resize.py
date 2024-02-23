from PIL import Image
import numpy as np
from mapping_pixels import *


def convert_to_greyscale(image):
    return image.convert("L")



def load_and_resize(image_path, new width = 100)
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image




def img_to_ascii(image, new width = 100):
    image = load_and_resize(image_path = image, new_width = 100)
    image = convert_to_greyscale(image)

    ascii str = map_pixels_to_ascii(image)



