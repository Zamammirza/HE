import utils, cv2
from brisque_calculation import calculate_brisque

path = r"processed/no_processing/0AKZCRZA_no_processing.png"
path = r"processed/splinet/0AKZCRZA_splinet.png"
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
print(calculate_brisque(image))