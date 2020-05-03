import cv2
import numpy as np

# 读取原始图片
img = cv2.imread("F:\\test\\cat.0.jpg")
print('img.shape:', img.shape)  # 高度，宽度，通道数

# 缩放成200x200的方形图像
img_200x200 = cv2.resize(img, (200, 200))
print('img_200x200.shape:', img_200x200.shape)

# 不直接指定缩放后大小，通过fx和fy指定缩放比例，0.5则长宽都为原来一半
# 等效于img_100x100 = cv2.resize(img, (100, 100))，注意指定大小的格式是(宽度,高度)
# 插值方法默认是cv2.INTER_LINEAR，这里指定为最近邻插值
img_100x100 = cv2.resize(img_200x200, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
print('img_100x100.shape:', img_100x100.shape)

# 在上张图片的基础上，上下各贴50像素的黑边，生成200x100的图像
img_200x100 = cv2.copyMakeBorder(img_100x100, 50, 50, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
print('img_200x100.shape:', img_200x100.shape)

# 在上张图片的基础上，上下各贴50像素的黑边,左右各贴100像素的黑边，生成300x300的图像
img_300x300 = cv2.copyMakeBorder(img_200x100, 50, 50, 100, 100, cv2.BORDER_CONSTANT, value=(0, 0, 0))
print('img_300x300.shape:', img_300x300.shape)

# 对照片中局部进行剪裁
cv2.imshow('img', img)
patch_img = img[220:550, -180:-50]
cv2.imshow('patch_img', patch_img)
cv2.waitKey(0)
