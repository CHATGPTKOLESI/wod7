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

        # Rabid görselini ara
        rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)

        if rabid_location is not None:
            pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
            print(f"Rabid'e tıklandı: {rabid_location}")

            # Her 2 döngüde bir uyarı görselini kontrol et
            loop_counter += 1
            if loop_counter % 2 == 0:
                try:
                    alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.8)
                    if alert_location is not None:
                        pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
                        print("Ctrl+R tuşuna basıldı.")
                        time.sleep(0.5)  # Bekle
                        pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
                        print("Alt+A tuşuna basıldı.")
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl', 'u')  # Ctrl + u tuşlarına bas
                        print("Ctrl+U tuşlarına basıldı.")


                    else:
                        print("Uyarı görseli bulunamadı, işlemlere devam ediliyor.")
                except Exception as e:
                    print(f"Alert kontrolünde hata oluştu: {e}")

                # Kod bloğu çalıştıktan sonra başa dön
                continue

            time.sleep(4)  # Bekle
            pyautogui.press('w')  # W tuşuna bas
            print("W tuşuna basıldı.")

            # Victory görselini kontrol et
            check_location = pyautogui.locateCenterOnScreen(check_image_path, confidence=0.60)
            if check_location is not None:
                print("Victory görseli bulundu!")
                time.sleep(0.5)  # 1 saniye bekle
                pyautogui.hotkey('alt', 'a')  # Victory bulunduğunda Alt+A tuşuna bas
                print("Alt+A tuşuna basıldı.")  # Durumu yazdır
                time.sleep(1.5)  # 0.5 saniye bekle

                # Yukarı scroll işlemi
                for _ in range(8):  # 200 birim yukarı 8 defa scroll
                    pyautogui.scroll(200)
                print("Yukarı scroll işlemi yapıldı.")

                # Yukarı scroll sonrası ek kodlar
                # Rabid görselini ara ve işlemleri tekrarla
                rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
                if rabid_location is not None:
                    pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
                    print(f"Rabid'e tıklandı: {rabid_location}")

                    loop_counter += 1
                    if loop_counter % 2 == 0:
                        try:
                            alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.8)
                            if alert_location is not None:
                                pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
                                print("Ctrl+R tuşuna basıldı.")
                                time.sleep(0.5)  # Bekle
                                pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
                                print("Alt+A tuşuna basıldı.")
                                time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'u')  # Ctrl + u tuşlarına bas
                                print("Ctrl+U tuşlarına basıldı.")
                            else:
                                print("Uyarı görseli bulunamadı, işlemlere devam ediliyor.")
                        except Exception as e:
                            print(f"Alert kontrolünde hata oluştu: {e}")


                    time.sleep(4)  # Bekle
                    pyautogui.press('w')  # W tuşuna bas
                    print("W tuşuna basıldı.")

                    # Victory görselini kontrol et
                    check_location = pyautogui.locateCenterOnScreen(check_image_path, confidence=0.60)
                    if check_location is not None:
                        print("Victory görseli bulundu!")
                        time.sleep(0.5)  # 1 saniye bekle
                        pyautogui.hotkey('alt', 'a')  # Victory bulunduğunda Alt+A tuşuna bas
                        print("Alt+A tuşuna basıldı.")  # Durumu yazdır
                        time.sleep(1.5)  # 0.5 saniye bekle

                # Aşağı scroll işlemi
                for _ in range(8):  # 200 birim aşağı 8 defa scroll
                    pyautogui.scroll(-200)
                print("Aşağı scroll işlemi yapıldı.")

                # Aşağı scroll sonrası ek kodlar
                rabid_location = pyautogui.locateCenterOnScreen(image_path, confidence=0.6)
                if rabid_location is not None:
                    pyautogui.doubleClick(rabid_location)  # Rabid görseline tıkla
                    print(f"Rabid'e tıklandı: {rabid_location}")

                    loop_counter += 1
                    if loop_counter % 2 == 0:
                        try:
                            alert_location = pyautogui.locateCenterOnScreen(alert_image_path, confidence=0.8)
                            if alert_location is not None:
                                pyautogui.hotkey('ctrl', 'r')  # Ctrl+R tuşuna bas
                                print("Ctrl+R tuşuna basıldı.")
                                time.sleep(0.5)  # Bekle
                                pyautogui.hotkey('alt', 'a')  # Alt+A tuşuna bas
                                print("Alt+A tuşuna basıldı.")
                                time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'u')  # Ctrl + u tuşlarına bas
                                print("Ctrl+U tuşlarına basıldı.")
                            else:
                                print("Uyarı görseli bulunamadı, işlemlere devam ediliyor.")
                        except Exception as e:
                            print(f"Alert kontrolünde hata oluştu: {e}")


                    time.sleep(4)  # Bekle
                    pyautogui.press('w')  # W tuşuna bas
                    print("W tuşuna basıldı.")
                    # Victory görselini kontrol et
                    check_location = pyautogui.locateCenterOnScreen(check_image_path, confidence=0.60)
                    if check_location is not None:
                        print("Victory görseli bulundu!")
                        time.sleep(0.5)  # 1 saniye bekle
                        pyautogui.hotkey('alt', 'a')  # Victory bulunduğunda Alt+A tuşuna bas
                        print("Alt+A tuşuna basıldı.")  # Durumu yazdır
                        time.sleep(1.5)  # 0.5 saniye bekle

        else:
            print("Rabid görseli bulunamadı.")

    except Exception as e:
        print(f"Tıklama işlemi sırasında hata oluştu: {e}")
        time.sleep(2)  # Hata durumunda bekleme süresini artırarak stabiliteyi artırın


        #burada yaptıuklarımı özetleyelim:
        #1) Rabidi gör -rabide tıkla - rabide w at - victory görünce çık
        #2) Yukarı scroll at aynılarını yap
        #3 )Aşağı scroll at aynılarıın yap
        #4 ) Bunu sürekli tekrarla
        #5=) Bunu yaparken uyarı çıkarsa 2 loopta 1 uyarı kodunu calistiyior ama çok hızlı tespit edemiyor uyarısı yavaş
        # 6) şuanlıuk kod en iyi çalışan yazdığım kod

        #7) FULL SCREEN VE F7 MODUNDAYKEN MAP COK BÜYÜK O YÜZDEN ÖNCE ORTA SONRA YUKARISI SONRA AŞAĞISI COK MANTIKLI DEĞİL
        #7.1) EN GÜZELİ DİREKT OLARAK EN YUKARI SCROLLMAKA VE SONRA EN AŞAĞI SCROLLAMA BU ŞEKİLDE MAPİ 2YE BÖLMÜŞ GİBİ OLURUM 3E BÖLMEK SAÇMA

