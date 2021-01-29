import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

def accentuateTheRoads(img):
    """Roads are generally gray and not so black or white, so I deleted whiter and blacker pixels and
    non-gray pixels"""
    roads = np.copy(img)
    for i in range(0,len(roads)):
        for j in range(0,len(roads[0])):
            pixel = roads[i][j]
            if(np.amax(pixel)-np.amin(pixel)>20 or np.amin(pixel)<55 or np.amax(pixel)>180):
                roads[i][j]=np.zeros((3))
    # plt.imshow(roads)
    # plt.show()
    cv2.imwrite("roads.jpg",roads)
    return roads
    return roads

def applyHough(img,roads):
    lines = cv2.HoughLinesP(cv2.cvtColor(roads, cv2.COLOR_BGR2GRAY),1,np.pi/180,100,minLineLength=100,maxLineGap=5)
    if(type(lines) == None):
        print("anan")
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
    return img

def final_q3(input_file_path, output_folder):
    img = cv2.imread(input_file_path)
    plt.imshow(img)
    plt.show()
    roads = accentuateTheRoads(img)
    roads = applyHough(img,roads)
    roads = postProcess(roads)
    img = overlay(img, roads)
    cv2.imwrite(output_folder,img)
    pass
final_q3("Dataset3/4.png","q4Res.jpg")