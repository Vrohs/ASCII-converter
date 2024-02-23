from PIL import Image
import numpy as np



def load_and_resize(image_path, new width = 100)
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height/width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image















#path = https://wonderfulengineering.com/wp-content/uploads/2014/10/image-wallpaper-15.jpg