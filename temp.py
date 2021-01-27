import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
from PIL import Image


image = Image.open('Dataset2/1.jpg')
image = np.array(image)
x=len(image)
y=len(image[0])
#Need to convert image into feature array based
#on rgb intensities
flat_image=np.reshape(image, [-1, 3])
 
#Estimate bandwidth
bandwidth2 = estimate_bandwidth(flat_image,
                                quantile=.004, n_samples=1000)
ms = MeanShift(bandwidth2, bin_seeding=True)
ms.fit(flat_image)
labels=ms.labels_
 
# Plot image vs segmented image
plt.figure(0)
plt.imshow(image)
plt.axis('off')
#plt.subplot(2, 1, 2)

plt.figure(1)
plt.imshow(np.reshape(labels, [x,y])) #cmap= 'gray'
plt.axis('off')
plt.show()