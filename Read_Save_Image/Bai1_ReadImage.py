import cv2
import numpy as np
"""
Syntax: 1. cv2.imread('path_to_image', flag)
            - Trả về 1 mảng 2D hoặc 3D chứa dữ liệu hình ảnh.
            (Ảnh nhị phân hoặc màu xám => 2D là đủ, ảnh màu => 3D)
        2. cv2.imshow('window_name', image)
            - Hiển thị ảnh trong một cửa sổ với tên 'window_name'.
            - Để đóng cửa sổ, nhấn phím bất kỳ hoặc sử dụng cv2.waitKey(0).
        3. cv2.imwrite('path_to_save', image)
            - Lưu ảnh vào đường dẫn 'path_to_save'.
            - Ảnh sẽ được lưu dưới định dạng tương ứng với phần mở rộng của tệp (ví dụ: .jpg, .png).\
            - Trả về giá trị Boolean

Options flag:
        - cv2.IMREAD_COLOR: Đọc ảnh màu (mặc định). (rgb)
        - cv2.IMREAD_GRAYSCALE: Đọc ảnh ở chế độ xám. (gray)
        - cv2.IMREAD_UNCHANGED: Đọc ảnh bao gồm cả kênh alpha nếu có. (rgba)

imread() hỗ trợ đọc các định dạng ảnh như: JPG, PNG, BMP, TIFF, WEBP, v.v.
"""
# Đọc ảnh màu
img = cv2.imread('D:/OpenCV/img/picture1.jpg', cv2.IMREAD_COLOR)

# Đọc ảnh màu xám
img_gray = cv2.imread('D:/OpenCV/img/picture1.jpg', cv2.IMREAD_GRAYSCALE)

# Đọc ảnh với kênh màu trong suốt - ảnh phải có kênh alpha (JPG hoặc PNG chỉ có RGB)
img_unchanged = cv2.imread('D:/OpenCV/img/picture1.jpg', cv2.IMREAD_UNCHANGED)
# In kích thước ảnh - (height, width, channels color - kênh màu)
# img.shape => trả về kích thước ảnh dưới dạng tuple
print('Image Dimensions:', img.shape)
print('Image Gray Dimensions:', img_gray.shape)
print('Image Unchanged Dimensions:', img_unchanged.shape)

# Hiển thị ảnh màu
cv2.imshow('Image', img)
cv2.waitKey(0) # Đợi phím bất kỳ để đóng cửa sổ
cv2.destroyAllWindows() # Đóng tất cả cửa sổ

# Tạo ảnh màu xám từ ndarray
ndarray_gray = np.full((300, 300, 3), 125, dtype=np.uint8)  # Tạo ảnh xám 300x300 với giá trị 125

# Hiển thị ảnh
cv2.imshow('Gray Image', ndarray_gray)
cv2.waitKey(0) 
cv2.destroyAllWindows()

img_ndarray_random = np.random.randint(255, size=(300, 600, 3))

isWritten = cv2.imwrite('D:/OpenCV/img/ndarray_random.jpg', img_ndarray_random)
if isWritten:
    print("Image saved successfully.")
else:
    print("Failed to save image.")