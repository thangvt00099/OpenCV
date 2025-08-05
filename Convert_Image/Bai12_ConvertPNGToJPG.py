import cv2
import numpy as np

png_img = cv2.imread("D:/OpenCV/img/input_image.png", cv2.IMREAD_UNCHANGED)

# Chất lượng ảnh [0, 100]
# Chuyển đổi với chỉ định chất lượng ảnh
# Mặc định kênh transparent của PNG => được điền màu đen
cv2.imwrite("D:/OpenCV/img/ConvertToJPG.jpg", png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

# Chuyển đổi ảnh PNG -> JPG chỉ định background Color
background_color = (100, 100, 255)
png_img_2 = cv2.imread("D:/OpenCV/img/input_image.png", cv2.IMREAD_UNCHANGED)
print(png_img_2.shape)

new_img = np.full_like(png_img_2, background_color + (255,), dtype=np.uint8)

# Trích xuất kênh alpha từ ảnh gốc
# Công thức trộn ảnh dựa trên kênh alpha
# pixel_result = background * (1 - alpha) + forceground * alpha
# alpha = 0 => pixel theo background
# alpha = 1 => pixel theo forceground (theo ảnh PNG)
# 0 < alpha < 1 => pixel trộn giữa 2 ảnh theo độ trong suốt
alpha_channel = png_img_2[:, :, 3]
for c in range(0, 3):
    new_img[:, :, c] = new_img[:, :, c] * (1 - alpha_channel / 255) + png_img_2[:, :, c] * (alpha_channel / 255)

cv2.imwrite("D:/OpenCV/img/output_image.jpg", new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
