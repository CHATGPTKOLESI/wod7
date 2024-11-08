import pyautogui
import time
import random

# Nepherto ve Diamond görsel yolları
nepherto_image_path = 'mordels2.png'
diamond_image_path = 'diamond.png'
attack_image_path = 'saldiri.png'  # Saldırı görseli
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı

# İlk Botu Açarken Bekleme Süresi
time.sleep(3)

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
        # Ekranda nepherto2.png görsellerini bul
        nepherto_locations = list(pyautogui.locateAllOnScreen(nepherto_image_path, confidence=0.6))

        # Eğer ekranda nepherto bulunmazsa, beklemeye alır
        if not nepherto_locations:
            print("Nepherto bulunamadı, tekrar deniyor...")
            time.sleep(0.2)
            continue

        # Rastgele bir konum seç ve o konuma tıkla
        location = random.choice(nepherto_locations)
        adjusted_x = location.left + 52 # 5 birim sağa
        adjusted_y = location.top - 22  # 8 birim yukarıda tıklama
        pyautogui.doubleClick(adjusted_x, adjusted_y)
        print(f"Yeni nepherto konumuna tıklama yapıldı: ({adjusted_x}, {adjusted_y})")

        time.sleep(1)
        # Diamond görselini kontrol et (Nepherto tıklama sonrası)
        try:
            diamond_location = pyautogui.locateOnScreen(diamond_image_path, confidence=0.6)
            if diamond_location:
                print("Diamond görseli bulundu, döngü başa sarılıyor...")
                pyautogui.hotkey('ctrl', 'w')  # Ctrl+W tuşuna bas
                continue  # Döngüyü başa sar
        except Exception as e:
            print(f"Diamond görseli kontrolü sırasında hata oluştu: {e}")
            # Hata olsa bile kod devam etsin

            # Tuş kombinasyonlarını sırasıyla uygula
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
            print("Ctrl+R tuşuna basıldı.")
            time.sleep(0.3)
            pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
            print("Alt+A tuşuna basıldı.")
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'u')  # Ctrl+U tuşuna bas
            print("Ctrl+U tuşuna basıldı.")



        time.sleep(2.7)

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

        #Şimdi aşağı scroll yapıp yaratık bulacak:


        # Hedef koordinatlarda bir tıklama
        time.sleep(1)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"{x}, {y} koordinatına bir defa sol tıklama yapıldı.")

        # Aşağı scroll işlemi
        print("Aşağı scroll işlemi başlıyor...")
        for _ in range(8):  # 200 birim aşağı 8 defa scroll
            pyautogui.scroll(-200)
        print("Aşağı scroll işlemi tamamlandı.")
        time.sleep(0.5)
        # Ekranda nepherto2.png görsellerini bul
        nepherto_locations = list(pyautogui.locateAllOnScreen(nepherto_image_path, confidence=0.6))

        # Eğer ekranda nepherto bulunmazsa, beklemeye alır
        if not nepherto_locations:
            print("Nepherto bulunamadı, tekrar deniyor...")
            time.sleep(0.2)
            continue

        # Rastgele bir konum seç ve o konuma tıkla
        location = random.choice(nepherto_locations)
        adjusted_x = location.left + 52  # 5 birim sağa
        adjusted_y = location.top - 22  # 8 birim yukarıda tıklama
        pyautogui.doubleClick(adjusted_x, adjusted_y)
        print(f"Yeni nepherto konumuna tıklama yapıldı: ({adjusted_x}, {adjusted_y})")

        time.sleep(1)

        try:
            diamond_location = pyautogui.locateOnScreen(diamond_image_path, confidence=0.6)
            if diamond_location:
                print("Diamond görseli bulundu, döngü başa sarılıyor...")
                time.sleep(0.2)
                pyautogui.hotkey('ctrl', 'w')  # Ctrl+W tuşuna bas
                continue  # Döngüyü başa sar
        except Exception as e:
            print(f"Diamond görseli kontrolü sırasında hata oluştu: {e}")
            # Hata olsa bile kod devam etsin

            # Tuş kombinasyonlarını sırasıyla uygula
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
            print("Ctrl+R tuşuna basıldı.")
            time.sleep(0.3)
            pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
            print("Alt+A tuşuna basıldı.")
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 'u')  # Ctrl+U tuşuna bas
            print("Ctrl+U tuşuna basıldı.")

        time.sleep(2.7)

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

    except Exception as e:
        print(f"İşlem sırasında hata oluştu: {e}")
        time.sleep(1)  # Hata durumunda kısa bir bekleme


