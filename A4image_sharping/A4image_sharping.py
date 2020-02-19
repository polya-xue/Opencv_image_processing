import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test2.jpg',0)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)#cv2.INTER_CUBIC)

#以下为三个用于边缘检测的算子:
#cv2.CV_64F 输出图像的深度(数据类型),可以使用 -1, 与原图像保持一致 np.uint8
laplacian=cv2.Laplacian(img,cv2.CV_64F)
# 参数 1,0 为只在 x 方向求一阶导数,最大可以求 2 阶导数。
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# 参数 0,1 为只在 y 方向求一阶导数,最大可以求 2 阶导数。
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

#可以清楚的看到边缘位置
# cv2.imshow('laplacian',laplacian)
# cv2.imshow('sobelx',sobelx)
# cv2.imshow('sobely',sobely)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()