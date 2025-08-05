import cv2
import numpy as np

"""
    - Làm nhiễu ảnh => giảm độ sắc nét (sharpness), độ tương phản (contrast) của ảnh
    => Khó trích xuất đặc trưng (feature) của ảnh
    - Sử dụng gaussian noise để làm nhiễu ảnh
1. cv2.add():
    - Thêm nhiễu vào ảnh với gaussian noise
2. cv2.randn():
    - Tạo ma trận nhiễu với kích thước giống ảnh gốc
    - Giá trị trung bình (mean) và độ lệch chuẩn (stddev) của nhiễu
3. Các trường hợp sử dụng thêm nhiễu ảnh:
    - Kiểm tra thuật toán xử lý ảnh
    - Tăng cường dữ liêu liệu (data augmentation) trong học sâu (deep learning)
    - Mô phỏng các điều kiện thực tế (real-world conditions) như nhiễu trong camera, ánh sáng yếu, v.v.
    - Tăng cường thẩm mỹ hình ảnh
"""
img = cv2.imread('D:/OpenCV/img/picture1.jpg', cv2.IMREAD_COLOR)

# Tạo gaussian noise
mean = 0
stddev = 100
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)

noisy_img = cv2.add(img, noise)
cv2.imshow('Noisy Image', noisy_img)
cv2.imwrite('D:/OpenCV/img/noisy_image.jpg', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()