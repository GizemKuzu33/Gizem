# import os
# from cryptography.fernet import Fernet

# dosyakonumu="C:\\Gizem\\dosyaislemleri\\sifre.txt"
# anahtarkonumu="C:\\Gizem\\dosyaislemleri\\key.data"
# #sadecebirkere
# def anahtarolustur():
#     key = Fernet.generate_key()
#     with open(anahtarkonumu,"wb") as dosya:
#         dosya.write(key)

# def anahtaroku():
#     if not os.path.exists(anahtarkonumu):
#         print("dosya olusturuldu...")
#         anahtarolustur()
#     with open(anahtarkonumu,"rb") as file:
#         key=file.read()
#         return key 
    
# anahtarolustur()
# key=anahtaroku()
# anahtar=Fernet(key)

#     # print("anahhtar", key)

# def tumunugoruntule(dosyayolu):
#     global anahtar
#     if os.path.exists(dosyayolu):

#         with open(dosyayolu,"r") as dosya:
#             icerik=dosya.readlines()
#             for satir in icerik:
#                 kullanıcıadı,sifre=satir.replace("\n","").split(":")
#                 sifre=anahtar.decrypt(sifre.encode()).decode()
#                 print("kullanıcı adı:{},sifre:{}".format(kullanıcıadı,sifre))
#     else:
#         print("dosya mevcut degil...")
# def kullanıcıekle(dosyayolu):
#     global anahtar
#     if os.path.exists(dosyayolu):
#         yenikullanıcıadı=input("kullanıcı adı giriniz")
#         yenisifre=input("sifre giriniz:")
#         yenisifre=anahtar.encrypt(yenisifre.encode()).decode()
#         with open(dosyayolu,"a+") as dosya:
#             dosya.write(yenikullanıcıadı+":"+yenisifre+"\n")
#     else:
#         print("dosya mevcut degil...")
#         exit()
# def kullanıcısil(dosyayolu):
#     if os.path.exists(dosyayolu):
#         kullanıcıadı=input("silinecek kullanıcı adı giriniz:")
#         with open(dosyayolu,"r") as dosya:
#             tumicerik=dosya.read()
#             if kullanıcıadı in tumicerik:
#                 print("yok olum böyle biri")
#                 return
            
#             dosya.seek(0) 
#             icerik=dosya.readlines()


#         for i,satir in enumerate(icerik):
#             if kullanıcıadı in satir:
#                 icerik.pop(i)


#         with open(dosyayolu,"w") as dosya:
#             dosya.writelines(icerik)

#     else:
#         print("dosya mevcut degil")

# def sifredegistirme(path):
#     global anahtar
#     if os.path.exists(path):
#         kullanıcıadı=input("kullanıcı adı giriniz:")
#         with open(path,"r") as dosya:
#             tumicerik=dosya.read()
#             if kullanıcıadı not in tumicerik:
#               print("yok olum böyle biri")
#               return
            
#             dosya.seek(0)
#             icerik=dosya.readlines()

#         for idx,satir in enumerate(icerik):
#             if kullanıcıadı in satir:
#              kullanıcıadı,sifre=satir.replace("\n","").split(":")
#              sifre=input("sifre giriniz:")
#              sifre=anahtar.encrypt(sifre.encode()).decode()
#              icerik[idx]=kullanıcıadı+":"+ sifre +"\n"
#              break

#         with open(path,"w") as dosya:
#             dosya.writelines(icerik)

        
           
#     print("secenekleriniz:\n"
#       "1.kullanıcı ve sifre görüntüle\n"
#       "2.kullanıcı ekle\n"
#       "3.kullanıcı silme\n"
#       "4.sifre degistirme\n"
#       "5.anahtar olustur\n"
#       "6.cıkıs\n"
#       "islem >:")
# cevap=input("bir secenek seciniz:")
# if cevap=="1":
#      sifregoruntule(dosyakonumu)
#     #tumunugoruntule
# elif cevap=="2":
#      kullanıcıekle(dosyakonumu)
#     #kullanıcıekle
# elif cevap=="3":
#      kullanıcısil(dosyakonumu)
#     #kulanıcısilme
# elif cevap=="4":
#     sifredegistirme(dosyakonumu)
#     #sifredegistirme
# elif cevap=="5":
#      anahtarolustur()
#      key= anahtaroku()
#      anahtar= Fernet(key)
# elif cevap=="6":
#     exit()
# else:
#      print("adamın canını sıkma...")

