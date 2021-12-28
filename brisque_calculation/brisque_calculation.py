import cv2
from brisque import BRISQUE
from matplotlib import image
import matplotlib.pyplot as plt

BRISQUE_INSTANCE = BRISQUE()

def calculate_brisque(image):  
    score = BRISQUE_INSTANCE.get_score(image)
    return score