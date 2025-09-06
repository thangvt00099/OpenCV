import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:/OpenCV/img/image2.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

# giãn nở ảnh
dilation = cv2.dilate(mask, kernel=kernal, iterations=3)

# xói mòn ảnh
erosion = cv2.erode(mask, kernel=kernal, iterations=5)

# Biến đổi hình thái mở => xói mòn ảnh trước => giãn nở ảnh
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel=kernal)

# Biến đổi hình thái đóng => giãn nở ảnh trước => xói mòn ảnh
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel=kernal)

# Biến đổi hình thái gradient
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel=kernal)

# Biến đổi hình thái mũ chóp
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel=kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'th']
images = [img, mask, dilation, erosion, opening, closing, gradient, th]

# plt.subplot(nrows, ncols, index)
for i in range(len(titles)):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()