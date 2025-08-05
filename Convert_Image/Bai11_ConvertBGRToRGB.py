import cv2

# OpenCV sử dụng BGR là màu mặc định  
img = cv2.imread('D:/OpenCV/img/input_image.jpg', cv2.IMREAD_UNCHANGED)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("DST of Image_rgb: ", img_rgb.shape)

cv2.imwrite("D:/OpenCV/img/img_rgb.jpg ", img_rgb)
cv2.imshow("Result: ", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()