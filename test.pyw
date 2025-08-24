import tkinter as tk
from tkinter import messagebox
import test1  # Uvoz druge stranice
import re  # Uvoz regex modula za validaciju

# Funkcija za validaciju unosa marke automobila
def validiraj_marku_unos(unos):
    # Dozvoljena su samo slova i maksimalno 15 znakova
    if re.fullmatch(r"[A-Za-z]{1,15}", unos):
        return True
    else:
        return False

# Funkcija za prelaz na drugu stranicu
def prelaz():
    marka = entry_marka.get()
    model = entry_model.get()
    
    # Provjera validnosti marke automobila
    if not validiraj_marku_unos(marka):
        messagebox.showerror("Greška", "Marka automobila smije sadržavati samo slova i maksimalno 15 znakova.")
        return

    if marka and model:
        root.destroy()  # Zatvaranje prve stranice
        test1.druga_str(marka, model)  # Prelaz na drugu stranicu sa markom i modelom
    else:
        messagebox.showerror("Greška", "Unesite marku i model automobila")

# Kreiranje glavnog prozora za prvu stranicu
root = tk.Tk()
root.title("Dobrodošli u AutoDomet")
root.geometry("400x300")

# Unos marke i modela
label_marka = tk.Label(root, text="Unesite marku automobila:")
label_marka.pack(pady=10)

entry_marka = tk.Entry(root)
entry_marka.pack(pady=5)

label_model = tk.Label(root, text="Unesite model automobila:")
label_model.pack(pady=10)

entry_model = tk.Entry(root)
entry_model.pack(pady=5)

button_nastavi = tk.Button(root, text="Nastavi", command=prelaz)
button_nastavi.pack(pady=20)

# Pokretanje prve stranice
root.mainloop()
