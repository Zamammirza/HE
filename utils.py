import os
import errno

import cv2

def load(image_filename, folder="image_database"):
    """Load image from database and return as grayscale OpenCV Image

    Parameters
    ----------
    image_filename : string
        The filename of the image in the `folder` (image_database by default)
    
    Returns
    -------
    image : 2D numpy array (grayscale image)
        The loaded image
    """
    print(f"loading {image_filename}")
    path = f"{folder}/{image_filename}"
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

def apply_to_all(module, ignore=None):
    """Load all images, process and save them

    Loads all images from `image_database` as grayscale, applies the function
    module.process to them and places the outputs in
    `processed/<module.__name__>`

    If you want to exclude certain files, create a file in the folder
    `image_database` called `.images_ignore` with a list of all filenames you
    would like to exclude. Alternatively, you can set the `ignore` parameter. 

    Parameters
    ----------
    module : Module with function `process`

    ignore: filename or list of filenames to ignore
    """
    image_names = os.listdir("image_database")
    # ignored files by default
    ignores = [".gitignore", ".image_ignore"]
    if ignore:
        if isinstance(ignore, list):
            ignores.extend(ignore)
        elif isinstance(ignore, str):
            ignores.append(ignore)
        else:
            raise Exception("`ignore` is not a list or string")
    try:       
        with open("image_database/.image_ignore", "r") as f:
            ignores.extend(f.read().splitlines())
    except FileNotFoundError:
        print("File '.image_ignore' not found - only ingnoring files ignored by default")
    for image_filename in image_names:
        if not image_filename in ignores:
            apply(module, image_filename)