# This script locates the image stickman.png in the region we give it and tell you if it can see it

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

while 1:
    if pyautogui.locateOnScreen('redSquare.bmp', region=(500, 0, 1200, 800), grayscale=True, confidence=1) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
