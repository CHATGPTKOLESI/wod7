import pyautogui
import time
import os

# Hedef görselin dosya yolu (aynı dizinde olduğunu varsayıyoruz)
image_path = 'rabid2.png'

# Döngü içinde sürekli çalışacak
while True:
    # İlk görseli ekranda ara
    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

    # Eğer görsel bulunduysa
    if location is not None:
        # Görsele tıkla
        pyautogui.doubleClick(location)
        print("Görsele tıklandı:", location)

        # 5 saniye bekle
        time.sleep(4)

        # "W" tuşuna bas
        pyautogui.press('w')
        print("W tuşuna basıldı.")

        # 3 saniye bekle
        time.sleep(3)

        # "Alt+A" tuşuna bas
        pyautogui.hotkey('alt', 'a')
        print("Alt+A tuşuna basıldı.")
    else:
        print("Görsel bulunamadı.")

    # Döngü sonunda küçük bir bekleme eklemek istersen
    time.sleep(1)  # 1 saniye bekleyip döngüye devam et