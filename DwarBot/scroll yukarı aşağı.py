import pyautogui
import time

# 2 saniye beklemeden önce bir süre için başlangıç
time.sleep(2)

# 8 defa yukarı scroll yap
for _ in range(8):
    pyautogui.scroll(200)

# Yukarı scroll işlemlerinden sonra 2 saniye bekle
time.sleep(2)

# 18 defa aşağı scroll yap
for _ in range(18):
    pyautogui.scroll(-200)
