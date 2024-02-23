from PIL import Image
import numpy as np



ASCII_chars = "@#$*."


def map_pixels_to_ascii(image, range_width = 25):
    pixels = np.array(image)
    pixels_to_chars = [ASCII_chars[pixel_value//range_width] for pixel_value in pixels.flatten()]
    return "".join(pixels_to_chars)
