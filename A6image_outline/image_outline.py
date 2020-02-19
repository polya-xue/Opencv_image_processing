#绘制轮廓：进行阈值处理或者canny边界检测后，寻找轮廓，绘制轮廓
import numpy as np
import cv2
img = cv2.imread('/home/polya/mine/picture/test2.jpg',1)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)#cv2.INTER_CUBIC)
imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#第一种方法：阈值检测后描绘边界
ret,thresh = cv2.threshold(imggrey,127,255,0)
#contour是一个 Python列表,其中存储这图像中的所有轮廓。每一个轮廓都是一个
# Numpy 数组,包含对象边界点(x,y)的坐标。
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('coutours',image)
#绘制轮廓
img = cv2.drawContours(img, contours, -1, (0,255,0), 1)
cv2.imshow('img_thresh',img)

#第二种，效果更好写，canny边界检测后描绘边界
edges = cv2.Canny(img,100,200)
image, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img_canny = cv2.drawContours(img, contours, -1, (0,255,0), 1)
cv2.imshow('img_canny',img_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()