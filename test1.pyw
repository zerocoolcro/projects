import tkinter as tk
from tkinter import messagebox
import test2  # Uvoz treće stranice

class Auto:
    def __init__(self, gorivo_na_sto_km):
        self.gorivo_na_sto_km = gorivo_na_sto_km

    def izracunaj_preostalo_gorivo(self, uliveno_gorivo, predjeni_km):
        potrosnja_po_km = self.gorivo_na_sto_km / 100
        potroseno_gorivo = predjeni_km * potrosnja_po_km
        preostalo_gorivo = uliveno_gorivo - potroseno_gorivo
        preostali_km = preostalo_gorivo / potrosnja_po_km if preostalo_gorivo > 0 else 0
        return preostalo_gorivo, preostali_km

# Funkcija koja se poziva kada korisnik pritisne dugme "Izračunaj"
def izracunaj(marka, model):
    try:
        uliveno_gorivo = float(entry_gorivo.get())
        predjeni_km = float(entry_km.get())
        potrosnja = float(entry_potrosnja.get())  
        auto = Auto(gorivo_na_sto_km=potrosnja)
        preostalo_gorivo, preostali_km = auto.izracunaj_preostalo_gorivo(uliveno_gorivo, predjeni_km)
        
        root.destroy()  # Zatvaranje druge stranice
        test2.treca_str(marka, model, preostalo_gorivo, preostali_km)  # Prelaz na treću stranicu
    except ValueError:
        messagebox.showerror("Greška", "Molimo unesite validne brojeve!")

def druga_str(marka, model):
    global root, entry_gorivo, entry_km, entry_potrosnja
    
    # Kreiranje glavnog prozora aplikacije
    root = tk.Tk()
    root.title(f"{marka} {model} - Unos podataka")

    label1 = tk.Label(root, text="Unesite količinu ulivenog goriva (u litrama):")
    label1.pack()

    entry_gorivo = tk.Entry(root)
    entry_gorivo.pack()

    label2 = tk.Label(root, text="Unesite broj pređenih kilometara:")
    label2.pack()

    entry_km = tk.Entry(root)
    entry_km.pack()

    label3 = tk.Label(root, text="Unesite potrošnju vašeg auta (litara na 100 km):")
    label3.pack()

    entry_potrosnja = tk.Entry(root)
    entry_potrosnja.pack()

    button_izracunaj = tk.Button(root, text="Izračunaj", command=lambda: izracunaj(marka, model))
    button_izracunaj.pack()


    root.mainloop()
