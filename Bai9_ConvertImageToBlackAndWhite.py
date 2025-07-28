import cv2
"""
B1: Đọc ảnh với IMREAD_GRAYSCALE
B2: Chuyển ảnh với ngưỡng (threshhold)
Syntax: cv2.threshold(
    img, 
    thresh,
    max_value, // giá trị tối đa gán cho điểm ảnh
    loại pp phân ngưỡng
) => trả về tuple 2 phần (giá trị ngưỡng thực tế đã sử dụng => ngưỡng
                        ảnh đã được phân ngưỡng => ảnh kết quả)
"""
img = cv2.imread('D:/OpenCV/img/image1.png', cv2.IMREAD_GRAYSCALE)

# threshold: [0-255]
thresh = 128
img_binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[0]
cv2.imshow("Result: ", img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()