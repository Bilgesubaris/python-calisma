import random

# 100 adet rastgele tam sayı üretme
sayilar = random.sample(range(1, 101), 100)

# Asal ve asal olmayan sayıları listeleme
asallar = []
bolunurler = []

for sayi in sayilar:
  if sayi <= 1:
    bolunurler.append(sayi)
  else:
    asal = True
    for i in range(2, int(sayi**0.5) + 1):
      if sayi % i == 0:
        asal = False
        break
    if asal:
      asallar.append(sayi)
    else:
      bolunurler.append(sayi)

# Dosyalara yazdırma
with open("asal.txt", "w") as f:
  f.write(" ".join(str(asal) for asal in asallar))
with open("bolunur.txt", "w") as f:
  f.write(" ".join(str(bolunur) for bolunur in bolunurler))

print("İşlem tamamlandı! Asal sayılar 'asal.txt' ve asal olmayanlar 'bolunur.txt' dosyasına kaydedildi.")

def sayi_olustur(dosya):
    with open('dosya.txt','w') as file:
     sayi= random.sample(range(1, 101), 100)
     file.write(f"{sayi}\n")

def asal_mi(sayi):
    for i in range (0,sayi):
      if sayi%i==0:
        return False
      else:
        return True

def dosya_yaz(dosya,asal,bolunur):
 with open('dosya','r') as file:
  sayilar =dosya.readlines()
  with open('asal','w') as asal:
   with open('bolunur','w') as asal:

    for sayi in sayilar:
      sayi=int(sayi.strip())
      if asal_mi(sayi):
        asal.write(f"{sayi}\n")
      else :
       bolunur.write(f"{sayi}\n")
