# Aufgabe 20

# Wieder der Versuch, matplotlib zu importieren
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Fehler: Das Paket 'matplotlib' ist nicht installiert.")
    print("Bitte installiere es mit dem Befehl: pip install matplotlib")
    exit()

# --- Teil a: Balkendiagramm mit fest einprogrammierten Daten ---
print("--- Aufgabe 20a ---")

# Die Daten direkt im Code definieren
monate_a = ["Jan", "Feb", "März", "April", "Mai", "Juni", "Juli", "Aug", "Sept", "Okt", "Nov", "Dez"]
temperaturen_a = [3, 5, 10, 14, 18, 21, 24, 24, 19, 14, 8, 4]

# Erstelle eine neue Zeichenfläche
plt.figure(1, figsize=(10, 6)) # figsize macht das Bild etwas breiter

# Erzeuge das Balkendiagramm
plt.bar(monate_a, temperaturen_a, color='skyblue')

# Füge Titel und Achsenbeschriftungen hinzu
plt.title("Monatliche Durchschnittstemperaturen für Stuttgart (manuell)")
plt.xlabel("Monat")
plt.ylabel("Temperatur in °C")

# Rotiere die Monatsnamen auf der x-Achse für bessere Lesbarkeit
plt.xticks(rotation=45)

# Speichere das Diagramm
dateiname_a = 'aufgabe_20a_diagramm.png'
plt.savefig(dateiname_a, bbox_inches='tight') # bbox_inches='tight' verhindert, dass die Labels abgeschnitten werden
print(f"Diagramm für Teil a) als '{dateiname_a}' gespeichert.")


# --- Teil b: Daten aus Datei einlesen und als Balkendiagramm darstellen ---
print("\n--- Aufgabe 20b ---")

# Leere Listen für die neuen Daten
monate_b = []
temperaturen_b = []

try:
    with open('KlimaStuttgart.txt', 'r', encoding='utf-8') as datei:
        for zeile in datei:
            # Trenne die Zeile in Monat und Temperatur
            teile = zeile.strip().split()
            if len(teile) == 2:
                monate_b.append(teile[0])
                temperaturen_b.append(float(teile[1])) # float() für den Fall von Kommazahlen

    print("Daten aus 'KlimaStuttgart.txt' erfolgreich eingelesen.")
    
    # Erstelle eine zweite Zeichenfläche
    plt.figure(2, figsize=(10, 6))

    # Erzeuge das Balkendiagramm mit den eingelesenen Daten
    plt.bar(monate_b, temperaturen_b, color='coral')

    # Füge Titel und Achsenbeschriftungen hinzu
    plt.title("Monatliche Durchschnittstemperaturen für Stuttgart (aus Datei)")
    plt.xlabel("Monat")
    plt.ylabel("Temperatur in °C")
    plt.xticks(rotation=45)

    # Speichere das zweite Diagramm
    dateiname_b = 'aufgabe_20b_diagramm.png'
    plt.savefig(dateiname_b, bbox_inches='tight')
    print(f"Diagramm für Teil b) als '{dateiname_b}' gespeichert.")

except FileNotFoundError:
    print("Fehler: 'KlimaStuttgart.txt' wurde nicht gefunden.")
except ValueError:
    print("Fehler beim Umwandeln einer Temperatur in eine Zahl.")
