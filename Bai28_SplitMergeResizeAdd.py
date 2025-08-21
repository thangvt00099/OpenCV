import cv2
import numpy as np
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"[{x}, {y}]")
        strXY = f"[{x}, {y}]"
        cv2.putText(
            img,
            strXY,
            (x, y),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 0),
            2
        )
        cv2.imshow('image', img)

if __name__ == '__main__':
    # img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.imread("D:\OpenCV\img\cr7.jpg", cv2.IMREAD_UNCHANGED)

    # Resize Image
    scale_percent = 25
    width_img = int(img.shape[1] * scale_percent / 100)
    height_img = int(img.shape[0] * scale_percent / 100)
    img = cv2.resize(img, (width_img, height_img))  

    # Cut and assign ball from image
    # img[y2-y1, x2-x1]
    # y2 - y1, x2 - x1 not changed
    ball = img[621:702, 200:291]
    img[566:647, 100:191] = ball

    # Show Image
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
