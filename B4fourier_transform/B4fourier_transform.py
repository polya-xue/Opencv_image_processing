#离散傅立叶变换
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/home/polya/mine/picture/test1.jpg',0)
img=cv2.resize(img,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)
#离散傅立叶变换

# #使用numpy数组的方式显示
# f = np.fft.fft2(img)
# #将图像变换的原点移动到频域矩形的中心
# fshift = np.fft.fftshift(f)
# # 对中心化后的结果进行对数变换
# magnitude_spectrum = 20*np.log(np.abs(fshift))
# #显示
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

#使用openCV的方式显示
#dft执行数组傅立叶变换
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()