dosyaKonumu="C:\\Gizem\\dosyaislemleri\\sifre.txt"
anahtarKonumu="C:\\Gizem\\dosyaislemleri\\key.data"

class Sifreyonetici():
    def __init__(self,dosyayolu,anahtaryolu):
        self.dosyaKonumu = dosyayolu
        self.anahtarKonumu = anahtaryolu

def anahtarOlustur(self):
    key = Fernet.generate_key()
    with open(self.anahtarKonumu,"wb") as dosya:
        dosya.write(key)

def anahtarOku(self):
    if not os.path.exists(aself.anahtarKonumu):
        print("Dosya olusturuldu...")
        anahtarOlustur()
    with open(self.anahtarKonumu, "rb") as file:
        key = file.read()
        return key

def tumunuGoruntule():
    if os.path.exists():
        with open(self.dosyaKonumu, "r") as dosya:
            for line in dosya:
                kullanici, sifre = line.replace("\n","").split(":")
                sifre = anahtar.decrypt(sifre.encode()).decode()
                print(f"Kullanıcı Adı: {kullanici}\t Sifre: {sifre}")
    else:
        print("Belirtilen konumda dosya mevcut değil...")
        
def kullaniciEkle(dosyaYolu):
    if os.path.exists(dosyaYolu):
        yeniKullaniciAdi = input("Kullanıcı Adı Giriniz :")
        yenSifre = input("Sifre Giriniz :")
        yenSifre = anahtar.encrypt(yenSifre.encode()).decode()

        with open(dosyaYolu, "a") as dosya:
            dosya.write(yeniKullaniciAdi+":"+yenSifre + "\n")
    else:
        print("Dosya mevcut değil...")
        exit()

def kullaniciSil(dosyaYolu):
    if os.path.exists(dosyaYolu):
        kullaniciAdi = input("Silinecek Kullanıcı Adini Girniz : ")
        with open(dosyaYolu, "r") as dosya:
            tumIcerik = dosya.read()
            if kullaniciAdi not in tumIcerik:
                print("Yok olum böle biri")
                return 
            
            dosya.seek(0)
            icerik = dosya.readlines()

        for i, satir in enumerate(icerik) :
            if kullaniciAdi in satir:
                icerik.pop(i)
            
        with open(dosyaYolu,"w") as dosya:
            dosya.writelines(icerik)

    else:
        print("Dosya yok...")

def sifreDegistirme(dosyaYolu):
    if os.path.exists(dosyaYolu):
        kullaniciAdi = input("Kullanıcı Adını Giriniz : ")
        with open(dosyaYolu, "r") as dosya:
            tumIcerik = dosya.read()
            if kullaniciAdi not in tumIcerik:
                print("Yok olum böle biri")
                return 

            dosya.seek(0)
            icerik = dosya.readlines() 
        
        for idx, satir in enumerate(icerik):
            if kullaniciAdi in satir:
                kullaniciAdi, sifre = satir.replace("\n","").split(":")
                sifre = input("Sifre Giriniz : ")
                sifre = anahtar.encrypt(sifre.encode()).decode()
                icerik[idx] = kullaniciAdi + ":" + sifre + "\n"
                break

        with open(dosyaYolu, "w") as dosya:
            dosya.writelines(icerik)


def main():
    print("Seçenekleriniz :\n"
        "1. Kullanıcı ve Şifre Görüntüle\n"
        "2. Kullanıcı Ekle\n"
        "3. Kullanıcı Silme\n"
        "4. şifre Değiştirme\n"
        "5. Anahtar Olustur\n"
        "6.Çıkış\n")

    cevap = input("Seçiminiz :")

    if cevap==  "1":
        tumunuGoruntule(dosyaKonumu)
        #TumunuGoruntule
    elif cevap == "2":
        kullaniciEkle(dosyaKonumu)
        #Kullanıcı Ekle
    elif cevap =="3":
        kullaniciSil(dosyaKonumu)
        #Kullanıcı Silme
    elif cevap == "4":
        sifreDegistirme(dosyaKonumu)
        #Sifre Değistirme

    elif cevap == "5":
        anahtarOlustur()

    elif cevap == "6":
        exit()
    else:
        print("Adamın canını sıkma... ")



if __name__ == "__main__":
    print("Bu aslında kütüphane dosyası...")
    tumunuGoruntule(dosyaKonumu)