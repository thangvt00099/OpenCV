import cv2
import time
"""
Syntax:
    cv2.rotate(src, degree)
"""
src = cv2.imread('D:/OpenCV/img/image2.png', cv2.IMREAD_UNCHANGED)

# Xoay 90 độ theo chiều kim đồng hồ
rotate_img_90 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('D:/OpenCV/img/rotate_img_90.png', rotate_img_90)
# cv2.imshow("Result: ", rotate_img_90)

# Xoay 180 độ
rotate_img_180 = cv2.rotate(src, cv2.ROTATE_180)
cv2.imwrite('D:/OpenCV/img/rotate_img_180.png', rotate_img_180)
# cv2.imshow("Result: ", rotate_img_180)

# Xoay 270 độ theo chiều kim đồng hồ
rotate_img_270 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('D:/OpenCV/img/rotate_img_270.png', rotate_img_270)


