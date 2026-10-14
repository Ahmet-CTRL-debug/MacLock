import serial
import time
import os

# Kendi portunu yazmayı unutma!
arduino_port = '/dev/cu.usbserial-A50285BI' 
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)
    print("Bağlantı başarılı! Şalter dinleniyor...")
except Exception as e:
    print(f"Bağlantı hatası: {e}")
    exit()

son_durum = "" 

while True:
    try:
        if ser.in_waiting > 0:
            gelen_veri = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if gelen_veri != "" and gelen_veri != son_durum:
                print(f"Şalter değişti: {gelen_veri}")
                
                if gelen_veri == "OFF":
                    os.system('say "Görüşürüz mister"')
                    time.sleep(1.5)
                    os.system("pmset displaysleepnow")
                    
                elif gelen_veri == "ON1":
                    os.system("caffeinate -u -t 2")
                    time.sleep(3) 
                    
                    os.system('''osascript -e 'tell application "System Events" to key code 36' ''')
                    time.sleep(2) 
                    
                    # ŞİFRENİ BURAYA YAZ 
                    os.system('''osascript -e 'tell application "System Events" to keystroke "AhmetAyse2"' ''')
                    time.sleep(0.5)
                    
                    os.system('''osascript -e 'tell application "System Events" to key code 36' ''')
                    os.system('say "Hoşgeldiniz Ahmet Bey"')
                    
                elif gelen_veri == "ON2":
                    os.system('open -a Safari "https://gemini.google.com"')
                
                son_durum = gelen_veri
                
    except Exception as e:
        print(f"Ufak bir iletişim hatası atlatıldı: {e}")
        
    time.sleep(0.1)