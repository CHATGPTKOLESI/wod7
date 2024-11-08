import pyautogui
import time
import random



# Görsellerin dosya yolları
image_paths = ['genie2.png', 'flower2.png', 'whad2.png']  # WhadWorm-OutcastGenie-Flower
attack_image_path = 'saldiri.png'  # Saldırı görseli
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı
diamond_image_path = 'diamond.png'
close_image_path = 'close2.png'
cancel_image_path = 'cancel2.png'


# Avlan ve full ekrana geçiş için kısa bir bekleme
time.sleep(4)

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

        # Her döngüden önce 1 saniye bekle
        time.sleep(1)


        # Hedef koordinatlar
        x = 951
        y = 648
        # Fareyi belirtilen koordinatlara taşı ve sol tıklama yap
        pyautogui.moveTo(x, y)  # Fareyi x=951, y=648 koordinatına taşı
        pyautogui.click()  # Sol tıklama yap
        print(f"{x}, {y} koordinatına bir defa sol tıklama yapıldı.")

        # Yukarı scroll işlemi
        print("İlk yukarı scroll işlemi başlıyor...")
        for _ in range(8):  # 200 birim yukarı 8 defa scroll
            pyautogui.scroll(200)
        print("Yukarı scroll işlemi tamamlandı.")
        time.sleep(0.5)


       ## Tüm görsellerin konumlarını bul ve bir listeye al
        all_locations = []
        for image_path in image_paths:
            locations = list(pyautogui.locateAllOnScreen(image_path, confidence=0.6))
            all_locations.extend(locations)

        # Eğer ekranda bir veya daha fazla görsel bulundaysa
        if all_locations:
            # Tüm konumlar arasından rastgele birini seç
            target_location = random.choice(all_locations)

            # Seçilen konumun merkez koordinatlarını alıp Y koordinatını ayarla
            center_x, center_y = pyautogui.center(target_location)
            adjusted_y = center_y - 25  # Merkezden 25 birim yukarıya tıklama
            pyautogui.doubleClick(center_x, adjusted_y)
            print(f"Savaş Başladı(Rastgele seçim yapıldı).: ({center_x}, {adjusted_y})")

        if not all_locations:
            time.sleep(0.2)
            print("Hiçbir görsel bulunamadı.")
            continue

        time.sleep(2)
        # Diamond görselini kontrol et (Mystra tıklama sonrası)
        try:
            diamond_location = pyautogui.locateOnScreen(diamond_image_path, confidence=0.6)
            if diamond_location:
                print("Diamond görseli bulundu, döngü başa sarılıyor...")
                pyautogui.hotkey('ctrl', 'w')  # Ctrl+W tuşuna bas
                continue  # Döngüyü başa sar

        except Exception as e:
            print(f"Diamond görseli bulunamadı.: {e}")
            # Hata olsa bile kod devam etsin

        try:
            cancel_location = pyautogui.locateCenterOnScreen(cancel_image_path, confidence=0.90)
            if cancel_location:
                adjusted_location = (cancel_location[0] + 60, cancel_location[1] + 35)
                pyautogui.leftClick(adjusted_location)
                print("Uyarı çıktı, döngü başa sarılıyor...")
                time.sleep(0.2)
                continue  # Döngüyü başa sar

        except Exception as e:
            print(f"Uyarı yok, devam: {e}")
            # Hata olsa bile kod devam etsin

        try:

            close_location = pyautogui.locateCenterOnScreen(close_image_path, confidence=0.90)
            if close_location:
                adjusted_location = (close_location[0] + 50, close_location[1] + 30)
                pyautogui.leftClick(adjusted_location)
                print("Uyarı 2 çıktı, döngü başa sarılıyor...")
                time.sleep(0.2)
                continue  # Döngüyü başa sarv


        except Exception as e:
            print(f"Uyarı 2 yok, devam: {e}")
            # Hata olsa bile kod devam etsin

        time.sleep(1)

        # Saldırı görselini kontrol et
        attack_location = pyautogui.locateCenterOnScreen(attack_image_path, confidence=0.7)
        if attack_location is not None:
            # Saldırı görseli bulunduğunda e - tab - 2 - 3 basıp sonra 4 ve V spamlayacak
            time.sleep(0.05)
            pyautogui.press('e')
            print("e tuşuna basıldı.")
            time.sleep(0.05)
            pyautogui.press('tab')
            print("tab tuşuna basıldı.")
            time.sleep(0.05)
            pyautogui.press('t')
            print("t tuşuna basıldı.")
            time.sleep(0.05)
            pyautogui.press('3')
            print("3 tuşuna basıldı.")
            time.sleep(0.05)
            pyautogui.press('2')
            print("2 tuşuna basıldı.")
            time.sleep(0.05)

            # "4" ve "v" tuşlarına sürekli basma döngüsü
            is_pressing_keys = True
            while is_pressing_keys:
                try:
                    pyautogui.press('4')
                    print("4 tuşuna basıldı.")
                    time.sleep(0.1)
                    pyautogui.press('5')
                    print("5 tuşuna basıldı.")
                    time.sleep(0.1)
                    pyautogui.press('v')
                    print("v tuşuna basıldı.")
                    time.sleep(0.2)

                    # "victory" görselinin varlığını kontrol et
                    check_location = pyautogui.locateOnScreen(check_image_path, confidence=0.75)
                    if check_location is not None:
                        print("Victory görseli bulundu!")
                        is_pressing_keys = False
                        pyautogui.hotkey('alt', 'a')
                        print("Alt+A tuşuna basıldı.")
                except Exception as e:
                    print(f"Tuşa basma işlemi sırasında hata oluştu: {e}")



            # 1.5 saniye bekle (tekrar alt+a bastığı için ufak bir bekleme).
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

            # Scroll işlemi sonrası Mystra moblarını tekrar ara
            time.sleep(0.5)

            ## Tüm görsellerin konumlarını bul ve bir listeye al
            all_locations = []
            for image_path in image_paths:
                locations = list(pyautogui.locateAllOnScreen(image_path, confidence=0.6))
                all_locations.extend(locations)

            # Eğer ekranda bir veya daha fazla görsel bulundaysa
            if all_locations:
                # Tüm konumlar arasından rastgele birini seç
                target_location = random.choice(all_locations)

                # Seçilen konumun merkez koordinatlarını alıp Y koordinatını ayarla
                center_x, center_y = pyautogui.center(target_location)
                adjusted_y = center_y - 25  # Merkezden 25 birim yukarıya tıklama
                pyautogui.doubleClick(center_x, adjusted_y)
                print(f"Savaş Başladı(Rastgele seçim yapıldı).: ({center_x}, {adjusted_y})")

            if not all_locations:
                time.sleep(0.2)
                print("Hiçbir görsel bulunamadı.")
                continue

            time.sleep(2)
            # Diamond görselini kontrol et (Mystra tıklama sonrası)
            try:
                diamond_location = pyautogui.locateOnScreen(diamond_image_path, confidence=0.6)
                if diamond_location:
                    print("Diamond görseli bulundu, döngü başa sarılıyor...")
                    pyautogui.hotkey('ctrl', 'w')  # Ctrl+W tuşuna bas
                    continue  # Döngüyü başa sar

            except Exception as e:
                print(f"Diamond görseli bulunamadı.: {e}")
                # Hata olsa bile kod devam etsin

            try:
                cancel_location = pyautogui.locateCenterOnScreen(cancel_image_path, confidence=0.90)
                if cancel_location:
                    adjusted_location = (cancel_location[0] + 60, cancel_location[1] + 35)
                    pyautogui.leftClick(adjusted_location)
                    print("Uyarı çıktı, döngü başa sarılıyor...")
                    time.sleep(0.2)
                    continue  # Döngüyü başa sar

            except Exception as e:
                print(f"Uyarı yok, devam: {e}")
                # Hata olsa bile kod devam etsin

            try:

                close_location = pyautogui.locateCenterOnScreen(close_image_path, confidence=0.90)
                if close_location:
                    adjusted_location = (close_location[0] + 50, close_location[1] + 30)
                    pyautogui.leftClick(adjusted_location)
                    print("Uyarı 2 çıktı, döngü başa sarılıyor...")
                    time.sleep(0.2)
                    continue  # Döngüyü başa sarv


            except Exception as e:
                print(f"Uyarı 2 yok, devam: {e}")
                # Hata olsa bile kod devam etsin

            time.sleep(1)

            # Saldırı görselini kontrol et
            attack_location = pyautogui.locateCenterOnScreen(attack_image_path, confidence=0.7)
            if attack_location is not None:
                # Saldırı görseli bulunduğunda e - tab - 2 - 3 basıp sonra 4 ve V spamlayacak
                time.sleep(0.05)
                pyautogui.press('e')
                print("e tuşuna basıldı.")
                time.sleep(0.05)
                pyautogui.press('tab')
                print("tab tuşuna basıldı.")
                time.sleep(0.05)
                pyautogui.press('t')
                print("t tuşuna basıldı.")
                time.sleep(0.05)
                pyautogui.press('3')
                print("3 tuşuna basıldı.")
                time.sleep(0.05)
                pyautogui.press('2')
                print("2 tuşuna basıldı.")
                time.sleep(0.05)

                # "4" ve "v" tuşlarına sürekli basma döngüsü
                is_pressing_keys = True
                while is_pressing_keys:
                    try:
                        pyautogui.press('4')
                        print("4 tuşuna basıldı.")
                        time.sleep(0.1)
                        pyautogui.press('5')
                        print("5 tuşuna basıldı.")
                        time.sleep(0.1)
                        pyautogui.press('v')
                        print("v tuşuna basıldı.")
                        time.sleep(0.2)

                        # "victory" görselinin varlığını kontrol et
                        check_location = pyautogui.locateOnScreen(check_image_path, confidence=0.75)
                        if check_location is not None:
                            print("Victory görseli bulundu!")
                            is_pressing_keys = False
                            pyautogui.hotkey('alt', 'a')
                            print("Alt+A tuşuna basıldı.")
                    except Exception as e:
                        print(f"Tuşa basma işlemi sırasında hata oluştu: {e}")



    except Exception as e:
        print(f"Tıklama işlemi sırasında hata oluştu: {e}")
        time.sleep(0.1)  # Hata durumunda bir süre bekle
