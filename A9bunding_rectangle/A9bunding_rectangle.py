#给边界上框矩形
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test6.jpg',1)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# #直角矩形，比较粗暴
# ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# #可以输出轮廓的层次结构
# print(hierarchy)
# for i in range(len(contours)):
#     cnt = contours[i]
#     x, y, w, h = cv2.boundingRect(cnt)
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.imshow('show',img)


# #最小外接矩形
# for i in range(len(contours)):
#     cnt = contours[i]
#     rect = cv2.minAreaRect(cnt)
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
# cv2.imshow('show',img)

#总之都是比较蠢笨的方法，还需要for循环

#外接正圆
#找到对象的外切圆
for i in range(len(contours)):
    cnt = contours[i]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    img = cv2.circle(img,center,radius,(0,255,0),2)
cv2.imshow('show',img)


cv2.waitKey()
cv2.destroyAllWindows()