from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import ctypes



class MoveClick:

    def click(x, y):
        try:
            print("Clicked at: " + str(x) + ", " + str(y))
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

