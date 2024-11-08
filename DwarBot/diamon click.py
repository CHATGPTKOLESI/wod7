import pyautogui
import time
import os

# Görsel dosyasının doğru dizinde olduğunu kontrol et
diamond_image_path = 'diamond.png'

time.sleep(1.5)

# Görseli sürekli aramak için bir döngü başlatıyoruz
while True:
    try:
        pyautogui.moveTo(949, 271)
        pyautogui.click()  # Sol tıklama yap

        time.sleep(0.8)

        # "diamond.png" görselini ekranda arıyoruz
        diamond_location = pyautogui.locateOnScreen(diamond_image_path, confidence=0.6)

        # Görsel bulunduysa ctrl+w tuşlarına bas
        if diamond_location:
            pyautogui.hotkey('ctrl', 'w')
            print("diamond.png bulundu ve ctrl+w tuşuna basıldı.")
            break  # Görsel bulunduğunda döngüyü sonlandırıyoruz

    except Exception as e:
        print(f"Diamond bulunamadı.: {e}")
        # Hata olursa döngü devam eder
        continue
