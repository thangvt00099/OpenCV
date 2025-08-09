import cv2

"""
Syntax: cv2.blur(img_src, kernel shapre => tuple)
"""

img_src = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_COLOR)

# Kernel (5, 5)
img_rst = cv2.blur(img_src, (5, 5))
cv2.imwrite("D:/OpenCV/img/blur_img.jpg", img_rst)
cv2.imshow("Result blur image", img_rst)

# Kernel (20, 20)
img_rst_2 = cv2.blur(img_src, (20, 20))
cv2.imwrite("D:/OpenCV/img/blur_img_2.jpg", img_rst_2)
cv2.imshow("Result blue image 2", img_rst_2)
cv2.waitKey(0)
cv2.destroyAllWindows()