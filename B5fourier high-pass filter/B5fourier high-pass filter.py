#图像傅立叶变换后使用高低通滤波器
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test1.jpg',0)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)

# #使用numpy数组的方式，使用高通滤波器，得到图像的边界
# f = np.fft.fft2(img)
# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))
# #高通滤波器
# rows, cols = img.shape
# crow,ccol = rows/2 , cols/2
# fshift[int(crow)-30:int(crow)+30, int(ccol)-30:int(ccol)+30] = 0
# #反向移动，使DC组件再次出现在左上角
# f_ishift = np.fft.ifftshift(fshift)
# #傅立叶逆变换
# img_back = np.fft.ifft2(f_ishift)
# # 取绝对值
# img_back = np.abs(img_back)
# plt.subplot(131),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
# plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(img_back)
# plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
# plt.show()
# plt.imshow(img_back, cmap = 'gray'),plt.title('Image after HPF')
# plt.show()
# plt.imshow(img_back),plt.title('Result in JET')
# plt.show()

#使用openCV的方式，使用低通滤波器，模糊图像
#构建一个掩模,与低频区域对应的地方设置为 1, 与高频区域对应的地方设置为 0。
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#低通滤波器掩模
rows, cols = img.shape
crow,ccol = rows/2 , cols/2
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[int(crow)-30:int(crow)+30, int(ccol)-30:int(ccol)+30] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

