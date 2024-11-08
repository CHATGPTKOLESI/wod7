import pyautogui
import time

# Görselin dosya yolu
image_path = 'nepherto2.png'  # Hedef görsel
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
        pyautogui.click()  # Sol tıklama yap
        print(f"{x}, {y} koordinatına bir defa sol tıklama yapıldı.")

        # Yukarı scroll işlemi
        print("İlk yukarı scroll işlemi başlıyor...")
        for _ in range(8):  # 200 birim yukarı 8 defa scroll
            pyautogui.scroll(200)
        print("Yukarı scroll işlemi tamamlandı.")

        # Yukarı scroll işleminden sonra bekle
        time.sleep(1)

        # Görseli kontrol et
        target_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
        if target_location is not None:
            # Y koordinatına 10 birim ekle
            adjusted_y = target_location.y - 8
            # Yeni koordinatlara çift tıkla
            pyautogui.doubleClick(target_location.x, adjusted_y)
            print(f"{image_path} görseline tıklandı: ({target_location.x}, {adjusted_y})")

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
            # Saldırı görseli bulunduğunda e - tab - 2 - 3 basıp sonra 4 ve V spamlayacak
            time.sleep(0.3)
            pyautogui.press('e')
            print("e tuşuna basıldı.")
            time.sleep(0.3)
            pyautogui.press('k')
            print("k tuşuna basıldı.")
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

            # Hedef koordinatlarda bir tıklama
            time.sleep(1.5)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            print(f"{x}, {y} koordinatına bir defa sol tıklama yapıldı.")

            # Aşağı scroll işlemi
            print("Aşağı scroll işlemi başlıyor...")
            for _ in range(8):  # 200 birim aşağı 8 defa scroll
                pyautogui.scroll(-200)
            print("Aşağı scroll işlemi tamamlandı.")

            # Scroll işlemi sonrası hedef görseli tekrar ara
            time.sleep(1)
            target_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
            if target_location is not None:
                adjusted_y = target_location.y - 8
                pyautogui.doubleClick(target_location.x, adjusted_y)
                print(f"{image_path} görseline tıklandı: ({target_location.x}, {adjusted_y})")

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

            # Saldırı görselini tekrar kontrol et
            attack_location = pyautogui.locateCenterOnScreen(attack_image_path, confidence=0.7)
            if attack_location is not None:
                # Saldırı görseli bulunduğunda e - tab - 2 - 3 basıp sonra 4 ve V spamlayacak
                time.sleep(0.3)
                pyautogui.press('e')
                print("e tuşuna basıldı.")
                time.sleep(0.3)
                pyautogui.press('k')
                print("k tuşuna basıldı.")
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
