import feedparser
import json
import os
import requests
from datetime import datetime
from flask import Flask, render_template, request

def ucitaj_podatke():
    if os.path.exists("korisnik_podaci.json"):
        with open("korisnik_podaci.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"ime": None}

def spremi_podatke(podaci):
    with open("korisnik_podaci.json", "w", encoding="utf-8") as f:
        json.dump(podaci, f, ensure_ascii=False, indent=2)

GROQ_API_KEY = "ur api"
GROQ_API_URL = ""

korisnik_podaci = ucitaj_podatke()

def odgovori_s_groq(upit, ime_korisnika):
    system_msg = (
        f"Ti si digitalni barba iz Kaštela. Govoriš isključivo na hrvatskom jeziku, gramatički ispravno. "
        f"Koristi ime korisnika ({ime_korisnika}) u odgovorima. "
        f"Govori prijateljski, s blagim humorom i savjetima, ali uvijek pazi na pravopis."
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": upit}
        ],
        "temperature": 0.7,
        "max_tokens": 1024
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Oprosti {ime_korisnika}, imam problema s povezivanjem. Pokušaj ponovno kasnije."
    except Exception as e:
        return f"Ups, dogodila se greška: {str(e)}"

# 🌐 Flask web aplikacija
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def barba_chat():
    poruka = ""
    odgovor = ""
    korisnik = ucitaj_podatke()

    # NOVO: spremi ime ako je uneseno u formi
    ime_forma = request.form.get("ime")
    if ime_forma:
        korisnik["ime"] = ime_forma.strip().capitalize()
        spremi_podatke(korisnik)

    if request.method == "POST":
        poruka = request.form.get("poruka", "")

        if poruka:
            ime_korisnika = korisnik.get("ime", "prijatelju")
            odgovor = odgovori_s_groq(poruka, ime_korisnika)

    return render_template("barba.html", 
                           ime=korisnik.get("ime", ""), 
                           odgovor=odgovor, 
                           poruka=poruka)

def pokreni_web():
    print("🌐 Pokrećem web verziju KaštelaBota...")
    print("📍 Otvori http://localhost:5000 u browseru")
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    pokreni_web()
