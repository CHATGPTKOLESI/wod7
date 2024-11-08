import pyautogui
import mouse  # Fare olaylarını dinlemek için
import time

print("Koordinatları kaydetmek için ekranda istediğiniz yere tıklayın. 'q' tuşuna basarak çıkış yapabilirsiniz.")

coordinates = []

def kaydet_koordinat(x, y):
    coordinates.append((x, y))
    print(f"Koordinat kaydedildi: {x}, {y}")
    if len(coordinates) == 2:
        print(f"İlk koordinat: {coordinates[0]}")
        print(f"İkinci koordinat: {coordinates[1]}")
        mouse.unhook_all()  # Tüm fare dinleyicilerini kapatır
        exit()

def kayit_olayi():
    x, y = pyautogui.position()
    kaydet_koordinat(x, y)

# Fare sol tıklamasını dinle
mouse.on_click(kayit_olayi)

# Programın sürekli çalışmasını sağla
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program durduruldu.")