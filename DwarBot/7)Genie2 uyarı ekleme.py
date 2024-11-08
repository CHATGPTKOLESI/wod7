import pyautogui
import time
import keyboard

# Hedef görselin dosya yolu (aynı dizinde olduğunu varsayıyoruz)
image_path = 'genie2.png'
alert_image_path = 'close.png'  # Tek uyarı mesajı
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı

# İlk çalışmayı kontrol etmek için bir değişken
first_run = True

# Döngü içinde sürekli çalışacak
while True:
    try:
        # İlk çalışmada "Alt+A" tuşuna basmadan önce 2 saniye beklev
        if first_run:
            time.sleep(2)  # Kod başladıktan 2 saniye bekle
            pyautogui.hotkey('alt', 'a')  # "Alt+A" tuşuna bas
            print("Alt+A tuşuna basıldı.")  # İlk çalışmada Alt+A basıldığını yazdır
            time.sleep(1)  # 1 saniye bekle
            first_run = False  # İlk çalışmayı tamamla

        # Görseli ekranda ara
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

        if location is not None:
            # Belirlenmiş görselin 8 birim üstüne tıklamak için y koordinatını ayarla
            adjusted_location = (location.x, location.y - 8)  # 8 birim yukarı kaydırıldı
            pyautogui.doubleClick(adjusted_location)  # Ayarlanan konuma çift tıklama yap
            print(f"Genie Tespit Edildi ve Saldırıldı.: {image_path} - Konum: {adjusted_location}")

            # Uyarı mesajını kontrol et
            for _ in range(5):  # Uyarıyı kontrol etmek için döngü
                try:
                    alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.6)

                    if alert_location is not None:
                        print("Uyarı görüldü! Sol tıklama yapılıyor.")
                        pyautogui.click()  # Uyarı mesajına bir kez sol tıklama yap
                        time.sleep(0.3)  # Tıklama sonrası kısa bir bekleme
                        # "Alt+A" tuşuna bas
                        pyautogui.hotkey('alt', 'a')
                        print("Alt+A tuşuna basıldı.")

                        # Görseli tekrar kontrol et
                        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
                        if location is not None:
                            adjusted_location = (location.x, location.y - 8)
                            pyautogui.doubleClick(adjusted_location)  # Uyarıdan sonra tekrar görsele tıklama yap
                            print(f"Genie Tespit Edildi ve Saldırıldı.: {image_path} - Konum: {adjusted_location}")

                except Exception:
                    # Hata durumunda döngüyü devam ettir
                    pass  # Hata olduğunda sadece devam et

            # İlk olarak 4 saniye bekle
            time.sleep(3.5)

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

                        time.sleep(0.3)  # 0.3 saniye bekle
                        pyautogui.hotkey('alt', 'a')  # Tekrar Alt+A tuşuna bas
                        print("Alt+A tuşuna tekrar basıldı.")  # Tekrar Alt+A basıldığını yazdır

                except Exception:
                    # Hata durumunda döngüyü devam ettir
                    time.sleep(0.1)  # Hata sonrası bir süre bekle

    except Exception:
        # Ana döngüde bir hata oluştu
        time.sleep(0.1)  # Hata sonrası bir süre bekle
