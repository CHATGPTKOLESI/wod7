import pyautogui
import time

# Hedef görselin dosya yolu (aynı dizinde olduğunu varsayıyoruz)
image_path = 'nepherto.png'

# Döngü içinde sürekli çalışacak
while True:
    # İlk görseli ekranda ara
    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

    # Eğer görsel bulunduysa
    if location is not None:
        # Görsele tıkla
        pyautogui.doubleClick(location)
        print("Görsele tıklandı:", location)

        # 3.5 saniye bekle
        time.sleep(3.5)

        # Sırasıyla tuşlara bas
        keys = ['k', 'e', 'tab', 't', '4']
        for key in keys:
            pyautogui.press(key)
            print(f"{key.upper()} tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

    else:
        print("Görsel bulunamadı.")

    # Döngü sonunda küçük bir bekleme eklemek isterseniz
    time.sleep(1)  # 1 saniye bekleyip döngüye devam et