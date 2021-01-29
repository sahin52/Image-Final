import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Dataset3/1.png")
# plt.imshow(img)
# plt.show()
print(img.dtype)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
print(sobelx.dtype)
print(type(sobely.dtype))
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

print(sobelx.shape)
sobely = ((sobely/21000+0.5)*256).astype(np.uint8)
sobely = cv2.cvtColor(sobely, cv2.COLOR_RGB2GRAY)

lines = cv2.HoughLinesP(sobely,1,np.pi/180,100,minLineLength=1200,maxLineGap=5)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    # plt.imshow(img)
    # plt.show()
plt.imshow(img)
plt.show()

