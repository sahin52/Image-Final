#e2264562 Sahin Kasap
import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage.segmentation as seg
from skimage.segmentation import mark_boundaries
import matplotlib.pyplot as plt
import argparse
import cv2 as cv


def generateSuperPixels(img):
    segments = seg.slic(img, n_segments = 9, sigma = 3,multichannel=True,start_label=1)
    plt.imshow(mark_boundaries(img, segments))
    plt.show()
    import skimage.measure as ms

    for i in range(len(img[0][0])):
        regions = ms.regionprops(segments, intensity_image=img[:,:,i])
        for region in regions:
            # print(r.coords)
            coords = region.coords
            mean_intensity = region.mean_intensity
            for j in range(len(coords)):
                img[rp[j][0]][rp[j][1]][i] = mean_intensity

    plt.imshow(img)
    plt.show()

    return img



def attributedGraph(img,suppix):
    return img


def nCutSegmentation(graph,suppix,img):
    return img
    pass






def final_q2(input_file_path, output_folder):
    image = cv.cvtColor(cv.imread(input_file_path),cv.COLOR_RGB2BGR)
    suppix  = generateSuperPixels(image)
    graph   = attributedGraph(image,suppix)
    ncutseg = nCutSegmentation(graph,suppix,image)




    cv.imwrite(output_folder,suppix)
    pass
