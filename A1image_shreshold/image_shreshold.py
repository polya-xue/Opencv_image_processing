#分别使用了不同的阈值，然后显示出来
import cv2
import numpy as np
from matplotlib import pyplot as plt

#简单阈值
# img = cv2.imread('/home/polya/mine/picture/test1.jpg',0)
# ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#  plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#  plt.title(titles[i])
#  plt.xticks([]),plt.yticks([])
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#迭代阈值法（自适应阈值）
img = cv2.imread('/home/polya/mine/picture/test1.jpg',0)
# 中值滤波
img = cv2.medianBlur(img,5)#使用中值滤波器来平滑（模糊）处理一张图片
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11 为 Block size, 2 为 C 值
#自适应阈值算法：CV_ADAPTIVE_THRESH_MEAN_C 阈值类型：CV_THRESH_BINARY
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
 plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
 plt.title(titles[i])
 plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()