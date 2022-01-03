import cv2

CLAHE = cv2.createCLAHE(clipLimit = 3, tileGridSize = (15, 15))

def process(image):
    """Apply clahe to the image


    Parameters
    ----------
    image : 2D numpy array (grayscale image)
        The input image
    
    Returns
    -------
    processed_image : 2D numpy array (grayscale image)
        A copy of the input image with clahe applied
    """
    return CLAHE.apply(image)
    