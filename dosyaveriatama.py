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
