#2D直方图，也就是彩色直方图
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)

# #转化维HSV格式，cv2来显示彩色图像直方图
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# plt.plot(hist)
# plt.show()

# #或者使用numpy来显示彩色直方图,图片格式为hsv
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# h=hsv[:,:,0]
# s=hsv[:,:,1]
# hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
# plt.plot(hist)
# plt.show()

# #绘制HSV 颜色2D直方图。颜色用的不多，所以看起来不明显
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
# plt.imshow(hist,interpolation = 'nearest')
# plt.show()

#彩色图像自适应直方图均衡化
cv2.imshow('img',img)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
channels = cv2.split(hsv)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe.apply(channels[2], channels[2])
cv2.merge(channels, hsv)
cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB, img)
cv2.imshow('img2',img)

cv2.waitKey()
cv2.destroyAllWindows()
