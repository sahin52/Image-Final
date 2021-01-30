#e2264562 Sahin Kasap
import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.morphology import skeletonize


cv = cv2
def getImages(input_file_path):
    res = []
    for _, _, files in os.walk(input_file_path):
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
        index = int((len(gray)-(len(gray)%2))/2)
        #print(index)
        color = gray[0][index]
        #for i in range(0,len(gray)):
            #if(gray[i][0][0]!=color[0] and gray[i][0][1]!=color[1] and gray[i][0][2]!=color[2]):
                #gray[i][0]=color
                    
        res.append(gray)
    
    return res
    pass

def bounding_box(images):
    res = []
    conts = []
    #return images
    for im in images:
        img = cv2.cvtColor(np.copy(im), cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cont in contours:
            x,y,w,h = cv2.boundingRect(cont)
            cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        # plt.imshow(img)
        # plt.show()
        res.append(img)
        conts.append(contours)
    return res,conts

def skeleton(images):
    res = []
    for image in images:
        res.append(skeletonize(image))

    return res
    #TODO

def numberOfLoops(images):
    res = []
    for image in images:
        res.append(0)
    return res
    #TODO
    pass

def measurePerformance(numberOfLoopies):

    correctResults = [1,1,1,0,0]#hardcoded
    total = 0
    for i in range (0,len(correctResults)):
        if(numberOfLoopies[i]==correctResults[i]):
            total+=1
    
    print("The ratio of true results is:")
    print(total/len(correctResults))
    
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
    # plt.imshow(images[0]/255.0, cmap="gray")
    # plt.show()
    # draw_images(images)
    boundedimage,conts = bounding_box(images) 
    images = skeleton(images)
    numberOfLoopies = numberOfLoops(images)
    measurePerformance(numberOfLoopies)
    pass
#final_q1("Dataset1","")

