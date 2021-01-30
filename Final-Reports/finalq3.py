#e2264562 Sahin Kasap

import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

debugMode = True

def accentuateTheRoads(img):
    """Roads are generally gray and not so black or white, so I deleted whiter and blacker pixels and
    non-gray pixels"""
    roads = np.copy(img)
    for i in range(0,len(roads)):
        for j in range(0,len(roads[0])):
            pixel = roads[i][j]
            min = pixel[0] if (pixel[0]<pixel[1] and pixel[0]<pixel[2]) else (pixel[1] if pixel[1]<pixel[2] else pixel[2])
            max = pixel[0] if (pixel[0]>pixel[1] and pixel[0]>pixel[2]) else (pixel[1] if pixel[1]>pixel[2] else pixel[2])
            if(max-min>20 or min<80 or max>180):
                roads[i][j][0]=0
                roads[i][j][1]=0
                roads[i][j][2]=0
    if(debugMode):
        plt.imshow(roads)
        plt.show()
    #cv2.imwrite("roads.jpg",roads)
    return roads

def applyHough(img,roads):
    lines = cv2.HoughLinesP(cv2.cvtColor(roads, cv2.COLOR_BGR2GRAY),cv2.HOUGH_PROBABILISTIC,np.pi/180,100,minLineLength=100,maxLineGap=8)
    if(type(lines) == None):
        pass
    else:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(roads,(x1,y1),(x2,y2),(0,255,0),2)

    return roads
    pass

def postProcess(img):

    return img
    pass
def overlay(img, roads):
    for i in range(0,len(roads)):
        for j in range(0,len(roads[0])):
            if(roads[i][j][1]==255 and roads[i][j][0]==0  and roads[i][j][2]==0 ):
                img[i][j] = [0,255,0]
                pass
            pass
        pass
    if(debugMode):
        plt.imshow(img)
        plt.show()
    return img

def final_q3(input_file_path, output_folder):
    print("final_q3 function started for "+input_file_path)
    img = cv2.imread(input_file_path)
    # plt.imshow(img)
    # plt.show()
    roads = accentuateTheRoads(img)
    print("roads are accentuated")
    roads = applyHough(img,roads)
    print("hough applied")
    roads = postProcess(roads)
    print("post processed")
    img = overlay(img, roads)
    print("roads overlayed")
    cv2.imwrite(output_folder,img)
    print("Image written! Done!")
    pass
final_q3("Dataset3/3.png","q3Res.jpg")