import cv2
import numpy as np
# dilation: giãn nở
"""
Syntax: cv2.dilate(src, kernel, dts, anchor, iterations, borderType, borderValue)
    - Kernel: ma trận sử dụng cho giãn nở ảnh.
    - anchor: giá trị mặc định (-1, -1). Neo ở giữa phần tử.
    - iterations: số lần giãn nở được sử dụng.
    - borderType: method ngoại suy (extrapolation) pixel
    - borderVlue: giá trị border hằng số.
"""
img = cv2.imread("D:/OpenCV/img/input_image.png", cv2.IMREAD_COLOR)
scale_percent = 200
width_img = int(img.shape[1] * scale_percent / 100)
height_img = int(img.shape[0] * scale_percent / 100)
dsize = (width_img, height_img)
img = cv2.resize(img, dsize)

kernel = np.ones((3, 3), np.uint8)

dilated = cv2.dilate(img, kernel, iterations=3)
cv2.imwrite("D:/OpenCV/img/dilated.jpg", dilated)
cv2.imshow("Result", dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()