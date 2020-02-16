#拆分三个通道并显示
import cv2
import numpy as np
img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
cv2.imshow('b',b)
#合并
img2 = cv2.merge((b, g, r))
cv2.imshow('Merge', img2)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

#另一种方法，数组切片法,还可赋值
# import cv2
# img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
# b_img = img[:,:,0] # B通道
# g_img = img[:,:,1] # G通道
# r_img = img[:,:,2] # R通道
# cv2.imshow('b', b_img )
# k=cv2.waitKey(0)
# cv2.destroyAllWindows()


# img[:,:,0]=255
# cv2.imshow('img',img)
# k=cv2.waitKey(0)
# cv2.destroyAllWindows()