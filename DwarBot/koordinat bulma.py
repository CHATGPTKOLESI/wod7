import pyautogui
import time

# x ve y koordinatlarını bulmak için mouse pozisyonunu almak
print("Koordinatları almak için fareyi istediğiniz yere getirin.")
time.sleep(3)  # Fareyi konuma getirmek için 3 saniye bekler

# Fare konumunu al
x, y = pyautogui.position()
print(f"Bulunan koordinatlar: x={x}, y={y}")

# Fareyi belirlenen koordinatlara hareket ettir ve tıkla
pyautogui.moveTo(x, y)  # Fareyi x, y koordinatına taşı
pyautogui.click()       # Sol tıklama yap
print("Belirtilen koordinata tıklama yapıldı.")
