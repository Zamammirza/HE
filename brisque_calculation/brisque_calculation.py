import cv2
from matplotlib import image
import matplotlib.pyplot as plt
from cv2.quality import QualityBRISQUE_compute, QualityBRISQUE_create

MODEL_FILENAME = "brisque_calculation/brisque_model_live.yml"
RANGE_FILENAME = "brisque_calculation/brisque_range_live.yml"
BRISQUE_INSTANCE = QualityBRISQUE_create(MODEL_FILENAME, RANGE_FILENAME)

def calculate_brisque(image):  
    score = BRISQUE_INSTANCE.compute(image)
    return score[0]