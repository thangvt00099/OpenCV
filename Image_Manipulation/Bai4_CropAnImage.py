import cv2
"""
Syntax slicing an image:
    img[y: y+h, x:x+w]
    Trong đó:
        x, y: tọa độ điểm bắt đầu (top-left)
        w, h: rộng, cao của khu vực quan tâm
        ROI: Region Of Interest (Khu vực quan tâm)
"""
img = cv2.imread('D:/OpenCV/img/picture1.jpg')

# Định nghĩa w, h
w, h = 200, 200

# Tính XY để cắt phần giữa của ảnh
print(img.shape)
img_h, img_w = img.shape[:2]
print(img_h, img_w)
x, y = (img_w // 2 - w // 2), (img_h // 2 - h // 2)
print(x, y, w, h)

cropped_img = img[y:y+h, x:x+w]
cv2.imwrite('D:/OpenCV/img/cropped_img.jpg', cropped_img)
cv2.imshow('Result Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()