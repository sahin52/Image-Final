import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("Dataset1/5.png",0)
#gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
ret,gray = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

plt.imshow(gray,cmap='gray')
plt.show()

