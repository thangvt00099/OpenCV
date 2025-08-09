import cv2
import numpy as np

src = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_COLOR)
scale_percent = 200
width_img = int(src.shape[1] * scale_percent / 100)
height_img = int(src.shape[0] * scale_percent / 100)
dsize = (width_img, height_img)
src = cv2.resize(src, dsize, interpolation=cv2.INTER_LANCZOS4)

green_channel = src[:, :, 1]
green_img = np.zeros(src.shape)
green_img[:, :, 1] = green_channel
cv2.imwrite("D:/OpenCV/img/green_channel.jpg", green_img)
cv2.imshow("Result", green_img)
cv2.waitKey(0)
cv2.destroyAllWindows()