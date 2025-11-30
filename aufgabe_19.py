# Aufgabe 19 (Erweiterung von Aufgabe 17)

# Versuche, matplotlib zu importieren.
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Fehler: Das Paket 'matplotlib' ist nicht installiert.")
    print("Bitte installiere es mit dem Befehl: pip install matplotlib")
    exit()

# --- Code aus Aufgabe 17 ---
# Initialisiere zwei leere Listen für die Spalten
spalte1 = [] # Wird zu x-Werten
spalte2 = [] # Wird zu y-Werten

dateiname = 'aufgabe_17_data.txt'

try:
    # Öffne die Datei zum Lesen
    with open(dateiname, 'r') as datei:
        for zeile in datei:
            teile = zeile.strip().split(' ')
            if len(teile) == 2:
                try:
                    spalte1.append(int(teile[0]))
                    spalte2.append(int(teile[1]))
                except ValueError:
                    print(f"Warnung: Konnte eine Zeile nicht in Zahlen umwandeln: '{zeile.strip()}'")

    print("Daten erfolgreich eingelesen.")
    print(f"X-Werte: {spalte1}")
    print(f"Y-Werte: {spalte2}")

    # --- Erweiterung für Aufgabe 19: Plotten der Daten ---
    if spalte1 and spalte2: # Nur plotten, wenn Daten vorhanden sind
        print("\nErstelle jetzt das Diagramm...")
        plt.figure(1)
        plt.plot(spalte1, spalte2, marker='o') # Linie mit Punkten
        plt.xlabel("Spalte 1 (X-Werte)")
        plt.ylabel("Spalte 2 (Y-Werte)")
        plt.title("Diagramm aus den Daten von Aufgabe 17")
        plt.grid(True)
        
        # Speichere das Diagramm als Bild
        plot_dateiname = 'aufgabe_19_diagramm.png'
        plt.savefig(plot_dateiname)
        print(f"Diagramm wurde als '{plot_dateiname}' gespeichert.")
    else:
        print("Keine Daten zum Plotten vorhanden.")

except FileNotFoundError:
    print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")
