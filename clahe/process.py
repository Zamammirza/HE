
import cv2

def process(image):
    """Apply BBHE to the image


    Parameters
    ----------
    image : 2D numpy array (grayscale image)
        The input image
    
    Returns
    -------
    processed_image : 2D numpy array (grayscale image)
        A copy of the input image with BBHE applied
    """

    
    clahe = cv2.createCLAHE(clipLimit = 15.0, tileGridSize = (20,20))
    v = clahe.apply(image)
    
    return v