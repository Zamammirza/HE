import utils, cv2, time
from brisque_calculation import calculate_brisque

started = time.time()

path = r"processed/no_processing/0AKZCRZA_no_processing.png"
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
print("unprocessed: " + str(calculate_brisque(image)))

path = r"processed/splinet/0AKZCRZA_splinet.png"
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
print("splinet: " + str(calculate_brisque(image)))

stopped = time.time()

print("took: " + str(stopped-started))

# with 0AKZCRZA.png took 23.5 s