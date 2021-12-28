from . import ContrastEnhancementPack

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

    levels = ContrastEnhancementPack.get_depth(image)
    processed_image = ContrastEnhancementPack.bbheq_util(image, levels)
    
    return processed_image