#absolutepath
dosyakonumu="C:\Gizem\dosyaislemleri\metin.txt"
#relativepath
relativedosyakonumu="dosyaislemleri\metin.txt"

# dosya=open(dosyakonumu,"r+",encoding="utf-8")
# print("dosya acıldıktan sonra konum:",dosya.tell())
# dosya.write("benim adım ebruli..."+"\n")
# icerik=dosya.read()
# print(icerik)
# print("yazdıktan sonra:",dosya.tell())
# icerik=dosya.readlines()
# dosya.writelines()


#  dosya.seek(0)
# print("dosya okunabilir mi:",dosya.readable())  
# dosya.close() 

# dosya=open(dosyakonumu,"r+",encoding="utf-8")
# icerik=dosya.readlines()
# icerik.insert(1,"benim adım batman")
# print(icerik)
# dosya.writelines(icerik)

# dosya=open(dosyakonumu,"r+",encoding="utf-8")
# dosya.read()
# dosya.close

import os
if os.path.exists(dosyakonumu):
    print("dosyayı buldum,işlem yapıyorum...")
    with open(dosyakonumu,"r+") as dosya:
        icerik=dosya.read()
        print(icerik)
else:
    print("dosya yok gözün kör olmasın...")
    
