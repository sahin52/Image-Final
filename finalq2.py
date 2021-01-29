import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt



def generateSuperPixels(img):
    return img



def attributedGraph(img,suppix):
    return img


def nCutSegmentation(graph,suppix,img):
    return img
    pass






def final_q2(input_file_path, output_folder):
    img     = cv.imread(input_file_path)
    suppix  = generateSuperPixels(img)
    graph   = attributedGraph(img,suppix)
    ncutseg = nCutSegmentation(graph,suppix,img)




    cv.imwrite(output_folder,img)
    pass