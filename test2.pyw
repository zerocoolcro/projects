import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

# Datoteka za spremanje povijesti
DATOTEKA_POVIJESTI = "povijest.txt"

# Lista za spremanje povijesti unosa
povijest = []

# Funkcija za učitavanje povijesti iz datoteke
def ucitaj_povijest():
    if os.path.exists(DATOTEKA_POVIJESTI):
        with open(DATOTEKA_POVIJESTI, "r") as file:
            povijest.extend(file.readlines())

# Funkcija za spremanje povijesti u datoteku
def spremi_povijest():
    with open(DATOTEKA_POVIJESTI, "a") as file:
        file.write(povijest[-1] + "\n")  # Sprema zadnji uneseni podatak

# Funkcija za prikaz povijesti
def prikazi_povijest():
    povijest_prozor = tk.Toplevel()
    povijest_prozor.title("Povijest")

    if povijest:
        for zapis in povijest:
            label_zapis = tk.Label(povijest_prozor, text=zapis.strip())  # Uklanjamo "\n"
            label_zapis.pack(pady=5)
    else:
        label_no_data = tk.Label(povijest_prozor, text="Nema povijesti unosa.")
        label_no_data.pack(pady=10)

    # Dodavanje gumba za brisanje povijesti
    button_obrisi = tk.Button(povijest_prozor, text="Obriši povijest", command=obrisi_povijest)
    button_obrisi.pack(pady=10)

    # Dodavanje gumba za zatvaranje prozora
    button_zatvori = tk.Button(povijest_prozor, text="Zatvori", command=povijest_prozor.quit)
    button_zatvori.pack(pady=10)

# Funkcija za brisanje povijesti
def obrisi_povijest():
    povijest.clear()  # Očisti povijest u memoriji
    with open(DATOTEKA_POVIJESTI, "w") as file:
        file.write("")  # Očisti datoteku
    messagebox.showinfo("Obrisano", "Povijest je obrisana.")  # Obavijest korisniku

# Funkcija za zatvaranje cijelog programa
def zatvori_program():
    global root
    if hasattr(root, "destroy"):        
        root.quit()  # Zaustavi Tkinter mainloop
        root.destroy()  # Uništi sve Tkinter prozore

# Funkcija za prikaz treće stranice
def treca_str(marka, model, preostalo_gorivo, preostali_km):
    # Spremanje trenutnog rezultata u povijest s datumom i vremenom
    vrijeme = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    novi_zapis = f"Datum: {vrijeme}, Auto: {marka} {model}, Preostalo gorivo: {preostalo_gorivo:.2f} L, Preostali kilometri: {preostali_km:.2f} km"
    povijest.append(novi_zapis)
    spremi_povijest()  # Spremi novi unos u datoteku

    # Kreiranje glavnog prozora za treću stranicu
    global root  # Moramo koristiti globalnu varijablu root
    root = tk.Tk()
    root.title("Rezultati")

    label_info = tk.Label(root, text=f"Auto: {marka} {model}")
    label_info.pack(pady=10)

    label_result = tk.Label(root, text=f"Preostalo gorivo: {preostalo_gorivo:.2f} litara\n"
                                       f"Možete preći još: {preostali_km:.2f} kilometara.")
    label_result.pack(pady=20)

    # Dugme za prikaz povijesti
    button_povijest = tk.Button(root, text="Pokaži povijest", command=prikazi_povijest)
    button_povijest.pack(pady=10)

    # Dugme za zatvaranje aplikacije
    button_exit = tk.Button(root, text="Zatvori", command=zatvori_program)
    button_exit.pack(pady=10)

    root.mainloop()
