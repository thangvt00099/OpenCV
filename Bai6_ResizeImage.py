import cv2
"""
Syntax resize img:
    cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    Trong đó:
        - src: source ảnh
        - dsize: kích thước mong muốn của ảnh đầu ra => tuple
        - fx: scale theo trục x hoặc trục hoành
        - fy: scale theo trục y hoặc trục tung
        interpolation:
            INTER_NEAREST
            INTER_LINEAR
            INTER_AREA
            INTER_CUBIC
            INTER_LANCZOS4
"""
src = cv2.imread('D:/OpenCV/img/image1.png', cv2.IMREAD_UNCHANGED)
print("Tuple size: ", src.shape)

scale_percent = 50
width_img = int(src.shape[1] * scale_percent / 100)
heigth_img = int(src.shape[0] * scale_percent / 100)

dsize = (width_img, heigth_img)

# Resize theo tỉ lệ ảnh
output = cv2.resize(src, dsize)
print("Size of image after resize 50%: ", output.shape)
cv2.imwrite('D:/OpenCV/img/output1.png', output)


# Resize theo trục x
width_img_2 = 300
dsize2 = (width_img_2, src.shape[0])
output2 = cv2.resize(src, dsize2, interpolation=cv2.INTER_LANCZOS4)
cv2.imwrite('D:/OpenCV/img/output2.png', output2)

# Resize theo trục y
height_img_2 = 300
dsize3 = (src.shape[1], height_img_2)
output3 = cv2.resize(src, dsize3, interpolation=cv2.INTER_LANCZOS4)
cv2.imwrite('D:/OpenCV/img/output3.png', output3)

