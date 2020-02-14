# import cv2
# #调用电脑自带的摄像头,可显示出灰白视频图像
# cap=cv2.VideoCapture(0)
# #k=cap.isOpened() 检查摄像头是否打开了
# #print(k)
# while(True):# Capture frame-by-frame
#  ret, frame = cap.read()
#  # Our operations on the frame come here
#  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#  # Display the resulting frame
#  cv2.imshow('frame',gray)
#  if cv2.waitKey(1)== ord('q'):# & 0xFF
#   break
# cap.release()
# cv2.destroyAllWindows()

#播放一个彩色视频并且保存到当前目录下
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
 ret, frame = cap.read()
 if ret==True:
  #为0是垂直旋转
  frame = cv2.flip(frame,1)
# write the flipped frame
  out.write(frame)
  cv2.imshow('frame',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
   break
 else:
  break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

