#更强大的一个边缘检测算法算法：Canny边缘检测
#具体算法比较复杂，不是很了解

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test2.jpg',0)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)#cv2.INTER_CUBIC)

edges = cv2.Canny(img,100,200)
cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()