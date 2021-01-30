import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def getImages(input_file_path):
    res = []
    for root, dirs, files in os.walk(input_file_path):
        for filename in files:
            res.append((cv2.imread(input_file_path+"/"+filename),filename))
    return res


def enhance_images(images):
    res = []
    for img in images:
        ret,gray = cv2.threshold(img,115,255,cv2.THRESH_BINARY)
        for i in range (0,len(gray)):
            for j in range(0,len(gray[0])):
                pixel = gray[i][j]
                if(not (pixel[0]==255 and pixel[1]==255 and pixel[2]==255)):
                    gray[i][j]=np.zeros((3))

                    
        res.append(gray)
    
    return res
    pass

def bounding_box(images):
    res = []
    return images
    for img in images:
        pass
    pass
    #TODO

def skeleton(images):
    return images
    #TODO

def numberOfLoops(images):
    return 0
    #TODO
    pass

def measurePerformance(numberOfLoopies):

    correctResults = []
    #TODO

    pass

def draw_images(images):
    for img in images:
        plt.imshow(img,cmap='gray')
        plt.show()


def seperateImageAndFilenames(images):
    imgs = []
    filenames=[]
    for img in images:
        imgs.append(img[0])
        filenames.append(img[1])
    return imgs,filenames


def final_q1(input_file_path,output_file):
    images = getImages(input_file_path)
    images,filenames = seperateImageAndFilenames(images)
    images = enhance_images(images)
    plt.imshow(images[0]/255.0, cmap="gray")
    plt.show()
    draw_images(images)
    images = bounding_box(images)
    images = skeleton(images)
    numberOfLoopies = numberOfLoops(images)
    measurePerformance(numberOfLoopies)
    pass
final_q1("Dataset1","")

