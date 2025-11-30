# Aufgabe 15

# Dateiname der zu lesenden Datei
dateiname = 'beispiel.txt'
# Initialisiere die Zeilennummer
zeilennummer = 1

try:
    # Öffne die Datei im Lesemodus
    with open(dateiname, 'r') as datei:
        # Gehe jede Zeile in der Datei durch
        for zeile in datei:
            # Gib die formatierte Zeile aus. .strip() entfernt überflüssige
            # Leerzeichen und Zeilenumbrüche am Anfang/Ende der Zeile.
            print(f"Zeile {zeilennummer}: {zeile.strip()}")
            # Erhöhe die Zeilennummer für die nächste Zeile
            zeilennummer += 1
except FileNotFoundError:
    print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")

