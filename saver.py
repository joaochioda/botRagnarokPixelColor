import pyautogui
import time

time.sleep(3)
im1 = pyautogui.screenshot(region=(500, 0, 1200, 800))
im1.save(r"./savedimage.png")
