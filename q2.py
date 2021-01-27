import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def removeGreen(img):
    
    return img
img =cv.imread("Dataset2/5.jpg")
#img = plt.imread("Dataset2/5.jpg")
img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
plt.imshow(img)
plt.show()

img = removeGreen(img)
