#绘制出直方图
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test3.jpg',1)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)

# # #第一种显示方法：使用matplot
# plt.hist(img.ravel(),256,[0,256]);
# plt.show()

# #第二种，分别显示三个分量的灰度值
# color = ('b','g','r')
# # 对一个列表或数组既要遍历索引又要遍历元素时
# # 使用内置 enumerrate 函数会有更加直接,优美的做法
# #enumerate 会将数组或列表组成一个索引序列。
# # 使我们再获取索引和索引内容的时候更加方便
# 用for循环来显示出三颜色
# for i,col in enumerate(color):
#  histr = cv2.calcHist([img],[i],None,[256],[0,256])
#  plt.plot(histr,color = col)
#  plt.xlim([0,256])
# plt.show()


#使用掩模
color = ('b','g','r')
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
#对比一下使用掩模和没使用的区别
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
plt.subplot(224),plt.plot(hist_full), plt.plot(hist_mask)
#plt.xlim([0,256])
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()