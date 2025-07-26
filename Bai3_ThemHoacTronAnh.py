import cv2
import numpy as np

"""
Syntax: cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
       - Thêm hoặc trộn 2 ảnh với nhau.
       - Trả về numpy array chứa giá trị pixels của ảnh kết quả.
       Trong đó:
       - src1: Ảnh đầu tiên.
         - alpha: Hệ số trọng số của ảnh đầu tiên.
       - src2: Ảnh thứ hai.
         - beta: Hệ số trọng số của ảnh thứ hai.
       - gamma: Hệ số bù (bias) được thêm vào tất cả các pixel của ảnh kết quả.
         - dst: Ảnh kết quả (nếu không truyền vào thì hàm sẽ tự tạo).
         (dst = src1 * alpha + src2 * beta + gamma)
"""
src1 = cv2.imread('D:/OpenCV/img/image1.png')
src2 = cv2.imread('D:/OpenCV/img/image2.png')

dst = cv2.addWeighted(src1, 1.0, src2, 1.0, 0.0)
cv2.imshow('Result Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
