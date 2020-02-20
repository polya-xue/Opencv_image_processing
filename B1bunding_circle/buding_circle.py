#边界圆形
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test6.jpg',1)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#找到对象的外切圆
for i in range(len(contours)):
    cnt = contours[i]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    img = cv2.circle(img,center,radius,(0,255,0),2)
cv2.imshow('show',img)

#找到对象的椭圆拟合,代码没运行成功

# cnt = contours[0]
# ellipse = cv2.fitEllipse(cnt)
# img = cv2.ellipse(img,ellipse,(0,255,0),2,shift=0)
# cv2.imshow('show2',img)
#
# cv2.waitKey()
# cv2.destroyAllWindows()