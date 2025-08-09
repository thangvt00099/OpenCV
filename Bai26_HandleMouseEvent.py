import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # Click chuột trái
        print(f"({x}, {y})")
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
        cv2.imshow('Image', img)
    
    if event == cv2.EVENT_RBUTTONDOWN: # Click chuột phải
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strXY = f"({blue}, {green}, {red})"
        cv2.putText(
            img,
            strXY,
            (x, y),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255, 255, 0),
            2
        )
        cv2.imshow('Image', img)

if __name__ == '__main__':  
    # img = np.zeros([512, 512, 3], np.uint8)
    img = cv2.imread("D:/OpenCV/img/image1.png", cv2.IMREAD_UNCHANGED)
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()