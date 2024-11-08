import pyautogui
import time

# Hedef görselin dosya yolu
image_path = 'rabid2.png'  # Rabid görseli

# Avlana ve full ekrana geçiş
time.sleep(2)

# İlk geçiş işlemleri için bir kontrol değişkeni
initial_setup_done = False

# Sürekli döngü
while True:
    try:
        # İlk kurulum yapılmadıysa işlemleri gerçekleştir
        if not initial_setup_done:
            pyautogui.hotkey('alt', 'a')  # Alt+Tab tuşuna bas
            print("Avlan Ekranına Geçildi.")
            time.sleep(1.5)
            initial_setup_done = True  # Kurulum tamamlandı

        # Her döngüden önce 0.5 saniye bekle
        time.sleep(0.5)


        # Rabid görselini ara
        rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

        if rabid_location is not None:
            pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
            print(f"Rabid'e tıklandı: {rabid_location}")

            time.sleep(3)  # 3 saniye bekle
            pyautogui.press('w')  # W tuşuna bas
            print("W tuşuna basıldı.")

            time.sleep(1)  # 1 saniye bekle
            pyautogui.hotkey('alt', 'a')  # Alt+Tab tuşuna bas
            print("Alt+a tuşuna basıldı.")

            time.sleep(1.8)  # 2 saniye bekle

            # Rabid görseli ile ilgili işlemler tamamlandıktan sonra scroll yap
            print("Scroll işlemi başlıyor...")
            for _ in range(8):  # 200 birim yukarı 8 defa scroll
                pyautogui.scroll(200)
            # Rabid görselini tekrar ara
            rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
            if rabid_location is not None:
                pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
                print(f"Rabid'e tekrar tıklandı: {rabid_location}")

                time.sleep(3)  # 3 saniye bekle
                pyautogui.press('w')  # W tuşuna bas
                print("W tuşuna basıldı.")

                time.sleep(1)  # 1 saniye bekle
                pyautogui.hotkey('alt', 'a')  # Alt+Tab tuşuna bas
                print("Alt+a tuşuna basıldı.")

            print("Yukarı scroll işlemleri tamamlandı.")

            time.sleep(1.8)

            for _ in range(8):  # 200 birim aşağı 16 defa scroll
                pyautogui.scroll(-200)
            # Rabid görselini tekrar ara
            rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
            if rabid_location is not None:
                pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
                print(f"Rabid'e tekrar tıklandı: {rabid_location}")

                time.sleep(3)  # 3 saniye bekle
                pyautogui.press('w')  # W tuşuna bas
                print("W tuşuna basıldı.")

                time.sleep(1)  # 1 saniye bekle
                pyautogui.hotkey('alt', 'a')  # Alt+Tab tuşuna bas
                print("Alt+a tuşuna basıldı.")

            print("Aşağı scroll işlemleri tamamlandı.")

        else:
            print("Rabid görseli bulunamadı.")

    except Exception as e:
        print(f"Tıklama işlemi sırasında hata oluştu: {e}")
        time.sleep(0.1)  # Hata durumunda bir süre bekle
