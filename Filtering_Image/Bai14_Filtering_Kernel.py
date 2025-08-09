import numpy as np
import cv2

# Syntax: cv2.filter2D(src, ddepth, kernel)
#       ddepth: độ sâu ảnh đầu ra, mặc định -1
#       kernel: ma trận lọc, thường là Numpy Array
# Một số kernel phổ biến:
# Làm mờ:	np.ones((3,3), np.float32)/9
# Làm sắc nét	[[0,-1,0],[-1,5,-1],[0,-1,0]]
# Phát hiện cạnh [[0,-1,0],[-1,4,-1],[0,-1,0]]


img_src = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_COLOR)

# kernel 5x5 => làm mờ đơn giản (Low Pass Filter)
kernel = np.array([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1]])
kernel = kernel / sum(kernel)
img_rst = cv2.filter2D(img_src, -1, kernel)
cv2.imwrite("D:/OpenCV/img/low_pass_filter.jpg", img_rst)
cv2.imshow("Low Pass Filter Kernel", img_rst)

# Custom kernel
kernel1 = np.array([[-2.0, -2.0],
                   [2.0, 2.0],
                   [-1.0, -1.0]])
print(np.sum(kernel1))
kernel1 = kernel1 / (np.sum(kernel1) if np.sum(kernel1) != 0 else 1)
img_rst_2 = cv2.filter2D(img_src, -1, kernel1)
cv2.imwrite("D:/OpenCV/img/custom_kernel.jpg", img_rst_2)
cv2.imshow("Kernel Custome", img_rst_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
