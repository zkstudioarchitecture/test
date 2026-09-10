print("Merhaba, dünya!")

ad = "Zeynep"
soyad = "Karaman"

tam_isim = ad + " " + soyad
print(tam_isim)

gulumse = "Ha"
print(gulumse * 3)


# STRING İŞLEMLERİ

mesaj = "Merhaba Yazılım"

# Büyük / Küçük Harf
print(mesaj.upper())
print(mesaj.lower())


# Karakter Sayısı (length)
# len'in parantezinin içine yazılır, yanına nokta konulmaz
uzunluk = len(mesaj)
print("Karakter sayısı:", uzunluk)


# Kelime değiştirme (Eski, Yeni)
yeni_mesaj = mesaj.replace("Yazılım", "Python")
print(yeni_mesaj)


# İNDEKSLEME

kurs = "PYTHON"

# P(0) Y(1) T(2) H(3) O(4) N(5)
# Bilgisayar saymaya sıfırdan başlar

print(kurs[0])
print(kurs[3])
print(kurs[-1])


# SLICING (Dilimleme)

mesaj = "KODLAMA"

print(mesaj[0:7:2])
print(mesaj[::-1])  # Metni tersten yazar


# SAYILAR

dogum_yılı = 2000       # int
kredi_borcu = -1500     # int
dolar_kuru = 32.45      # float

# int ve float toplanırsa sonuç float olur
sonuc = dogum_yılı + 0.5
print(type(sonuc))


# ROUND
fatura = 145.87

print(round(fatura))
print(round(fatura, 1))


# ABS = Negatifi pozitife çevirir
sıcaklık = -12

print(abs(sıcaklık))


# BOOL (DOĞRU / YANLIŞ)

# Doğrudan atama
oyun_bitti_mi = False
hesap_onaylı_mı = True


# Karşılaştırma işlemlerinin sonucu daima bool olur
sonuc = (10 > 3)
print(sonuc)


# SAYILARDA BOOL

# Sıfır hariç her sayı True'dur
print(bool(28))
print(bool(0))


# STRINGLERDE BOOL

# String boşsa False, doluysa True
print(bool("Zeynep"))
print(bool(" "))
print(bool(""))


# INPUT

# input() kullanıcıdan veri alır.
# Ancak input() ile alınan veri STRING'dir.

#girdi = input("Doğum yılınız: ")

# String'i integer'a çeviriyoruz
#doğum_yılı = int(girdi)

#yas = 2026 - doğum_yılı
#print("Yaşınız:", yas)


# FLOAT

# Kullanıcıdan alınan fiyatı float'a çeviriyoruz
#fiyat = float(input("Ürünün fiyatı: "))

#print(fiyat)


# STR

puan = 99

# Sayıyı string'e çevirerek metinle birleştiriyoruz
mesaj = "Sınav notunuz: " + str(puan)

print(mesaj)


# BOOL TEKRAR

print(bool(28))
print(bool(0))

# özel işlemler mod/tam bölme
#sayı tek mi çift mi
sayi = 15
kalan = sayi % 2
print( kalan)

#para üstü hesaplama
odenen = 250
tutar = 45
para_ustu = odenen - tutar
print(para_ustu)
# müsteriye kaç tane 20lik vermeliyim 
yirmilik_adet = para_ustu // 20
print(yirmilik_adet)

print("deneme")

#kısayol operatörleri denemeler += , -=
skor = 100
skor = skor + 50
print(skor)
skor += 50
print(skor)

sepet = 0
sepet += 39.45
sepet += 40.42
sepet -= 29.90
print(sepet)

