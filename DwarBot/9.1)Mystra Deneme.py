import pyautogui
import time
import random

# Görsellerin dosya yolları
image_paths = ['whad2.png', 'genie2.png', 'flower2.png']  # WhadWorm-OutcastGenie-Flower
attack_image_path = 'saldiri.png'  # Saldırı görseli
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı

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

        # Rastgele bir görseli ara
        for image_path in image_paths:
            target_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
            if target_location is not None:
                # Y koordinatına 10 birim ekle
                adjusted_y = target_location.y - 8
                # Yeni koordinatlara çift tıkla
                pyautogui.doubleClick(target_location.x, adjusted_y)
                print(f"{image_path} görseline tıklandı: ({target_location.x}, {adjusted_y})")
                break  # Bir görsel bulduktan sonra döngüden çık

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

        time.sleep(3)

        # Saldırı görselini kontrol et
        attack_location = pyautogui.locateCenterOnScreen(attack_image_path, confidence=0.7)

        if attack_location is not None:
            # Saldırı görseli bulunduğunda e - tab - 2 - 3 basıp sonra 4ve V spamlayacak. Victory ekranını görene kadaar.
            time.sleep(0.3)
            # "e" tuşuna bas
            pyautogui.press('e')
            print("e tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

            # "tab" tuşuna bas
            pyautogui.press('tab')
            print("tab tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

            # "t" tuşuna bas
            pyautogui.press('t')
            print("t tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

            # "3" tuşuna bas
            pyautogui.press('3')
            print("3 tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

            # "2" tuşuna bas
            pyautogui.press('2')
            print("2 tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

            # "4" ve "v" tuşlarına sürekli basma döngüsü
            is_pressing_keys = True  # Sürekli basma döngüsünü başlat
            while is_pressing_keys:
                try:
                    # "4" tuşuna bas
                    pyautogui.press('4')
                    print("4 tuşuna basıldı.")
                    time.sleep(0.2)  # 0.2s bekle

                    # "v" tuşuna bas
                    pyautogui.press('v')
                    print("v tuşuna basıldı.")
                    time.sleep(0.2)  # 0.2 s bekle

                    # "victory" görselinin varlığını kontrol et
                    check_location = pyautogui.locateOnScreen(check_image_path, confidence=0.75)
                    if check_location is not None:
                        print("Victory görseli bulundu!")  # Görsel bulundu mesajı
                        is_pressing_keys = False  # Victory görseli bulunduğunda döngüyü kır
                        pyautogui.hotkey('alt', 'a')  # Victory bulunduğunda Alt+A tuşuna bas
                        print("Alt+A tuşuna basıldı.")  # Alt+A basıldığını yazdır


                except Exception as e:
                    print(f"Tuşa basma işlemi sırasında hata oluştu: {e}")
                      # Hata durumunda döngüden çık



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
            for image_path in image_paths:
                target_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
                if target_location is not None:
                    # Y koordinatına 10 birim ekle
                    adjusted_y = target_location.y - 15
                    # Yeni koordinatlara çift tıkla
                    pyautogui.doubleClick(target_location.x, adjusted_y)
                    print(f"{image_path} görseline tekrar tıklandı: ({target_location.x}, {adjusted_y})")
                    break  # Bir görsel bulduktan sonra döngüden çık

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

            time.sleep(3)

            # Saldırı görselini kontrol et
            attack_location = pyautogui.locateCenterOnScreen(attack_image_path, confidence=0.7)

            if attack_location is not None:
                # Saldırı görseli bulunduğunda e - tab - 2 - 3 basıp sonra 4ve V spamlayacak. Victory ekranını görene kadaar.
                time.sleep(0.3)
                # "e" tuşuna bas
                pyautogui.press('e')
                print("e tuşuna basıldı.")
                time.sleep(0.05)  # 50 ms bekle

                # "tab" tuşuna bas
                pyautogui.press('tab')
                print("tab tuşuna basıldı.")
                time.sleep(0.05)  # 50 ms bekle

                # "t" tuşuna bas
                pyautogui.press('t')
                print("t tuşuna basıldı.")
                time.sleep(0.05)  # 50 ms bekle

                # "3" tuşuna bas
                pyautogui.press('3')
                print("3 tuşuna basıldı.")
                time.sleep(0.05)  # 50 ms bekle

                # "2" tuşuna bas
                pyautogui.press('2')
                print("2 tuşuna basıldı.")
                time.sleep(0.05)  # 50 ms bekle

                # "4" ve "v" tuşlarına sürekli basma döngüsü
                is_pressing_keys = True  # Sürekli basma döngüsünü başlat
                while is_pressing_keys:
                    try:
                        # "4" tuşuna bas
                        pyautogui.press('4')
                        print("4 tuşuna basıldı.")
                        time.sleep(0.2)  # 0.2s bekle

                        # "v" tuşuna bas
                        pyautogui.press('v')
                        print("v tuşuna basıldı.")
                        time.sleep(0.2)  # 0.2 s bekle

                        # "victory" görselinin varlığını kontrol et
                        check_location = pyautogui.locateOnScreen(check_image_path, confidence=0.75)
                        if check_location is not None:
                            print("Victory görseli bulundu!")  # Görsel bulundu mesajı
                            is_pressing_keys = False  # Victory görseli bulunduğunda döngüyü kır
                            pyautogui.hotkey('alt', 'a')  # Victory bulunduğunda Alt+A tuşuna bas
                            print("Alt+A tuşuna basıldı.")  # Alt+A basıldığını yazdır


                    except Exception as e:
                        print(f"Tuşa basma işlemi sırasında hata oluştu: {e}")
                          # Hata durumunda döngüden çık

        else:
            # Saldırı görseli bulunamadığında rabid görseline tekrar tıkla
            print("Saldırı görseli bulunamadı, rastgele bir görsele tekrar tıklanacak.")
            for image_path in image_paths:
                target_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
                if target_location is not None:
                    # Y koordinatına 6 birim ekle
                    adjusted_y = target_location.y + 6
                    # Yeni koordinatlara çift tıkla
                    pyautogui.doubleClick(target_location.x, adjusted_y)
                    print(f"{image_path} görseline tekrar tıklandı: ({target_location.x}, {adjusted_y})")
                    break  # Bir görsel bulduktan sonra döngüden çık

    except Exception as e:
        print(f"Tıklama işlemi sırasında hata oluştu: {e}")
        time.sleep(0.1)  # Hata durumunda bir süre bekle
