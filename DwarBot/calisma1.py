import os

# Hedef görsellerin dosya yolları (aynı dizinde olduğunu varsayıyoruz)
image_paths = [f'rabid{i}.png' for i in range(1, 10)]

# Geçerli görsel dosyalarını kontrol et
valid_image_paths = [path for path in image_paths if os.path.exists(path)]

if not valid_image_paths:
    print("Hiçbir görsel dosyası bulunamadı.")
else:
    print(f"Bulunan görsel dosyaları: {valid_image_paths}")