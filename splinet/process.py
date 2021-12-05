import os

import cv2
import numpy as np
import torch
import torchvision

import splinet
from splinet.NeuralSpline import NeuralSpline


def process(image):
    """Apply SpliNet Optimization to the image

    Parameters
    ----------
    image : 2D numpy array (grayscale image)
        The input image

    Returns
    -------
    processed_image : 2D numpy array (grayscale image)
        A copy of the input image with enhancement applied
    """
    image_splinet_format = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    splinet_input = torch.stack((torchvision.transforms.ToTensor()(image_splinet_format),))
    # If this ends with "Killed" in the terminal, there might not be enough RAM
    out, _ = spline(splinet_input)
    processed_image = out[0][0, :, :, :].detach().numpy() # RGB x H x W
    processed_image = np.transpose(processed_image, axes=(1,2,0))
    processed_image = np.flip(processed_image, axis=2)
    processed_image = cv2.cvtColor(processed_image, cv2.COLOR_RGB2GRAY)
    processed_image = np.round(processed_image*255).astype(np.uint8)
    return processed_image


# create net with the most default settings I could find
spline = NeuralSpline(n=10, nc=8, nexperts=1).cpu()
# load weights for net
device = torch.device('cpu')
module_path = os.path.dirname(splinet.__file__)
state = torch.load(f"{module_path}/expB.pth", map_location=device) # I hope B is well balanced
# other models are either too dark or E is too bright most of the time
spline.load_state_dict(state['state_dict'])
# put into non-training mode
spline.eval()
