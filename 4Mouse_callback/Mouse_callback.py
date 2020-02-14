import cv2
import numpy as np

# #使用鼠标画图，在图片上双击过的位置绘制一个圆圈，按esc退出
#
# #event=[i for i in dir(cv2) if 'EVENT'in i] 创建一个鼠标事件回调函数，可以用来查看有哪些汉书可用
# #mouse callback function
# def draw_circle(event,x,y,flags,param):
#  if event==cv2.EVENT_LBUTTONDBLCLK:
#   cv2.circle(img,(x,y),10,(255,0,0),-1)
# # 创建图像与窗口并将窗口与回调函数绑定
# img=np.zeros((512,512,3),np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# while(1):
#  cv2.imshow('image',img)
#  if cv2.waitKey(20)&0xFF==27:
#   break
# cv2.destroyAllWindows()

#根据选择的模式在拖动鼠标时绘制矩形或者是圆圈(就像画图程序中一样)。所以
# 回调函数包含两部分,一部分画矩形,一部分画圆圈。这是一个典型的
# 例子他可以帮助理解与构建人机交互式程序,比如物体跟踪,图像分割等。
# 当鼠标按下时变为 True
drawing=False
# 如果 mode 为 true 绘制矩形。按下 'm' 变成绘制曲线。
mode=True
ix,iy=-1,-1
# 创建回调函数
def draw_circle(event,x,y,flags,param):
 global ix,iy,drawing,mode
# 当按下左键是返回起始位置坐标
 if event==cv2.EVENT_LBUTTONDOWN:
  drawing=True
  ix,iy=x,y
# 当鼠标左键按下并移动是绘制图形。 event 可以查看移动, flag 查看是否按下
 elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
  if drawing==True:
   if mode==True:
    cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
   else:
# 绘制圆圈,小圆点连在一起就成了线, 3 代表了笔画的粗细
    cv2.circle(img,(x,y),3,(0,0,255),-1)
# 下面注释掉的代码是起始点为圆心,起点到终点为半径的
#    r=int(np.sqrt((x-ix)**2+(y-iy)**2))
#    cv2.circle(img,(x,y),r,(0,0,255),-1)
# 当鼠标松开停止绘画。
 elif event==cv2.EVENT_LBUTTONUP:
  drawing==False
 # if mode==True:
 #  cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
 # else:
 #  cv2.circle(img,(x,y),5,(0,0,255),-1)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
 cv2.imshow('image',img)
 k=cv2.waitKey(1)&0xFF
 if k==ord('m'):
  mode=not mode
 elif k==27:
  break