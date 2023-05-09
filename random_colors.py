"""
1. write a program using Python that will generate an image of a random hexadecimal color each time it is run

2. adjust the code such that the output file is named according to the hexadecimal values used to generate the color image
"""

from PIL import Image
import random


def generate_random_color():
    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Convert RGB to hexadecimal color code
    color_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    return color_code


def generate_color_image(color_code, width=200, height=200):
    # Create a new image with the specified dimensions
    image = Image.new("RGB", (width, height), color_code)

    # Save the image as a PNG file with a name based on the color code
    file_name = color_code[1:] + ".png"
    image.save(file_name)
    print("Image saved as", file_name)


# Generate a random color
color = generate_random_color()

# Generate and save the color image
generate_color_image(color)
