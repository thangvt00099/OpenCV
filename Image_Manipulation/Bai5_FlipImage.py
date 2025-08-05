import cv2

"""
Flip Image: lật ảnh
Syntax: cv2.flip(src, flipCode[, dst])
    Trong đó:
        src: đầu vào ảnh
        flipCode: - 0: lật ảnh quanh trục x
                  - 1: lật ảnh quanh trục y (bất kì giá trị dương nào)
                  - -1: lật ảnh quanh cả 2 trục (bất kì giá trị âm nào)
        dst: mảng đầu ra có kích thước và kiểu như ảnh gốc
"""
img = cv2.imread('D:/OpenCV/img/image1.png', cv2.IMREAD_COLOR)
flipped_img = cv2.flip(img, -1)
cv2.imwrite('D:/OpenCV/img/flipped_img.jpg', flipped_img)
cv2.imshow('Result Image', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()