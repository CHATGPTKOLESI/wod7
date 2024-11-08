import pyautogui
import time

# Görsellerin dosya yolları
image_path = 'rabid2.png'  # Rabid görseli
attack_image_path = 'saldiri.png'  # Saldırı görseli

# Avlan ve full ekrana geçiş için kısa bir bekleme
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
            pyautogui.hotkey('f11')  # F11 tuşuna bas
            print("Tam Ekran Moduna Geçildi.")

            pyautogui.hotkey('ctrl', 'u')  # Ctrl+U tuşuna bas
            print("Ctrl+U tuşuna basıldı.")

            initial_setup_done = True  # Kurulum tamamlandı

        # Her döngüden önce 1.5 saniye bekle
        time.sleep(1.5)
        # Hedef koordinatlar
        x = 951
        y = 648
        # Fareyi belirtilen koordinatlara taşı ve sol tıklama yap
        pyautogui.moveTo(x, y)  # Fareyi x=951, y=648 koordinatına taşı
        pyautogui.click()  # Sol tıklama yap. Scroll Yukarı Aşağıda Ekran Ortasından Çıktığı İçin Fare ile Tam Ortaya 1 Defa Tıklıyoruz.

        print(f"{x}, {y} koordinatına bir defa sol tıklama yapıldı.")

        # Yukarı scroll işlemi
        print("İlk yukarı scroll işlemi başlıyor...")
        for _ in range(8):  # 200 birim yukarı 8 defa scroll
            pyautogui.scroll(200)
        print("Yukarı scroll işlemi tamamlandı.")

        # Yukarı scroll işleminden sonra bekle
        time.sleep(1)

        # Rabid görselini ara
        rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

        if rabid_location is not None:
            pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
            print(f"Rabid'e tıklandı: {rabid_location}")

            # Tuş kombinasyonlarını sırasıyla uygula
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
            print("Ctrl+R tuşuna basıldı.")
            time.sleep(0.3)
            pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
            print("Alt+A tuşuna basıldı.")
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'u')  # Ctrl+U tuşuna bas
            print("Ctrl+U tuşuna basıldı.")

            time.sleep(2)

            # Saldırı görselini kontrol et
            attack_location = pyautogui.locateCenterOnScreen(attack_image_path, confidence=0.7)

            if attack_location is not None:
                # Saldırı görseli bulunduğunda W ve Alt+A tuşlarına basma işlemleri
                print("Saldırı görseli bulundu!")
                time.sleep(0.4)  # 0.1 saniye bekle
                pyautogui.press('w')  # W tuşuna bas
                print("W tuşuna basıldı.")

                time.sleep(1.3)  # 1 saniye bekle
                pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
                print("Alt+A tuşuna basıldı.")


                # 1.5 saniye bekle.
                time.sleep(1.5)
                # Hedef koordinatlar
                x = 951
                y = 648
                # Fareyi belirtilen koordinatlara taşı ve sol tıklama yap
                pyautogui.moveTo(x, y)  # Fareyi x=951, y=648 koordinatına taşı
                pyautogui.click()  # Sol tıklama yap. Scroll Yukarı Aşağıda Ekran Ortasından Çıktığı İçin Fare ile Tam Ortaya 1 Defa Tıklıyoruz.

                print(f"{x}, {y} koordinatına bir defa sol tıklama yapıldı.")
                # Aşağı scroll işlemi
                print("Aşağı scroll işlemi başlıyor...")
                for _ in range(8):  # 200 birim aşağı 8 defa scroll
                    pyautogui.scroll(-200)
                print("Aşağı scroll işlemi tamamlandı.")

                # Scroll işlemi sonrası Rabid görselini tekrar ara
                time.sleep(1)

                # Rabid görselini yeniden ara
                rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
                if rabid_location is not None:
                    pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
                    print(f"Rabid'e tekrar tıklandı: {rabid_location}")

                    # Tuş kombinasyonlarını sırasıyla uygula
                    time.sleep(0.3)
                    pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
                    print("Ctrl+R tuşuna basıldı.")
                    time.sleep(0.3)
                    pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
                    print("Alt+A tuşuna basıldı.")
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'u')  # Ctrl+U tuşuna bas
                    print("Ctrl+U tuşuna basıldı.")

                    time.sleep(2)

                    # Saldırı görselini kontrol et
                    attack_location = pyautogui.locateCenterOnScreen(attack_image_path, confidence=0.7)

                    if attack_location is not None:
                        # Saldırı görseli bulunduğunda W ve Alt+A tuşlarına basma işlemleri
                        print("Saldırı görseli bulundu!")
                        time.sleep(0.5)  # 2 saniye bekle
                        pyautogui.press('w')  # W tuşuna bas
                        print("W tuşuna basıldı.")

                        time.sleep(1.3)  # 1 saniye bekle
                        pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
                        print("Alt+A tuşuna basıldı.")


            else:
                # Saldırı görseli bulunamadığında rabid görseline tekrar tıkla
                print("Saldırı görseli bulunamadı, Rabid'e tekrar tıklanacak.")
                pyautogui.doubleClick(rabid_location)  # Rabid görseline tekrar tıkla
                print(f"Rabid'e tekrar tıklandı: {rabid_location}")

        else:
            print("Rabid görseli bulunamadı.")

    except Exception as e:
        print(f"Tıklama işlemi sırasında hata oluştu: {e}")
        time.sleep(0.1)  # Hata durumunda bir süre bekle
