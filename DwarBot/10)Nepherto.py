import pyautogui
import time
import random

# Nepherto ve Diamond görsel yolları
nepherto_image_path = 'nepherto2.png'
diamond_image_path = 'diamond.png'
close_image_path = 'close2.png'
cancel_image_path = 'cancel2.png'
attack_image_path = 'saldiri.png'  # Saldırı görseli
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı

# İlk Botu Açarken Bekleme Süresi
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
        adjusted_x = location.left + 32  # 5 birim sağa
        adjusted_y = location.top - 16  # 8 birim yukarıda tıklama
        pyautogui.doubleClick(adjusted_x, adjusted_y)
        print(f"Yeni nepherto konumuna tıklama yapıldı: ({adjusted_x}, {adjusted_y})")

        time.sleep(2)
        # Diamond görselini kontrol et (Nepherto tıklama sonrası)
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
        adjusted_x = location.left + 32  # 55 birim sağa
        adjusted_y = location.top - 16  # 8 birim yukarıda tıklama
        pyautogui.doubleClick(adjusted_x, adjusted_y)
        print(f"Yeni nepherto konumuna tıklama yapıldı: ({adjusted_x}, {adjusted_y})")

        time.sleep(2)
        # Diamond görselini kontrol et (Nepherto tıklama sonrası)
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



#Bot Özellikleri:
#1) İlk açılırken 4 saniye bekliyo. Avlana geçip full ekran ve full avlan modu açıyor. (1 seferlik)
#2) Mapin tam ortasına click atıp yukarı çıkıyor yukarıda rastgele neferto seçip saldırıyor.
#3) Nefertoya saldırır saldırmaz 3 kontrol yapar sırasıyla: elmas ekranı açılırsa kapatır, dövüş doluysa reddeder, yaratık gittiyse close basar.
#4) Tekrar en başa dönüp yukarda neferto buluyor.
#5) #5.1) Nefertoyu bulur ve saldırırsa, dövüşe girdiğini ok setini görünce anlıyor anlamak için 2.5- 3 sn bekliyor. Anladığı an:
#5.2) sırası ile e - k - tab - t basıp sonra 4-5-v tuşları spamlıyor. Victory ekranını gördüğü an alt+a basıyor.
#6) İlk yukarda nefertoyu keserse, avlana dönüp aşağı scroll atıp aşağıda nefertoya saldırıyor.
#7) Nefertoya saldırır saldırmaz 3 kontrol yapar sırasıyla: elmas ekranı açılırsa kapatır, dövüş doluysa reddeder, yaratık gittiyse close basar.
#8) Bu esnada eğer elmas tuşuna basarsa ctrl+w ile kapatıp tekrar en başa dönüp YUKARIDA neferto buluyor.
#8.1) Nefertoyu bulur ve saldırırsa, dövüşe girdiğini ok setini görünce anlıyor anlamak için 3sn bekliyor. Anladığı an:
#8.2) sırası ile e - k - tab - t basıp sonra 4-5-v tuşları spamlıyor. Victory ekranını gördüğü an alt+a basıyor.
#9) Buraya kadar gelirse burdan  tekrar en başa dönüp yukarıda neferto arıyor.

#Botun hala sıkıntıları neler:
#1) Bot eğer nefertoya dalar ve dövüş içine geçemez ise 3sn bekliyor. Fakat bunu daha aza çekince dövüşe girdiğini kaçırabilir, bu sebeple mecbur tutuyorum.
#2) İlk daldığı nefertoyu bulamaz ise tekrar yukarıda arıyor. Sürekli bi yukarı bi aşağıda aramıyor maalesef.

# Yeni yaptıklarım 07.11.2024 için:
# Bot artık sürekli ekran yenilemiyor bunun yerine dövüşleri reddedip yenisini arıyor burdan zaman kazancı oluyor bu sebeple dövüşe girişteki 3sn beklemeyi
# bir miktar azaltabilirim belki 2 saniyeye çekebilirim.