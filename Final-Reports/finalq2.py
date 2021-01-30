#e2264562 Sahin Kasap
import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.segmentation as seg
from skimage.segmentation import mark_boundaries
import matplotlib.pyplot as plt
import argparse
import cv2 as cv

debugMode = True

def generateSuperPixels(img):
    segments = seg.slic(img, n_segments = 10, sigma = 3,multichannel=True,start_label=1)
    if(debugMode):
        plt.imshow(mark_boundaries(img, segments))
        plt.show()


    return segments



def attributedGraph(img,segments):
    import skimage.measure as ms
    imcopy = np.copy(img)
    for i in range(len(imcopy[0][0])):
        regions = ms.regionprops(segments, intensity_image=imcopy[:,:,i])
        for region in regions:
            # print(r.coords)
            coords = region.coords
            mean_intensity = region.mean_intensity
            for j in range(len(coords)):
                imcopy[coords[j][0]][coords[j][1]][i] = mean_intensity
    if(debugMode):
        plt.imshow(imcopy)
        plt.show()
    return imcopy


def nCutSegmentation(graph,segments,img):
    width = int(len(graph)/2)
    height = int(len(graph[0])/2)
    color = graph[width][height]
    emptyimage = np.zeros(graph.shape,dtype=np.uint8)
    for i in range (0,len(graph)):
        for j in range (0,len(graph[0])):
            pixel = graph[i][j]
            if( pixel[0]==color[0] and pixel[1]==color[1] and pixel[2]==color[2]):
                emptyimage[i][j][0] = img[i][j][0]
                emptyimage[i][j][1] = img[i][j][1]
                emptyimage[i][j][2] = img[i][j][2]
    
    if(debugMode):
        plt.imshow(emptyimage)
        plt.show()
    
    return emptyimage
    pass






def final_q2(input_file_path, output_folder):
    print("final_q2 function started for "+input_file_path)
    image = cv.cvtColor(cv.imread(input_file_path),cv.COLOR_RGB2BGR)
    segments  = generateSuperPixels(image)
    graph   = attributedGraph(image,segments)
    ncutseg = nCutSegmentation(graph,segments,image)




    cv.imwrite(output_folder,segments)
    pass
