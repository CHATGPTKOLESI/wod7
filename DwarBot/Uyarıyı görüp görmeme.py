import pyautogui
import time

# Uyarı mesajı için kontrol edilecek görselin dosya yolu
alert_image_path = 'close.png'  # Uyarı görselinin dosya yolu

# Kontrol süresi (saniye cinsinden)
check_duration = 10  # 10 saniye boyunca kontrol et
start_time = time.time()  # Başlangıç zamanını al

# Süre bitene kadar döngüde kontrol yap
while time.time() - start_time < check_duration:
    # Uyarı görselini ekranda ara
    alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.6)

    if alert_location is not None:
        print("Uyarı gördüm!")  # Uyarı bulunduğunda mesajı yazdır
        pyautogui.rightClick(alert_location)  # Uyarı üzerine bir kez sağ tıkla
        print("Uyarıya sağ tıklandı.")  # Sağ tıklama yapıldığını yazdır
        break  # Uyarı bulunduktan sonra döngüden çık
    else:
        print("Hata")  # Uyarı bulunamadığında hata mesajı yazdır
        time.sleep(1)  # 1 saniye bekle ve tekrar dene
