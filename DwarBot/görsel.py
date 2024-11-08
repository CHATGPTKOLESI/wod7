from pyautogui import *
import pyautogui
import time

while 1:
    if pyautogui.locateOnScreen('ali.png') !=None:
        print("ali burda")
        time.sleep(1)

    else:
        print("ali yok")
        time.sleep(1)
