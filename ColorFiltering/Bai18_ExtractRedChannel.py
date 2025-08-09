import cv2
import numpy as np
src = cv2.imread("D:/OpenCV/img/input_image.png", cv2.IMREAD_UNCHANGED)
scale_percent = 200
width_img = int(src.shape[1] * scale_percent / 100)
height_img = int(src.shape[0] * scale_percent / 100)
dsize = (width_img, height_img)
src = cv2.resize(src, dsize, interpolation=cv2.INTER_LANCZOS4)

red_channel = src[:, :, 2]
red_img = np.zeros(src.shape)
red_img[:, :, 2] = red_channel
cv2.imwrite("D:/OpenCV/img/red_channel.png", red_img)
cv2.imshow("Result", red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()