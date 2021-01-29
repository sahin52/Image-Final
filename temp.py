#this includes segmentation

# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
import argparse
import cv2 as cv
from skimage.measure import regionprops


# load the image and convert it to a floating point data type
image =cv.cvtColor(cv.imread("Dataset2/5.jpg"),cv.COLOR_RGB2BGR)


# apply SLIC and extract (approximately) the supplied number
# of segments
segments = slic(image, n_segments = 250, sigma = 5,multichannel=True)

# show the output of SLIC
fig = plt.figure("Superpixels -- %d segments%")
ax = fig.add_subplot(1, 1, 1)
ax.imshow(mark_boundaries(image, segments))
plt.axis("off")

# show the plots
plt.show()

def paint_region_with_avg_intensity(rp, mi, channel,image):
    for i in range(rp.shape[0]):
        image[rp[i][0]][rp[i][1]][channel] = mi

for i in range(3):
    regions = regionprops(segments, intensity_image=image[:,:,i])
    for r in regions:
        paint_region_with_avg_intensity(r.coords, int(r.mean_intensity), i,image)
plt.imshow(image)
plt.show()
