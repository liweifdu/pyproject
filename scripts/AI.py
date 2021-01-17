import cv2
import numpy as np
from matplotlib import pyplot as plt

#gamma 变换
def gamma_trans(img,gamma):
    #具体做法先归一化到1，然后gamma作为指数值求出新的像素值再还原
    gamma_table = [np.power(x/255.0,gamma)*255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    return cv2.LUT(img, gamma_table)

img = cv2.imread("F:\\hyj\\baby_noise.jpg",0)
print(img.shape)
cv2.imshow("original",img)

'''
#gammma 变换
dst = gamma_trans(img, 1.5)
'''

'''
#二值化
th1,dst = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
'''

'''
#直方图均衡化
dst = cv2.equalizeHist(img)
'''

'''
#缩放图像
rows, cols, channel = img.shape
matrix=np.array([[0.5,0,0],[0,0.5,0],[0,0,1]],np.float32)
dst=cv2.warpPerspective(img,matrix,(int(cols/2),int(rows/2)))
'''

'''
#图像插值：INTER_NEAREST最邻近插值，INTER_LINEAR 双线性插值，INTER_AREA 使用像素区域关系进行重采样，INTER_CUBIC 4x4像素邻域的双三次插值，INTER_LANCZOS4 8x8像素邻域的Lanczos插值
rows, cols, channel = img.shape
dst=cv2.resize(img, (int(cols*2),int(rows*2)), interpolation=cv2.INTER_LANCZOS4)
'''

'''
#图像配准
# 我们可以通过cv2.getRotationMatrix2D函数得到转换矩阵
#matrix = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# 得到变换的矩阵，通过这个矩阵再利用warpAffine来进行变换
# 第一个参数就是旋转中心，元组的形式，这里设置成相片中心
# 第二个参数90，是旋转的角度
# 第三个参数1，表示放缩的系数，1表示保持原图大小
#points1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
#points2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
#根据四对点获得透视变换矩阵
#matrix = cv2.getPerspectiveTransform(points1,points2)
'''

'''
#图像平滑（模糊）
dst=cv2.blur(img,(5,5))
dst=cv2.GaussianBlur(img,(5,5),2)
dst=cv2.medianBlur(img,5)
'''

cv2.imshow("dst",dst)
#np.ravel()将数据变成一维度的
plt.hist(dst.ravel() , 256, [0, 256])
plt.show()