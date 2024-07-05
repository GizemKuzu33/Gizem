import tkinter as tk



root= tk.Tk()
root.title( "Merhaba Python")
root.geometry("300x50")

etiket=tk.Label(root,text="Metin", font=30)
etiket.pack(side=tk.LEFT, padx=5)


root.mainloop()