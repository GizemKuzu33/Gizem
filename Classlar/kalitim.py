""""KALITIM DERSİ"""
""""BU KOD HATA VERDİ HOCA DÜZELTİP GÖNDERECEK"""
# from abc import ABC, abstractmethod

# class Sekiller(ABC):
#     def __init__(self):
#         pass
#     @abstractmethod
#     def alan(self):
#         raise NotImplementedError("Bu fonksiyon yazılmalı...")
#     @abstractmethod
#     def cevresi(self):
#         raise NotImplementedError("Bu fonksiyon yazılmalı...")

# class Daire(Sekiller):
#     def __init__(self,yaricap):
#         self.yaricap = yaricap

#     def alan(self):
#         alan = 3*(self.yaricap**2)
#         return alan

# daire1 = Daire(5)
# print(daire1.alan())


# kalıtım örneği
# class Hayvan():
#     def __init__(self,adi,yasi,turu,cinsi):
#         self.adi = adi
#         self.yasi = yasi
#         self.turu = turu
#         self.cinsi = cinsi

#     def sesCikart(self):
#         pass
#     def yemekYer(self):
#         pass
#     def ozellikleriniyazdir(self):
#         return (f"adi:{self.adi}, yasi : {self.yasi}, turu : {self.turu}, cinsi: {self.cinsi}")
    
# class Kopek(Hayvan):
#     def __init__(self,adi,yasi,turu,cinsi):
#         super().__init__(adi,yasi,turu,cinsi)
#         self.turu = turu

#     def sesCikart(self):
#         print("havliyorum")

#     def yemekYer(self):
#         print("kopek maması yerim")

#     def ozellikleriniyazdir(self):
#         return super().ozellikleriniyazdir()
    
# kopek1 = Kopek("deniz",2,"terier","bi sey")
# print(kopek1.ozellikleriniyazdir())


