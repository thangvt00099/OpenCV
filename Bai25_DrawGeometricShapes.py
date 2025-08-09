import cv2
import numpy as np

# img = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_COLOR)
# print(img.shape)

img = np.zeros([512, 512, 3], np.uint8)

# Vẽ line
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# Vẽ arrow line
img = cv2.arrowedLine(img, (0, 0), (200, 200), (0, 255, 0),5)

# Vẽ rectangle
img = cv2.rectangle(img, (0, 0), (100, 100), (255, 0, 0), 5)

# Vẽ circle
img = cv2.circle(img, (100, 100), 50, (255, 0, 0), 5)
cv2.putText(
    img, 
    "OpenCV",
    (10, 300), 
    cv2.FONT_HERSHEY_COMPLEX, 
    1,
    (255, 0, 123, 255),
    2
)

cv2.imwrite("D:/OpenCV/img/draw_image.png", img)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()