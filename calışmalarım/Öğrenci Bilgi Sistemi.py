ogrenciler = {
    101: ["Zeynep", 95],
    102: ["İrem", 90]
}


def ogrenci_ekle():
    try:
        numara = int(input("Öğrenci numarası: "))
        isim = input("Öğrenci adı: ")
        notu = int(input("Öğrenci notu: "))

        if notu < 0 or notu > 100:
            print("HATA: Not 0-100 arasında olmalıdır.")
            return

        ogrenciler[numara] = [isim, notu]

        print("Öğrenci başarıyla eklendi.")

    except ValueError:
        print("HATA: Numara ve not sayı olmalıdır.")


def ogrencileri_listele():
    if len(ogrenciler) == 0:
        print("Henüz kayıtlı öğrenci yok.")
    else:
        print("\n--- ÖĞRENCİ LİSTESİ ---")

        for numara, bilgiler in ogrenciler.items():
            print(
                f"Numara: {numara} | "
                f"İsim: {bilgiler[0]} | "
                f"Not: {bilgiler[1]}"
            )


while True:

    print("\n===== ÖĞRENCİ BİLGİ SİSTEMİ =====")
    print("1 - Öğrenci Ekle")
    print("2 - Öğrencileri Listele")
    print("3 - Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        print("Program kapatılıyor...")
        break
    else:
        print("HATA: Lütfen 1, 2 veya 3 seçiniz.")
