import tkinter as tk
import test2  # Uvoz modula za povijest

def prikazi_historiju():
    # Kreiramo okvir (Frame) za povijest u glavnom prozoru
    frame_history = tk.Frame(root)  # Umjesto Toplevel() koristimo Frame u glavnom prozoru
    frame_history.pack(pady=20)

    # Funkcija za brisanje povijesti
    def obrisi_povijest():
        # Očisti povijest iz datoteke i iz memorije
        test2.povijest.clear()
        with open(test2.DATOTEKA_POVIJESTI, "w") as file:
            file.write("")  # Očisti datoteku
        label_info.config(text="Povijest je obrisana.")
        # Brišemo sve postojeće oznake nakon što obrišemo povijest
        for widget in frame_history.winfo_children():
            if isinstance(widget, tk.Label) and widget != label_info:
                widget.destroy()

    # Inicijalizacija label_info
    label_info = tk.Label(frame_history)
    label_info.pack(pady=10)

    # Učitavanje povijesti
    if not test2.povijest:
        label_info.config(text="Nema unesenih podataka")
    else:
        label_info.config(text="Povijest podataka:")
        for unos in test2.povijest:
            label = tk.Label(frame_history, text=unos.strip())  # Prikaži povijest
            label.pack(pady=5)

    # Dodavanje gumba za brisanje povijesti
    button_obrisi = tk.Button(frame_history, text="Obriši povijest", command=obrisi_povijest)
    button_obrisi.pack(pady=10)

    # Dodavanje gumba za zatvaranje povijesti
    button_zatvori = tk.Button(frame_history, text="Zatvori", command=zatvori_program.destroy)
    button_zatvori.pack(pady=10)

def zatvori_program():
    # Funkcija za zatvaranje glavnog prozora i svih podprozora
    root.quit()  # Zaustavi Tkinter mainloop
    root.destroy()  # Uništi sve Tkinter prozore

# Kreiramo glavni prozor aplikacije
root = tk.Tk()
root.title("Glavni prozor")

# Dugme za prikaz povijesti
button_povijest = tk.Button(root, text="Pokaži povijest", command=prikazi_historiju)
button_povijest.pack(pady=10)

# Dugme za zatvaranje aplikacije
button_exit = tk.Button(root, text="Zatvori aplikaciju", command=zatvori_program)
button_exit.pack(pady=10)

root.mainloop()
