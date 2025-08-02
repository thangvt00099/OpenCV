import cv2

"""
Syntax: cv2.cvtColor(src, code, dst, dstCn)
    - src: nguồn ảnh
    - code: ví dụ: cv2.COLOR_BGR2GRAY chuyển sang ảnh xám
    - dst: mảng đầu ra kích thước và kiểu với src [Optional]
    - dstCn: Số lượng kênh trong ảnh gốc
"""

img = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_COLOR)

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('D:/OpenCV/img/grayscale_img.png', grayscale_img)
cv2.imshow("Result: ", grayscale_img)
cv2.waitKey(0)
cv2.destroyAllWindows()