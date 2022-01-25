"""Problem 2
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın."""

a= int(input("1.sayı:"))
b = int(input("2.sayı:"))
ortak_bolen = []
buyukSayı = 0
if a > b :
    buyukSayı= a
else:
    buyukSayı = b
for i in range(1,buyukSayı) :
    if (a % i ==0) and (b % i ==0) :
        ortak_bolen.append(i)
print("{} ve {} EBOB'u:{}".format(a,b,max(ortak_bolen)))
