import random
tekrar= int(input("Dizinin uzuluğunu giriniz: "))
dizi=[]
for i in range (tekrar):
 sayi= random.randint(0,100)
 dizi.append(sayi)
print(dizi)
