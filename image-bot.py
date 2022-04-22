import cv2
import mss
import numpy as np
import time
import os
import win32api
import win32con

dirname = os.path.dirname(__file__)
animal_path = os.path.join(dirname, 'presente')

SCT = mss.mss()


def check_animal(animal):
    template_gray = cv2.cvtColor(animal, cv2.COLOR_RGB2GRAY)
    image_gray = cv2.cvtColor(main_screen(height=800), cv2.COLOR_RGB2GRAY)
    result_animal = cv2.matchTemplate(
        image=image_gray, templ=template_gray, method=cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc_animal = cv2.minMaxLoc(result_animal)
    # print(max_val)
    if max_val > .75:
        print(max_val)
        return max_loc_animal
    else:
        return None


def Put_Away(animal_name, animals):
    keep_testing = True
    find = False
    while keep_testing:
        for animal in animals:
            animal_loc = check_animal(animal)
            if animal_loc is not None:
                print(animal_loc[0] + left_start+20)
                print(animal_loc[1] + top_start+20)

                win32api.SetCursorPos((animal_loc[0], animal_loc[1]))
                time.sleep(0.1)

                win32api.keybd_event(win32con.VK_F1, 0, 0, 0)
                time.sleep(0.1)
                win32api.keybd_event(
                    win32con.VK_F1, 0, win32con.KEYEVENTF_KEYUP, 0)

                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

                time.sleep(0.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

                time.sleep(2)

                return True
            else:
                keep_testing = False
    print('aperta f2')
    win32api.keybd_event(win32con.VK_F2, 0, 0, 0)
    win32api.keybd_event(
        win32con.VK_F2, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)

    return False


def main_screen(height=800):
    scr = SCT.grab({
        'left': left_start,
        'top': top_start,
        'width': 1100,
        'height': height
    })
    img = np.array(scr)
    return cv2.cvtColor(img, cv2.IMREAD_COLOR)


if __name__ == "__main__":
    while True:
        print("Starting in 2....")
        time.sleep(2)
        left_start = 0
        top_start = 0

        color = main_screen()

        pigs = [
            cv2.imread(os.path.join(animal_path, 'image-left.png'),
                       cv2.IMREAD_UNCHANGED),
            cv2.imread(os.path.join(animal_path, 'image-right.png'),
                       cv2.IMREAD_UNCHANGED),
            cv2.imread(os.path.join(animal_path, 'back-left.png'),
                       cv2.IMREAD_UNCHANGED),
            cv2.imread(os.path.join(animal_path, 'back-right.png'),
                       cv2.IMREAD_UNCHANGED),
        ]

        # wait = 4
        replay_shown = None
        while replay_shown is None:
            while True:
                Put_Away("Monster", pigs)
                time.sleep(0.1)
            # Check Cow
