import cv2

"""
putText(
    image,
    text,
    position,
    font-family,
    font-size,
    font-color,
    font-stroke - độ dày chữ
)
"""
image = cv2.imread('D:/OpenCV/img/image1.png', cv2.IMREAD_UNCHANGED)
position = (10, 50)
cv2.putText(
    image,
    "Python Example OpenCV",
    position,
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (255, 0, 123, 255),
    2
)
cv2.imwrite('D:/OpenCV/img/write_text.png', image)
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()