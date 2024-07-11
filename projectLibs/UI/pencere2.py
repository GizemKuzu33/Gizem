import tkinter as tk
from tkinter import ttk
import time as t

pencere = tk.Tk()
pencere.title("User İnterface")
pencere.geometry("800x600")
pencere.resizable(False,False)

lblEtiket=tk.Label(pencere,text="Bu bir etiket",font=("Arial",15),bd=2,relief="solid")
# lblEtiket.place(x=50,y=50)
lblEtiket.grid(row=0,column=0,padx=5,pady=5)

enGiris = tk.Entry(pencere,width=15,font=("Helvetica",15),bg="blue",fg="white",bd=3)
enGiris.grid(row=1, column=0,padx=5,pady=10)

btnDugme  = tk.Button(pencere,text="Tıkla",bg="red",fg="white",bd=2)
btnDugme.grid(row=0,column=1,padx=5,pady=5)

deger = ["Deger1","Deger2","Deger3"]
cmbBox = ttk.Combobox(pencere,values=deger)
cmbBox.grid(row=1,column=1,padx=5,pady=5)

frmTabela = tk.Frame(pencere)
frmTabela.grid(row=0,column=4)

lblEtiket2 = tk.Label(frmTabela,text="Frame Üstü", font=10)
lblEtiket2.pack(side=tk.LEFT,padx=5,pady=5)

btnDugme2 = tk.Button(frmTabela,text="Frm Tıkla", font=10)
btnDugme2.pack(side=tk.LEFT,padx=5,pady=5)

rdButton = tk.Radiobutton(pencere, text="Grp 1 Button 1",variable=1,value=1)
rdButton.grid(row=2,column=0)

rdButton1 = tk.Radiobutton(pencere, text="Grp 1 Button 2",variable=1,value=2)
rdButton1.grid(row=3,column=0)
rdButton1.select()


rdButton2 = tk.Radiobutton(pencere,text="Grp 2 Button 1",variable=1,value=3)
rdButton2.grid(row=4,column=0)

rdButton3 = tk.Radiobutton(pencere,text="Grp 2 Button 2",variable=1,value=34)
rdButton3.grid(row=5,column=0)
rdButton3.select()

btn3= tk.Button(pencere,text="Extra",font=15)
btn3.grid(row=6,column=0)

listBox = tk.Listbox(pencere, height=5)
listBox.insert(1,"İlk Eleman")
listBox.insert(2,"İkinci Eleman")
listBox.insert(3,"Üçüncü Eleman")
listBox.grid(row=3,column=1,rowspan=4)

slider = tk.Scale(pencere,from_=0, to=100,orient=tk.HORIZONTAL)
slider.grid(row=2,column=3,columnspan=3,rowspan=2)

spinner = tk.Spinbox(pencere,from_=0,to=100)
spinner.grid(row=10,column=20)

cBox = tk.Checkbutton(pencere,text="Python")
cBox.grid(row=10, column=4)

pBar = ttk.Progressbar(pencere, length=100, mode="indeterminate")
pBar.grid(row=11,column=4)
for i in range(100):
    pBar["value"] = i
    t.sleep(0.1)
    pencere.update()

pencere.mainloop() 