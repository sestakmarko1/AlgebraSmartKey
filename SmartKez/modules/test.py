import tkinter as tk


#pozivne funkcije
def on_click():
    print('I was clicked')

def on_change_label():
    labela.pack_forget()

#osnovni prozor uvijek ide prvi tj prva stvar koju definiramo
root = tk.Tk()

# postavljamo osnovne parameter window
# nisu obvezne
root.title('NAslov prozora')
root.geometry('600x400')

# dodvanje samih elementa 
ne_klikabilni_gumb = tk.Button(
    root, 
    text='Gumb',
    bg='red',
    activebackground='green')

klikabilini_gumb = tk.Button(
    root, 
    text="click me!",
    command=on_click
    )

promijeni_labelu = tk.Button(
    root,
    text='Change label',
    command=on_change_label
    )

labela = tk.Label(
    root,
    text='Obicna labela',
    font=('Segoe UI', 16)
    )

# tk.Radiobutton()
# tk.Checkbutton()
# tk.Frame()
# tk.Image()
# tk.Menu()
# tk.Scrollbar()
# tk.Text()
# ...

# geometrija
ne_klikabilni_gumb.pack()
klikabilini_gumb.pack(
        padx=10,
        pady=30
    )
promijeni_labelu.pack(
    padx=30,
    pady=30
    )
labela.pack()

# konacno pokrecemo prikaz
root.mainloop() # -> glavni loop, zamislite kao beskonacni while koji generira izlged samog prozora