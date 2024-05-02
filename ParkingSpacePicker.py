import cv2
import pickle

try:
    with open("CarParkPos", "rb") as f:
        pos_list = pickle.load(f)
except:
    pos_list = []

width, height = 107, 48

def mouse_click(event, x, y, *args):
    if event == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for idx, pos in enumerate(pos_list):
            x1, y1 = pos
            if x1 < x < x+width and y1 < y < y1+height:
                pos_list.pop(idx)
                
    with open("CarParkPos", "wb") as f:
        pickle.dump(pos_list, f)
            

while True:
    img = cv2.imread("carParkImg.png")
    for pos in pos_list:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    cv2.imshow("Car Parking Slot", img)
    cv2.setMouseCallback("Car Parking Slot", mouse_click)
    cv2.waitKey(1)