import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test3.jpg',1)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)#cv2.INTER_CUBIC)

# #腐蚀操作
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)#腐蚀一次
# # plt.subplot(121),plt.imshow(img),plt.title('Original')
# # plt.xticks([]), plt.yticks([])
# # plt.subplot(122),plt.imshow(erosion),plt.title('erosion')
# # plt.xticks([]), plt.yticks([])
# # plt.show()
# cv2.imshow('Original',img)
# cv2.imshow('erosion',erosion)

# #膨胀操作
# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(img,kernel,iterations = 1)
# cv2.imshow('Original',img)
# cv2.imshow('dilation',dilation)

# #开原酸，先腐蚀后膨胀
# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# cv2.imshow('Original',img)
# cv2.imshow('opening',opening)

#闭运算，先膨胀后腐蚀
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Original',img)
cv2.imshow('closing',closing)


cv2.waitKey(0)
cv2.destroyAllWindows()