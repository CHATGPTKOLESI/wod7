import pyautogui
import time

# Hedef görsellerin dosya yolları (aynı dizinde olduğunu varsayıyoruz)
image_path_1 = 'worm.png'
image_path_2 = 'genie.png'
image_path_3 = 'flower.png'
alert_image_path = 'close.png'
# Kontrol edilecek görselin dosya yolu
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı

# İlk çalışmayı kontrol etmek için bir değişken
first_run = True

# Döngü içinde sürekli çalışacak
while True:
    try:
        # İlk çalışmada "Alt+A" tuşuna basmadan önce 2 saniye bekle
        if first_run:
            time.sleep(2)  # Kod başladıktan 2 saniye bekle
            pyautogui.hotkey('alt', 'a')  # "Alt+A" tuşuna bas
            print("Alt+A tuşuna basıldı.")
            time.sleep(1)  # 1 saniye bekle
            first_run = False  # İlk çalışmayı tamamla

        # İlk görseli ekranda ara
        location = pyautogui.locateCenterOnScreen(image_path_1, confidence=0.6)
        if location is not None:
            pyautogui.doubleClick(location)
            print(f"Görsele çift tıklandı: {image_path_1} - Konum: {location}")
        else:
            # İkinci görseli ekranda ara
            location = pyautogui.locateCenterOnScreen(image_path_2, confidence=0.6)
            if location is not None:
                pyautogui.doubleClick(location)
                print(f"Görsele çift tıklandı: {image_path_2} - Konum: {location}")
            else:
                # Üçüncü görseli ekranda ara
                location = pyautogui.locateCenterOnScreen(image_path_3, confidence=0.6)
                if location is not None:
                    pyautogui.doubleClick(location)
                    print(f"Görsele çift tıklandı: {image_path_3} - Konum: {location}")
                else:
                    print("Hiçbir görsel bulunamadı.")

                    # Yukarı scroll yap
                    pyautogui.scroll(100)  # Yukarı scroll (pozitif değer)
                    print("Fare yukarı doğru scroll yapıldı.")
                    time.sleep(0.5)  # 0.5 saniye bekle

                    # Görselleri tekrar kontrol et
                    continue  # Döngünün başına geri dön

        # İlk olarak 4 saniye bekle
        time.sleep(4)

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

        # "4" tuşuna bas
        pyautogui.press('4')
        print("4 tuşuna basıldı.")
        time.sleep(0.05)  # 50 ms bekle

        # "v" tuşuna bas
        pyautogui.press('v')
        print("v tuşuna basıldı.")
        time.sleep(0.05)  # 50 ms bekle

        # "4" ve "v" tuşlarına sürekli basma
        while True:
            pyautogui.press('4')
            print("4 tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

            pyautogui.press('v')
            print("v tuşuna basıldı.")
            time.sleep(0.05)  # 50 ms bekle

            # "victory" görselinin varlığını kontrol et
            check_location = pyautogui.locateCenterOnScreen(check_image_path, confidence=0.6)
            if check_location is not None:
                # "Alt+A" tuşuna bas
                pyautogui.hotkey('alt', 'a')
                print("Alt+A tuşuna basıldı.")
                break  # Eğer "victory" görseli bulunursa döngüden çık

        # Uyarı mesajını kontrol et
        alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.6)
        if alert_location is not None:
            # Uyarı mesajına tıkla
            pyautogui.click(alert_location)
            print(f"Uyarı mesajına tıklandı: {alert_location}")

            # Uyarı mesajından sonra döngüye geri dön
            continue

    except Exception as e:
        print("Bir hata oluştu:", e)
        # Hata durumunda döngüye devam et
        time.sleep(0.1)  # Hata sonrası bir süre bekle
