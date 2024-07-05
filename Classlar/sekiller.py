# Nesne oluşturma,İÇİNE DEĞER ATAMA,KULLANMA
# class Ucgen:
#     """Bu bir ucgen sekil sınıf taslağı"""

#     def __init__(self,taban,kenar2,kenar3,yukseklik):
#         print("Contructor calıstı...")
#         self.kenar2 = kenar2
#         self.kenar3 = kenar3
#         self.taban = taban
#         self.yukseklik = yukseklik
    
#     def alanı(self):
#         return (self.taban * self.yukseklik)/2
    
#     def cevre(self):
#         return self.taban + self.kenar2 + self.kenar3
    
#     def __del__(self):
#         print("Nesne hafızadan silindi...")

# class daire():
#     """Daire sınıfının nesne taslağı"""

#     def __init__(self,yarıcap):
#         self.yarıcap = yarıcap

#     def alanı(self):
#         return 3*(self.yarıcap**2)
    
#     def cevre(self):
#         return 2*3*self.yarıcap

# daire = daire(5)
# print(daire.cevre())
# print(daire.alanı())  

# class Dortgen():
#     """Dortgen sınıfının nesne taslağı"""

#     def __init__(self,kenar1,kenar2):
#         self.kenar = kenar1
#         self.kenar2 = kenar2
#     def alanı(self):
#         return (self.kenar2*self.kenar)
#     def cevre(self):
#         return 2*(self.kenar+self.kenar2)
    
# dortgen = Dortgen(4,2)
# print(dortgen.alanı())
# print(dortgen.cevre())

        # print("Taban = ", taban, "yuksek:",yukseklik)

# ucgen1 = Ucgen(taban=5,yukseklik=3,kenar2=4,kenar3=3)

# print(ucgen1.yukseklik)
# print("Alanı:",ucgen1.alanı())
# print("cevresi :", ucgen1.cevre())

# print(ucgen1.__doc__)

# class Kitap():
#     def __init__(self,kitapadı,tür,yazar):
#        self.kitapadı = kitapadı
#        self.tür = tür
#        self.yazar = yazar

#     def bilgileridok(self):
#         print(self.kitapadı)
#         print(self.tür)
#         print(self.yazar)

# kitap = Kitap("suc ve ceza","psikoloji","Dostoyevski")
# kitap.bilgileridok() 

class Kopek():
     def __init__(self,kopekcinsi,tür,yası,rengi):
        self.kopekcinsi = kopekcinsi
        self.tür = tür
        self.yası = yası
        self.rengi = rengi
     def bilgileridok(self):
         print(self.kopekcinsi)
         print(self.tür)
         print(self.yası)
         print(self.rengi)

kopek = Kopek("fino","pomeranian","3","sarı")
kopek.bilgileridok()