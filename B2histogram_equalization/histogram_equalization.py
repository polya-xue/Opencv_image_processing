#直方图均衡化

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test3.jpg',0)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)

#使用Numpy 来进行直方图均衡化,且用numpy来计算一维直方图
#flatten() 将数组变成一维
hist,bins = np.histogram(img.flatten(),256,[0,256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
#显示直方图
#plt.plot(hist)
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
#加批注
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

# # 用变换函数把现在的直方图映射到一个广泛分布的直方图中
# # 构建 Numpy 掩模数组, cdf 为原数组,当数组元素为 0 时,掩盖(计算时被忽
# cdf_m = np.ma.masked_equal(cdf,0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# # 对被掩盖的元素赋值,这里赋值为 0
# cdf = np.ma.filled(cdf_m,0).astype('uint8')
# img2 = cdf[img]
#
# #重新显示
# #flatten() 将数组变成一维
# hist,bins = np.histogram(img2.flatten(),256,[0,256])
# # 计算累积分布图
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()
# plt.plot(cdf_normalized, color = 'b')
# #显示直方图
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# #加批注
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()
# #实际效果是给图像增加了对比度
# cv2.imshow('img2',img2)


# #第二种方法：OpenCV 中的直方图均衡化
# #这个函数的输入图片仅仅是一副灰度图像,输出结果是直方图均衡化之后的图像。
# equ = cv2.equalizeHist(img)
# res = np.hstack((img,equ))
# #stacking images side-by-side
# cv2.imshow('res.png',res)

# #第三种方法：CLAHE 有限对比适应性直方图均衡化
# #为了避免增强对比度带来的信息丢失，使用ClAHE方法，将图像分为很多个小块，分别做均衡化
# # create a CLAHE object (Arguments are optional).
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(img)
# res = np.hstack((img,cl1))
# cv2.imshow('clahe_',res)



cv2.waitKey()
cv2.destroyAllWindows()
