print("""********************************
Yapmak İstediğiniz işlemi seçiniz:

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
****************************************
""")
while True:
    islem = input("İşlem Seçiniz (Çıkış için 'b' ya basalım): ")
    if islem == 'b':
        print("Çıkılıyor...")
        quit()
    elif islem == "1":
        print("------Toplama İşlemi------")
        sayi1 = int(input("1.Sayıyı Giriniz: "))
        sayi2 = int(input("2.Sayıyı Giriniz: "))
        print("{}  +   {}    =  {}".format(sayi1, sayi2, sayi1+sayi2))
    elif islem == "2":
        print("------Çıkarma İşlemi------")
        sayi1 = float(input("1.Sayıyı Giriniz: "))
        sayi2 = float(input("2.Sayıyı Giriniz: "))
        print("{}  -   {}    =  {}".format(sayi1, sayi2, sayi1-sayi2))
    elif islem == "3":
        print("------Çarpma İşlemi------")
        sayi1 = float(input("1.Sayıyı Giriniz: "))
        sayi2 = float(input("2.Sayıyı Giriniz: "))
        print("{}  x   {}    =  {}".format(sayi1, sayi2, sayi1*sayi2))
    elif islem == "4":
        print("------Bölme İşlemi------")
        try:
            sayi1 = int(input("1.Sayıyı Giriniz: "))
            sayi2 = int(input("2.Sayıyı Giriniz: "))
            print("{}  /   {}    =  {:.2f}".format(sayi1, sayi2, sayi1/sayi2))
        except ZeroDivisionError:
            print("Bir sayıyı 0'a bölemezsiniz!")
        except ValueError:
            print("Lütfen sadece sayı girin!")
    else:
        print("Geçersiz Seçenek...")
