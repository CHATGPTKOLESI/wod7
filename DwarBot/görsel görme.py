import pyautogui
import time

# Kontrol edilecek görselin adı
check_image_path = 'victory.png'

# Victory görselini kontrol et
check_location = pyautogui.locateOnScreen(check_image_path, confidence=0.75)
if check_location is not None:
    print("Victory görseli bulundu!")
    time.sleep(1)  # 1 saniye bekle
    pyautogui.hotkey('alt', 'a')  # Victory bulunduğunda Alt+A tuşuna bas
    print("Alt+A tuşuna basıldı.")  # Durumu yazdır
else:
    print("Victory görseli bulunamadı.")
