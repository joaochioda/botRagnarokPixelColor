import cv2 as cv
import numpy as np
import os
from time import time
from time import sleep
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter
import win32api
import win32con

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture(
    'RagnaTales | Gepard Shield 3.0 (^-_-^)')
# initialize the Vision class
vision_limestone = Vision('black-mystic2.png')
# initialize the trackbar window
vision_limestone.init_control_gui()

# limestone HSV filter
hsv_filter = HsvFilter(0, 124, 0, 179, 255, 255, 0, 0, 0, 0)

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # pre-process the image
    processed_image = vision_limestone.apply_hsv_filter(screenshot, hsv_filter)

    # do object detection
    rectangles = vision_limestone.find(processed_image, 0.4)

    # draw the detection results onto the original image
    # output_image = vision_limestone.draw_rectangles(screenshot, rectangles)

    # display the processed image
    # cv.imshow('Processed', processed_image)
    # cv.imshow('Matches', output_image)

    # debug the loop rate
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
