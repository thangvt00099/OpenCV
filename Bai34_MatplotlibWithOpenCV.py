import matplotlib.pyplot as plt
import cv2

# OpenCV đọc ảnh ở định dạng BGR
# Matplotlib đọc ảnh ở định dạng RGB

img = cv2.imread('D:/OpenCV/img/input_image.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('image', img)

# Convert ảnh BGR => RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show img by matplotlib
plt.imshow(img)
# plt.xticks([]) # disable trục x
# plt.yticks([]) # disable trục y
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()