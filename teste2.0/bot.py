# https://www.classicgame.com/game/Whack+a+Mole

# imports
from re import template
import cv2
import pyautogui
from time import sleep
import time
import os
import win32api
import win32con
# No cooldown time
pyautogui.PAUSE = 0

# template and dimensions

template = cv2.imread("imgs/image-left.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
template_w, template_h = template_gray.shape[::-1]

# game window dimensions
x, y, w, h = 0, 0, 1100, 679
sleep(3)

# main

while True:

    # screenshot
    pyautogui.screenshot("imgs/image1.png", (x, y, w, h))
    image = cv2.imread("imgs/image1.png")

    while True:

        # show what the computer sees
        image_mini = cv2.resize(
            src=image,
            dsize=(450, 350)  # must be integer, not float
        )
        cv2.imshow("vision", image_mini)
        cv2.waitKey(10)

        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(
            image=image_gray,
            templ=template_gray,
            method=cv2.TM_CCOEFF_NORMED
        )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # threshold
        if max_val >= 0.6:
            print('achou')

            win32api.SetCursorPos((max_loc[0], max_loc[1]))
            time.sleep(0.1)

            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(0.1)

            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.5)

            image = cv2.rectangle(
                img=image,
                pt1=max_loc,
                pt2=(
                    max_loc[0] + template_w,  # = pt2 x
                    max_loc[1] + template_h  # = pt2 y
                ),
                color=(0, 0, 255),
                thickness=-1  # fill the rectangle
            )

        else:
            break
