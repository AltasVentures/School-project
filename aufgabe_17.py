# Aufgabe 17

# Initialisiere zwei leere Listen für die Spalten
spalte1 = []
spalte2 = []

dateiname = 'aufgabe_17_data.txt'

try:
    # Öffne die Datei zum Lesen
    with open(dateiname, 'r') as datei:
        # Gehe jede Zeile der Datei durch
        for zeile in datei:
            # Entferne führende/folgende Leerzeichen und teile die Zeile am Leerzeichen
            teile = zeile.strip().split(' ')
            
            # Stelle sicher, dass wir genau zwei Teile haben
            if len(teile) == 2:
                try:
                    # Wandle die Teile in Zahlen um und füge sie den Listen hinzu
                    zahl1 = int(teile[0])
                    zahl2 = int(teile[1])
                    spalte1.append(zahl1)
                    spalte2.append(zahl2)
                except ValueError:
                    print(f"Warnung: Konnte eine Zeile nicht in Zahlen umwandeln: '{zeile.strip()}'")
            else:
                print(f"Warnung: Zeile hat nicht das erwartete Format (zwei Zahlen): '{zeile.strip()}'")

    # Gib die beiden erstellten Listen aus
    print("Liste der ersten Spalte:")
    print(spalte1)
    print("\nListe der zweiten Spalte:")
    print(spalte2)

except FileNotFoundError:
    print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")
