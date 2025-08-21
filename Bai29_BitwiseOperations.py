import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"({x}, {y})")
        strXY = f"[{x}, {y}]"
        cv2.putText(
            img2,
            strXY,
            (x, y),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 0),
            2
        )
        cv2.imshow('image_2', img2)

img1 = cv2.imread("D:/OpenCV/img/image2.png", cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_UNCHANGED)
bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img2, img1)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("image_1", img1)
cv2.imshow("image_2", img2)
# cv2.imshow("bitAnd", bitAnd)
# cv2.imshow("bitOr", bitOr)
# cv2.imshow("bitXor", bitXor)
cv2.imshow("bitNot", bitNot1)
# cv2.imshow("bitNot", bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()