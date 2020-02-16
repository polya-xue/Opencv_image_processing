import cv2
import numpy as np
img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)

# #图像收放
# # 下面的 None 本应该是输出图像的尺寸,但是因为后边我们设置了缩放因子
# # 因此这里为 None
# res1=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# # OR
# # 这里呢,我们直接设置输出图像的尺寸,所以不用设置缩放因子
# height,width=img.shape[:2]
# res2=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('res1',res1)
# cv2.imshow('res2',res2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #图像平移
# h, w = img.shape[:2]
# # 设置平移矩阵
# bias = 100
# M = np.float32([[1, 0, bias], [0, 1, bias]])
# # 获取平移图像
# dst = cv2.warpAffine(img, M, (w, h), borderValue=(255, 0, 0))
# cv2.imshow('input---dst', np.hstack([img, dst]))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#图像旋转45度
rows,cols = img.shape[:2]
# 这里的第一个参数为旋转中心,第二个为旋转角度,第三个为旋转后的缩放因子
# 可以通过设置旋转中心,缩放因子,以及窗口大小来防止旋转后超出边界的问题
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)
# 第三个参数是输出图像的尺寸中心
dst=cv2.warpAffine(img,M,(2*cols,2*rows))
while(1):
 cv2.imshow('img',dst)
 if cv2.waitKey(1)&0xFF==27:
  break
cv2.destroyAllWindows()