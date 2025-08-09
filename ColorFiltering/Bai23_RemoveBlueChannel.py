import cv2
import numpy as np

src = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_UNCHANGED)
scale_percent = 200
width_img = int(src.shape[1] * scale_percent / 100)
height_img = int(src.shape[0] * scale_percent / 100)
dsize = (width_img, height_img)
src = cv2.resize(src, dsize, interpolation=cv2.INTER_LANCZOS4)

src[:, :, 0] = np.zeros([src.shape[0], src.shape[1]])
cv2.imwrite("D:/OpenCV/img/delete-blue-channel.png", src)
cv2.imshow("Result", src)
cv2.waitKey(0)
cv2.destroyAllWindows()