print(sepet//1)

print(5 == 3)
print(4 != 3)
print("a" == "A") #PROGRAM BÜYÜK KÜÇÜK HARF DUYARLIDIR 
print(15 >= 15)

gerçek_sifre = "python 2287"
girilen_sifre = "pyton 2287"
print(gerçek_sifre == girilen_sifre)

#zincirleme karşılaştırma pythona özgüdür
yas = 24 
print(18 <= yas <= 30)

# and or not
#and
kullanici_adi = "irem"
sifre = 2104
giriş_izni = (kullanici_adi == "irem") and (sifre == "123")
print(giriş_izni)

#or
puan = 100
uye = True
gecer_mi = (puan>110) or uye
print(gecer_mi)

#not
print(not True)

# if

sicaklik = 105

if sicaklik >= 100:
    print("Uyarı: Su Kaynıyor!")
    print("Ocağın altını kapatın.")
    print("Sıcaklık kontrol sistemi devrede.")

# Metnin içinde kelime arama
mesaj = "Kazandınız! Lütfen linke tıklayın"
if "link" in mesaj:
    print("Dikkat: Spam ihtimali!")

if "link" in mesaj:
    print("Dikkat Virüs İhtimali")

# if-else 
yas = 16
if yas >= 18:   
    print("Ehliyet kursuna başvurabilirsiniz.")
else:
    bekleme = 18 - yas
    print(f"Ehliyet alamazsınız. {bekleme} yıl daha bekleyin.")

sayi = 15
if sayi % 2 == 0:
    print("Bu bir ÇİFT sayıdır")
else:
    print("Bu bir TEK sayıdır")

# else if = elif
puan=100
if puan >= 85:
    print("Notunuz pekiyi (AA)")
elif puan >= 70:
    print("Notunuz iyi (BB)")
elif puan >= 50:
    print("Notunuz geçer (CC)")
else:
    print("Notunuz kaldınız (FF)")

#gerçek hayat seneryosu
sepet_tutari=500
vip_uye= True
if (sepet_tutari >= 550) or (vip_uye== True):
    kargo_ucreti: 0
    print("Tebrikler! Kargo Bedava. ")
else:
    kargo_ucreti = 40
    print(f"Kargo Ücreti: {kargo_ucreti} TL")
toplam_odeme = sepet_tutari 
print("Ödenecek toplam tutar", toplam_odeme)

#Kredi onay sistemi
maas = 70000
kredi_notu = 1600
if maas >= 40000:
    print("Maaş şartı sağlandı. Puan kontrol ediliyor...")
    if kredi_notu >=1500:
        print("Krediniz ONAYLANDI!")
    else:
        print("Maaşınız yeterli ancak puanınız düşük.")
else:
    print("Maaşınız kredi çekmek için yeterli değil.")
# nested if olan bu yapıyı hoca çok fazla tavsiye etmiyor

# for döngüsü
meyveler =["elma", "armut", "çilek", "nar"]
for m in meyveler:
    print("sepetteki meyve", m )

kelime = "PYTHON"
for harf in kelime:
    print("Harf:", harf)

# for ve range
#sadece bitiş belirleme 
for i in range(3):
    print(f"{i}. kez merhaba")

#başlangıç ve bitiş belirleme
for i in range(1, 4):
    print("sayı", i)

#adım miktarı ile atlama
for sayı in range(0, 10, 2):
    print("çift", sayı)

#While döngüsü
sayac = 1

while sayac <= 4:
    # Sayaç 4 ve 4'ten küçük olduğu SÜRECE:
    print(f"{sayac}. Tur tamamlandı.")

    # SONSUZ DÖNGÜYÜ ENGELLEMEK İÇİN:
    # Sayacı her turda 1 artırmalıyız ki
    # bir noktada 4'ü geçsin
    # ve koşul False olup döngü bitsin.
    sayac += 1

print("Yarış bitti! Sayacın son değeri:", sayac)

# Kapsamlı While Senaryosu: Şifre Doğrulama

dogru_sifre = ""
girilen_sifre = ""

# Girilen şifre doğru şifreye EŞİT OLMADIĞI SÜRECE dön:
while girilen_sifre != dogru_sifre:
    girilen_sifre = input("Lütfen şifrenizi girin: ")

    if girilen_sifre != dogru_sifre:
        print("HATA: Yanlış şifre, tekrar deneyin!\n")

# While koşulu False olduğunda (yani şifre eşitlendiğinde)
# döngü biter ve program buraya gelir.
print("Giriş Başarılı. Sisteme Hoşgeldiniz!")

#break ve continue
for sayi in range(1, 10):
    if sayi == 3:
        print("3'ü atlıyorum (continue)")
        continue  # 3'ü yazdırmaz, hemen başa dönüp 4'e geçer

    if sayi == 6:
        print("6'ya geldim, döngüyü kırıyorum (break)")
        break  # Döngüyü komple bitirir (7,8,9'a hiç bakmaz)

    print("Sayı:", sayi)

# Çıktı:
# Sayı: 1
# Sayı: 2
# 3'ü atlıyorum (continue)
# Sayı: 4
# Sayı: 5
# 6'ya geldim, döngüyü kırıyorum (break)

#LİSTE
# Liste Oluşturma
meyveler = ["Elma", "Muz", "Kiraz"]
karisik = [10, "Python", True, 3.14]

# Elemanlara İndeks ile Ulaşma (0'dan başlar)
print(meyveler[0])  # Elma
print(meyveler[-1])  # Kiraz (Son eleman)

# Slicing (Parçalama) [baş : bitiş]
sayilar = [10, 20, 30, 40, 50]
print(sayilar[1:4])  # [20, 30, 40] (4 dahil değil)

# Listedeki bir elemanı değiştirme (Listeler Mutable'dır)
meyveler[1] = "Çilek"
print(meyveler)  # ['Elma', 'Çilek', 'Kiraz']

# Listeye eleman ekleme ve çıkarma

diller = ["Python", "Java"]

# ELEMAN EKLEME
diller.append("C++")  # Sona ekler
print(diller)  # ['Python', 'Java', 'C++']

# 1. indekse (araya) JavaScript ekle, diğerlerini sağa kaydır
diller.insert(1, "JavaScript")
print(diller)  # ['Python', 'JavaScript', 'Java', 'C++']

# ELEMAN SİLME
diller.remove("Java")  # İsme göre bul ve sil

# pop() indeks ile siler
# Boş bırakılırsa en sondakini siler
silinen = diller.pop()  # C++ silindi
print("Silinen dil:", silinen)
print("Son durum:", diller)  # ['Python', 'JavaScript']

# SIRALAMA VE ARAMA
notlar = [45, 100, 85, 60, 100]

# KÜÇÜKTEN BÜYÜĞE SIRALAMA
notlar.sort()
print(notlar)

# BÜYÜKTEN KÜÇÜĞE SIRALAMA
notlar.sort(reverse=True)
print(notlar)

# LİSTEYİ TERSİNE ÇEVİRME
notlar.reverse()
print(notlar)

# ARAMA VE SAYMA
yuz_adedi = notlar.count(100)
print("Kaç tane 100 var:", yuz_adedi)

# 85 NOTU KAÇINCI İNDEKSTE?
sira = notlar.index(85)
print("85'in indeksi:", sira)

#Listeler ve Döngülerin gücü
sepet = [150, 30, 800, 45]
toplam = 0
kargo_bedava = []  # Boş bir liste oluşturduk

for fiyat in sepet:
    toplam += fiyat  # Hepsini topla

    # 100 TL üzeri ürünleri ayrı listeye atalım
    if fiyat > 100:
        kargo_bedava.append(fiyat)

print("Toplam Ödeme:", toplam)  # 1025
print("Kargosu Bedava Olanlar:", kargo_bedava)  # [150, 800]

# len() ile listede kaç eleman olduğunu bulabiliriz
print("Sepetteki ürün adedi:", len(sepet))  # 4

# DOĞRU KOPYALAMA (Shallow Copy)
liste_X = ["Python", "Java"]
liste_Y = liste_X.copy()  # Yeni ve bağımsız bir liste oluşturuldu

liste_Y.append("C++")

print("X Listesi:", liste_X)  # ['Python', 'Java']
print("Y Listesi:", liste_Y)  # ['Python', 'Java', 'C++']

#iç içe listeler (matrisler)
# 3 öğrencinin [Vize, Final] notları
sinif = [
    [50, 60],  # 0. Öğrenci
    [90, 85],  # 1. Öğrenci
    [30, 40]   # 2. Öğrenci
]

# 1. öğrencinin tüm notları
print(sinif[1])  # [90, 85]

# 1. öğrencinin SADECE Final notu (85'e ulaşmak)
# Önce 1. öğrenciyi seç, sonra onun içindeki 1. indeksi seç
print(sinif[1][1])  # 85

# 2. öğrencinin vize notu
print(sinif[2][0])  # 30

#Kurallı Liste
sayilar = [1, 2, 3, 4, 5]

# Eski / Klasik Yöntem
kareler_eski = []

for s in sayilar:
    kareler_eski.append(s ** 2)

# PYTHONIC YÖNTEM (List Comprehension)
kareler_yeni = [s ** 2 for s in sayilar]

print(kareler_yeni)  # [1, 4, 9, 16, 25]

# İçine IF şartı da eklenebilir (Sadece çift olanlar)
ciftler = [s for s in sayilar if s % 2 == 0]

print(ciftler)  # [2, 4]

#Demet (Tupple)
# Tuple oluşturma
renkler = ("Kırmızı", "Mavi", "Sarı")

# İndeksleme listelerle aynıdır
print(renkler[0])  # Kırmızı

# DEĞİŞTİRİLEMEZ (Immutable)
# renkler[0] = "Yeşil"  # HATA VERİR! (TypeError)
# renkler.append("Yeşil")  # HATA VERİR!
# Tuple'da append yoktur.

# Tek elemanlı Tuple (Virgül şart)
sahte_tuple = ("Python")
print(type(sahte_tuple))  # <class 'str'>

gercek_tuple = ("Python",)  # Virgül koyduk!
print(type(gercek_tuple))  # <class 'tuple'>

#tuple metotları ve unpacking
sonuclar = (10, 50, 10, 90)

print(sonuclar.count(10))  # 10 elemanından 2 tane var
print(sonuclar.index(90))  # 90 elemanı 3. indekste

print("--------------------")

# Bir kullanıcının verisi: (Ad, Yaş, Meslek)
kullanici = ("Ali", 25, "Mühendis")

# Paket Açma (Unpacking)
isim, yas, meslek = kullanici
print(isim, meslek)  # Ali Mühendis

# Python'da Hızlı Değişken Takası (Swap)
a = 10
b = 20

# Tuple mantığı ile tek satırda takas
a, b = b, a

print("a:", a, "b:", b)  # a: 20 b: 10

# Kümeler (Sets)
# Küme oluşturma (Tekrarlı elemanlar yazsak bile silinir)
sayilar = {1, 2, 3, 3, 3, 4, 4}
print(sayilar)  # {1, 2, 3, 4}

# Ekleme ve Silme (Append değil add kullanılır)
sayilar.add(5)
sayilar.add(5)  # İkinci 5'i eklemez
sayilar.remove(2)
print(sayilar)  # {1, 3, 4, 5}

# İndeks YOKTUR!
# print(sayilar[0])  # HATA (TypeError)

# Pratik: Bir listedeki tekrarlananları temizleme
isimler_listesi = ["Ali", "Ayşe", "Ali", "Ali"]

# Set'e çevir, temizle, tekrar listeye al
temiz_liste = list(set(isimler_listesi))

print(temiz_liste)  # ['Ayşe', 'Ali']

# Matematiksel Küme İşlemleri
a_grubu = {"Python", "Java", "C++"}
b_grubu = {"Java", "Go", "Rust"}

# BİLEŞİM (Union) - Her iki gruptaki tüm diller
print(a_grubu | b_grubu)
# {"Python", "Java", "C++", "Go", "Rust"}

# KESİŞİM (Intersection) - Ortak diller
print(a_grubu & b_grubu)
# {"Java"}

# FARK (Difference) - A'da olup B'de olmayanlar
print(a_grubu - b_grubu)
# {"Python", "C++"}

# SİMETRİK FARK - Sadece birinde olanlar
print(a_grubu ^ b_grubu)

# Sözlük Oluşturma {Key: Value}
ogrenci = {
    "ad": "Zeynep",
    "yas": 26,
    "bolum": "Mimar"
}

# Veriye (Value) Anahtar (Key) ile ulaşmak
print(ogrenci["ad"])  
print(ogrenci["bolum"])  

# Veriyi güncellemek
ogrenci["yas"] = 21

# Sözlüğe YENİ bir Anahtar-Değer eklemek
ogrenci["not_ortalaması"] = 4

print(ogrenci)
# {'ad': 'Ayşe', 'yas': 21, 'bolum': 'Yazılım', 'not_ortalaması': 3.5}

#Güvenli veri çekme get() metotu
araba = {
    "marka": "Tesla",
    "model": "Model 3"
}

# HATALI YAKLAŞIM:
# print(araba["renk"])  # KeyError! Program çöker.

# GÜVENLİ YAKLAŞIM: get()
print(araba.get("marka"))  # Tesla
print(araba.get("renk"))  # None (Çökmedi!)

# Bulamazsa bizim mesajımızı göstersin:
renk_bilgisi = araba.get("renk", "Renk bilgisi girilmemiş.")
print(renk_bilgisi)  # Renk bilgisi girilmemiş.

#Sözlük metotları: keys, values, items
urun = {
    "isim": "Laptop",
    "fiyat": 25000,
    "stok": 15
}

# Sadece Anahtarları (Keys) Almak
print(urun.keys())

# Sadece Değerleri (Values) Almak
print(urun.values())

# İkisini Birden Almak (Items)
# Liste içinde tuple'lar olarak döner
print(urun.items())

# sözlğkler ve for döngüsü
puanlar = {
    "Ahmet": 85,
    "Zeynep": 95,
    "Can": 60
}

# Standart Döngü (Sadece isimleri basar)
for kisi in puanlar:
    print(kisi)

print("----------------")

# Profesyonel Döngü (.items() ile iki değişkenli)
for isim, notu in puanlar.items():
    print(f"{isim} adlı öğrencinin notu: {notu}")

#iç içe sözcükler ve json benzerliği
kullanicilar = {
    1: {
        "ad": "Ahmet",
        "rol": "Admin"
    },
    2: {
        "ad": "Zeynep",
        "rol": "Kullanıcı"
    }
}

# 1 numaralı kullanıcının "ad" değerine ulaşmak
# Çift anahtar kullanımı!
isim = kullanicilar[1]["ad"]
print(isim)  # Ahmet

# 2 numaralı kullanıcının rolünü bulmak
print(kullanicilar[2]["rol"])  

#Fonksiyonu tanımlama def ve çağırma
# 1. Fonksiyonu Tanımlamak (Hazırlamak)
def merhaba_de():
    # Fonksiyonun içindeki kodlar da girintili olmalıdır
    print("Merhaba!")
    print("Sisteme hoşgeldiniz.")


# 2. Fonksiyonu Çağırmak (Çalıştırmak)
print("Program Başladı...")

merhaba_de()  # Çağırdık!
merhaba_de()  # İstediğimiz kadar çağırabiliriz

#Parametreler ve Argümanlar
# 'isim' adında bir parametre alıyor
def selamla(isim):
    print(f"Selamlar, {isim} bey/hanım!")

# 'Ahmet' argümanını yolluyoruz
selamla("Ahmet")
# Çıktı: Selamlar, Ahmet bey/hanım!

selamla("Zeynep")
# Çıktı: Selamlar, Zeynep bey/hanım!


# ÇOKLU PARAMETRE
def topla(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {sonuc}")

topla(10, 5)  # 10 + 5 = 15
topla(20, 30)  # 20 + 30 = 50

#En önemli kavram Return mantığı
# YALNIZCA PRINT YAPAN FONKSİYON (Değer Döndürmez)
def print_ile_kare_al(sayi):
    print(sayi ** 2)

sonuc1 = print_ile_kare_al(4)  # Ekrana 16 yazar ama...
print("Sonuc1'in içi:", sonuc1)  # None (İçi boştur!)


# RETURN YAPAN FONKSİYON (Değer Döndürür)
def return_ile_kare_al(sayi):
    return sayi ** 2

sonuc2 = return_ile_kare_al(4)  # Ekranda 16 yazmaz ama...
print("Sonuc2'nin içi:", sonuc2)  # 16 (Hesabı bize verdi!)


# Artık onu başka matematikte kullanabiliriz:
yeni_hesap = sonuc2 + 10
print(yeni_hesap)  # 26

# varsayılan (default) parametreler ve çoklu dönüş
# 1. Varsayılan (Default) Parametre
def hosgeldin(isim="Misafir"):
    print(f"Sisteme hoşgeldin, {isim}!")

hosgeldin("Zeynep") 
hosgeldin()         


# 2. Birden Fazla Değer Döndürme (Return)
def istatistik_getir(notlar):
    en_yuksek = max(notlar)
    en_dusuk = min(notlar)
    return en_yuksek, en_dusuk

sinif_notlari = [50, 90, 40, 100]

# Tuple Unpacking ile iki değeri yakalıyoruz
tavan, taban = istatistik_getir(sinif_notlari)

print("En yüksek:", tavan)  # 100
print("En düşük:", taban)   # 40

#Esnek Argümanlar
# *args Örneği (Sınırsız Sayı Toplama)
def coklu_topla(*sayilar):
    toplam = 0

    for s in sayilar:
        toplam += s

    return toplam


print(coklu_topla(10, 20))        # 30
print(coklu_topla(1, 2, 3, 4))   # 10


# **kwargs Örneği (Sınırsız İsimlendirilmiş Argüman)
def kisi_olustur(**bilgiler):
    print(bilgiler)  # Bilgiler bir sözlük (dictionary) olur


kisi_olustur(ad="Ali", yas=25, sehir="Bursa")

#Modern Python typhe hinting ve docstring
# Parametrelerin (str, int) ve Return (str) tiplerini belirttik
def kullanici_kayit(isim: str, yas: int) -> str:
    """
    Bu fonksiyon sisteme yeni bir kullanıcı kaydeder.

    Parametreler:
        isim (str): Kullanıcının ad ve soyadı.
        yas (int): Kullanıcının yaşı (18'den büyük olmalı).

    Dönüş (Return):
        (str) Başarı veya hata mesajı döndürür.
    """
    if yas < 18:
        return "Yaşınız tutmuyor."

    return f"{isim} başarıyla kaydedildi!"
mesaj = kullanici_kayit("Zeynep", 25)
print(mesaj)

# Lambda (anonim) fonksiyonlar
# 1. Klasik Yöntem (def)
def kare_al(x):
    return x ** 2
print(kare_al(5))  # 25


# 2. LAMBDA YÖNTEMİ (Tek Satır)
kare_lambda = lambda x: x ** 2
print(kare_lambda(5))  # 25


# Birden fazla parametre de alabilir
topla_lambda = lambda a, b: a + b
print(topla_lambda(10, 40))  # 50

# Fonksiyonel araçlar
sayilar = [1, 2, 3, 4, 5, 6]

# MAP Kullanımı (Tüm sayıların karesini alalım)
# Listenin her elemanı lambda'daki x yerine geçer
kareler = list(map(lambda x: x ** 2, sayilar))
print("Kareler:", kareler)
# [1, 4, 9, 16, 25, 36]


# FILTER Kullanımı (Sadece çift olanları ayıklayalım)
# Lambda fonksiyonu True döndürenleri tutar
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çift Sayılar:", ciftler)

#Yerel(Local) ve Küresel(Global) Değişkenler
mesaj = "Ben GLOBAL değişkenim"

def test_fonksiyonu():
    isim = "Ben LOCAL değişkenim"
    print("İçeriden okuyorum:", mesaj)  # Global'i okuyabilir
    print(isim)

test_fonksiyonu()

# Global olana dışarıdan ulaşabiliriz
print(mesaj)

# DİKKAT! Local değişkene DIŞARIDAN ULAŞILAMAZ!
# print(isim)  # HATA VERİR! (NameError)
# "isim" adlı değişken, fonksiyon bitince yok olur.

#Globali değiştirmek: global komutu
puan = 100  # Global değişken

# 1. Hatalı Deneme (Dışarıdakini değiştirmez)
def puan_artir_hata():
    puan = 500  # İçeride yeni bir local "puan" yarattı

puan_artir_hata()
print("Hatadan sonra puan:", puan)  # Hala 100!


# 2. Doğru Deneme (global anahtar kelimesi ile)
def puan_artir_dogru():
    global puan  # Dışarıdaki "puan" kutusunu içeri getir
    puan = 500  # Artık dışarıdakini güncelliyoruz

puan_artir_dogru()
print("Doğrudan sonra puan:", puan)  # 500 oldu!

# Hata Yakalama
# 1. Hatalı Yaklaşım (Çökmeye Müsait)
# yas = int(input("Yaşınız: "))
# Kullanıcı klavyeden A yazarsa ÇÖKER! (ValueError)
# print("Yaşınız:", yas)


# 2. Doğru Yaklaşım (Hata Yakalama)
#try:
    # Riskli bölge: Dönüşüm işleminde hata çıkabilir
    #yas = int(input("Yaşınızı rakamla girin: "))
    #print("Harika! Yaşınız:", 26)

#except:
    # try bloğunda herhangi bir satırda hata çıkarsa buraya düşer
    #print("HATA: Lütfen harf veya kelime girmeyin, rakam kullanın!")


# Program çökmediği için buradaki kodlar çalışmaya devam eder
#print("Program sonu...")

# Spesifik hatalar yakalamak
#try:
    #sayi1 = int(input("Bölünecek sayıyı girin: "))
    #sayi2 = int(input("Bölen sayıyı girin: "))

    #sonuc = sayi1 / sayi2

    #print("Sonuç:", sonuc)

#except ValueError:
    # Kullanıcı sayı yerine harf girdiyse
    #print("HATA: Sadece tam sayı girmelisiniz!")

#except ZeroDivisionError:
    # Kullanıcı bölen olarak 0 girdiyse
    #print("HATA: Hiçbir sayı sıfıra bölünemez!")

#except Exception as hata:
    # Beklenmeyen başka bir hata oluşursa
    #print("Bilinmeyen bir hata oluştu:", hata)

try:
    dosya_adi = "veriler.txt"

    # Dosyayı okumaya çalışıyoruz (Simülasyon)
    print(f"{dosya_adi} açılıyor...")

    hesaplama = 10 / 2

except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu")

else:
    # Hiç hata çıkmadığı için burası çalışacak
    print("İşlemler başarıyla tamamlandı. Sonuç:", hesaplama)

finally:
    # Hata olsa da olmasa da bu mesaj yazılacak!
    print("Dosya bağlantısı güvenle kapatıldı.")

#Kendi hatamızı fırlatmak: raise
def sisteme_kayit_ol(yas):
    # Eğer yaş 0'dan küçükse BİLİNÇLİ OLARAK hata fırlat
    if yas < 0:
        raise ValueError("Yaş negatif olamaz!")

    # 18'den küçükse başka bir hata fırlat
    if yas < 18:
        raise PermissionError("18 yaşından küçükler giremez.")

    return "Sisteme kayıt başarılı."


try:
    # Fırlatılan (raise edilen) hatayı burada yakalıyoruz
    sonuc = sisteme_kayit_ol(-5)
    print(sonuc)

except ValueError as err:
    print("Geçersiz Değer Hatası:", err)

except PermissionError as err:
    print("Yetki Hatası:", err)

