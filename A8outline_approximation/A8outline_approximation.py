#轮廓近似
import cv2
import numpy as np
img = cv2.imread('/home/polya/mine/picture/test5.jpg',1)
imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 假设我们要在一幅图像中查找一个矩形,但是由于图像的
# 种种原因,我们不能得到一个完美的矩形,而是一个“坏形状”(如下图所示)。
# 现在你就可以使用这个函数来近似这个形状()了。这个函数的第二个参数叫
# epsilon,它是从原始轮廓到近似轮廓的最大距离。它是一个准确度参数。选
# 择一个好的 epsilon 对于得到满意结果非常重要。
ret,thresh = cv2.threshold(imggrey, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
#cv2.imshow('img',thresh)
image,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
#计算出轮廓周长
epsilon = 0.015*cv2.arcLength(cnt,True)
#得到轮廓近似的数组
approx = cv2.approxPolyDP(cnt,epsilon,True)
cv2.polylines(img, [approx], True, (0, 0, 255), 2)
cv2.imshow('img',img)

# # 凸包检测
# # 凸包与轮廓近似相似,但不同,对有些图来说，效果更好些
# # 函数 cv2.convexHull() 可以用来检测一个曲线是否具有凸性缺陷,并能纠
# # 正缺陷。一般来说,凸性曲线总是凸出来的,至少是平的。如果有地方凹进去
# # 了就被叫做凸性缺陷。
# img = cv2.imread('/home/polya/mine/PycharmProjects/小成sky/openCV/tutorial_045/test.jpg',1)
# imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imggrey, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
# image,contours,hierarchy = cv2.findContours(thresh, 1, 2)
# for i in range(len(contours)):
#     # 对轮廓进行凹性检测, 返回 bool
#     convex = cv2.isContourConvex(contours[i])
#     #print("convex: ", convex)
#
#     # hull: 传入轮廓, 返回凸包上的坐标
#     hull = cv2.convexHull(points=contours[i], returnPoints=True)
#     total = len(hull)
#     for k in range(len(hull)):
#         x1, y1 = hull[k % total][0]
#         x2, y2 = hull[(k+1) % total][0]
#         cv2.circle(img, (x1, y1), 4, (255, 0, 0), 2, 8, 0)
#         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
#      #print(hull)
# cv2.imshow('contours-hull', img)


cv2.waitKey(0)
cv2.destroyAllWindows()