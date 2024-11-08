import pyautogui
import time

# Hedef görselin dosya yolu
image_path = 'rabid2.png'  # Rabid görseli
alert_image_path = 'notrecovered.PNG'  # Uyarı görseli

# Kod açılınca 1.5 sn geç başlat
time.sleep(1.5)

# İlk geçiş işlemleri için bir kontrol değişkeni
initial_setup_done = False
last_alert_check_time = time.time()  # En son alert kontrolü yapılan zaman

# Sürekli döngü
while True:
    try:
        # İlk kurulum yapılmadıysa işlemleri gerçekleştir
        if not initial_setup_done:
            pyautogui.hotkey('alt', 'a')  # Alt+Tab tuşuna bas
            print("Avlan Ekranına Geçildi.")
            time.sleep(1.5)
            initial_setup_done = True  # Kurulum tamamlandı

        # Rabid görselini ara
        rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

        if rabid_location is not None:
            pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
            print(f"Rabid'e tıklandı: {rabid_location}")

            # 15 saniyede bir alert görselini kontrol et
            current_time = time.time()
            if current_time - last_alert_check_time >= 15:
                alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.8)
                last_alert_check_time = current_time  # Zamanı güncelle

                if alert_location is not None:
                    pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
                    print("Ctrl+R tuşuna basıldı.")
                    time.sleep(0.5)  # Bekle
                    pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
                    print("Alt+A tuşuna basıldı.")


            time.sleep(4)  # Bekle
            pyautogui.press('w')  # W tuşuna bas
            print("W tuşuna basıldı.")

            time.sleep(1)  # Bekle
            pyautogui.hotkey('alt', 'a')  # Alt+Tab tuşuna bas
            print("Alt+A tuşuna basıldı.")

    except Exception as e:
        print(f"Tıklama işlemi sırasında hata oluştu: {e}")
        time.sleep(2)
