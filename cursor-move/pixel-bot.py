from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import ctypes

time.sleep(2)


def click(x, y):
    try:
        win32api.SetCursorPos((x, y))
        time.sleep(0.1)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)

        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.5)

    except:
        print("Error: click()", x, y)
        raise

# Color of center: (255, 219, 195)
# 500, 0, 1200, 800

click(500, 0)

while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(500, 0, 1200, 800))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if b == 66 and r == 231 and g == 33:
                flag = 1
                print("Found at: ", x, y)
                click(x+510, y+10)
                time.sleep(0.5)
                break

        if flag == 1:
            break
