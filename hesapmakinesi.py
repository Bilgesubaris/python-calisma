print("Hesap Makinesi\n")

sayi1 = float(input("İlk sayıyı giriniz: "))
sonuc = sayi1

while True:
    print("\nYapmak istediğiniz işlemi seçiniz:")
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Çıkış")

    secim = input("Seçiminizi yapınız (1/2/3/4/5): ")

    if secim == '5':
        print("👉 Hesaplama sona erdi. Sonuç:", sonuc)
        break

    sayi2 = float(input("Sonraki sayıyı giriniz: "))

    if secim == '1':
        sonuc += sayi2
    elif secim == '2':
        sonuc -= sayi2
    elif secim == '3':
        sonuc *= sayi2
    elif secim == '4':
        if sayi2 != 0:
            sonuc /= sayi2
        else:
            print("❌ Sıfıra bölünemez!")
            continue
    else:
        print("❌ Geçersiz işlem seçimi!")
        continue

    print("✅ Güncel Sonuç:", sonuc)

