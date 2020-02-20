#查找轮廓的不同特征,例如面积,周长,重心,边界框等。
import cv2
import numpy as np
img = cv2.imread('/home/polya/mine/picture/test4.jpg',0)

ret,thresh = cv2.threshold(img,127,255,0)
image,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
#函数 cv2.moments() 会将计算得到的矩以一个字典的形式返回
M = cv2.moments(cnt)
#求得面积
area = cv2.contourArea(cnt)
print(area)
#求得周长
perimeter = cv2.arcLength(cnt,True)
print(perimeter)



