import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
import matplotlib.pyplot as plt
import argparse
import cv2 as cv





def generateSuperPixels(img):
    segments = slic(img, n_segments = 9, sigma = 3,multichannel=True)


    plt.imshow(mark_boundaries(img, segments))
    plt.show()

    return img



def attributedGraph(img,suppix):
    return img


def nCutSegmentation(graph,suppix,img):
    return img
    pass






def final_q2(input_file_path, output_folder):
    image =cv.cvtColor(cv.imread(input_file_path),cv.COLOR_RGB2BGR)
    suppix  = generateSuperPixels(image)
    graph   = attributedGraph(image,suppix)
    ncutseg = nCutSegmentation(graph,suppix,image)




    cv.imwrite(output_folder,img)
    pass
