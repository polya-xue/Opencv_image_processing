import cv2
import numpy as np
img1 = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
img2 = cv2.imread('/home/polya/mine/picture/test2.jpg',1)
# #直接相加
# cv2.imshow('dst',cv2.add(img1,img2))
# cv2.waitKey(0)
# cv2.destroyAllWindow()
# #权重相加
# dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindow()

#按位运算
# and
dst1 = cv2.bitwise_and(img1, img2)
# or
dst2 = cv2.bitwise_or(img1, img2)
# not
dst3 = cv2.bitwise_not(img1, img2)
# xor
dst4 = cv2.bitwise_xor(img1, img2)
# cv2.imshow('and-or-not-xor', np.hstack(([dst1, dst2, dst3, dst4])))
cv2.imshow('or', np.hstack(( dst2)))
cv2.waitKey(0)
cv2.destroyAllWindows()