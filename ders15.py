"""metin="python123program456"

harf_sayısı=0
numara_sayısı=0

for harf in metin:
    if harf.isalpha():
        harf_sayısı+=1

    if harf.isdigit():
        numara_sayısı+=1    

print("metin içinde {} adet harf ve {} \ adet sayı bulunmaktadır".format(harf_sayısı,numara_sayısı))        
"""
"""metin="python123program456"

aranacak_harf="p"

adedi= metin.count(aranacak_harf)


print(metin.count(aranacak_harf))
"""
"""metin="ey edip adanada pide ye"

if metin == metin [::-1]:
    print("palindromdur")
else:
    print("değildir")"""

"""liste1=[1,5,3,6,9]    
liste2=[8,4,7,2,6]

liste3=liste1.copy()
liste3.extend(liste2)
print(liste3)

essizliste=liste1.copy()

for eleman in liste2:
    if eleman in essizliste:
        None
    else:
        essizliste.append(eleman)
print(essizliste)

benzersizliste=[]

for item in liste1:
    if item in liste2:
        benzersizliste.append(item)

for item in liste2:
    if item not in liste1:
        benzersizliste.append(item)

print(benzersizliste)

print(max(liste1))
print(min(liste1))"""

"""

"""
"""while True :
        cevap = int (input("Bir sayı giriniz:"))

        if cevap >= 1 and cevap <= 100:

            if cevap % 3 == 0 and cevap % 5 == 0:
                print("Fizz Buzz")

            elif cevap % 3 == 0 :
                print("Fizz")

            elif cevap % 5 == 0:
                print("Buzz")

            else:
                print("Hiç birine uymadı")


        else:
          if cevap == 0:
            print("çıkıyoruz...")
            break    
          print("Girdiğiniz sayı limit dışı")
"""

# 1    2     3 
# taş kağıt makas
input("""Seçiminiz :
      1.Taş 
      2.Kağıt 
      3.Makas
      q.Çıkış
:""")
if not cevap.isdigit(and cevap == "q":
   print("çıkış")
   #break

rastgelesayı = radint (1,3)
    