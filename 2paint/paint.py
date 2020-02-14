import cv2
import numpy as np
#一共包含三个：画矩形线段，画多边形，写字

# #画图,在一幅彩色图片上画线段矩形之类
# img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
# #画了一条线段
# cv2.line(img,(0,0),(100,100),(255,0,0),5)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #画矩形
# cv2.rectangle(img,(100,0),(300,300),(0,255,0),3)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
# #确定了为三通道（深度为3）shape[0]是宽，shape[1]是高
# print(img.shape[2])
# (B,G,R) = cv2.split(img)
# #展现图的三个通道
# cv2.imshow("Red",R)
# cv2.imshow("Green",G)
# cv2.imshow("Blue",B)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #画多边形 画多边形,需要指点每个顶点的坐标。用这些点的坐标构建一个大小等于
# #行数 X1X2 的数组,行数就是点的数目。这个数组的数据类型必须为 int32。
# #这里画一个黄色的具有四个顶点的多边形。
# #img = np.zeros((512,512,3), np.uint8) #也可以建立一个矩阵，然后在矩阵上画点
# img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
# pts = np.array([[100,50],[200,300],[270,220],[350,410]], np.int32) #构建矩阵
# pts = pts.reshape((-1,1,2)) # 这里 reshape 的第一个参数为 -1, 表明这一维的长度是根据后面的维度的计算出来的。
# # cv2.polylines() 可以被用来画很多条线。只需要把想要画的线放在一
# # 个列表中,将这个列表传给函数就可以了。每条线都会被独立绘制。这会比用
# # cv2.line() 一条一条的绘制要快一些。
# cv2.polylines(img,[pts],True,(0,255,255))
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#写字
img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 5,(255,255,255),cv2.LINE_AA) #linetype=cv2.LINE_AA
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()