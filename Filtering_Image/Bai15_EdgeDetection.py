import cv2

"""
Syntax: cv2.Canny(img, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
    - threshold1: ngưỡng dưới. Các gradient (độ biến thiên cường độ pixel) < giá trị này => loại bỏ và không được coi là cạnh.
    - threshold2: ngưỡng trên. Các gradient > giá trị này => được coi là cạnh mạnh
    - edges: số lượng kênh trong ảnh output
    - apertureSize: xác định kích thước bộ lọc Sobel => tính toán gradient cua ảnh
Lưu ý: Ảnh phải là màu xám, nếu là ảnh màu => chuyển sang xám
"""
img = cv2.imread("D:/OpenCV/img/input_image.png", cv2.IMREAD_COLOR)

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold1 = 30
threshold2 = 200

edges = cv2.Canny(grayscale_img, threshold1, threshold2)

cv2.imwrite("D:/OpenCV/img/edges.jpg", edges)
cv2.imshow("Result", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()