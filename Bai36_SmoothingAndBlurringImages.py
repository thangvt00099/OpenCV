import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:/OpenCV/img/input_image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel=kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur']
images = [img, dst, blur, gblur]

for i in range(len(titles)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()