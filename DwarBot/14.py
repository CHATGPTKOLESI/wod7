import pyautogui
import time
import random

# Görsellerin dosya yolları
image_paths = ['genie2.png', 'flower2.png', 'whad2.png']  # WhadWorm-OutcastGenie-Flower
attack_image_path = 'saldiri.png'  # Saldırı görseli
check_image_path = 'victory.png'  # Kontrol edilecek görselin adı

# Avlan ve full ekrana geçiş için kısa bir bekleme
time.sleep(2)

# Sürekli döngü
while True:
    try:
        # Her döngüden önce 1.5 saniye bekle
        time.sleep(1.5)

        # Hedef koordinatlar
        x = 951
        y = 648
        # Fareyi belirtilen koordinatlara taşı ve sol tıklama yap
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"{x}, {y} koordinatına bir defa sol tıklama yapıldı.")

        # Tüm görsellerin konumlarını bul ve bir listeye al
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
            pyautogui.click(center_x, adjusted_y)
            print(f"Savaş Başladı(Rastgele seçim yapıldı).: ({center_x}, {adjusted_y})")
            time.sleep(3)  # Tıklamadan sonra kısa bir bekleme
        else:
            print("Hiçbir görsel bulunamadı.")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        time.sleep(0.1)  # Hata durumunda kısa bir süre bekle
