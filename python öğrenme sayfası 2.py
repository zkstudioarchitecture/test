#Dosyaya yazma write() metodu
# Dosyayı yazma modunda açıyoruz
# (Dosya yoksa otomatik oluşur)

dosya = open("notlar.txt", "w")

# write() ile metin yazıyoruz
dosya.write("Python öğreniyorum.\n")
dosya.write("Dosya işlemleri çok kolay.\n")
dosya.write("3. satır burada.")

# Dosyayı kapatmak ZORUNLUDUR
dosya.close()
print("notlar.txt başarıyla yazıldı!")

#Dosyadan okuma 
# 1. read() -> Hepsini tek string al
dosya = open("notlar.txt", "r")
icerik = dosya.read()
print(icerik)
dosya.close()

# 2. readlines() -> Liste olarak al
dosya = open("notlar.txt", "r")
satirlar = dosya.readlines()
print(satirlar)
dosya.close()

# 3. readline() -> Tek satır oku
dosya = open("notlar.txt", "r")
ilk = dosya.readline()
print("İlk satır:", ilk)
dosya.close()

# Dosyayı satır satır gezmek (En Verimli)
dosya = open("notlar.txt", "r")

satir_no = 1

for satir in dosya:
    # strip() -> baştaki/sondaki boşluk ve \n siler
    temiz = satir.strip()
    print(f"{satir_no}. satır: {temiz}")
    satir_no += 1

dosya.close()

# Çıktı:
# 1. satır: Python öğreniyorum.
# 2. satır: Dosya işlemleri çok kolay.
# 3. satır: 3. satır burada.

#Veri ekleme: Append Modu
# Önce w modu ile temel dosyayı oluşturuyoruz
dosya = open("gunluk.txt", "w")
dosya.write("1. gün: Başladım.\n")
dosya.close()

# Şimdi "a" modu ile SONUNA ekliyoruz
# Eski "1. gün" satırı SİLİNMEZ
dosya = open("gunluk.txt", "a")

dosya.write("2. gün: Devam ediyorum.\n")
dosya.write("3. gün: Dosya öğrendim.\n")

dosya.close()

# Dosyanın son hali:
# 1. gün: Başladım.
# 2. gün: Devam ediyorum.
# 3. gün: Dosya öğrendim.

#Profosyonel yöntem with bloğu
# ESKİ YÖNTEM
dosya = open("veri.txt", "r")
icerik = dosya.read()
dosya.close()

# MODERN YÖNTEM (with bloğu)
with open("veri.txt", "r") as dosya:
    icerik = dosya.read()
    print(icerik)

# Blok bitince dosya OTOMATİK kapanır
# Ayrıca close() yazmaya gerek yok!


# Yazma için de aynı mantık:
with open("yeni.txt", "w") as f:
    f.write("with bloğu harika!")

#Yapılacaklar listesini diske kaydetme
# 1) Yapılacaklar listesini dosyaya kaydet
gorevler = ["Market alışverişi", "Python çalış", "Spor yap"]

with open("gorevler.txt", "w", encoding="utf-8") as f:
    for gorev in gorevler:
        f.write(gorev + "\n")  # Her görevi alt satıra yaz

print("Görevler kaydedildi.")


# 2) Daha sonra programı tekrar açtığımızda dosyadan geri yükle
with open("gorevler.txt", "r", encoding="utf-8") as f:
    kayitli_gorevler = [satir.strip() for satir in f]

print("Yüklenen görevler:", kayitli_gorevler)

# ['Market alışverişi', 'Python çalış', 'Spor yap']

# encoding="utf-8" -> Türkçe karakter (ç, ş, ğ, ü) sorunlarını önler!

import os

dosya_adi = "veriler.txt"

# Dosya var mı diye kontrol et
if os.path.exists(dosya_adi):
    print("Dosya mevcut, okunuyor...")

    with open(dosya_adi, "r") as f:
        print(f.read())

else:
    print("Dosya bulunamadı! Oluşturuluyor...")

    with open(dosya_adi, "w") as f:
        f.write("Yeni dosya oluşturuldu.")

# Dosyanın boyutunu öğren
print(os.path.getsize(dosya_adi))  # Boyut (byte)

# Dosyayı yeniden adlandır
# os.rename("eski.txt", "yeni.txt")

# Dosyayı sil
# os.remove("gereksiz.txt")

#programın kaç kez açıldığını saymak 
import os
dosya = "sayac.txt"

# 1) Dosya yoksa 0'dan başla, varsa içindeki sayıyı oku
if os.path.exists(dosya):
    with open(dosya, "r") as f:
        sayac = int(f.read())
else:
    sayac = 0

# 2) Sayacı bir artır
sayac += 1
print(f"Bu programı {sayac}. kez açtınız.")

# 3) Yeni değeri dosyaya geri yaz
with open(dosya, "w") as f:
    f.write(str(sayac))
# Program her çalıştırıldığında sayı 1 artarak devam eder.