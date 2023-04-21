import cv2
# import time
# from json_generate import send_data
from structure import *
import requests

# led_left["seg"][0]["col"] = [[12, 34, 56]]
# print(led_left)

# for x in led_left["seg"]:
#     for y in x:
#         print(y, x[y])


DEBUG = True
LEFT = False
TOP = False
RIGHT = False
BOTTON = False

def start():
    cap = cv2.VideoCapture('full.mp4')
    # cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video stream or file")
    else:
        while cap.isOpened():

            # fps = int(cap.get(5))
            # frame_count = cap.get(7)
            # print("Frame Rate : ", fps, "frames per second"," Frame count : ", frame_count)

            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (1280, 720))
                h, w = frame.shape[:2]

                # time.sleep(.07)

                left = 40
                top = 55
                step = 120
                # circles left
                if LEFT:
                    margin_top = top
                    margin_left = left
                    val = 0
                    for i in range(margin_top, 700, step):
                        val += 1
                        # altura x largura
                        (b, g, r) = (frame[i, margin_left])


                        led_left["seg"][0]["col"] = [[r, g, b]]
                        print(led_left)
                        # requests.post(url="http://192.168.15.7/json/state", data=led_left)
                        # json_leds = send_data(5, 11, (b, g, r))


                        # largura x altura
                        if DEBUG:
                            frame = cv2.circle(frame, (margin_left, i), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                            frame = cv2.circle(frame, (margin_left, i), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)
                            # frame = cv2.line(frame, (margin_left + 25, itens_left), (280, itens_left), (0, 0, 0), thickness=25)
                            # frame = cv2.putText(frame, f'{b}, {g}, {r}', (margin_left + 20, itens_left + 10), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(int(b), int(g), int(r)))
                # print(val)

                if TOP:
                    # circles top
                    margin_top = top
                    margin_left = left
                    for i in range(margin_left, 1250, step):
                        (b, g, r) = (frame[margin_left, i])
                        if DEBUG:
                            frame = cv2.circle(frame, (i, margin_top), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                            frame = cv2.circle(frame, (i, margin_top), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)

                if RIGHT:
                    # circles rigth
                    margin_top = top
                    margin_right = w - left
                    for i in range(margin_top, 700, step):
                        (b, g, r) = (frame[i, margin_right])
                        if DEBUG:
                            frame = cv2.circle(frame, (margin_right, i), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                            frame = cv2.circle(frame, (margin_right, i), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)

                if BOTTON:
                    # circles botton
                    margin_top = h - top
                    margin_left = left
                    for i in range(margin_left, 1250, step):
                        (b, g, r) = (frame[margin_top, i])
                        if DEBUG:
                            frame = cv2.circle(frame, (i, margin_top), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                            frame = cv2.circle(frame, (i, margin_top), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)


                cv2.imshow('Frame', frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                cap.release()
                start()

cv2.destroyAllWindows()



if __name__ == "__main__":
    start()


