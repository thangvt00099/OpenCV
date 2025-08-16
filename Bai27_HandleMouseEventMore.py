import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        w, h = 50, 50
        top_left = (x - w // 2, y - h // 2)
        bottom_right = (x + w // 2, y + h // 2)
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 5)
        center_rectangle = (x, y)
        points.append(center_rectangle)
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 255, 0), 5)
        cv2.imshow('image', img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 20, (0, 255, 0), 5)
        center_circle = (x, y)
        points.append(center_circle)
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)
    


if __name__ == '__main__':
    # img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.imread("D:/OpenCV/img/image2.png", cv2.IMREAD_UNCHANGED)
    cv2.imshow('image', img)
    points = []
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()