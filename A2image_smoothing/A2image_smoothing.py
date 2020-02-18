import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)#cv2.INTER_CUBIC)

# #卷积法，建立一个数组，和图像做卷积，起到平滑作用
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)#-1指瞄点
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()


#另一种方法：使用滤波器，blur是卷积核，可以拥有不同类型的权重

# # 对每个像素平均求和，是低通滤波器，消除高频，
# blur = cv2.blur(img,(5,5))
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

# #高斯卷积核，可有效的去除高斯噪音
# blur = cv2.GaussianBlur(img,(5,5),0)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

# #中值滤波，以中值代替像素值
# blur = cv2.medianBlur(img,5)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

#双边滤波,同时使用空间高斯权重和灰度值相似性高斯权重。空间高斯函
# 数确保只有邻近区域的像素对中心点有影响,灰度值相似性高斯函数确保只有
# 与中心像素灰度值相近的才会被用来做模糊运算。所以这种方法会确保边界不
# 会被模糊掉,因为边界处的灰度值变化比较大。
#9 邻域直径,两个 75 分别是空间高斯函数标准差,灰度值相似性高斯函数标准差
blur = cv2.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()