import cv2
from brisque import BRISQUE
from matplotlib import image
import matplotlib.pyplot as plt
import pybrisque

def brisq(image):
 pybrisque.brisq()   
brisq = BRISQUE()

#brisq.get_feature('/path')
image = cv2.imread(r'E:\tasks\overexposedcorrected.jpg')

score = brisq.get_score(r'E:\tasks\overexposedcorrected.jpg')
print (score)

plt.imshow(image)
plt.show()
