import tkinter as tk

pencere = tk.Tk()
pencere.title("ilk UI")

lblEtiket = tk.Label(pencere,text="bu bir label",bd=0)
lblEtiket.pack(side=tk.LEFT,padx=30,pady=30)

enGiris = tk.Entry(pencere, width = 20, font=30, bg="purple",fg="white",bd=0)
enGiris.pack(side=tk.LEFT,padx=10)
btnDugme = tk.Button(pencere,text="Tıkla",bg="blue",fg="yellow",border=3)
btnDugme.pack(side=tk.LEFT,padx=10)

pencere.geometry("600x400")

pencere.mainloop()