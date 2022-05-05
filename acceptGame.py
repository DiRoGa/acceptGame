import imagesearch as imagesearch
import pyautogui as pyautogui
from python_imagesearch.imagesearch import *

# Search for the github logo on the whole screen
# note that the search only works on your primary screen.

# This is intended to be used as examples to be copy pasted, do not run the whole file at once

accept = imagesearch_loop("C:/Users/perom/PycharmProjects/EssenceCalculator/images/accept.jpg", 0.5)

if accept[0] != -1:
    click_image("C:/Users/perom/PycharmProjects/EssenceCalculator/images/accept.jpg", accept, "left", 0.2)