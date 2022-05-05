import imagesearch as imagesearch
import pyautogui as pyautogui
from python_imagesearch.imagesearch import *
import urllib
# Search for the github logo on the whole screen
# note that the search only works on your primary screen.

# This is intended to be used as examples to be copy pasted, do not run the whole file at once
image = urllib.urlretrieve("https://imgur.com/a/x4CUiXY")
accept = imagesearch_loop(image, 0.5)

if accept[0] != -1:
    click_image(image, accept, "left", 0.2)