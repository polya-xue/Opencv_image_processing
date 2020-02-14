# #获取彩色像素值并修改
# import cv2
# import numpy as np
# img = cv2.imread('/home/polya/mine/picture/test1.jpg',1)
# px=img[100,100]
# print(px)
# img[100,100]=[255,255,255]
# print(px)
# blue=img[100,100,0]
# print(blue)

# #获取灰度亮度值
# import cv2
# import numpy as np
# img = cv2.imread('/home/polya/mine/picture/test1.jpg',0)
# px=img[100,100]
# print(px)

# 上面提到的方法被用来选取矩阵的一个区域,比如说前 5 行的后 3
# 列。对于获取每一个像素值,也许使用 Numpy 的 array.item() 和 ar-
# ray.itemset() 会更好。但是返回值是标量。如果你想获得所有 B,G,R 的
# 值,你需要使用 array.item() 分割他们。
import cv2
import numpy as np
img=cv2.imread('/home/polya/mine/picture/test1.jpg',1)
print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))

