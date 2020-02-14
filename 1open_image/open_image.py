import cv2
#下面的程序将会加载一个灰度图,显示图片,按下’s’键保存后退出,或者
#按下 ESC 键退出不保存。

img = cv2.imread('/home/polya/mine/picture/test1.jpg',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k == 27:# wait for ESC key to exit
 cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
 cv2.imwrite('//pic/save1.jpg', img)
cv2.destroyAllWindows()

#读取图像的简单代码
#img = cv2.imread('/home/polya/mine/picture/test1.jpg',0)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()