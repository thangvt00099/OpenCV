import numpy as np
import cv2

def nothing(x):
    print(x)

cv2.namedWindow('Image')

cv2.createTrackbar('CP', 'Image', 10, 400, nothing)

switch = 'color/gray'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

while (1):
    img = cv2.imread('D:/OpenCV/img/image1.png', cv2.IMREAD_COLOR)
    k = cv2.waitKey(1) & 0xFF
    pos = cv2.getTrackbarPos('CP', 'Image')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(
        img,
        str(pos),
        (50, 150),
        font,
        4,
        (0, 0, 255)
    )
    if k == 27:
        break

    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.imshow('Image', img)
 
cv2.destroyAllWindows()