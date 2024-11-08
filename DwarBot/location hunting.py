import pyautogui
import time

# Hedef görsellerin dosya yolları (her biri manuel olarak belirtiliyor)
first_image_path = 'location.png'  # İlk görsel
second_image_path = 'hunt.png'  # İkinci görsel

# Döngü sayısı
repeat_count = 4

for _ in range(repeat_count):
    # İlk görseli ekranda ara
    first_location = pyautogui.locateCenterOnScreen(first_image_path, confidence=0.5)
    if first_location is not None:
        # Eğer ilk görsel bulunduysa, ona tıkla
        pyautogui.doubleClick(first_location)
        print(f"İlk görsele tıklandı: {first_image_path} - Konum: {first_location}")
    else:
        print(f"İlk görsel bulunamadı: {first_image_path}")

    # 2 saniye bekle
    time.sleep(2)

    # İkinci görseli ekranda ara
    second_location = pyautogui.locateCenterOnScreen(second_image_path, confidence=0.5)
    if second_location is not None:
        # Eğer ikinci görsel bulunduysa, ona tıkla
        pyautogui.doubleClick(second_location)
        print(f"İkinci görsele tıklandı: {second_image_path} - Konum: {second_location}")
    else:
        print(f"İkinci görsel bulunamadı: {second_image_path}")

    # 2 saniye bekle
    time.sleep(2)

print("Döngü tamamlandı.")