import cv2
import numpy as np
import bbhe

print("Hello, World!")

bbhe.process(
    np.array([[1, 2], [3, 4]], dtype=np.uint8)
)