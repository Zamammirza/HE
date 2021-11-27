import os
import errno

import cv2
import numpy as np

def load(image_filename):
    """Load image from database and return as grayscale OpenCV Image

    Parameters
    ----------
    image_filename : string
        The filename of the image in the folder `image_database`
    
    Returns
    -------
    image : 2D numpy array (grayscale image)
        The loaded image
    """
    path = f"image_database/{image_filename}"
    if not os.path.isfile(path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise Exception(f"\"{path}\" couldn't be read as an image by OpenCV.")
    return image

def apply(module, image_filename):
    """Load image, process and save it

    Loads the image from `image_database` as grayscale, applies the function
    module.process to it and places the output in `processed/<module.__name__>`

    Parameters
    ----------
    module : Module with function `process`

    image_filename : string 
        The filename of the image in the folder `image_database`
    """
    image = load(image_filename)
    processed = module.process(image)

    # create output folder if it doesn't exist
    output_folder = f"processed/{module.__name__}"
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)
    
    # add algorithm name to filename
    basename, extension = os.path.splitext(image_filename)
    output_path = f"{output_folder}/{basename}_{module.__name__}{extension}"

    # write and handle error
    write_retval = cv2.imwrite(output_path, processed)
    if not write_retval:
        raise Exception(f"OpenCV could not write processed image to {output_path}")

def apply_to_all(module):
    """Load all images, process and save them

    Loads all images from `image_database` as grayscale, applies the function
    module.process to them and places the outputs in `processed/<module.__name__>`

    Parameters
    ----------
    module : Module with function `process`
    """
    image_names = os.listdir("image_database")
    for image_filename in image_names:
        if not image_filename == ".gitignore":
            apply(module, image_filename)