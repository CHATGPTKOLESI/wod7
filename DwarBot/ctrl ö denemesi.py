import pyautogui
import time

# Hedef görselin dosya yolu
image_path = 'rabid2.png'  # Rabid görseli
alert_image_path = 'notrecovered.PNG'  # Uyarı görseli
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı

# Kod açılınca 1.5 sn geç başlat
time.sleep(1.5)

# İlk geçiş işlemleri için bir kontrol değişkeni
initial_setup_done = False
loop_counter = 0  # Döngü sayacı

# Sürekli döngü
while True:
    try:
        # İlk kurulum yapılmadıysa işlemleri gerçekleştir
        if not initial_setup_done:
            pyautogui.hotkey('alt', 'a')  # Alt+Tab tuşuna bas
            print("Avlan Ekranına Geçildi.")
            time.sleep(1.5)

            pyautogui.press('f11')  # F11 tuşuna bas
            print("Tam ekran yapıldı.")
            time.sleep(1.5)

            pyautogui.hotkey('ctrl', 'u')  # Ctrl + u tuşlarına bas
            print("Ctrl+U tuşlarına basıldı.")
            time.sleep(1.5)

            initial_setup_done = True  # Kurulum tamamlandı
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        break  # Hata durumunda döngüden çık