import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import datetime as dt

pencere = tk.Tk()
pencere.title("Stok Kontrol Formu")
pencere.geometry("600x500")

def degerOku():
    data=[grMalzemeStokKodu.get(),
          grMalzemeAdı.get(),
          grMiktar.get(),
          grBirim.get(),
          grGirişTarihi.get_date(),
          grMalzemeninUretim.get(),
          grMalzemeninSonKullanmaTarihi.get_date()]
    print(data)

def formTemizle():
    grMalzemeStokKodu.delete(0,tk.END)
    grMalzemeAdı.delete(0,tk.END)
    grMiktar.delete(0,tk.END)
    grBirim.delete(0,tk.END)
    grGirişTarihi.set_date(dt.datetime.today())
    grMalzemeninUretim.set_date(dt.datetime.today())
    grMalzemeninSonKullanmaTarihi.get()
    

notebook = ttk.Notebook(pencere)
tab1=ttk.Frame(notebook)
notebook.add(tab1,text="Stok Giriş")

tab2=ttk.Frame(notebook)
notebook.add(tab2,text="Stok Çıkış")

notebook.pack(expand=True,fill="both")

#MALZEME GİRİŞ STOK KOD ETİKET VE GİRİŞ ARACI
etMalzemeStokKodu= tk.Label(tab1,text="Malzeme Stok Kodu")
etMalzemeStokKodu.grid(row=0,column=0,padx=5,pady=5,sticky="w")

grMalzemeStokKodu = tk.Entry(tab1,bd=0)
grMalzemeStokKodu.grid(row=0,column=1,padx=5,pady=5)

#MALZEME ADI ETİKET VE GİRİŞ ARACI
etMalzemeAdı= tk.Label(tab1,text="Malzeme Adı")
etMalzemeAdı.grid(row=1,column=0,padx=5,pady=5,sticky="w")

grMalzemeAdı = tk.Entry(tab1,bd=0)
grMalzemeAdı.grid(row=1,column=1,padx=5,pady=5)

#MİKTAR ETİKET VE GİRİŞ ARACI
etMiktar = tk.Label(tab1,text="Miktar")
etMiktar.grid(row=2,column=0,padx=5,pady=5)

grMiktar = tk.Entry(tab1,bd=0)
grMiktar.grid(row=2,column=1,padx=5,pady=5)

#BİRİM ETİKET VE GİRİŞ ARACI
etBirim =tk.Label(tab1,text="Birim")
etBirim.grid(row=3,column=0,padx=5,pady=5)

grBirim=tk.Spinbox(tab1,from_=0,to=1000,bd=0)
grBirim.grid(row=3,column=1,padx=5,pady=5)

#GİRİŞ TARİHİ ETİKET VE GİRİŞ ARACI
etGirişTarihi=tk.Label(tab1, text="Giriş Tarihi")
etGirişTarihi.grid(row=0, column=2, padx=5, pady=5)

grGirişTarihi=DateEntry(tab1,bd=0)
grGirişTarihi.grid(row=0, column=3, padx=5, pady=5)

#MALZEME ÜRETİM TARİHİ
etMalzemeninUretim=tk.Label(tab1, text="Malzemenin Üretim Tarihi")
etMalzemeninUretim.grid(row=1, column=2, padx=5, pady=5)

grMalzemeninUretim=DateEntry(tab1,bd=0)
grMalzemeninUretim.grid(row=1, column=3, padx=5, pady=5)

#MALZEME LOT NUMARASI
etLotNumarası=tk.Label(tab1, text="Lot Numarası")
etLotNumarası.grid(row=2, column=2, padx=5, pady=5)

grLotNumarası=tk.Entry(tab1,bd=0)
grLotNumarası.grid(row=2, column=3, padx=5, pady=5)

#MALZEME SON KULLANMA TARİHİ ETİKET VE GİRİŞ ARACI
etMalzemeninSonKullanmaTarihi=tk.Label(tab1, text="Malzemenin Son Kullanma Tarihi")
etMalzemeninSonKullanmaTarihi.grid(row=3, column=2, padx=5, pady=5)

grMalzemeninSonKullanmaTarihi=DateEntry(tab1,bd=0)
grMalzemeninSonKullanmaTarihi.grid(row=3, column=3, padx=5, pady=5,sticky="we")

#TAB2 WİDGETLARI
#ÜRETİME VERİLİŞ TARİHİ
etÜretimeVerilişTarihi=tk.Label(tab2, text="Üretime Veriliş Tarihi")
etÜretimeVerilişTarihi.grid(row=0, column=0, padx=5, pady=5)

grÜretimeVerilişTarihi=DateEntry(tab2,bd=0)
grÜretimeVerilişTarihi.grid(row=0, column=1, padx=5, pady=5)

etÇıktıMiktarı=tk.Label(tab2, text="Çıktı Miktarı")
etÇıktıMiktarı.grid(row=1, column=0, padx=5, pady=5)

#ÇIKTI MİKTARI
grÇıktıMiktarı=tk.Entry(tab2,bd=0)
grÇıktıMiktarı.grid(row=1, column=1, padx=5, pady=5)

etÇıktıLotNumarası=tk.Label(tab2, text="Çıktı Lot Numarası")
etÇıktıLotNumarası.grid(row=2, column=0, padx=5, pady=5)

grÇıktıLotNumarası=tk.Entry(tab2,bd=0)
grÇıktıLotNumarası.grid(row=2, column=1, padx=5, pady=5)

btnDegerOku= tk.Button(tab1,text="Deger Oku",command=degerOku)
btnDegerOku.grid(row=4,column=0)

btnDegerSil= tk.Button(tab1,text="Temizle",command=formTemizle)
btnDegerSil.grid(row=4,column=3)
    
pencere.mainloop()