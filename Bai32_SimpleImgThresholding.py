import cv2
import numpy as np

img = cv2.imread('D:/OpenCV/img/gradient.png', 0)
img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_LANCZOS4)

# Ngưỡng nhị phân
# _, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Ngưỡng nhị phân nghịch đảo
# _, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

# _, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)

_, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO)

cv2.imshow('Image', img)
cv2.imshow('th1', th1)

cv2.waitKey(0)
cv2.destroyAllWindows()