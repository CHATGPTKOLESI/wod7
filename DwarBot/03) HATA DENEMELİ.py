import pyautogui
import time
import os

# Hedef görselin dosya yolu (aynı dizinde olduğunu varsayıyoruz)
image_path = 'rabid2.png'
alert_image_path = 'close.png'

# Döngü içinde sürekli çalışacak
while True:
    try:
        # İlk görseli ekranda ara
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

        # Eğer görsel bulunduysa
        if location is not None:
            # Görsele tıkla
            pyautogui.doubleClick(location)
            print("Görsele tıklandı:", location)

            # 5 saniye bekle
            time.sleep(3.5)

            # "W" tuşuna bas
            pyautogui.press('w')
            print("W tuşuna basıldı.")

            # 3 saniye bekle
            time.sleep(2.5)

            # "Alt+A" tuşuna bas
            pyautogui.hotkey('alt', 'a')
            print("Alt+A tuşuna basıldı.")

            # Uyarı mesajını kontrol et
            alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.6)
            if alert_location is not None:
                # Uyarı mesajına tıkla
                pyautogui.click(alert_location)
                print(f"Uyarı mesajına tıklandı: {alert_location}")

                # Uyarı mesajından sonra döngüye geri dön

                continue
                # Bu satır ile döngünün başına geri dön



    except Exception as e:
        print("Bir hata oluştu:", e)
        # Hata durumunda döngüye devam et
        time.sleep(0.1)  # Hata sonrası bir süre bekle